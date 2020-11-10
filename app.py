import os
import sys
sys.path.append(f'{os.getcwd()}/../')
from __init__ import app
from hashlib import md5
from pipelines import ResultsPipelines
from flask import jsonify, request
from datetime import datetime


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """
    This is the home route endpoint.
    this route reads the readme file for better understanding of the methods the api has.
        :method: GET:
        :return:
        """
    return "CAT,AGS"

@app.route('/gett', methods=['GET'], strict_slashes=False)
def home2():
    """
    This is the home route endpoint.
    this route reads the readme file for better understanding of the methods the api has.
        :method: GET:
        :return:
        """
    res = dict(request.args)
    return jsonify(res)

@app.route('/writeMessage', methods=['POST'], strict_slashes=False)
def write_message():
    """
    This is the writeMessage route endpoint.
    this route takes the following parameters: user, password, receiver, message, subject
        :method: POST:
        :return:
        """
    res = dict(request.args)
    if not all(x in res.keys() for x in ['user', 'password', 'receiver', 'message', 'subject']):
        return jsonify({'error': {'status_code': 406, 'description': 'the query you have entered is not valid'}})
    user, password, receiver, message, subject = res['user'], res['password'], res['receiver'], res['message'], res['subject']
    pass_hash = md5(password.encode()).hexdigest()
    res = ResultsPipelines().write_message(user, pass_hash, receiver, message, subject, creation_date=datetime.now())
    if res:
        return jsonify({'success writing message': {'to': receiver, 'message': message, 'subject': subject}})
    else:
        return jsonify({'error': {'user_error': 407, 'description': 'the user/password you have entered is not valid'}})


@app.route('/readMessage', methods=['POST'], strict_slashes=False)
def get_message():
    """
    This is the readMessage route endpoint.
    this route takes the following parameters: user, password
        :method: POST:
        :param: user
        :param: password
        :return: if query is valid then a json with unread message will return
        """
    res = dict(request.args)
    if not all(x in res.keys() for x in ['user', 'password']):
        return jsonify({'error': {'status_code': 406, 'description': 'the query you have entered is not valid'}})

    user, password = res['user'], res['password']
    pass_hash = md5(password.encode()).hexdigest()
    message = ResultsPipelines().read_message(user, pass_hash)
    if message:
        post = {'sender': message.sender, 'receiver': message.receiver, 'message': message.message,
                'subject': message.subject, 'creation_date': message.creation_date}
    
        return jsonify(post)
    elif not message and type(message) is not bool:
        return jsonify({'no unread mails': True})
    else:
        return jsonify({'error': {'user_error': 407, 'description': 'the user/password you have entered is not valid'}})


@app.route('/getAllMessages', methods=['POST'], strict_slashes=False)
def get_all_messages():
    """
    This is the getAllMessages route endpoint.
    this route takes the following parameters: user, password
        :method: POST:
        :param: user
        :param: password
        :return: if query is valid then a json with all messages will return
        """
    res = dict(request.args)
    if not all(x in res.keys() for x in ['user', 'password']):
        return jsonify({'error': {'status_code': 406, 'description': 'the query you have entered is not valid'}})

    user, password = res['user'], res['password']
    pass_hash = md5(password.encode()).hexdigest()
    messages = ResultsPipelines().get_all_messages(user, pass_hash)
    if messages:
        post = [{'sender': message.sender, 'receiver': message.receiver, 'message': message.message,
                 'subject': message.subject, 'creation_date': message.creation_date} for message in messages]
        return jsonify(post)
    elif not messages and type(messages) is not bool:
        return jsonify({'no mails': True})
    else:
        return jsonify({'error': {'user_error': 407, 'description': 'the user/password you have entered is not valid'}})


@app.route('/getUnreadMessages', methods=['POST'], strict_slashes=False)
def get_unread_messages():
    """
    This is the getUnreadMessages route endpoint.
    this route takes the following parameters: user, password
        :method: POST:
        :param: user
        :param: password
        :return: if query is valid then a json with all unread messages will return
        """
    res = dict(request.args)
    if not all(x in res.keys() for x in ['user', 'password']):
        return jsonify({'error': {'status_code': 406, 'description': 'the query you have entered is not valid'}})

    user, password = res['user'], res['password']
    pass_hash = md5(password.encode()).hexdigest()
    messages = ResultsPipelines().get_unread_messages(user, pass_hash)
    if messages:
        post = [{'sender': message.sender, 'receiver': message.receiver, 'message': message.message,
             'subject': message.subject, 'creation_date': message.creation_date} for message in messages]
        return jsonify(post)
    elif not messages and type(messages) is not bool:
        return jsonify({'no unread messages': True})
    else:
        return jsonify({'error': {'user_error': 407, 'description': 'the user/password you have entered is not valid'}})


@app.route('/deleteMessage', methods=['POST'], strict_slashes=False)
def delete_massage():
    """
    This is the deleteMessage route endpoint.
    this route takes the following parameters: user, password, message_id and deletes the message if the query is valid
        :method: POST:
        :param: user
        :param: password
        :param: message_id
        :return:
        """
    res = dict(request.args)
    if not all(x in res.keys() for x in ['user', 'password', 'message_id']):
        return jsonify({'error': {'status_code': 406, 'description': 'the query you have entered is not valid'}})

    user, password, message_id = res['user'], res['password'], res['message_id']
    pass_hash = md5(password.encode()).hexdigest()
    res = ResultsPipelines().delete_message(user, pass_hash, message_id)
    if res:
        return jsonify({'success deleting message': {'message_id': message_id, 'user': user}})
    else:
        return jsonify({'error': {'user_error': 407, 'description': 'the user/password you have entered is not valid'}})


@app.route('/signUp', methods=['POST'], strict_slashes=False)
def sign_up():
    """
    This is the signUp route endpoint.
    this route takes the following parameters: user, password and creates a user if the query is valid.
    :param: POST:
    :return:
    """
    res = dict(request.args)
    print(res)
    if not all(x in res.keys() for x in ['user', 'password']):
        return jsonify({'error': {'status_code': 406, 'description': 'the query you have entered is not valid'}})

    user, password = res['user'], res['password']
    pass_hash = md5(password.encode()).hexdigest()
    res = ResultsPipelines().sign_up(user, pass_hash)
    if res:
        return jsonify({'success signing up': {'user': user}})
    else:
        return jsonify({'error': {'user_error': 408, 'description': 'the user you have entered already exists'}})


if __name__ == '__main__':
    app.run(debug=False)
