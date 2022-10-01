# client
from socket import *

serverName = "localhost"
serverPort = 12001

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

should_continue = ''
while(should_continue != 'n'):
    message = input('Input lowercase sentence:\n')
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    should_continue = input('Continue?[y/n]\n');

clientSocket.close()


