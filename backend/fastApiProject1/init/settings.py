from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fastapi import FastAPI
import configparser
import redis

app = FastAPI()

config = configparser.ConfigParser()
config.read('init/config.ini')

SECRET_KEY = config.get('Secret_key', 'KEY')
GmailKey = config.get('Gmail', 'GPW')
GmailAdress = config.get('Gmail', 'Adress')

engine = create_engine("postgresql://docker:DataBasePassword5432@localhost:5432/school_album")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

redis_conn = redis.StrictRedis(host='localhost', port=6379, db=0)
