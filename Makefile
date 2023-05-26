.PHONY: install venv format get-poetry freeze install-reqs

install:
	@echo "Running Poetry..."
	poetry install
	@echo "Installing Git hooks..."
	poetry run pre-commit install

install-reqs:
	pip install -r requirements.txt

get-poetry:
	open "https://python-poetry.org/docs/#installing-with-the-official-installer"
	xdg-open "https://python-poetry.org/docs/#installing-with-the-official-installer"

venv:
	poetry shell

format:
	poetry run black .

freeze:
	pip freeze > requirements.txt
	git add requirements.txt
	git commit -m "[feat] Update dependencies"