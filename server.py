from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask import Flask

# Engine payload to prevent a "too many packets in payload" error. See https://github.com/miguelgrinberg/python-engineio/issues/142
from engineio.payload import Payload

from makeIDs import *

Payload.max_decode_packets = 300

# Do flask run to run the flask application

app = Flask(__name__)

socketio = SocketIO(app)

roomDict = {}

@app.route("/")
def hello_world():
    return "<p> Hello world!</p>"

@socketio.on('connect')
def test_connect(auth):
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

# automatically create a room when a host connects
@socketio.on('host connection')
def createHost(data):
    hostRoomID = generateUniqueID(roomDict)
    hostID = generateHostID(roomDict)
    roomDict.update({hostID : hostRoomID})
    print("host has connected with ID " + hostID + " and room ID " + hostRoomID)
    emit('room and host code', {'roomID' : hostRoomID, 'hostID' : hostID})

@socketio.on('host disconnection')
def deleteHost(data):
    roomDict.pop(data['roomID'])
    print("Host has disconnected")
    # emit('kickUsers', None, to=data['roomID'])

@socketio.on('join')
def on_join(data):
    print("Request to join room")

@socketio.on('drawn')
def updateBoard(data):
    emit('updateBoard', {'prevCoord' : data['prevCoord'], 'currCoord' : data['currCoord']}, broadcast = True)



if __name__ == '__main__':
    socketio.run(app)