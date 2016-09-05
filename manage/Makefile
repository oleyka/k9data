VERSION=$(/usr/bin/env python setup.py --version)

default: test

venv:
	virtualenv venv
	. venv/bin/activate
	pip install -Ur requirements.txt

test: venv
	python setup.py pytest

download: venv
	python download.py

clean:
	@find . -name \*.pyc -exec rm -v '{}' +
	@find . -name __pycache__ -prune -exec rm -vfr '{}' +
	@find . -name .cache -prune -exec rm -vfr '{}' +
	@rm -rf build bdist cover dist sdist
	@rm -rf .tox .eggs
	@rm -rf distribute-* *.egg *.egg-info

.PHONY: default test clean
