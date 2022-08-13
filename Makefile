

freeze:
	pip freeze > requirements.txt

runserver:
	./manage.py runserver 127.0.0.1:8001

install:
	pip install -r requirements.txt

makemigrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate

test:
	./manage.py test
