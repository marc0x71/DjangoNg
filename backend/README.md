# Backend

## Installazione
```shell
cd backend/
python3 -m venv env
source env/bin/activate
pip install django djangorestframework django-cors-headers requests whitenoise 
django-admin startproject mybackend
cd mybackend/
./manage.py startapp my_app
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```

## Avvio server
```shell
cd backend/
source env/bin/activate
cd mybackend/
./manage.py runserver
```
