default: build
venv:
	python3 -m venv --clear venv
setup: requirements.txt
	. venv/bin/activate; pip3 install --upgrade pip wheel setuptools
	. venv/bin/activate; pip3 install -Ur requirements.txt
serve:
	. venv/bin/activate; mkdocs serve
build:
	. venv/bin/activate; mkdocs build

