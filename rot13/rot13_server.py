from socket import socket, AF_INET, SOCK_STREAM
import codecs


def rot13_translation(client_object, client_address):
    while True:
        inbytes = client_object.recv(1024)
        if inbytes:
            outbytes = codecs.encode(inbytes.decode(), 'rot_13').encode()
            client_object.send(outbytes)
        else:
            break
    print('{0}:{1} disconnected'.format(*client_address))


def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('', 1068))
    server.listen(3)

    while True:
        client, address = server.accept()
        print('{0}:{1} connected'.format(*address))
        rot13_translation(client, address)
        client.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nServer closed.')
