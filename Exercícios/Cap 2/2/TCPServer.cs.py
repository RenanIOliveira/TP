from socket import *

serverPort = 12000


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', serverPort))
    server_socket.listen()
    print('The server is ready to receive')
    while True:
        conn, client_address = server_socket.accept()
        message = conn.recv(2048)
        print('Received: ' + message.decode())
        modified_message = message.decode().upper()
        conn.send(modified_message.encode())
        conn.close()


if __name__ == '__main__':
    main()
