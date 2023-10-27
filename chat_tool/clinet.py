import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Define the port on which you want to connect
port = 12345

# Connect to the server
client_socket.connect((host, port))

while True:
    message = input('Enter your message: ')
    client_socket.send(message.encode('utf-8'))
    data = client_socket.recv(1024).decode('utf-8')
    print('Received:', data)

# Close the socket
client_socket.close()
