#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship
from os import environ


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        __tablename__: table name in MySQL
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        reviews: list of rewiews
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if environ.get('HBNB_TYPE_STORAGE') == "db":
        cities = relationship('City', foreign_keys=[city_id],
                              back_populates='places')
        user = relationship('User', foreign_keys=[user_id],
                            back_populates='places')
    else:
        @property
        def reviews(self):
            """getter attribute reviews that returns the list of Review instances
            with place_id equals to the current Place.id
            Return:
            list of reviews
            """
            list_reviews = []
            all_reviews = models.storage.all(Review)
            for review_item in all_reviews.items():
                if review_item.place_id == self.id:
                    list_review.append(review_item)

            return list_review
