#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Class defining Amenity"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity',
                                  viewonly=True)


    def __init__(self,*args,**kwargs):
        """New Amenity instance"""
        super().__init__(**kwargs)
