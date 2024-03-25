.PHONY: run
run:
	python manage.py runserver

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: model
model: migrations migrate ;