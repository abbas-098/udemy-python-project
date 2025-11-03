test:
	poetry run pytest

run-webapp:
	streamlit run src/main.py

ci-fmt:
	ruff format src tests --check

fmt:
	ruff format src tests

ci-lint:
	ruff check src tests --check

lint:
	ruff check src tests --fix
