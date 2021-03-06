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
    if is_authenticated():
        return redirect(url_for("profile"))

    if request.method == "POST":
        username = request.form.get("username").lower()
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": username})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        register = {
            "username": username,
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = username
        flash("Registration Successful!")
        return redirect(url_for("profile"))

    return render_template("sign-up.html")


# Log in page
@app.route("/login", methods=["GET", "POST"])
def login():
    if is_authenticated():
        return redirect(url_for("profile"))

    if request.method == "POST":
        username = request.form.get("username").lower()
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": username})

        if existing_user:
            # Make sure password input matches database password
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = username
                # Send Admin to manage categories
                if session['user'] == "admin":
                    flash("Welcome Admin")
                    return redirect(url_for('get_categories'))
                flash("Welcome, {}!".format(username.capitalize()))
                return redirect(url_for("profile"))
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
@app.route("/profile", methods=["GET", "POST"])
def profile():
    # Check if user name is authenticated
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
    # If user is authenticated
    if is_authenticated():
        # Remove user from session cookies
        flash("You have successfully logged out")
        session.pop("user")

    return redirect(url_for("login"))


# Add sneakers form
@app.route("/add_sneakers", methods=["GET", "POST"])
def add_sneakers():
    # Check if user is authenticated
    if is_authenticated():
        if request.method == "POST":
            # Create dictionary to collect all form data
            add = {
                "category_name": request.form.get("category_name").lower(),
                "shoe_name": request.form.get("shoe_name").lower(),
                "release_year": request.form.get("release_year"),
                "shoe_description": request.form.get(
                    "shoe_description"),
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
            return redirect(url_for('profile'))
    # Create categories variable to alphabetically sort html select
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add-sneakers.html", categories=categories)


# Edit sneakers form
@app.route("/edit_sneakers/<sneaker_id>", methods=["GET", "POST"])
def edit_sneakers(sneaker_id):
    # Check if user is authenticated
    if is_authenticated():
        # Check if object id is valid
        if not is_object_id_valid(sneaker_id):
            abort(400)
        if request.method == "POST":
            # Create dictionary to collect all form data
            add = {
                "category_name": request.form.get("category_name").lower(),
                "shoe_name": request.form.get("shoe_name").lower(),
                "release_year": request.form.get("release_year"),
                "shoe_description": request.form.get("shoe_description"),
                "image_url": request.form.get("image_url"),
                "date_added": datetime.today().replace(microsecond=0),
                "user": session["user"]
            }

            # Update mongodb sneakers collection
            mongo.db.sneakers.update({"_id": ObjectId(sneaker_id)}, add)
            flash("Your sneakers have been updated!")
            return redirect(url_for('profile'))

    sneaker = mongo.db.sneakers.find_one_or_404({"_id": ObjectId(sneaker_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit-sneakers.html", sneaker=sneaker, categories=categories)


# Delete sneakers
@app.route("/delete_sneakers/<sneaker_id>")
def delete_sneakers(sneaker_id):
    # Check if user is authenticated
    if is_authenticated():
        # Check if object id is valid
        if not is_object_id_valid(sneaker_id):
            abort(400)
        mongo.db.sneakers.remove({"_id": ObjectId(sneaker_id)})
        flash("Sneakers successfully deleted")
        return redirect(url_for('profile'))

    flash("You must be a user to delete sneakers")
    return redirect(url_for("login"))


# Manage Categories
@app.route("/get_categories")
def get_categories():
    # Check if user is authenticated
    if not is_authenticated():
        flash("You must be authenticated to list categories")
        return redirect(url_for("login"))

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    if session["user"] == "admin":
        return render_template("categories.html", categories=categories)
    flash("Only Admin can access categories!")
    return redirect(url_for("profile"))


# Add category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # Check if user is authenticated
    if is_authenticated():
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name").lower()
            }

            # Check if category name already exists in database
            existing_category = list(mongo.db.categories.find(category))
            if len(existing_category) > 0:
                flash("Category already exists! Try again")
                return redirect(url_for("add_category"))
            mongo.db.categories.insert_one(category)
            flash("New category added")
            return redirect(url_for("get_categories"))

        return render_template("add-category.html")


# Edit category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # Check if user is authenticated
    if is_authenticated():
        # Check if object id is valid
        if not is_object_id_valid(category_id):
            abort(400)
        if request.method == "POST":
            query = {
                "category_name": request.form.get("category_name").lower()
            }
            # Check if category name already exists in database
            existing_category = list(mongo.db.categories.find(query))
            if len(existing_category) > 0:
                flash("Category already exists! Try again")
                return redirect(url_for("get_categories"))
            mongo.db.categories.update({"_id": ObjectId(category_id)}, query)
            flash("Category has been updated!")
            return redirect(url_for("get_categories"))
    category = mongo.db.categories.find_one_or_404(
        {"_id": ObjectId(category_id)})
    return render_template("edit-category.html", category=category)


# Delete category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    # Check if user is authenticated
    if is_authenticated():
        # Check if object id is valid
        if not is_object_id_valid(category_id):
            abort(400)
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("Category successfully deleted")
        return redirect(url_for("get_categories"))

    flash("You must be an admin to delete categories")
    return redirect(url_for("get_categories"))


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
            debug=False)
