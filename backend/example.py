from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return "example"

def run():
    # Runs the Flask app on host=0.0.0.0 (accessible locally and via LAN)
    app.run(host='0.0.0.0', port=8080)

def example():
    # Start Flask in a separate thread so it doesn’t block your bot
    t = Thread(target=run)
    t.daemon = True  # This ensures the thread closes when the main program ends
    t.start()
