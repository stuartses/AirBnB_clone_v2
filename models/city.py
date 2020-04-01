#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = sqlalchemy.Column(sqlalchemy.String(length=128), nullable=False)
    state_id = sqlalchemy.Column(sqlalchemy.String(length=60),
                                 sqlalchemy.ForeignKey('states.id'),
                                 nullable=False)
