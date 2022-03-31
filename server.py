import socket  # Used for network connection
import threading  # Used for performing multiple tasks at the same time

#  Connection values
host = '127.0.0.1'
port = 55555

#  Creating a socket at server side using TCP/IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#  Bind the socket with the given values
s.bind((host, port))

#  Allow multiple connections to the socket
s.listen()

#  Lists of clients and their characteristic nicknames
clients = []
nicknames = []


#  Sending messages to all connected clients
def distribute(message):
    for client in clients:
        client.send(message)


def remove_client(client):
    # Removing And disconnecting Clients
    index = clients.index(client)
    clients.remove(client)
    client.close()
    nickname = nicknames[index]
    distribute('{} left!'.format(nickname).encode('utf-8'))
    print("[DISCONNECTION] {} left the chat".format(nickname))
    nicknames.remove(nickname)


#  Managing messages from clients
def manage(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            distribute(message)
            message = message.decode().split(": ")

            if message[1] == "SHUTDOWN":
                remove_client(client)

        except:
            # Removing And Closing Clients
            remove_client(client)
            break


def listen():
    while True:
        # Constantly accepts new client connection
        client, address = s.accept()
        print("[CONNECTION] with {}".format(str(address)))

        # Asks for a nickname and saves it
        client.send('NAME'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Print and distribute nickname
        print("Nickname is {}".format(nickname))
        distribute("{} joined! ".format(nickname).encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))

        # Start managing thread for this client
        thread = threading.Thread(target=manage, args=(client,))
        thread.start()


print("[LISTENING] Server is listening for connection...")
listen()
