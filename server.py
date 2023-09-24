import socket
import threading

host = '127.0.0.1'

port = 8881

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))

server.listen()

print(f'Server Running on {host}:{port}')

clients = []
userNames = []

def brodcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

def handle_message(client):
    while True:
        try:
            message = client.recv(1024)
            brodcast(message, client)
        except:
            index = clients.index(client)
            userName = userNames[index]
            brodcast(f'ChatBot: {userName} disconnected'.encode('utf-8'))
            clients.remove(client)
            userNames.remove(userName)
            client.close()
            break

def recive_connection():
    while True:    
        client, address = server.accept()
        client.send("@username".encode('utf-8'))
        userName = client.recv(1024).decode('utf-8')

        clients.append(client)
        userNames.append(userName)
        print(f'{userName} is connected with {str(address)}')

        message = f'ChatBot: {userName} joined the Chat!'.encode('utf-8')
        brodcast(message, client)
        client.send('Connected to server'.encode('utf-8'))

        thread = threading.Thread(target=handle_message, args=(client,))
        thread.start()

recive_connection()