all: test

dev:
	python manage.py runserver

test:
	-rm test.sqlite3
	pytest --reuse-db --cov=.
