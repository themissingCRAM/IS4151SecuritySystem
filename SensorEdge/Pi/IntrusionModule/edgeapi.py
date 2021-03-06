import sqlite3
from flask import make_response
import socket

EDGE_CONNECTOR = "CameraEdge"

DB_NAME = "shs"

# def emergency(edgeconnector):
#     if edgeconnector != EDGE_CONNECTOR:
#         print("starting emergency")
#         host = socket.gethostname()
#         port = 6789
#         s = socket.socket()
#         s.connect((host, port))
#         message = "globalemergency"
#         s.send(message.encode("utf-8"))
#         s.close()
#     else:
#         print("its actually local")
#     return make_response('Message Sent', 200)

# def stopemergency():
#     host = socket.gethostname()
#     port = 6789
#     s = socket.socket()
#     s.connect((host, port))
#     message = "stopemergency"
#     s.send(message.encode("utf-8"))
#     s.close()
#     return make_response('Alarm Stopped', 200)

def status(statusNumber):
    host = socket.gethostname()
    port = 6789
    s = socket.socket()
    s.connect((host, port))
    if statusNumber == 0:
        message = "arm"
        s.send(message.encode("utf-8"))
        s.close()
        return make_response("Armed", 200)
    elif statusNumber == 1:
        message = "unarm"
        s.send(message.encode("utf-8"))
        s.close()
        return make_response("Unarmed", 200)
    elif statusNumber == 2:
        message = "alarm"
        s.send(message.encode("utf-8"))
        s.close()
    else:
        return make_response("Error", 400)
    
def settings(gad, fad, md):
    print("Settings called")
    #Connection to DB
    conn = sqlite3.connect(DB_NAME)
    curr = conn.cursor()
    curr.execute("INSERT INTO SETTINGS (globalalarmtime, forcedalarmtime, motiondetection) VALUES (?,?,?)", (gad, fad, md,))
    conn.commit()
    curr.close()
    conn.close()
    host = socket.gethostname()
    port = 6789
    s = socket.socket()
    s.connect((host, port))
    message = "setting"
    s.send(message.encode("utf-8"))
    s.close()
    return make_response("Done",200)