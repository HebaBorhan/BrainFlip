from flask import Flask, render_template

app = Flask(__name__)

# Register blueprints

with app.app_context():

    from src.login import login_bp
    from src.game import game_bp

    from src.dashboard import dashboard_bp
    from src.leaderboard import leaderboard_bp
    from src.registration import register_bp

    app.register_blueprint(login_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(leaderboard_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(register_bp)

    @app.route("/", methods=["GET"])
    @app.route("/landing", methods=["GET"])
    def landing():
        return render_template("landing.html")

    @app.teardown_appcontext
    def teardown_db(exception):
        """remove the current SQLAlchemy Session"""
        from src.models import storage

        storage.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
