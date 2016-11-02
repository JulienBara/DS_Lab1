import socket
import sys

host = "localhost"
port = 8000

while 1:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try :
        socket.connect((host, port))
        print 'Connected'
    except :
        print 'Connection error'
        sys.exit()

    msg = raw_input("What is your message? (X to quit): ")

    if msg == 'X' or msg == 'x':
        socket.close()
        break

    else:
        socket.send("GET /?message=" + msg + "\n\n")
        print socket.recv(4096)
