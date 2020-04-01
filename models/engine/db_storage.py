#!/usr/bin/python3
"""This is the file DBStorage class for AirBnB
"""
import json
from models.base_model import BaseModel, State
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review

import sqlalchemy
from sqlalchemy import (create_engine)

class DBStorage:
    """This class
    Attributes:
        __engine: conection to data base
        __session: session in data base
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes instance of DBStorage
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                           format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                  HBNB_MYSQL_HOST, HBNB_MYSQL_DB
                           ), pool_pre_ping=True)

        if HBNB_ENV == "test":
            self.__engine.drop_all()

        # create a session
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=engine)
        self.__session = Session()

    def all(self, cls=None):
        """List all data in table
        Arguments:
            cls: input class
        Return:
            dictionary
        """

        all_list = []
        all_dict = {}
        if cls is Not None:
            all_list = self.__session.query(cls).all()
            for cls_obj in all_list:
                key = "{}.{}".format(cls_obj.__class__.__name__, cls_obj.id)
                all_dict[key] = cls_obj
        else:
            all_list.append(self.__session.query(User).all())
            all_list.append(self.__session.query(State).all())
            all_list.append(self.__session.query(City).all())
            all_list.append(self.__session.query(Amenity).all())
            all_list.append(self.__session.query(Place).all())
            all_list.append(self.__session.query(Review).all())

            for query_list in all_list:
                for cls_obj in query_list:
                    key = "{}.{}".format(cls_obj.__class__.__name__, cls_obj.id)
                    all_dict[key] = cls_obj

    def new(self, obj):
        """Add the object to the current database session
        Argument:
            obj: input object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        """
        if obj is not None:
            pass
        
