from flask import Flask
from login import app as login_app
from game import app as game_app
from leaderboard import leaderboard_bp
from dashboard import dashboard_bp
from registration import app as registration_app

app = Flask(__name__)

# Register blueprints
app.register_blueprint(login_app)
app.register_blueprint(game_app)
app.register_blueprint(leaderboard_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(registration_app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
