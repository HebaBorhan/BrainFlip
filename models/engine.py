#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import os
"""from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review"""


class DBStorage:
    """This class manages storage of hbnb models in db"""
    __engine = None
    __session = None

    def __init__(self):
        """inistantiate the engine"""
        load_dotenv()
        user = os.getenv('BF_MYSQL_USER')
        password = os.getenv('BF_MYSQL_PWD')
        host = os.getenv('BF_MYSQL_HOST')
        database = os.getenv('BF_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """Apply query on the current database session"""
        objects = {}
        classes = (State, City, User, Place, Amenity, Review)
        if cls:
            query = self.__session.query(cls)
            for obj in query.all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        else:
            for types in classes:
                query = self.__session.query(types)
                for obj in query.all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.close()
