import jwt
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes 

from .authentication import SafeJWTAuthentication
from .serializers import UserSerializer
from .utils import generate_access_token, generate_refresh_token

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SafeJWTAuthentication])
@ensure_csrf_cookie
def profile(request):
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user })

@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    response = Response()
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required')

    user = User.objects.filter(username=username).first()
    if(user is None):
        raise exceptions.AuthenticationFailed('user not found')
    if (not user.check_password(password)):
        raise exceptions.AuthenticationFailed('wrong password')

    serialized_user = UserSerializer(user).data

    (access_token, token_expiration) = generate_access_token(user)
    (refresh_token, token_refresh) = generate_refresh_token(user)

    response.set_cookie(key='refreshtoken', value=refresh_token, path='/', max_age=settings.TOKEN_REFRESH_EXPIRATION, samesite='None', secure=True, httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_user,
        'expiration': token_expiration,
        'refresh': token_refresh
    }

    return response

@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def refresh_view(request):
    print("COOKIES",request.COOKIES)
    User = get_user_model()
    refresh_token = request.COOKIES.get('refreshtoken')
    if refresh_token is None:
        raise exceptions.AuthenticationFailed(
            'Authentication credentials were not provided!')
    
    try:
        payload = jwt.decode(refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed('Refresh token expired, please log in again')

    user = User.objects.filter(id=payload['user_id']).first()
    
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')

    if not user.is_active:
        raise exceptions.AuthenticationFailed('User is inactive')

    access_token = generate_access_token(user)
    return Response({'access_token': access_token})
