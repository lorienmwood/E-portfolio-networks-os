# Initial code for TCP client
# import socket

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(('localhost', 65432))

# message = input("Enter message: ")
# client_socket.sendall(message.encode())

# response = client_socket.recv(1024)

# print(f"Server response: {response.decode()}")

# client_socket.close()


# EXERCISE 1
# import socket
# import datetime

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(('localhost', 65432))

# message = input("Enter message: ")
# start_time = datetime.datetime.now()
# client_socket.sendall(message.encode())

# response = client_socket.recv(1024)

# end_time = datetime.datetime.now()
# print(f"Time taken (TCP): {end_time - start_time}")

# print(f"Server response: {response.decode()}")

# client_socket.close()

# EXERCISE 2
# import socket
# import datetime

# # Create a UDP socket
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# # Take input message from user
# message = input("Enter message: ")
# # message = "Hello, UDP Server!"

# # Measure time before sending data
# start_time = datetime.datetime.now()

# # Send data to the server
# client_socket.sendto(message.encode(), ('localhost', 65432))

# # Receive response
# response, server_address = client_socket.recvfrom(1024)

# # Measure time after receiving data
# end_time = datetime.datetime.now()

# print(f"Server response: {response.decode()}")
# print(f"Time taken (UDP): {end_time - start_time}")

# client_socket.close()

# EXERCISE 3
# import socket
# import datetime

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(('localhost', 65432))

# # Open the file to send 
# with open('file_to_send.txt', 'rb') as f:
#     start_time = datetime.datetime.now()
    
#     # Send the file content
#     client_socket.sendfile(f)

# end_time = datetime.datetime.now()

# print(f"Time taken (TCP): {end_time - start_time}")

# client_socket.close()

# EXERCISE 4

import socket
import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open the file to send 
with open('file_to_send.txt', 'rb') as f:
    start_time = datetime.datetime.now()
    
          # Send the file data in chunks
    while True:
        data = f.read(1024)
        if not data:
            break
        client_socket.sendto(data, ('localhost', 65432))  # Send using UDP

end_time = datetime.datetime.now()

print(f"Time taken (UDP): {end_time - start_time}")

client_socket.close()
