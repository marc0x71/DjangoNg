import jwt
from rest_framework.authentication import BaseAuthentication
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions, HTTP_HEADER_ENCODING
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        # Return the failure reason instead of an HttpResponse
        return reason

class SafeJWTAuthentication(BaseAuthentication):
    
    keyword = 'Token'
    
    def authenticate(self, request):

        # headers/Authorization = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
        User = get_user_model()
        authorization_header = request.headers.get('Authorization', b'')

        if not authorization_header:
            return None
        
        data = authorization_header.split(' ')
        
        if data[0]!=self.keyword:
            return None
        
        try:
            access_token = data[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Invalid token')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        print(payload)
        
        user = User.objects.filter(id=payload['user_id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User is inactive')

        return (user, None)
