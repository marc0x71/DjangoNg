# Backend

## Installazione
```shell
cd backend/
python3 -m venv DjangoNg
source DjangoNg/bin/activate
pip install django djangorestframework django-cors-headers requests whitenoise 
django-admin startproject mybackend
cd mybackend/
./manage.py makemigrations
./manage.py migrate
./manage.py startapp my_app
```

## Avvio server
```shell
cd backend/
python3 -m venv DjangoNg
source DjangoNg/bin/activate
cd mybackend/
./manage.py startapp my_app
```
