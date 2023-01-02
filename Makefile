SHELL := /usr/bin/bash
init:
	pip install -r requirements.txt

env:
	@if [ -d ./venv ]; then source ./venv/bin/activate; else python3 -m venv venv && source ./venv/bin/activate && pip install -r requirements.txt; fi
	@echo -e "\n\nBe sure to run 'source ./venv/bin/activate'"

clean:
	@if [ -d ./venv ]; then rm -rf ./venv; fi
	@if [ -d ./__pycache__ ]; then rm -rf ./__pycache__; fi
	@if [ -d ./build ]; then rm -rf ./build; fi
	@if [ -d ./dist ]; then rm -rf ./dist; fi
	@rm -rf *.egg
