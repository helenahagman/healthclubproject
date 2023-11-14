import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/member")
def member():
    return render_template("member.html")


@app.route("/personaltrainer")
def personaltrainer():
    return render_template("personaltrainer.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)