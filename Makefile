VERSION = $(shell python -m tag version | head -n1)
DATE = $(shell date -u '+%B %Y')

default: help

help:
	@echo 'make:           Display help.'
	@echo 'make clean:     Delete compiled files.'
	@echo 'make init:      Install requirements.txt.'
	@echo 'make readme:    Create README documentation.'
	@echo 'make test:      Run unit tests.'

clean:
	find . -depth -name __pycache__ -type d -exec rm -r -- {} \;

docs: man readme

init:
	pip install -r requirements.txt

man:
	./docs/man.bash \
		| pod2man --center='tag manual' \
			--name='TAG' \
			--date='$(DATE)' \
			--release='$(VERSION)' \
		> docs/tag.1

readme:
	./docs/readme.bash > README.md

test:
	python -m unittest

.PHONY: help clean docs init man readme test
