from multiprocessing import Process
from Akira.bot import start_bot
from Akira.web import run_flask

if __name__ == "__main__":
    try:
        # Start Flask web server in a separate process
        flask_process = Process(target=run_flask)
        flask_process.start()

        # Start the Pyrogram bot
        start_bot()

    except Exception as e:
        print(f"Error while starting bot or Flask: {e}")
