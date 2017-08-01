# python-networking
#### Networking using sockets

- rot13/**rot13_server.py**
  - Simple TCP Server for a single client which returns the *rot13* cypher of the received data.
- rot13/**rot13_client.py**
  - Simple TCP Server to send data and print a response.

- chat/**chat_server.py**
  - TCP Server for concurrent clients which broadcasts the received data for all clients using non-blocking sockets and select().
- chat/**chat_client.py**
  - TCP Client using threading to print received data without waiting for input.
