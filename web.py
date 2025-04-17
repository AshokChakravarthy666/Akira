from flask import Flask
from threading import Thread

# Initialize Flask app
app = Flask(__name__)

# Sample route to check if the web server is working
@app.route('/')
def home():
    return "Akira Bot Web Server is Running!"

def run_web():
    app.run(debug=True, use_reloader=False)  # Avoid reloader when using threading

# Optionally, you can use this to run it in a separate thread
def run_web_threaded():
    thread = Thread(target=run_web)
    thread.start()
