# Imports
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import json, hashlib, random
# For PyInstaller:
import asyncio, engineio.async_threading, jinja2

# Variables
app = Flask(__name__)
io = SocketIO(app)

clients=[]

# Functions
def randomize_targets(list_of_names):
    ''' Returns a dict of names such that randomize(list)[name] = name's target '''
    final = {}
    random.shuffle(list_of_names)
    for name in list_of_names:
        if list_of_names.index(name) == (len(list_of_names) - 1):
            i = 0
        else:
            i = (list_of_names.index(name) + 1)
        final[name] = list_of_names[i]
    return final

def hash(data):
    return hashlib.md5(str(data).encode('utf-8')).hexdigest()

# Routing
@app.route("/") #home
def index():
   return render_template("index.html")

@app.route('/<filename>')
def return_html(filename):
    return render_template(filename)

@app.errorhandler(500)
def handler(e):
    return render_template('500.html').format(e)

# Socket.io events
@io.on('connect')
def connected():
    pass

@io.on('disconnect')
def disconnect():
    pass

@io.on('test')
def return_test():
    print('hi')
    emit('a-ok') # Emits *to client*

# Main
if __name__ == '__main__':
   app.run()

# This is so much easier in Python than NodeJS
