PATH:=venv/bin:$(PATH)
VERSION=$(/usr/bin/env python setup.py --version)

K9BREED?="TEST"
K9DATAPATH?=$(PWD)/data

default: test

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	venv/bin/pip install -Ur requirements.txt
	source venv/bin/activate

test: venv
	./venv/bin/python setup.py pytest

download: venv
	cd k9data; k9data_path=$(K9DATAPATH) ../venv/bin/python download.py

unzip: venv
	cd k9data; k9data_path=$(K9DATAPATH) ../venv/bin/python unzip.py
	cd $(K9DATAPATH); find . -name \*.zip -exec rm -v '{}' +

sanitize: venv
	@cd k9data; k9data_path=$(K9DATAPATH) k9data_breed=$(K9BREED) ../venv/bin/python sanitize.py

clean:
	@find . -name \*.pyc -exec rm -v '{}' +
	@find . -name __pycache__ -prune -exec rm -vfr '{}' +
	@find . -name .cache -prune -exec rm -vfr '{}' +
	@rm -rf build bdist cover dist sdist
	@rm -rf .tox .eggs
	@rm -rf distribute-* *.egg *.egg-info

.PHONY: default test download unzip clean
