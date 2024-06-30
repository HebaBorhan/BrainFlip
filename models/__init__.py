#!/usr/bin/python3
"""This module instantiates an object of class DBStorage"""
from models.engine import DBStorage
from dotenv import load_dotenv
from flask import Flask
from web_flask.game import app as game_blueprint


load_dotenv()
storage = DBStorage()
storage.reload()

app = Flask(__name__)

app.register_blueprint(game_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
