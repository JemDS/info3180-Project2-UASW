# info3180-Project2-UASW
For this project we will create a fictional Auto Sales site called United Auto  Sales that will allow users to add cars that they want to sell, search for  available cars and be able to view some more information on those cars.  Users can also add a car to their favourites so they can quickly get back to  it.


# Flask Server
## Config
### Basic DB configuration
``
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://[user]:[password]@localhost/[db_name]"``
## Setup

### Start virtualenv
`` cd server cd venv cd scripts activate ``

### Install Requirements

``pip install -r requirements.txt``


### Run Migration
``python flask-migrate.py db upgrade``

### Launch Server

``cd server python run.py``
