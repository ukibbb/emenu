lint:
	bash -c "\
		isort .;\
		black .;\
		flake8 .;\
		pydocstyle .;\
	"

test:
	docker-compose run --rm backend pytest --cov=.

superuser:
	docker-compose run --rm backend python manage.py createsuperuser

migrate:
	docker-compose run --rm backend python manage.py migrate

sh:
	docker-compose run --rm backend sh

migrations:
	cd backend && python manage.py makemigrations

attach:
	docker attach backend
