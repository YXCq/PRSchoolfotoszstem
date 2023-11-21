from init.settings import Base
from sqlalchemy.types import LargeBinary
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    photo1 = Column(LargeBinary)
    photo2 = Column(LargeBinary)
    login = Column(String)
    email = Column(String)
    password = Column(String)
    classroom = Column(String)


class Login(BaseModel):
    login: str
    password: str
