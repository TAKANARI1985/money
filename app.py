from flask import *
app = Flask(__name__)


@app.route("/")
def money():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
