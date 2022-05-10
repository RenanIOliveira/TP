from socket import *

serverName = 'localhost'
serverPort = 12003


def main():
    client_socket = socket(AF_INET, SOCK_STREAM)
    while True:
        client_socket.connect((serverName, serverPort))
        print('Input lowercase sentence')
        message = input()
        client_socket.send(message.encode())
        modified_message, server_address = client_socket.recvfrom(2048)
        print(modified_message.decode())
        client_socket.shutdown(SHUT_RDWR)

        print('Send another message? [y/n]')
        another = input() == 'y'
        if not another:
            break


if __name__ == '__main__':
    main()
