#!/usr/bin/python3
"""Start a dashboard session"""
from flask import Blueprint, render_template, redirect, request, url_for
from src.models import storage
from src.models.user import User
from src.models.score import Score


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():
    """Render the dashboard page"""
    username = request.cookies.get("username")
    if not username:
        return redirect(
            url_for("game.login")
        )  # Redirect to login if user is not authenticated

    user = storage.get_user_by_username(username)
    if not user:
        return redirect(url_for("game.login"))  # Redirect to login if user is not found

    # Get the 10 highest scores for the user
    get_scores = storage.session.query(Score).filter_by(user_id=user.username)
    top_scores = get_scores.order_by(Score.score.desc()).limit(10).all()

    return render_template("dashboard.html", user=user, top_scores=top_scores)
