run:
	uvicorn app.main:app --reload --port 5173
init:
	alembic init alembic
revision:
	alembic revision --autogenerate
upgrade:
	alembic upgrade head
history:
	alembic history
startapp:
	python3 manage.py startapp expense
migrate:
	python3 manage.py migrate
makemigrations:
	python3 manage.py makemigrations
runserver:
	python3 manage.py runserver
createsuperuser:
	python manage.py createsuperuser --username admin --email admin@example.com
jazzmin:
	pip install django-jazzmin