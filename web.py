import os
from flask import Flask

PORT = int(os.getenv("PORT", 8080))

app = Flask(__name__)

@app.route("/")
def health():
    return "✅ Pyrogram bot is healthy", 200

def run_flask():
    app.run(host="0.0.0.0", port=PORT)
