import datetime
import jwt
from django.conf import settings


def generate_access_token(user):

    expiration = datetime.datetime.now() + datetime.timedelta(seconds=settings.TOKEN_CREATION_EXPIRATION)
    access_token_payload = {
        'user_id': user.id,
        'exp': expiration,
        'iat': datetime.datetime.now(),
    }
    access_token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm='HS256') #.decode('utf-8')
    return (access_token, expiration)


def generate_refresh_token(user):
    expiration = datetime.datetime.now() + datetime.timedelta(seconds=settings.TOKEN_REFRESH_EXPIRATION)
    refresh_token_payload = {
        'user_id': user.id,
        'exp': expiration,
        'iat': datetime.datetime.now()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm='HS256') #.decode('utf-8')

    return (refresh_token, expiration)
