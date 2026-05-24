from flask import Flask, render_template

# updated by codex: switched to package-safe imports
from api_time_machine.routes.api_routes import api
from api_time_machine.routes.ai_routes import ai
from api_time_machine.routes.replay_routes import replay

app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(ai)
app.register_blueprint(replay)


@app.route("/")
def dashboard():

    return render_template("dashboard.html")


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=5000)
