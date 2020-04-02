#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        __tablename__: table name in MySQL
        place_amenities: relationship many to many with Place
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if environ.get('HBNB_TYPE_STORAGE') == "db":
        place_amenities = relationship("Place", secondary=place_amenity)
