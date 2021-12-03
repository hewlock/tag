default: help

help:
	@echo 'readme:  Create README documentation.'
	@echo 'test:    Run unit tests.'

readme:
	./README.sh > README.md

test:
	python -m unittest
