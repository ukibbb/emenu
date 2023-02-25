lint:
	bash -c "\
		isort .;\
		black .;\
		flake8 .;\
		pydocstyle .;\
	"
