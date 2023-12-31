from sqlalchemy.exc import SQLAlchemyError
from src.db import session
from src.mod import User


if __name__ == '__main__':
    login = input('Login: ')
    password = input('Password: ')
    try:
        user = User(login=login, password=password)
        session.add(user)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(e)
    finally:
        session.close()
