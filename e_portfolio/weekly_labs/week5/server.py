# INITIAL CODE
# import socket

# # Create a TCP socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('localhost', 65432))
# server_socket.listen(1) # Allow 1 pending connection
# print("TCP Server is listening...")

# while True:
#     client_socket, client_address = server_socket.accept()
#     print(f"Connected to {client_address}")
    
#     data = client_socket.recv(1024)
#     print(f"Received: {data.decode()}")

#     # Echo back the data
#     client_socket.sendall(b"ACK: " + data)
#     client_socket.close()

# EXERCISE 1
# import socket
# import datetime

# # Create a TCP socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('localhost', 65432))
# server_socket.listen(1) # Allow 1 pending connection
# print("TCP Server is listening...")

# while True:
#     client_socket, client_address = server_socket.accept()
#     print(f"Connected to {client_address}")
    
#     start_time = datetime.datetime.now()

#     data = client_socket.recv(1024)
#     print(f"Received: {data.decode()}")

#     end_time = datetime.datetime.now()
#     print(f"Time taken (TCP): {end_time - start_time}")

#     # Echo back the data
#     client_socket.sendall(b"ACK: " + data)
#     client_socket.close()

# EXERCISE 2
# import socket
# import datetime

# # Create a UDP socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind(('localhost', 65432))
# print("UDP Server is listening...")

# while True:
#     # Receive data from client
#     data, client_address = server_socket.recvfrom(1024)
#     print(f"Received: {data.decode()} from {client_address}")

#     # Measure time before responding
#     start_time = datetime.datetime.now()

#     # Send acknowledgment back
#     server_socket.sendto(b"ACK: " + data, client_address)

#     # Measure time after sending
#     end_time = datetime.datetime.now()
#     print(f"Time taken (UDP): {end_time - start_time}")

# EXERCISE 3
# import socket
# import datetime

# # Create a TCP socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('localhost', 65432))
# server_socket.listen(1) # Allow 1 pending connection
# print("TCP Server is listening...")

# while True:
#     client_socket, client_address = server_socket.accept()
#     print(f"Connected to {client_address}")

#     with open('received_file.txt', 'wb') as f:  # Open file to write data
#         while True:
#             data = client_socket.recv(1024)
#             if not data:
#                 break
#             f.write(data)  # Write the received data to the file
#         print("File received and logged!")
    
#     start_time = datetime.datetime.now()

#     data = client_socket.recv(1024)


#     end_time = datetime.datetime.now()
#     print(f"Time taken (TCP): {end_time - start_time}")


#     client_socket.close()

# EXERCISE 4
import socket
import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65432))
print("UDP Server is listening...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    with open('received_file_udp.txt', 'wb') as f:
        while True:
            data, client_address = server_socket.recvfrom(1024)
            if not data:
                break
            f.write(data)
        print("File received and logged using UDP!")

    start_time = datetime.datetime.now()

    end_time = datetime.datetime.now()
    print(f"Time taken (TCP): {end_time - start_time}")


    client_socket.close()