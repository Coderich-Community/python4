from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}

HOST = "localhost"
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)  # ( address family, socket type )
SERVER.bind(ADDR)  # binding address to server


def accept_incoming_connections():
    """handling for incoming clients"""
    while True:
        client, client_address = SERVER.accept()  # wait for incoming connection
        print("%s:%s has connected." % client_address)
        client.send(
            bytes(
                "Greetings from server!" + " Now type your name and press enter!",
                "utf-8",
            )
        )  # send bytes with utf-8 encoding
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()  # creating thread


# client handler function
def handle_client(client):  # client socket as arguement
    """Handles a single client connection."""
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = "Welcome %s! If you ever want to quit, type {quit} to exit." % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" %name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." %name, "utf8"))
            break

def broadcast(msg, prefix=""):
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

if __name__ == "__main__":
    SERVER.listen(5) # listen(maxConnections)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()

    # We join() ACCEPT_THREAD so that the main script waits for it to complete and doesn’t jump to the next line, which closes the server.
    ACCEPT_THREAD.join()
    SERVER.close()