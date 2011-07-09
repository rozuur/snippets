"""
connect to server telnet://localhost:50000/

only works for SET and GET commands
"""

import socket
import os

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50000              # Arbitrary non-privileged port
print 'Starting server at port', PORT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

stored = {} # dictionary to store all key value pairs
conn, addr = s.accept()
print 'Connected by', addr

while 1:
        data = conn.recv(1024)
        if not data: break
        print 'Recieved', data
        cmd = data
        if cmd.startswith('SET'):
                s, key, value = cmd.split()
                stored[key] = value
        elif cmd.startswith('GET'):
                s, key = cmd.split()
                if key in stored:
                        conn.send(stored[key])

print 'Closing connection'
conn.close()

