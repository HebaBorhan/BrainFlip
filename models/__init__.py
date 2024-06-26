#!/usr/bin/python3
"""This module instantiates an object of class FileStorage & DBStorage"""
from models.engine import DBStorage
from dotenv import load_dotenv
import os

load_dotenv()
storage = DBStorage()
storage.reload()
