from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fastapi import FastAPI
import configparser

app = FastAPI()

config = configparser.ConfigParser()
config.read('init/config.ini')

SECRET_KEY = config.get('Secret_key', 'KEY')

engine = create_engine("postgresql://docker:8uR%23m!9PzL$2@localhost:5432/school_album")
Base = declarative_base()
session = sessionmaker(bind=engine)()
