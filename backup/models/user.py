#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.score import Score
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship



class User(BaseModel, Base):
    """Represents a user for registration"""
    __tablename__ = 'users'
    
    username = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    scores = relationship('Score', backref='user', cascade='all, delete')

    def __init__(self, *args, **kwargs):
        """Initialize user"""
        super().__init__(*args, **kwargs)
