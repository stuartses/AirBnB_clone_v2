#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
import sqlalchemy


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        cities: list of cities in state
    """
    __tablename__ = "states"
    name = sqlalchemy.Column(sqlalchemy.String(length=128), nullable=False)
    cities = sqlalchemy.relationship('City', backref='state',
                                     cascade='all, delete')

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances
           with state_id equals to the current State.id
        Return:
            list of cities
        """
        list_cities = []
        all_cities = models.storage.all(City)
        for city_item in all_cities.items():
            if city_item.state_id == self.id:
                list_cities.append(city_item)

        return list_cities
