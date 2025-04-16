from pyrogram import filters
from Akira.bot import app
from Akira.db.mongo import users
from Akira.config import ADMINS
from pyrogram.errors import FloodWait
import asyncio
import logging

# Configure logging
logger = logging.getLogger(__name__)

# List of admin IDs who can use the broadcast command
admins = [int(admin.strip()) for admin in ADMINS.split(",") if admin.strip().isdigit()]

async def broadcast_message(message, media=None):
    """Broadcasts a message to all users in the database."""
    all_users = await users.find().to_list(length=None)
    if not all_users:
        logger.error("No users found in the database.")
        return 0, 0  # No users to broadcast to

    sent_count = 0
    failed_count = 0

    for user in all_users:
        chat_id = user.get("chat_id")  # Ensure you're using 'chat_id'
        if not chat_id:
            logger.warning(f"Skipping user without chat_id: {user}")
            continue

        try:
            if media:
                # If media is provided, send media group (only one media file in this case)
                await app.send_media_group(chat_id, [media])
            else:
                # Otherwise, send a text message
                await app.send_message(chat_id, message)
            sent_count += 1
        except FloodWait as e:
            logger.warning(f"Flood wait for {e.x} seconds, retrying later.")
            await asyncio.sleep(e.x)  # Sleep for the flood wait time
            continue
        except Exception as e:
            failed_count += 1
            logger.error(f"Failed to send message to {chat_id}: {e}")

    return sent_count, failed_count


@app.on_message(filters.command("broadcast") & filters.user(admins))
async def broadcast_handler(client, message):
    if message.reply_to_message:
        # Get the replied message
        replied_message = message.reply_to_message

        # Prepare the broadcast message or media
        if replied_message.text:
            broadcast_msg = replied_message.text
            media = None
        elif replied_message.photo:
            broadcast_msg = "Broadcasting a photo..."
            media = replied_message.photo
        elif replied_message.video:
            broadcast_msg = "Broadcasting a video..."
            media = replied_message.video
        elif replied_message.audio:
            broadcast_msg = "Broadcasting audio..."
            media = replied_message.audio
        elif replied_message.document:
            broadcast_msg = "Broadcasting a document..."
            media = replied_message.document
        else:
            broadcast_msg = "Unsupported media type."
            media = None

        # Send the broadcast message or media to all users
        sent, failed = await broadcast_message(broadcast_msg, media)

        # Reply with the result
        await message.reply(f"✅ Broadcast complete.\n\n📤 Sent: `{sent}`\n❌ Failed: `{failed}`")
    else:
        await message.reply("❌ Please reply to a message to broadcast it.")
