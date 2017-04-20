from socket import socket, AF_INET, SOCK_STREAM
import select

def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.setblocking(False)
    server.bind(('', 1067))
    server.listen(3)
    print('Listening')

    inputs = [server]
    outputs = []
    messages = []

    while True:
        read_list, write_list, except_list = select.select(inputs, outputs, inputs)

        for sock in read_list:
            if sock is server:
                client, address = server.accept()
                print('{0}:{1} connected'.format(*address))
                inputs.append(client)
            else:
                message = sock.recv(1024)
                if message:
                    messages.append(message)
                if sock not in outputs:
                    outputs.append(sock)

        for sock in write_list:
            for message in messages:
                for client in outputs:
                    client.send(message)
                messages.remove(message)

        for sock in except_list:
            inputs.remove(sock)
            if sock in outputs:
                outputs.remove(sock)
            sock.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nServer closed.')
