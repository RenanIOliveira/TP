# server
from socket import *

serverPort = 12001
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))
serverSocket.listen()

print("The server is ready to receive")

while True:
    conn, addr = serverSocket.accept()
    print("connected\n")
    while True:
        message,clientAddress = conn.recvfrom(2048)
        if not message: break
        print(message)
        modifiedMessage = message.decode().upper()
        conn.sendto(modifiedMessage.encode(),addr)
    print("connection closed")
