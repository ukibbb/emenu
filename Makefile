lint:
	bash -c "\
		isort .;\
		black .;\
		flake8 .;\
		pydocstyle .;\
	"

test:
	docker-compose run --rm backend pytest --cov=.
