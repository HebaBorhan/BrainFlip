#!/usr/bin/python3
"""This module instantiates an object of class DBStorage"""
from models.engine import DBStorage
from dotenv import load_dotenv
from flask import Flask
from web_flask.game import app as game_blueprint
from web_flask.dashboard import dashboard_bp
from web_flask.leaderboard import leaderboard_bp


load_dotenv()
storage = DBStorage()
storage.reload()

app = Flask(__name__)

app.register_blueprint(game_blueprint)
app.register_blueprint(dashboard_bp)
app.register_blueprint(leaderboard_bp)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
