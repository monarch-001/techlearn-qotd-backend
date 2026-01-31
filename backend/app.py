from flask import Flask
from backend.routes.qotd import qotd_bp
from backend.routes.submission import submission_bp
from backend.routes.stats import stats_bp
from backend.routes.leaderboard import leaderboard_bp
from backend.routes.meta import meta_bp
from backend.routes.users import users_bp

API_PREFIX = "/api/v1"

def create_app():
    app = Flask(__name__)

    app.register_blueprint(qotd_bp, url_prefix=API_PREFIX)
    app.register_blueprint(submission_bp, url_prefix=API_PREFIX)
    app.register_blueprint(stats_bp, url_prefix=API_PREFIX)
    app.register_blueprint(leaderboard_bp, url_prefix=API_PREFIX)
    app.register_blueprint(meta_bp, url_prefix=API_PREFIX)
    app.register_blueprint(users_bp, url_prefix=API_PREFIX)

    return app

# 👇 THIS IS THE CRITICAL LINE
app = create_app()

@app.route("/", methods=["GET"])
def index():
    return {
        "service": "TechLearn QOTD Backend",
        "status": "running",
        "version": "v1",
        "base_url": "/api/v1",
        "endpoints": {
            "daily_challenge": "/api/v1/daily-challenge",
            "submit_solution": "/api/v1/daily-challenge/submissions",
            "stats": "/api/v1/stats",
            "leaderboard": "/api/v1/leaderboard",
            "meta": "/api/v1/meta"
        }
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

