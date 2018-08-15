from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
# For PyInstaller:
import asyncio, engineio.async_threading, jinja2

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run()
