#!/usr/bin/python3
"""Start a login session"""
from flask import Blueprint, request, jsonify, render_template
from src.models import storage
import re
from src.models.user import User

login_bp = Blueprint("login", __name__)





@login_bp.route("/api/login", methods=["POST", "GET"])
def login_user():
    """Login existed user"""
    if request.method == "GET":
        return render_template('login.html')
    data = request.get_json()

    username_or_email = data.get("username_or_email")
    password = data.get("password")

    if not username_or_email or not password:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Username/email and password are required",
                }
            ),
            400,
        )

    db = storage._DBStorage__session
    try:
        # Check if username_or_email is an email address
        if re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", username_or_email):
            user = db.query(User).filter(User.email == username_or_email).first()
        else:
            user = db.query(User).filter(User.username == username_or_email).first()

        if not user or not user.verify_password(password):
            return (
                jsonify(
                    {"success": False, "message": "Invalid username/email or password"}
                ),
                401,
            )

        # Here you can set up a session or token for authentication
        return jsonify({"success": True, "message": "Login successful"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": "Server error"}), 500


@login_bp.route("/api/forgot_password", methods=["POST"])
def forgot_password():
    """Reset the password"""
    data = request.get_json()
    email = data.get("email")

    if not email:
        return jsonify({"success": False, "message": "Email is required"}), 400

    db = storage._DBStorage__session
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return jsonify({"success": False, "message": "Email not found"}), 404

        # Implement password reset logic (e.g., sending reset link or code)
        return jsonify({"success": True, "message": "Password reset link sent"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": "Server error"}), 500


if __name__ == "__main__":
    login_bp.run(host="0.0.0.0", port=5000)
