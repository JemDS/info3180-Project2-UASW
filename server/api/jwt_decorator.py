from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import app
import sys
# imports for PyJWT authentication
import jwt
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        # return 401 if token is not passed
        if not token:
            return jsonify({"message": "Token is missing !!"}), 401
        try:
            # decoding the payload to fetch the stored details
            print(token, file=sys.stderr)
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        
            current_user = User.query.filter_by(id=data["public_id"]).first()
        except Exception as e:
            print(str(e), file=sys.stderr)
            return jsonify({"message": "Token is invalid !!"}), 401
        # returns the current logged in users contex to the routes
        return f(current_user, *args, **kwargs)

    return decorated