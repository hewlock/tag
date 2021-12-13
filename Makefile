VERSION = $(shell python3 tag.py version)
DATE = $(shell date -u '+%Y-%m-%d')

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
	pod2man --center='tag manual' \
		--date='tag-$(VERSION)' \
		--release=$(DATE) \
		docs/tag.pod docs/tag.1

readme:
	cat ./docs/readme.md > README.md
	./docs/readme.bash >> README.md

test:
	python -m unittest

.PHONY: help clean docs init man readme test
