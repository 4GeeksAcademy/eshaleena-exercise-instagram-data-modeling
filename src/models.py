import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique = True, nullable=False)
    firstname = Column(String(250), unique = True, nullable=False)
    lastname = Column(String(250), unique = True, nullable=False)
    email = Column(String(250), unique = True, nullable=False)
    password = Column(String(250), nullable = False)


class Media(Base):
    __tablename__ = 'chararcter'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique = True, nullable = False)
    birth_year = Column(Integer, nullable = False)
    homeworld = Column(String(250), nullable = False)
    person_id = Column(Integer, ForeignKey('character.id'))
    person = relationship(Chararcter)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique = True, nullable=False)
    password = Column(String(250), nullable = False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique = True, nullable=False)
    password = Column(String(250), nullable = False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
