

freeze:
	pip freeze > requirements.txt

runserver:
	./manage.py runserver 127.0.0.1:8001

install:
	pip install -r requirements.txt

project:
	django-admin startproject config .

migrate:
	./manage.py migrate

test:
	./manage.py test
