#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
import sqlalchemy


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
    email = sqlalchemy.Column(sqlalchemy.String(length=128),
                              nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String(length=128),
                                 nullable=False)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=128),
                                   nullable=False)
    last_name = sqlalchemy.Column(sqlalchemy.String(length=128),
                                  nullable=False)
    places = sqlalchemy.orm.relationship('Place', backref='user',
                                         cascade='all, delete')
    reviews = sqlalchemy.orm.relationship('Review', backref='user',
                                          cascade='all, delete')
