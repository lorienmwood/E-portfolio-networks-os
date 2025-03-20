# Networks and Operating Systems - Transport Layer in Networks PT-1

## Notes
- This Lab we looked at the transport layer which manages end to end communications between devices.

### 1. Building a Simple UDP Server
<!-- import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))
print("UDP Server is ready to receive API data...")
while True:
data, client_address = server_socket.recvfrom(2048)
print(f"Received data from {client_address}: {data.decode()}") -->

- import socket, this imports the built in socket module
- server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM), creates a new socket object
- socket.AF_INET, specifies IPv4 addressing (Internet Protocol version 4) 
- socket.SOCK_DGRAM, UDP socket
- server_socket.bind(('localhost', 65433))
- while True:,infinite loop to continuously listen for incoming UDP packets
- data, client_address = server_socket.recvfrom(2048), recvfrom() is a UDP-specific method 
- print(f"Received data from {client_address}: {data.decode()}"), prints address

### 2. Building a Simple UDP Client
<!-- import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)
message = b"Hello, UDP Server!"
# Send message to the server
client_socket.sendto(message, server_address)
client_socket.close() -->

### 3. Building a Simple API data collection Application



## Exercises
- Exercise 1: Using the previous two scripts make a chat application in which clients can chat using a server
- Exercise 2: Let the use make a dictionary with the users IP address
- Exercise 3: Add authentication step to the application in which the sever would ask the client for username and password to initiate the communication.
- Exercise 4: Write functions that would encrypt the messages in the client and decrypt them in the server.
- Exercise 5: Check the API website and update the script to compare the temperate between the university and the British Library.
- Exercise 6: Experiment with other applications of the API.
