import time
from socket import *
from threading import Thread

serverPort = 12003


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', serverPort))
    server_socket.listen()
    print('The server is ready to receive')
    while True:
        print('waiting')
        conn, client_address = server_socket.accept()
        print('connection accepted')
        t1 = Thread(target=worker, args=(conn,))
        t1.start()


def worker(conn):
    message = conn.recv(2048)
    # time.sleep(20)
    print('Received: ' + message.decode())
    modified_message = message.decode().upper()
    conn.send(modified_message.encode())
    conn.close()


if __name__ == '__main__':
    main()
