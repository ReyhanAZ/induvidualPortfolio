import socket
import random
import threading
import time

#  Choosing either a bot or a characteristic nickname
nickname = input("Choose your nickname or a bot (fati, rey, z, jolly): ")


#  Connecting to the created socket at server side using TCP/IP protocol
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


#  List of my chatbots
chatbots = ["rey", "fati", "z", "jolly"]


#  List of 'fun' and 'boring' activities
fun = ["play", "cook", "train", "code", "draw"]

boring = ["clean", "read", "work", "walk", "sleep"]


def rey(action):
    reply = [
        "{}: I personally think {} is a waste of time. ".format(nickname, action + "ing"),
        "{}: {} is not my favorite, but I guess it's okay. ".format(nickname, action + "ing"),
        "{}: You know me so well! {} is the best. ".format(nickname, action + "ing")
    ]

    if action in fun or action in boring:
        return random.choice(reply)

    else:
        reply2 = [
            "{}: Can't say that i expected that. ".format(nickname),
            "{}: That is a good idea! ".format(nickname),
            "{}: Ehm...? ".format(nickname)
        ]

        return random.choice(reply2)


def fati(action):
    if action in fun:
        reply3 = [
            "{}: {} is so much fun !".format(nickname, action + "ing"),
            "{}: YESS! I love {} ".format(nickname, action + "ing"),
            "{}: I'm sick so I don't feel like {} right now ".format(nickname, action + "ing")
        ]

        return random.choice(reply3)

    elif action in boring:
        reply4 = [
            "{}: Is {} really a suggestion? ".format(nickname, action + "ing"),
            "{}: {}? Don't we have anything better to do? ".format(nickname, action + "ing"),
            "{}: I'm bored already, so {} sounds like a bad idea... ".format(nickname, action + "ing")
        ]

        return random.choice(reply4)

    else:
        return "{}: Maybe we could do something else?... ".format(nickname)


def z(action):
    if action in fun:
        reply5 = [
            "{}: Did you say {}? That would be awesome! ".format(nickname, action + "ing"),
            "{}: {} is a wonderful idea! ".format(nickname, action + "ing"),
            "{}: That is exciting! I've heard {} is so much fun. ".format(nickname, action + "ing")
        ]

        return random.choice(reply5)

    elif action in boring:
        reply6 = [
            "{}: {}?.. That is so unoriginal. ".format(nickname, action + "ing"),
            "{}: No thanks, {} is tiresome. ".format(nickname, action + "ing"),
            "{}: Dude, {} is so lame. ".format(nickname, action + "ing")
        ]

        return random.choice(reply6)

    else:
        return "{}: I don't really care. ".format(nickname)


def jolly(action):
    if action in boring or action in fun:
        return "{}: You know I enjoy {}! ".format(nickname, action + "ing")

    else:
        return "{}: I will support anything! ".format(nickname)


#  Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NAME' Send Nickname
            message = client.recv(1024).decode('utf-8')
            if message == 'NAME':
                client.send(nickname.encode('utf-8'))
            else:
                if ":" in message:

                    msg_split = message.split(": ")
                    #  Split the message in two and inspect what was before the colon,
                    #  so it is possible to decide whether it is a nickname or a bot.

                    if msg_split[0] not in chatbots:
                        a = ""
                        i = 0

                        #  Searching if the message from a client includes an activity that is in my list of activities
                        while i < len(boring):
                            if boring[i] in message.lower():
                                a = boring[i]

                            if fun[i] in message.lower():
                                a = fun[i]
                            i += 1

                        botmessage = ""

                        # Call the function for the bots that is in the chatroom/connected to the server.
                        if nickname.lower() == "rey":
                            botmessage = rey(a)

                        elif nickname.lower() == "fati":
                            botmessage = fati(a)

                        elif nickname.lower() == "z":
                            botmessage = z(a)

                        elif nickname.lower() == "jolly":
                            botmessage = jolly(a)

                        print(message)
                        client.send(botmessage.encode('utf-8'))

                    else:
                        time.sleep(0.5)
                        print(message)

                else:
                    print(message)
        except:
            #  Close Connection When Error
            print("An error occurred!")


#  Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))


#  Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

if nickname not in chatbots:
    send_thread = threading.Thread(target=write)
    send_thread.start()
