SHELL := /usr/bin/bash
init:
	pip install -r requirements.txt

env:
	@if [ -d ./venv ]; then source ./venv/bin/activate; else python3 -m venv venv &&	source ./venv/bin/activate && pip install -r requirements.txt; fi
	echo "Be sure to 'source ./venv/bin/activate"

clean:
	@if [ -d ./venv ]; then rm -rf ./venv; fi
	@if [ -d ./__pycache__ ]; then rm -rf ./__pycache__; fi