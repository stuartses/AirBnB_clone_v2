#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
import sqlalchemy


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        __tablename__: name of mySQL table
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"
    text = sqlalchemy.Column(sqlalchemy.String(length=1024), nullable=False)
    place_id = sqlalchemy.Column(sqlalchemy.String(length=60),
                                 sqlalchemy.ForeignKey('places.id'),
                                 nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.String(length=60),
                                sqlalchemy.ForeignKey('users.id'),
                                nullable=False)
