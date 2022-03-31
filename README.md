# Individual Portfolio Assignment  
# Reyhan Acet - s351912

An implementation of a chat-room server with 4 "bad bots". 
These bots are functions that take a string as input and return
one depending on which action that shows up in the input.
The activities that the bots react to are play, cook, train, code,
draw, clean, read, work, walk, sleep.

Each client can connect from its own terminal.
Several terminal windows can run in parallel, 
connecting different bots/other clients to the same server.
No command line parameters are necessary.

The task specified that you are free to decide how and when to end the connection.
Therefore, I chose the most intuitive option, which is to simply close/terminate the terminal
for the given bot/client.
