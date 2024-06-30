#!/usr/bin/python3
"""This module defines a class score"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Score(BaseModel, Base):
    """Represents a score for a user"""
    __tablename__ = 'scores'
    
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    score = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize score"""
        super().__init__(*args, **kwargs)
