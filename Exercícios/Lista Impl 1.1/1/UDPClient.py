from socket import *

serverName = 'localhost'
serverPort = 12000


def main():
    client_socket = socket(AF_INET, SOCK_DGRAM)

    while True:
        print('Input lowercase sentence')
        message = input()

        client_socket.sendto(message.encode(), (serverName, serverPort))
        modified_message, server_address = client_socket.recvfrom(2048)
        print(modified_message.decode())
        client_socket.close()

        print('Send another message? [y/n]')
        another = input() == 'y'
        if not another:
            break


if __name__ == '__main__':
    main()
