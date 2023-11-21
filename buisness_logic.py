from init.settings import session
from utils import photo_changes
from jwt_op import jwt_en
from models import User
import base64


def pasting(credentials):
    session.add(User(login=credentials[0], email=credentials[1],
                     password=credentials[2], classroom=credentials[3]))
    session.commit()


def login(credentials):
    x = session.query(User.email).filter(User.email == credentials[0], User.password == credentials[1]).first()
    if x:
        return {"msg": "logged in",
                "cookie": jwt_en({"email": x[0]})}
    return {"msg": "registered"}


def photo_upl(credentials):
    user = session.query(User).filter(User.email == credentials[2]["cookie"]["email"]).first()
    user.photo1 = credentials[0].file.read() if credentials[0] else None
    user.photo2 = credentials[1].file.read() if credentials[1] else None
    session.commit()


def main_page(skip: int = 0, limit: int = 9):
    users = session.query(User).offset(skip).limit(limit).all()
    for user in users:
        photo_changes(user)
    return users


def user_page(id_):
    user = session.query(User).filter(id=id_).first()
    photo_changes(user)
    return user