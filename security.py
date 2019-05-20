from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    """
    Function that gets called when the user calls the /auth endpoint with their username and password.

    :param username: User's name in string format.
    :param password: User's password in string format.
    :return: User object, if authentication was successful. Else, None.

    """

    user = UserModel.find_by_username(username)

    if user and safe_str_cmp(user.password, password):
        return user

    return None


def identity(payload):

    """
    Function that gets called when the user has already authenticated and JWT has verified the authorization header.
    :param payload: A dictionary with 'identity' as key, which is the user ID.
    :return: User object.

    """

    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

