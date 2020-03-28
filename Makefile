all: test

dev:
	python manage.py runserver

test:
	touch test.sqlite3
	-rm test.sqlite3
	pytest --reuse-db --cov=.

deps:
	pipenv lock --requirements > requirements.txt
