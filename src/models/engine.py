#!/usr/bin/python3
"""This module defines a class to manage database storage for BrainFlip"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import os
from src.models.base_model import Base
from src.models.user import User
from src.models.score import Score


classes = {"User": User, "Score": Score}


class DBStorage:
    """This class manages storage of BrainFlip models in db"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate the engine"""
        load_dotenv('brainflip.env')
        user = os.getenv("BF_MYSQL_USER")
        password = os.getenv("BF_MYSQL_PWD")
        host = os.getenv("BF_MYSQL_HOST")
        database = os.getenv("BF_MYSQL_DB")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{database}", pool_pre_ping=True
        )

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.close()

    def delete(self, obj=None):
        """Delete an object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def get_user_by_username(self, username):
        """Retrieve a user by username"""
        return self.__session.query(User).filter(User.username == username).first()

    def get_user_by_email(self, email):
        """Retrieve a user by email"""
        return self.__session.query(User).filter(User.email == email).first()

    def get_top_scores(self, limit=15):
        """Retrieve the top scores"""
        return (
            self.__session.query(Score).order_by(Score.score.desc()).limit(limit).all()
        )
