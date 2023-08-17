## Задачи

### Задача 1

Добавьте в makefile задачи для автоматического форматирования кода по `pep8`, а также для публикации проекта в PyPI. Добавьте информационное сообщение для каждой задачи в `makefile`.

**Ответ**

([код](/projects/packaging/pep_formating/makefile)):

```makefile
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
	$(PYTHON) setup.py sdist bdist_wheel

docs:
	@echo "Generating documentation..."
	pipenv run pdoc --html $(PACKAGE_NAME) --output-dir docs --force

publish: package
	@echo "Publishing the package to PyPI..."
	pipenv run twine upload dist/*

format:
	@echo "Formatting code with autopep8..."
	pipenv run autopep8 --in-place --recursive mtracker tests

```

### Задача 2

Прямой вызов `setup.py` считается не самым надежным на сегодня способом. Мы написали урок с его использованием для того, чтобы показать явно все шаги. Прочитайте [статью](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html) и замените вызов `python setup.py` на `python -m build`. 

**Ответ**

([код](/projects/packaging/setup_to_build/makefile)):

```makefile
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
```
