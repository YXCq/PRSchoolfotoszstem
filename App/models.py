from init.settings import Base
from sqlalchemy.types import LargeBinary
from sqlalchemy import Column, String, Integer, SmallInteger
from pydantic import BaseModel


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    photo1 = Column(LargeBinary, nullable=True)
    photo2 = Column(LargeBinary, nullable=True)
    login = Column(String)
    email = Column(String)
    password = Column(String)
    classroom = Column(String)
    status = Column(SmallInteger)


class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher = Column(String)


class Login(BaseModel):
    login: str
    password: str
