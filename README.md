# Sockets-Tests
This project holds two seperate projects, the goal is to create a server, which users can conenct to, and exchange messages in real time.<br />
<br />
The Two projects present Here are: <br />
### Django channels <br />
Held in every file and folder except the one named "easy" (For task difficulty).<br />
Which uses Django channels in order to create a WebSocket which passes the received messages in real time.<br />
[Couldn't test it well so i passed to the other task, the reason being the Websocket status jumps from 0 to 2 directly]<br /><br />
To test it out, do: <br />

  $ python3 -m venv env<br />
  $ source env/bin/activate<br />
  $ pip3 install django<br />
  $ pip3 install channels<br />
  $ python3 manage.py migrate<br />
  $ python3 manage.py runserver<br />
  
 ### Python sockets <br />
 This one uses Python sockets, with a server, that manages and communicates with clients, and a client side, which can be as many as we want, it helps us pick a name and directly have real time access to messages provided by other connected clients.
 
 To test it out, just run the server and as many Clients as you want. <br />
# Folders and files
* folder: easy: Python sockets task
* Everything else: Django Channels task
