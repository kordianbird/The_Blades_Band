import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/news1")
def newsone():
    return render_template("news1.html")


@app.route("/news2")
def newstwo():
    return render_template("news2.html")


@app.route("/news3")
def newsthree():
    return render_template("news3.html")


@app.route("/news4")
def newsfour():
    return render_template("news4.html")


@app.route("/index")
def index():
    comments = mongo.db.comments.find()
    return render_template("index.html", comments=comments)


@app.route("/news")
def news():
    return render_template("news.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/concerts")
def concerts():
    return render_template("concerts.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/1html")
def onehtml():
    return render_template("1.html")


@app.route("/2html")
def twohtml():
    return render_template("2.html")


@app.route("/3html")
def threehtml():
    return render_template("3.html")


@app.route("/4html")
def fourhtml():
    return render_template("4.html")


@app.route("/5html")
def fivehtml():
    return render_template("5.html")


@app.route("/6html")
def sixhtml():
    return render_template("6.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)