#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = Book_tg_bot
PYTHON_VERSION = 3.12.7
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
.PHONY: requirements
requirements:
	poetry install

## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8 and black (use `make format` to do formatting)
.PHONY: lint
lint:
	poetry run flake8 RAG
	poetry run isort --check --diff --profile black RAG
	poetry run black --check --config pyproject.toml RAG

## Format source code with black
.PHONY: format
format:
	poetry run black --config pyproject.toml RAG
