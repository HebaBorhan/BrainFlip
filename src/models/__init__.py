#!/usr/bin/python3
"""This module instantiates an object of class DBStorage"""
from .engine import DBStorage
from .base_model import BaseModel, Base
from .user import User
from .score import Score


storage = DBStorage()
storage.reload()
