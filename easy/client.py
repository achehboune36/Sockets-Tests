
import socket
import threading
from config import PORT, FORMAT, DISCONNECT_MESSAGE, SERVER, new_line

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(2048).decode(FORMAT), new_line)

def listen():
    while True:
        msg = client.recv(2048).decode(FORMAT)
        if msg:
            print(msg, new_line)

def main():
    user_name = str(input("Please enter a user name: "))
    client.send(user_name.encode(FORMAT))

    while True:
        thread = threading.Thread(target=listen)
        thread.start()

        String = str(input(""))
        send(String)
        if String == DISCONNECT_MESSAGE:
            break

main()
