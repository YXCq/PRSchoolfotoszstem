from init.settings import session, redis_conn
from Logic.utils import photo_changes, error_parsing, hashing, send_email, creating_cookies
from Logic.jwt_op import jwt_en
from App.models import User, Class


def pasting(credentials):
    """User registration function,
     uses random hash values to guarantee secure login"""
    login_, email, classroom, token, status = credentials[0], \
        credentials[1], credentials[2], credentials[3], credentials[4]
    user = session.query(User).filter(User.email == email).first()

    if user:
        return {"msg": "This email is already used"}

    elif token["user_status"] == 0:
        return {"msg": "You don`t have access to do that"}

    else:
        session.add(User(login=login_, email=email,
                         classroom=classroom, status=status))
        rand = hashing(login_)
        redis_conn.set(rand, email)
        send_email(rand, email)
        session.commit()
        return {"msg": "You successfully registered"}


def login(credentials):
    """User login that is using jwt-token convertation and sending cookie data"""
    mail, password = credentials[0], credentials[1]
    x = session.query(User).filter(User.email == mail, User.password == hashing(password)).first()
    if x:
        return {"msg": "logged in",
                "cookie": jwt_en(creating_cookies(x.email, x.status, x.classroom))}
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


def main_page(skip: int = 0, limit: int = 9, user: dict = False, id_: int = ...):
    """Shows all users using pagination with frontend"""
    try:
        users = session.query(User).filter(User.classroom == user["classroom"]).offset(skip).limit(limit).all()
        if users.classroom != id_ and user["user_status"] == 0 or user["user_status"] == 1:
            return {"msg": "that`s not your class!"}
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


def class_create(name, token, teacher_id):
    teacher = session.query(User).filter(User.email == teacher_id).first()
    if token["user_status"] == 0 or token["user_status"] == 1:
        return {"msg": "You don`t have access to do that"}

    elif teacher is None:
        return {"msg": "this user does not exist"}

    else:
        session.add(Class(name=name, teacher=teacher_id))
        session.commit()
        id_ = session.query(Class.id).order_by(Class.id.desc()).first()
        teacher.classroom = id_[0]
        session.commit()
        return {"msg": "You successfully registered class"}


def all_classes(token):
    if token["user_status"] == 0 or token["user_status"] == 1:
        return {"msg": "you dont have access to that action"}
    else:
        return session.query(Class).all()


def all_teachers(token):
    if token["user_status"] == 0 or token["user_status"] == 1:
        return {"msg": "you dont have access to that action"}
    else:
        return session.query(User).filter(User.status == 1).all()


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

