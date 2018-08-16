#imports
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
# For PyInstaller:
import asyncio, engineio.async_threading, jinja2

app = Flask(__name__)
socketio = SocketIO(app)

#routing
@app.route("/") #home
def index():
   return render_template("index.html")

@app.route('/<filename>')
def return_html(filename):
    return render_template(filename)

@app.errorhandler(500)
def handler(e):
    return render_template('500.html').format(e)

if __name__ == '__main__':
   app.run()

# This is so much easier in Python than NodeJS
