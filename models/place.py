#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
import sqlalchemy


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
    city_id = sqlalchemy.Column(sqlalchemy.String(length=60),
                                sqlalchemy.ForeignKey('cities.id'),
                                nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.String(length=60),
                                sqlalchemy.ForeignKey('users.id'),
                                nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(length=128),
                             nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String(length=1024),
                                    nullable=False)
    number_rooms = sqlalchemy.Column(sqlalchemy.Integer, default=0,
                                     nullable=False)
    number_bathrooms = sqlalchemy.Column(sqlalchemy.Integer, default=0,
                                         nullable=False)
    max_guest = sqlalchemy.Column(sqlalchemy.Integer, default=0,
                                  nullable=False)
    price_by_night = sqlalchemy.Column(sqlalchemy.Integer, default=0,
                                       nullable=False)
    latitude = sqlalchemy.Column(sqlalchemy.Float,
                                 nullable=False)
    longitude = sqlalchemy.Column(sqlalchemy.Float,
                                  nullable=False)
    reviews = sqlalchemy.orm.relationship('Review', backref='place',
                                          cascade='all, delete')

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

    amenity_ids = []
