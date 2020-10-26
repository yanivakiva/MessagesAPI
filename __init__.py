from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'