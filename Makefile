setup:
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	./manage.py makemigrations
	./manage.py migrate
	./manage.py runserver

freeze:
	pip freeze > requirements.txt

runserver:
	./manage.py runserver 127.0.0.1:8001

venv:
	source venv/bin/activate

install:
	pip install -r requirements.txt

test:
	./manage.py test
