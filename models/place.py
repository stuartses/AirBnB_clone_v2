#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Table, Column, String, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship
from os import environ


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True))


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
        amenity_ids: list of Amenity ids
        reviews: list of rewiews
        amenities: relationship many to many with Amenity
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
    amenity_ids = []

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        cities = relationship('City', foreign_keys=[city_id],
                              back_populates='places')
        user = relationship('User', foreign_keys=[user_id],
                            back_populates='places')
        amenities = relationship("Amenity ", secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """getter attribute reviews that returns the list of Review
            instances with place_id equals to the current Place.id
            Return:
            list of reviews
            """
            list_reviews = []
            all_reviews = models.storage.all(Review)
            for review_item in all_reviews.items():
                if review_item.place_id == self.id:
                    list_review.append(review_item)

            return list_review

        @property
        def amenities(self):
            """Getter attribute amenities that returns the list of Amenity
            instances based on the attribute amenity_ids that contains all
            Amenity.id linked to the Place

            Return:
            list of amenities
            """
            list_amenities = []
            for amenity_obj in amenity_ids:
                if amenity_obj.id == self.id:
                    list_amenities.append(amenity_obj)

            return list_amenities

        @amenities.setter
        def amenities(self, amenity_obj):
            """Setter attribute amenities that handles append method for adding
            an Amenity.id to the attribute amenity_ids
            """
            if amenity_obj.__class__.name == "Amenity":
                self.amenity_ids.append(amenity_obj)
