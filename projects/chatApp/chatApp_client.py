from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

# connecting to server
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000  # Default value.
else:
    PORT = int(PORT)
    
BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


def receive():
    """Handles receiving of message"""
    while True:
        try: 
            msg =  client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        
        except OSError: # client might've left chat
            break

def send(event=None): # event is passed by binders
    """Sending message handler"""
    msg = my_msg.get()
    my_msg.set("") # input field clear
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

def on_closing(event=None):
    my_msg.set("{quit}")
    send()



top = tkinter.Tk()
top.title("Chat App")

message_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar() 
my_msg.set("Message here:")
scrollbar = tkinter.Scrollbar(message_frame) # to navigate through past messages.

msg_list = tkinter.Listbox(message_frame, height=30, width=100, yscrollcommand = scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()

message_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg, width=50)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()
top.protocol("WM_DELETE_WINDOW", on_closing)


# message_threading start
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop() 