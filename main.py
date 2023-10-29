# from flask import Flask, render_template, redirect, url_for
# from dbservice import db, Households  # Import your SQLAlchemy models

# app = Flask(__name__)
# app.secret_key = "Mackaysltd"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Kevin254!@localhost:5432/mackaysdb"

# # Initialize SQLAlchemy
# db.init_app(app)

# @app.route("/")
# def mackays():
#     return render_template("index.html")

# @app.route("/households")
# def households():
#     # Query the database for household records
#     records = Households.query.all()
#     households = [house.__dict__ for house in records]  # Convert SQLAlchemy objects to dictionaries
#     return render_template("households.html", households=households)

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()  # Create the database tables if they don't exist
#     app.run(debug=True)
from flask import render_template,redirect,url_for,session
from dbservice import *

app.secret_key = "Mackaysltd"


@app.route("/")
def mackays():
    return render_template("index.html")


@app.route("/households")
def households():
    records = Households.query.all()
    households=[house for house in records]
    return render_template("households.html", households=households)

if __name__== "__main__":
    app.run(debug=True)