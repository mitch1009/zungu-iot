import json

from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql import roles

from main.config import jwt
from main.model import User


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    """

    :param user:
    :return:
    """
    return user


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    """

    :param _jwt_header:
    :param jwt_data:
    :return:
    """
    try:
        identity = jwt_data["sub"]
        return User.query.filter_by(account_number=identity).one_or_none()
    except NoResultFound as e:
        print(e)
        return None


@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    """

    :param jwt_header:
    :param jwt_payload:
    :return:
    """
    return {"message": jwt_payload, "success": False}, 401
