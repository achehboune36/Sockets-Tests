"""
        Script for Creating server, accept connections and share massages
"""
import socket 
import threading
import time
import os
from datetime import datetime as d
from config import HEADER, PORT ,FORMAT ,DISCONNECT_MESSAGE, new_line

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

list_of_clients = []

def main():
    """Launcher"""
    print("[STARTING] server is starting...")
    try:
        start()
    except Exception as e:
        print(f'[ERROR] cannot start server {e}...')

def start():
    """
        Listens for connections and creates a thread for them
    """
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()

        global list_of_clients
        list_of_clients.append(conn)

        try:
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
        except Exception as e:
            print(f"[ERROR] error while creating new thread!")

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

def handle_client(conn, addr):
    """
        Handles client's requests

        Args:
                :param conn: client address
                :param addr: connections host and port

        Returns:
                :returns: None
    """
    print(f"[NEW CONNECTION] {addr} connected.")

    user_name = conn.recv(HEADER).decode(FORMAT)
    connected = True
    while connected:
        try:
            msg = conn.recv(HEADER).decode(FORMAT)
        except Exception as e:
            print(f'[ERROR] Input error {e}')

        if msg:
            date = d.now()
            ts = date.strftime("%Y-%m-%d %H:%M:%S")

            if len(msg) > 50:
                print(f"[DEBUG] {addr} {user_name} Message to long {ts}")
                conn.send(f"[{ts}] Message to long!\n".encode(FORMAT))

            elif msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[DEBUG] {addr} {user_name} {ts}")
                conn.send(f"[{ts}] Disconnected!".encode(FORMAT))

            else:
                message = f"[{ts}] {user_name}: {msg.replace(new_line, '')}"
                print(f"[DEBUG] {message}")
                conn.send(message.encode(FORMAT))
                broadcast(message, conn)

    conn.close()

def broadcast(message, conn):
    """
        Handles broadcasting messages

        Args:
                :param message: client's message
                :param conn: client's address

        Returns:
                :returns: None
    """
    global list_of_clients
    for client in list_of_clients:
        if client != conn:
            try:
                client.send(message.encode(FORMAT))

            except Exception as e:
                client.close() 
                remove(client)

def remove(conn):
    """
        Handles removing broken links

        Args:
                :param conn: client's address

        Returns:
                :returns: None
    """
    global list_of_clients
    if conn in list_of_clients:
        list_of_clients.remove(conn)

# Entry point of the application
if __name__ == '__main__':
        main()
