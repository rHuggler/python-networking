from socket import socket, AF_INET, SOCK_STREAM
import sys
import threading


def send_message(client_object):
    while True:
        response = client_object.recv(1024)
        if response:
            print(response.decode())


def main():
    client = socket(family=AF_INET, type=SOCK_STREAM)
    client.connect((sys.argv[1], int(sys.argv[2])))
    print('Connected to {0}:{1}'.format(*sys.argv[1:]))

    thread = threading.Thread(target=send_message, args=(client,))
    thread.daemon = True
    thread.start()

    while True:
        message = input('').encode('ascii')
        client.send(message)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nClient closed')
