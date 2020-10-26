Messages's REST API
================
this project includes a rest api which exposes six methods. <br></br>
writeMessage, readMessage, getAllMessages, getUnreadMessages, deleteMessage, signUp
<br></br>

### writeMessage
<br></br>

this method is only accessible by a POST request
the method writeMessage requires user, password, receiver, message, subject as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary which will report on the success
of the request. if not, it will report the query was not valid.
<br></br>

### readMessage
<br></br>

this method is only accessible by a POST request
the method readMessage requires user and password as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary which will contain one unread message. <br></br>
if not, it will report the query was not valid.

<br></br>

### getAllMessages
<br></br>

this method is only accessible by a POST request
the method getAllMessages requires user and password as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary which will contain all message sent to the user. <br></br>
if not, it will report the query was not valid.

<br></br>

### getUnreadMessages
<br></br>

this method is only accessible by a POST request
the method getUnreadMessages requires user and password as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary which will contain all unread message sent to the user. <br></br>
if not, it will report the query was not valid.

<br></br>

### deleteMessage
<br></br>

this method is only accessible by a POST request
the method deleteMessage requires user, password and message_id as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary reporting that the message was deleted. <br></br>
if not, it will report the query was not valid.

<br></br>

### SignUp
<br></br>

this method is only accessible by a POST request
the method SignUp requires user and password as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary reporting that signup was successful. <br></br>
if not, it will report the query was not valid.

<br></br>

How to install
==============
<br></br>

clone the reopsitory into your directory. <br></br>
cd into the server directory and run the following command in the terminal: <br></br>
export FLASK_APP=REST.py <br></br>
to run the flask framework run flask run in the terminal. <br></br>
<br></br>

How to use
============
<br></br>

### Postman
<br></br>

you can query the Messages REST API using postman
<br></br>
e.g.:
<br></br>
to interact with writeMessage: <br></br>
<img src="https://i.imgur.com/kQsO1oW.png" width=500 />

<br></br>
to interact with readMessage: <br></br>
<img src="https://i.imgur.com/eB1BJuH.png" width=500 />

<br></br>
to interact with getAllMessages: <br></br>
<img src="https://i.imgur.com/D4EUkeC.png" width=500 />

<br></br>
to interact with getUnreadMessages: <br></br>
<img src="https://i.imgur.com/trklb2u.png" width=500 />

<br></br>
to interact with deleteMessage: <br></br>
<img src="https://i.imgur.com/FMZVkHx.png" width=500 />

<br></br>
to interact with signUp: <br></br>
<img src="https://i.imgur.com/rZAApOk.png" width=500 />

<br></br>

Compatibility
=============
<br></br>

Messages's rest api requires Python 3.6+

<br></br>

Requirements
===========
<br></br>

flask, flask-alchemy, SQLAlchemy


