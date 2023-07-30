PACKAGE_NAME := mtracker
PYTHON := pipenv run python

.PHONY: install test clean package docs publish format build

install:
	@echo "Setting up pipenv virtual environment..."
	pipenv install --dev

test:
	@echo "Running tests..."
	pipenv run pytest

clean:
	@echo "Cleaning up..."
	rm -rf dist/ build/ *.egg-info

package:
	@echo "Packaging the library..."
	$(PYTHON) -m build

docs:
	@echo "Generating documentation..."
	pipenv run pdoc --html $(PACKAGE_NAME) --output-dir docs --force

publish: package
	@echo "Publishing the package to PyPI..."
	pipenv run twine upload dist/*

format:
	@echo "Formatting code with autopep8..."
	pipenv run autopep8 --in-place --recursive mtracker tests
