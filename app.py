import os
from flask import Flask
if os.path.exists("env.py"):
    import env


# Create an instance of flask
app = Flask(__name__)


@ app.route("/")
def test():
    return "testing routes"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)