#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        __tablename__: name of mySQL table
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
        places: relationship with Place
        reviews: relationship with Review
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    if environ.get('HBNB_TYPE_STORAGE') == "db":
        places = relationship('Place', back_populates='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete-orphan')
