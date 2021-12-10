default: help

help:
	@echo 'make:           Display help.'
	@echo 'make clean:     Delete compiled files.'
	@echo 'make init:      Install requirements.txt.'
	@echo 'make readme:    Create README documentation.'
	@echo 'make test:      Run unit tests.'

clean:
	find . -depth -name __pycache__ -type d -exec rm -r -- {} \;

init:
	pip install -r requirements.txt

readme:
	cat ./docs/readme.md > README.md
	./docs/readme.bash >> README.md

test:
	python -m unittest

.PHONY: help clean init readme test
