PACKAGE_NAME := my-library
PYTHON := python3

.PHONY: install test clean

install:
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install -r requirements.txt

test:
	@echo "Running tests..."
	$(PYTHON) -m pytest

clean:
	@echo "Cleaning up..."
	rm -rf dist/ build/ *.egg-info
