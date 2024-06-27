#!/usr/bin/python3
from flask import Flask, request, jsonify
from models import engine, storage
import re


app = Flask(__name__)


@app.route("/api/register", methods=["POST"])
def register_user():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"success": False, "message": "All fields are required"}), 400

    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if not re.match(email_regex, email):
        return jsonify({"success": False, "message": "Invalid email format"}), 400

    db = next(get_db())
    try:
        # Check for existing username
        existing_user = db.query(models.User).filter(models.User.username == username).first()
        if existing_user:
            return jsonify({"success": False, "message": "Username already exists"}), 400

        # Check for existing email
        existing_email = db.query(models.User).filter(models.User.email == email).first()
        if existing_email:
            return jsonify({"success": False, "message": "Email already registered"}), 400

        # Create new user
        new_user = models.User(username=username, email=email, password=password)
        db_storage.new(new_user)
        db_storage.save()
        return jsonify({"success": True, "message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"success": False, "message": "Server error"}), 500

if __name__ == "__main__":
    app.run(port=5000)