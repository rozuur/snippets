"""
connect to server telnet localhost:50000

only works for SET and GET commands
use END to close connection
"""

import socket
import os

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50000              # Arbitrary non-privileged port
print 'Starting server at port', PORT
print 'Connect to server as telnet localhost:50000'
print 'use "END" to close connection'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

stored = {} # dictionary to store all key value pairs
activeChild = []

def reapChildren():
        while activeChild:
                pid, stat = os.waitpid(0, os.WNOHANG)
                if not pid: break
                activeChild.remove(pid)
        
def handleClient(conn):
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
                elif cmd.startswith('END'):
                        break
        conn.close()
        os._exit(0)


while 1:
        conn, addr = s.accept()
        print 'Connected by', addr
        childpid = os.fork()
        reapChildren()
        if childpid == 0:
                handleClient(conn)
        else:
                activeChild.append(childpid)

print 'Closing connection'
conn.close()

