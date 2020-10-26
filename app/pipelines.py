from server.models import Messages, Users
from sqlalchemy import create_engine
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.orm import sessionmaker


class ResultsPipelines:
    def __init__(self):
        engine = create_engine('sqlite:///messages.db', connect_args={"check_same_thread": False}, poolclass=SingletonThreadPool)
        self.Session = sessionmaker(bind=engine)

    def _insert_item(self, item):
        """
        this function takes a Table Object as an argument and inserts it into the database
        :param item:
        :return:
        """
        try:
            session = self.Session()
            session.add(item)
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)
        finally:
            session.close()

    def _update_message(self, user, message_id=False, read=True):
        """
        this is an update method which takes a user and an optional of message id and if to mark the read True or False
        this method updates the messages read column to True(default)
        :param user:
        :param message_id:
        :param read:
        :return:
        """
        try:
            session = self.Session()

            if message_id:
                session.query(Messages).filter(Messages.id == message_id and Messages.receiver == user).update({'read': read})
            else:
                session.query(Messages).filter(Messages.receiver == user).update({'read': read})

            session.commit()
        except Exception as e:
            session.rollback()
            print(e)
        finally:
            session.close()

    def _delete_message(self, user, message_id):
        """
        this is the delete message method. this method takes a user as an argument and deletes the message by the
        message id identifier
        :param user:
        :param message_id:
        :return:
        """
        try:
            session = self.Session()
            session.query(Messages).filter(Messages.id == message_id and Messages.receiver == user).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)
        finally:
            session.close()

    def write_message(self, user, password, receiver, message, subject, creation_date):
        """
        this method takes the following arguments and creates a message object and inserts it into the database
        :param user:
        :param password:
        :param receiver:
        :param message:
        :param subject:
        :param creation_date:
        :return:
        """
        if self.check_user_password(user, password):
            result = Messages(user, receiver, message, subject, creation_date)
            self._insert_item(result)

    def read_message(self, user, password):
        """
        this method takes a user and a password and checks if its valid, and if so checks the first unread message
        and updates the read column of the message to True
        :param user:
        :param password:
        :return:
        """
        if self.check_user_password(user, password):
            session = self.Session()
            message = session.query(Messages).filter(Messages.receiver == user).filter(Messages.read == 0).first()
            if message:
                self._update_message(user=user, message_id=message.id)
            return message

    def check_user_password(self, user, password):
        """
        this method takes a user and password as an argument and checks if the user and the password is in the users
        data base
        :param user:
        :param password:
        :return:
        """
        session = self.Session()
        return session.query(Users).filter(Users.password == password and Users.user == user).first()

    def get_all_messages(self, user, password):
        """
        this method takes a user and password, and checks if the user and password are in the data base and if so
        retrieves all the messages sent to the user
        :param user:
        :param password:
        :return:
        """
        if self.check_user_password(user, password):
            session = self.Session()
            self._update_message(user)
            return session.query(Messages).filter(Messages.receiver == user).all()

    def get_unread_messages(self, user, password):
        """
        this method takes a user and password, and checks if the user and password are in the data base and if so
        retrieves all the unread messages sent to the user
        :param user:
        :param password:
        :return:
        """
        if self.check_user_password(user, password):
            session = self.Session()
            results = session.query(Messages).filter(Messages.receiver == user).filter(Messages.read == 0).all()
            self._update_message(user)
            return results

    def delete_message(self, user, password, message_id):
        """
        this method takes a user and a password and checks if the user and password match in the users table
        and if so it will delete the message id if the message id is connected to the user.
        :param user:
        :param password:
        :param message_id:
        :return:
        """
        if self.check_user_password(user, password):
            self._delete_message(user, message_id)

    def sign_up(self, user, password):
        """
        this method takes a user and a password and checks if it exists in the database, if not then it will
        create a new Users object containing the user and password and will insert it into the database
        :param user:
        :param password:
        :return:
        """
        if not self.Session().query(Users).filter(Users.user == user).first():
            user = Users(user, password)
            self._insert_item(user)


if __name__ == '__main__':
    pass
