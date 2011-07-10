"""
connect to server telnet localhost 50000

only works for SET and GET commands
"""

import socket
import os

HOST = ''                 # local host
PORT = 50000              # Arbitrary non-privileged port
print 'Starting server at port', PORT
print 'Connect to server as telnet localhost 50000'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5) # allows 5 pending connections

stored = {} # dictionary to store all key value pairs
activeChild = []

def reapChildren():
        while activeChild:
                # don't hang if no child exited
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
        conn.close()
        os._exit(0)


while 1:
        conn, addr = s.accept()
        print 'Connected by', addr
        reapChildren()
        childpid = os.fork()
        if childpid == 0:
                handleClient(conn)
        else:
                activeChild.append(childpid)

conn.close()

