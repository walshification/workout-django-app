PIPENV_RUN := pipenv run

test: lint pytest

lint:
	${PIPENV_RUN} black . --check
	${PIPENV_RUN} flake8 --config setup.cfg
	${PIPENV_RUN} mypy .
	${PIPENV_RUN} isort --check-only --diff .

pytest:
	${PIPENV_RUN} pytest

fmt:
	${PIPENV_RUN} autoflake . --recursive --in-place \
		--remove-all-unused-imports --remove-unused-variables \
		--exclude '\.git,\.mypy_cache'
	${PIPENV_RUN} black . --exclude '\.git|\.mypy_cache'
	${PIPENV_RUN} isort .
