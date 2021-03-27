install:
		poetry install
build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		pip install dist/*.whl

lint:
		poetry run flake8 copy_files
		poetry run flake8 tests

pytest:
		poetry run pytest --cov=copy_files tests/ --cov-report xml