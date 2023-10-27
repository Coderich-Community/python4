import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Define the port on which you want to connect
port = 12345

# Bind the socket to the address and port
server_socket.bind((host, port))

# Now wait for a client to connect
server_socket.listen(1)

print(f'Waiting for connections on {host}:{port}...')

# Accept the connection
client_socket, addr = server_socket.accept()

print('Got connection from', addr)

while True:
    data = client_socket.recv(1024).decode('utf-8')
    print('Received:', data)
    message = input('Enter your message: ')
    client_socket.send(message.encode('utf-8'))

# Close the socket
client_socket.close()
