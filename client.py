import socket
import threading
from SHXBOTH_LTONSH import enigma

userName = input("Enter Your username:")

host = '127.0.0.1'

port = 8881

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def recive_message():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "@username":
                client.send(userName.encode('utf-8'))
            else:
                print(message)
        except:
            print('An error Ocurred')
            client.close()
            break

def write_message():
    while True:
        message = input("")
        #message = f"{userName}: {input('')}"
        encrypted_message = enigma(message, "DJH")
        newText = f"{userName}: {encrypted_message}"
        #client.send(message.encode('utf-8'))
        client.send(newText.encode('utf-8'))

recive_thread = threading.Thread(target=recive_message)
recive_thread.start()

write_thread = threading.Thread(target=write_message)
write_thread.start()


