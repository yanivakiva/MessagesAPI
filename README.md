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

How to install
==============
clone the reopsitory into your directory. <br></br>
cd into the server directory and run the following command in the terminal: <br></br>
export FLASK_APP=REST.py <br></br>
to run the flask framework run flask run in the terminal. <br></br>

How to use
============
### cURL
(to use the commands to query the api the flask app needs to be running)
you can use the cURL command through the terminal to query the api. <br></br>
e.g.:
<br></br>
to interact with getAddress: curl -F "file=@</PATH/TO/YOUR/CSV/FILE>" http://127.0.0.1:5000/api/getAddress  <br></br>
to interact with getResult: curl http://127.0.0.1:5000/api/getResult?result_id=<RESULT_ID> 


Compatibility
=============
Messages's rest api requires Python 3.6+


Requirements
===========
flask, flask-alchemy, SQLAlchemy


