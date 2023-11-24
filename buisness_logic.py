from init.settings import session
from utils import photo_changes
from jwt_op import jwt_en
from models import User


def pasting(credentials):
    """User registration function"""

    if "@" in credentials[1]:
        session.add(User(login=credentials[0], email=credentials[1],
                         password=credentials[2], classroom=credentials[3]))
        session.commit()
        return {"msg": "You succesfully registered"}
    else:
        return {"msg": "please write an email type"}


def login(credentials):
    """User login that is using jwt-token convertation and sending cookie data"""

    x = session.query(User.email).filter(User.email == credentials[0], User.password == credentials[1]).first()
    if x:
        return {"msg": "logged in",
                "cookie": jwt_en({"email": x[0]})}
    return {"msg": "something went wrong"}


def photo_upl(credentials):
    # TODO: password hashing if needed, also as a great idea make gmail password updating

    p1, p2, info, password = credentials[0], credentials[1], credentials[2], credentials[3]
    user = session.query(User).filter(User.email == info["cookie"]["email"]).first()
    if password:
        user.password = password
    user.photo1 = p1.file.read() if p1 else None
    user.photo2 = p2.file.read() if p2 else None
    session.commit()
    return {"msg": "profile updating went succesfully"}


def main_page(skip: int = 0, limit: int = 9):
    """Shows all users using pagination with frontend"""

    users = session.query(User).offset(skip).limit(limit).all()
    for user in users:
        photo_changes(user)
    return users


def user_page(id_):
    user = session.query(User).filter(User.id == id_).first()
    return photo_changes(user)
