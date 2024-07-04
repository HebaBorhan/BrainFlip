#!/usr/bin/python3
"""Start a leaderboard session"""
from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from models import storage
from models.user import User
from models.score import Score

leaderboard_bp = Blueprint('leaderboard', __name__)

@leaderboard_bp.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()

@leaderboard_bp.route('/leaderboard', methods=['GET'])
def leaderboard():
    """Display the leaderboard"""
    top_scores = storage.get_top_scores()
    return render_template('leaderboard.html', scores=top_scores)

@leaderboard_bp.route('/api/leaderboard', methods=['GET'])
def api_leaderboard():
    """Display the ditales within leaderboard"""
    top_scores = storage.get_top_scores()
    leaderboard_data = [{
        'rank': idx + 1,
        'username': score.user.username,
        'score': score.score
    } for idx, score in enumerate(top_scores)]
    return jsonify(leaderboard_data)
