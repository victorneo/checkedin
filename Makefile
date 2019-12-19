all: test

dev:
	python manage.py runserver

test:
	-rm test.sqlite3
	pytest --cov=.
