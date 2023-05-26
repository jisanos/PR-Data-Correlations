.PHONY: install venv format

install:
	@echo "Running Poetry..."
	poetry install
	@echo "Installing Git hooks..."
	poetry run pre-commit install

get-poetry:
	open "https://python-poetry.org/docs/#installing-with-the-official-installer"
	xdg-open "https://python-poetry.org/docs/#installing-with-the-official-installer"

venv:
	poetry shell

format:
	poetry run black .