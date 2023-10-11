SHELL := /bin/bash
.DEFAULT_GOAL := build

init:
	pip install -r requirements.txt

env:
	@if [ -d ./venv ]; then echo 'run source ./venv/bin/activate'; else python3.11 -m venv venv; fi

clean:
	@if [ -d ./venv ]; then rm -rf ./venv; fi
	@if [ -d ./build ]; then rm -rf ./build; fi
	@if [ -d ./dist ]; then rm -rf ./dist; fi
	@rm -rf $(shell find . -name '*__pycache__*')
	@rm -rf $(shell find . -name '*.egg*')
build:
	python3 -m build

dev-install:
	pip install -e .
