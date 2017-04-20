from socket import socket, AF_INET, SOCK_STREAM
import sys


def main():
    client = socket(family=AF_INET, type=SOCK_STREAM)
    client.connect((sys.argv[1], int(sys.argv[2])))
    print('Connected to {0}:{1}'.format(*sys.argv[1:]))

    while True:
        message = input('>').encode('ascii')
        client.send(message)
        response = client.recv(len(message))
        print(response.decode)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nClient closed')
