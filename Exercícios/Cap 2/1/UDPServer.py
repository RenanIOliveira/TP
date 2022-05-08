from _ast import While
from socket import *

serverPort = 12000


def main():
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('', serverPort))
    print('The server is ready to receive')
    while True:
        message, client_address = server_socket.recvfrom(2048)
        modified_message = message.decode().upper()
        server_socket.sendto(modified_message.encode(), client_address)


if __name__ == '__main__':
    main()
