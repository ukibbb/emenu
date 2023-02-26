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
