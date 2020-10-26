from __init__ import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(1000))
    receiver = db.Column(db.String(1000))
    message = db.Column(db.String(1000))
    subject = db.Column(db.String(1000))
    creation_date = db.Column(db.DateTime)
    read = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, sender, receiver, message, subject, creation_date, read=False):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.subject = subject
        self.creation_date = creation_date if creation_date else datetime.now()
        self.read = read


    def __repr__(self):
        return f"Messages('sender: {self.sender}', receiver: '{self.receiver}', message: {self.message}, " \
               f"subject: {self.subject}, creation_date: {self.creation_date}, read: {self.read}"


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(1000))
    password = db.Column(db.String(128))

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __repr__(self):
        return f"User('user: {self.user}', pass: '{self.password}'"


if __name__ == '__main__':
    pass