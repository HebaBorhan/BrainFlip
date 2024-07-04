#!/usr/bin/python3
"""Start a registration session"""
from flask import Blueprint, request, jsonify, render_template
from src.models import storage
import re
from src.models.user import User

register_bp = Blueprint("register", __name__)


@register_bp.route("/api/register", methods=["POST", "GET"])
def register_user():
    """Register a new user"""
    if request.method == "GET":
        return render_template('registration.html')

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    confirm_password = data.get("confirm_password")

    if not username or not email or not password or not confirm_password:
        return jsonify({"success": False, "message": "All fields are required"}), 400

    if password != confirm_password:
        return (
            jsonify({"success": False, "message": "Error: passwords don't match"}),
            400,
        )

    email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    if not re.match(email_regex, email):
        return jsonify({"success": False, "message": "Invalid email format"}), 400

    db = storage._DBStorage__session
    try:
        # Check for existing username
        existing_user = db.query(User).filter(User.username == username).first()
        if existing_user:
            return (
                jsonify({"success": False, "message": "Username is already used"}),
                400,
            )

        # Check for existing email
        existing_email = db.query(User).filter(User.email == email).first()
        if existing_email:
            return (
                jsonify({"success": False, "message": "Email is already registered"}),
                400,
            )

        # Create new user
        new_user = User(username=username, email=email, password=password)
        storage.new(new_user)
        storage.save()
        return (
            jsonify(
                {"success": True, "message": "User registered completed successfully"}
            ),
            201,
        )
    except Exception as e:
        return jsonify({"success": False, "message": "Server error"}), 500
