import string
import random

def generateUniqueID(roomDict):
    chars = string.ascii_uppercase
    size = 5
    roomID = ''.join(random.choice(chars) for _ in range(size))

    # ensure that the room is unique, else regenerate
    while roomID in roomDict.values():
        roomID = ''.join(random.choice(chars) for _ in range(size))
    
    return roomID

def generateHostID(roomDict):
    chars = string.digits
    size = 10
    hostID = ''.join(random.choice(chars) for _ in range(size))

    while hostID in roomDict.keys():
        hostID = ''.join(random.choice(chars) for _ in range(size))

    return hostID 