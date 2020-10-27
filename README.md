Messages's REST API
================
this project includes a rest api which exposes six methods. <br></br>
writeMessage, readMessage, getAllMessages, getUnreadMessages, deleteMessage, signUp

### writeMessage
this method is only accessible by a POST request
the method writeMessage requires user, password, receiver, message, subject as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary which will report on the success
of the request. if not, it will report the query was not valid.

### readMessage
this method is only accessible by a POST request
the method readMessage requires user and password as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary which will contain one unread message. <br></br>
if not, it will report the query was not valid.


### getAllMessages
this method is only accessible by a POST request
the method getAllMessages requires user and password as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary which will contain all message sent to the user. <br></br>
if not, it will report the query was not valid.


### getUnreadMessages
this method is only accessible by a POST request
the method getUnreadMessages requires user and password as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary which will contain all unread message sent to the user. <br></br>
if not, it will report the query was not valid.


### deleteMessage
this method is only accessible by a POST request
the method deleteMessage requires user, password and message_id as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary reporting that the message was deleted. <br></br>
if not, it will report the query was not valid.


### SignUp
this method is only accessible by a POST request
the method SignUp requires user and password as parameters
and returns a dictionary. <br></br>
if the parameters are valid, the api will return a dictionary reporting that signup was successful. <br></br>
if not, it will report the query was not valid.


How to use
============
### Postman
you can query the Messages REST API using postman <br></br>
at: http://127.0.0.1:5000 if your'e running the flask server locally. <br></br>
the flask server is also hosted at Heroku at: <br></br> 
https://akiva-messages-api.herokuapp.com/
<br></br>
and can be queried like so:


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

