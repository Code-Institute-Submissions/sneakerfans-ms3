import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


# Create an instance of flask
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# Instance of pymongo
mongo = PyMongo(app)


@app.route("/")
# Home page
@app.route("/get_sneakers")
def get_sneakers():
    # Show 6 random documents from sneakers collection
    # Credit:
    # https://stackoverflow.com/questions/2824157/random-record-from-mongodb
    sneakers = mongo.db.sneakers.aggregate(
        [{"$sample": {"size": 6}}])
    return render_template("sneakers.html", sneakers=sneakers)


# Browse collection page
@app.route("/all_sneakers")
def all_sneakers():
    # Find all sneakers in database
    sneakers = list(mongo.db.sneakers.find())
    return render_template("all-sneakers.html", sneakers=sneakers)


# Sneaker description page
@app.route("/full_info/<sneaker_id>")
def full_info(sneaker_id):
    # Check if object id is valid
    # or call call 400 error handler
    if not is_object_id_valid(sneaker_id):
        abort(400)
    # Find specific sneakers from collection using primary id
    # if not found return a 404 redirect
    sneaker = mongo.db.sneakers.find_one_or_404({"_id": ObjectId(sneaker_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "full-info.html", sneaker=sneaker, categories=categories)


# Search box
@app.route("/search", methods=["GET", "POST"])
def search():
    # Retrieve user query from search form
    query = request.form.get("query")
    # Find sneakers from text index search based on user form input
    sneakers = list(mongo.db.sneakers.find({"$text": {"$search": query}}))
    return render_template("all-sneakers.html", sneakers=sneakers)


# Sign Up page
@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("sign-up.html")


# Log in page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Make sure password input matches database password
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}!".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # Password does not match
                flash("Incorrect password and/or username")
                return redirect(url_for("login"))

        else:
            # username does not exist
            flash("Incorrect password and/or username")
            return redirect(url_for("login"))

    return render_template("login.html")


# My sneakers page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if is_authenticated():
        sneakers = list(mongo.db.sneakers.find())
        # Retrieve active username from database
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        if session["user"]:
            return render_template(
                "profile.html", username=username, sneakers=sneakers)

    return redirect(url_for("login"))


# Log out
@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add sneakers form
@app.route("/add_sneakers", methods=["GET", "POST"])
def add_sneakers():
    if request.method == "POST":
        # Create dictionary to collect all form data
        add = {
            "category_name": request.form.get("category_name"),
            "shoe_name": request.form.get("shoe_name"),
            "release_year": request.form.get("release_year"),
            "shoe_description": request.form.get("shoe_description"),
            "image_url": request.form.get("image_url"),
            "date_added": datetime.today().replace(microsecond=0),
            "user": session["user"]
        }

        # Check if shoe name already exists in database
        existing_sneaker = mongo.db.sneakers.find_one(
            {"shoe_name": request.form.get("shoe_name").lower()})

        if existing_sneaker:
            flash("Sneakers already added! Try a different sneaker")
            return redirect(url_for("add_sneakers"))

        # Insert all form data to mongodb sneakers collection
        mongo.db.sneakers.insert_one(add)
        flash("Your sneakers have been added!")
        return redirect(url_for("get_sneakers"))
    # Create categories variable to alphabetically sort html select
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add-sneakers.html", categories=categories)


# Edit sneakers form
@app.route("/edit_sneakers/<sneaker_id>", methods=["GET", "POST"])
def edit_sneakers(sneaker_id):
    if request.method == "POST":
        # Create dictionary to collect all form data
        add = {
            "category_name": request.form.get("category_name"),
            "shoe_name": request.form.get("shoe_name"),
            "release_year": request.form.get("release_year"),
            "shoe_description": request.form.get("shoe_description"),
            "image_url": request.form.get("image_url"),
            "date_added": datetime.today().replace(microsecond=0),
            "user": session["user"]
        }

        # Update mongodb sneakers collection
        mongo.db.sneakers.update({"_id": ObjectId(sneaker_id)}, add)
        flash("Your sneakers have been updated!")

    sneaker = mongo.db.sneakers.find_one({"_id": ObjectId(sneaker_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit-sneakers.html", sneaker=sneaker, categories=categories)


# Delete sneakers
@app.route("/delete_sneakers/<sneaker_id>")
def delete_sneakers(sneaker_id):
    mongo.db.sneakers.remove({"_id": ObjectId(sneaker_id)})
    flash("Sneakers successfully deleted")
    return redirect(url_for("get_sneakers"))


# 404 error page
# Credit: https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
@app.errorhandler(404)
def page_not_found(e):
    # Show user error page
    return render_template('404.html'), 404


# 400 error page
# Credit: Guido Cecilio mentor
@app.errorhandler(400)
def bad_request(e):
    # Show bad request page
    return render_template('400.html'), 400


# 500 error page
# Credit: Guido Cecilio mentor
@app.errorhandler(Exception)
def internal_server_error(e):
    # Show internal server/application error page
    return render_template('500.html'), 500


# Check if the id is a valid object in database
# Credit: Guido Cecilio mentor
def is_object_id_valid(id_value):
    """ Validate is the id_value is a valid ObjectId
    """
    return id_value != "" and ObjectId.is_valid(id_value)


# Check if user is authenticated
# Credit Guido Cecilio Mentor
def is_authenticated():
    """ Ensure that user is authenticated
    """
    return 'user' in session


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
