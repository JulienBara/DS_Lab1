import socket
import sys

if len(sys.argv) > 2:
    host = str(sys.argv[1])
    port = int(sys.argv[2])
else:
    host = "localhost"
    port = 8000

while 1:
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try :
        socketClient.connect((host, port))
    except :
        print 'Connection error'
        sys.exit()

    msg = raw_input("What is your message? (X to quit): ")

    if msg == 'X' or msg == 'x':
        socketClient.close()
        break

    else:
        socketClient.send("GET /?message=" + msg + "\n\n")
        print socketClient.recv(4096)
