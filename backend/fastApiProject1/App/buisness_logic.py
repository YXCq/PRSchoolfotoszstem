from init.settings import session, redis_conn
from Logic.utils import photo_changes, error_parsing, hashing, send_email
from Logic.jwt_op import jwt_en
from App.models import User


def pasting(credentials):
    """User registration function"""
    login_, email, classroom = credentials[0], credentials[1], credentials[2]

    if session.query(User).filter(User.email == email).first():
        return {"msg": "This email is already used"}

    else:
        session.add(User(login=login_, email=email,
                         classroom=classroom))
        rand = hashing(login_)
        redis_conn.set(rand, email)
        send_email(rand, email)
        session.commit()
        return {"msg": "You succesfully registered"}


def login(credentials):
    """User login that is using jwt-token convertation and sending cookie data"""

    x = session.query(User.email).filter(User.email == credentials[0], User.password == hashing(credentials[1])).first()
    if x:
        return {"msg": "logged in",
                "cookie": jwt_en({"email": x[0]})}
    return {"msg": "something went wrong"}


def photo_upl(credentials):
    """photo profile uploading, also password updating"""
    p1, p2, info, password = credentials[0], credentials[1], credentials[2], hashing(credentials[3])
    user = session.query(User).filter(User.email == info["cookie"]["email"]).first()
    if password:
        user.password = password
    user.photo1 = p1.file.read() if p1 else None
    user.photo2 = p2.file.read() if p2 else None
    session.commit()
    return {"msg": "profile updating went succesfully"}


def main_page(skip: int = 0, limit: int = 9):
    """Shows all users using pagination with frontend"""
    try:
        users = session.query(User).offset(skip).limit(limit).all()

        for user in users:
            photo_changes(user)

        return users

    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback the session in case of an exception
        session.rollback()
        return "An error occurred. Please try again."

    finally:
        session.close()


def user_page(id_):
    """user page"""
    try:
        user = session.query(User).filter(User.id == id_).first()

        if user:
            photo_changes(user)
            return user
        else:
            return "There is no user with that ID."

    except Exception as e:
        error_parsing(e)

    finally:
        session.close()


def profile_connect(text, password):
    """connecting profile """
    try:
        mail = redis_conn.get(text).decode('utf-8')
        user = session.query(User).filter(User.email == mail).first()
        user.password = hashing(password)
        session.commit()
        redis_conn.delete(text)
        return {"msg": "password updated"}
    except AttributeError:
        return {"msg": "code is not available anymore"}

