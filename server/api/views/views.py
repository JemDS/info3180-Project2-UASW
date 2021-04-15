"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your apilication.
"""

from api import app, db, login_manager
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    make_response,
    jsonify,
)
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy import or_
from api.forms import LoginForm
from api.models import User, Car, Favourite
from werkzeug.security import generate_password_hash, check_password_hash
from api.jwt_decorator import token_required
from datetime import datetime, timedelta
import jwt
import sys

###
# Routing for your apilication.
###


@app.route("/")
def home():
    """Render website's home page."""
    return render_template("home.html")


@app.route("/about/")
def about():
    """Render the website's about page."""
    return render_template("about.html")


@app.route("/api/auth/login", methods=["GET", "POST"])
def login():
    form = request.form
    if request.method == "POST":
        # change this to actually validate the entire form submission
        # and not just one field

        # Get the username and password values from the form.
        username = form["username"].lower()
        password = form["password"]  # could use request.form['password']

        # using your model, query database for a user based on the username
        # and password submitted. Remember you need to compare the password hash.
        # You will need to import the appropriate function to do so.
        # Then store the result of that query to a `user` variable so it can be
        # passed to the login_user() method below.

        user = User.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.password, password):
            login_user(user)

            token = jwt.encode(
                {
                    "public_id": user.id,
                    "exp": datetime.utcnow() + timedelta(minutes=30),
                },
                app.config["SECRET_KEY"],
            )
            return make_response(jsonify({"token": token, "user": user.to_json()}), 201)
    return make_response(
        "Could not verify",
        403,
        {"WWW-Authenticate": 'Basic realm ="Wrong Password !!"'},
    )


@app.route("/api/register", methods=["POST"])
def signup():
    form = request.form
    if request.method == "POST":
        try:
            username = form["username"]
            password = form["password"]
            firstName = form["first_name"]
            lastName = form["last_name"]
            email = form["email"]
        except KeyError:
            return make_response(
                "Error on Server",
                403,
                {"WWW-Authenticate": 'Basic realm ="Wrong Password !!"'},
            )
        user = User(
            first_name=firstName,
            last_name=lastName,
            username=username.lower(),
            password=password,
            biography=None,
            email=email,
            photo=None,
            location=None,
        )

        db.session.add(user)
        db.session.commit()
        return make_response(
            "User created sucessfully",
            201,
        )


@app.route("/api/cars", methods=["POST", "GET"])
@login_required
@token_required
def getCars(current_user):
    print(current_user, file=sys.stderr)
    if request.method == "GET":
        cars = Car.query.all()
        return make_response(
            jsonify({"cars": [car.to_json() for car in cars]}),
            201,
        )
    elif request.method == "POST":
        form = request.form
        user_id = form["user_id"]
        make = form["make"]
        model = form["model"]
        colour = form["colour"]
        year = form["year"]
        transmission = form["transmission"]
        car_type = form["car_type"]
        price = form["price"]
        photo = form["photo"]
        description = form["description"]

        car = Car(
            user_id=user_id,
            make=make,
            model=model,
            colour=colour,
            year=year,
            transmission=transmission,
            car_type=car_type,
            price=price,
            photo=photo,
            description=description,
        )

        db.session.add(car)
        db.session.commit()
        return make_response(
            jsonify({"car": car.to_json()}),
            201,
        )


@app.route("/api/cars/<car_id>", methods=["GET"])
@login_required
@token_required
def getCarById(current_user, car_id):
    if request.method == "GET":
        car = Car.query.filter_by(id=car_id).first()
        if car is not None:
            return make_response(
                jsonify(car.to_json()),
                201,
            )
        else:
            return make_response(
                "Car not foud",
                403,
            )


@app.route("/api/cars/<car_id>/favourite", methods=["POST"])
@login_required
@token_required
def addFavouriteCarById(current_user, car_id):
    if request.method == "POST":
        favourite = Favourite.query.filter_by(car_id=car_id, user_id=int(current_user.get_id())).first()
        print(favourite,file=sys.stderr)
        if favourite is None:  
            try:

                db.session.add(favourite)
                db.session.commit()
                return make_response(
                        "Added to Favourites",
                        201,
                    )
            except:
                make_response(
                    "Car or User not foud",
                    403,
                )
        else:
             return make_response(
                        "Already a favourite for user",
                        403,
                    )

@app.route("/api/search", methods=["GET"])
@login_required
@token_required
def search(current_user):
    if request.method == "GET":
        query= request.args.get('query')
        
        search = "%{}%".format(query)
        cars = Car.query.filter(or_(Car.make.like(search), Car.model.like(search)))
        return make_response(
            jsonify({"cars": [car.to_json() for car in cars]}),
            201,
        )

@app.route("/api/users/<user_id>", methods=["GET"])
@login_required
@token_required
def getUserById(current_user,user_id):
    if request.method == "GET":
        user = User.query.filter_by(id=user_id).first()
        if user is not None:
            return make_response(
                jsonify(user.to_json()),
                201,
            )
        else:
            return make_response(
                "Car not foud",
                403,
            )


@app.route("/api/users/<user_id>/favourites", methods=["GET"])
@login_required
@token_required
def getCarsByUserFavourite(current_user,user_id):
    if request.method == "GET":
        cars = db.session.query(
           Car
        ).join(Favourite).filter(Favourite.user_id == int(current_user.get_id()))


        if cars is not None:
            return make_response(
                jsonify({"cars": [car.to_json() for car in cars]}),
                201,
            )
        else:
            return make_response(
                "Car not foud",
                403,
            )



@app.route("/api/auth/logout")
def logout():
    logout_user()
    flash("You've been logged out: Have a great day!", "info")
    return make_response(
        "User logged out sucessfully",
        201,
    )


# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


###
# The functions below should be applicable to all Flask apps.
###


@app.route("/<file_name>.txt")
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + ".txt"
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "public, max-age=0"
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")