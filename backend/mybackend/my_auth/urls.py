from django.urls import include, path

from my_auth.views import profile, login_view

urlpatterns = [
    path('login', login_view, name='login_view'),
    path('profile', profile, name='profile'),
]
