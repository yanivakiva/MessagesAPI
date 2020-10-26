import os
import sys
sys.path.append(f'{os.getcwd()}/../')
from __init__ import app
from hashlib import md5
from server.pipelines import ResultsPipelines
from flask import jsonify, request
from datetime import datetime


@app.route('/writeMessage', methods=['GET'], strict_slashes=False)
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
    ResultsPipelines().write_message(user, pass_hash, receiver, message, subject, creation_date=datetime.now())
    return jsonify({'success writing message': {'to': receiver, 'message': message, 'subject': subject}})


@app.route('/readMessage', methods=['GET'], strict_slashes=False)
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
    post = {'sender': message.sender, 'receiver': message.receiver, 'message': message.message,
            'subject': message.subject, 'creation_date': message.creation_date}
    return jsonify(post)


@app.route('/getAllMessages', methods=['GET'], strict_slashes=False)
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
    post = [{'sender': message.sender, 'receiver': message.receiver, 'message': message.message,
            'subject': message.subject, 'creation_date': message.creation_date} for message in messages]
    return jsonify(post)


@app.route('/getUnreadMessages', methods=['GET'], strict_slashes=False)
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
    post = [{'sender': message.sender, 'receiver': message.receiver, 'message': message.message,
             'subject': message.subject, 'creation_date': message.creation_date} for message in messages]
    return jsonify(post)


@app.route('/deleteMessage', methods=['GET'], strict_slashes=False)
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
    if not all(x in res.keys() for x in ['user', 'password', 'messagee_id']):
        return jsonify({'error': {'status_code': 406, 'description': 'the query you have entered is not valid'}})

    user, password, message_id = res['user'], res['password'], res['message_id']
    pass_hash = md5(password.encode()).hexdigest()
    ResultsPipelines().delete_message(user, pass_hash, message_id)
    return jsonify({'success deleting message': {'message_id': message_id, 'user': user}})


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
    ResultsPipelines().sign_up(user, pass_hash)
    return jsonify({'success signing up': {'user': user}})


if __name__ == '__main__':
    app.run(debug=True)
