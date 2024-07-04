#!/usr/bin/python3
"""Start a score recording session for a game"""
from flask import request, jsonify, Blueprint
from src.models.user import User
from src.models.score import Score
from src.models import storage


game_bp = Blueprint("game", __name__)


# @game_bp.teardown_appcontext
# def teardown_db(exception):
#     """remove the current SQLAlchemy Session"""
#     storage.close()


@game_bp.route("/api/user", methods=["GET"])
def get_user():
    user_id = request.cookies.get("user_id")
    if not user_id:
        return jsonify({"message": "User not authenticated"}), 401

    user = storage.get(User, user_id)
    if user:
        return jsonify({"username": user.username}), 200

    return jsonify({"message": "User not found"}), 404


@game_bp.route("/api/score", methods=["POST"])
def add_score():
    """record the score"""
    data = request.get_json()
    username = request.cookies.get("username")  # Assuming user_id is stored in cookies
    if not username:
        return jsonify({"message": "User not authenticated"}), 401

    score_value = data.get("score")
    if score_value is None:
        return jsonify({"message": "Score is required"}), 400

    user = storage.get(User, username=username)
    if user:
        score = Score(user_id=user.username, score=score_value)
        storage.new(score)
        storage.save()
        return jsonify({"message": "Score added successfully"}), 201
    return jsonify({"message": "User not found"}), 404


@game_bp.route("/api/scores", methods=["GET"])
def get_scores():
    """Fetch scores ordered by score in descending order"""
    try:
        scores = storage.session.query(Score).order_by(Score.score.desc()).all()
        return jsonify([score.to_dict() for score in scores]), 200
    except Exception as e:
        print(f"Error fetching scores: {str(e)}")
        return jsonify({"message": "Failed to fetch scores"}), 500
