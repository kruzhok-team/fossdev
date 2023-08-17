## Задачи 

### Задача 1 

1. Организуйте код библиотеки `useful_utils`, который содержит модули для математических операций и работы со строками, в виде библиотеки.

    * Определите модули и их функциональность: в структуре каталогов создайте отдельные файлы модулей для представления различных функций вашей библиотеки: math_operations.py и string_utils.py.

    * Функции в math_operations.py:

        * add(a, b): принимает два аргумента a и b и возвращает их сумму.
        * subtract(a, b): принимает два аргумента a и b и возвращает их разницу.
        * multiply(а, b): принимает два аргумента a и b и возвращает их произведение.
        * devide(а, b): принимает два аргумента a и b и возвращает результат деления a на b.

    * Функции для string_utils.py:
        * concatenate(a, b): принимает две строки a и b и возвращает их конкатенацию.
        * reverse(s): принимает строку s и возвращает ее реверс.
        * substring(s, i, j): принимает строку s и возвращает подстроку.

    * Создайте файл `__init__.py` и напишите содержимое так, чтобы функции из модулей были доступны, когда кто-то импортирует вашу библиотеку, т.е. чтобы можно было выполнить импорт таким образом.

        ```python
        from useful_utils import add, subtract, multiply, divide, concatenate, reverse
        ```

    * Протестируйте свой код: создайте отдельный каталог тестов для написания тестовых случаев для вашей библиотеки. Реализуйте тесты для каждой функции.
    * Напишите `setup.py`
    * Добавьте README: Создайте файл README.md с кратким описанием вашей библиотеки, инструкциями по ее установке и использованию и примерами использования каждой функции.


**Ответ**

Структура проекта:

```
my_library/
    |-- useful_utils/
    |   |-- __init__.py
    |   |-- math_operations.py
    |   |-- string_utils.py
    |-- tests/
    |   |-- test_math_operations.py
    |   |-- test_string_utils.py
    |-- setup.py
    |-- README.md
```

Содержимое `math_operations.py`:

([код](/projects/code_to_lib/useful_utils/useful_utils/math_operations.py)):

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """
    Return the result of dividing two numbers.

    If b is zero, raise a ValueError.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Содержимое `string_utils.py`:

([код](/projects/code_to_lib/useful_utils/useful_utils/string_utils.py)):

```python
def concatenate(a, b):
    """Concatenate two strings and return the result."""
    return a + b

def reverse(s):
    """Return the reverse of the input string."""
    return s[::-1]
    
def substring(s, i, j):
    """Return the substring of the input string."""
    if j < len(s) and i < len(s)
    return s[i:j]
```

Содержимое `__init__.py`:

([код](/projects/code_to_lib/useful_utils/useful_utils/__init__.py)):

```python
# __init__.py

# Import functions from math_operations.py
from .math_operations import add, subtract, multiply, divide

# Import functions from string_utils.py
from .string_utils import concatenate, reverse, substring
```

Содержимое `setup.py`:

([код](/projects/code_to_lib/useful_utils/setup.py)):

```python
from setuptools import setup, find_packages

setup(
    name='useful-utils',
    version='1.0.0',
    packages=find_packages(),
    description='Utils to make life easier',
    author='Your Name',
    author_email='your_name@example.com',
    url='https://github.com/your_username/your_repository',
    install_requires=[
        'pytest'
    ],
)
```

Содержимое тестов (может отличаться):

([код](/projects/code_to_lib/useful_utils/tests/test_math_operations.py)):

```python
from useful_utils.math_operations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 5) == 4

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 7) == 3

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(20, 4) == 5
    assert divide(7, 2) == 3.5
```

([код](/projects/code_to_lib/useful_utils/tests/test_string_utils.py)):

```python
from useful_utils.string_utils import concatenate, reverse, substring

def test_concatenate():
    assert concatenate('Hello', 'World') == 'HelloWorld'
    assert concatenate('Python', ' is awesome') == 'Python is awesome'

def test_reverse():
    assert reverse('hello') == 'olleh'
    assert reverse('Python') == 'nohtyP'

def test_substring():
    assert substring('hello', 2, 4) == 'll'
    assert substring('hello', 2, 1) == ''
    assert substring('hello', 1, 1) == ''
```

### Задача 2

Добавьте дополнительные данные в setup.py.

В этой задаче вы улучшите файл setup.py, который писали для предыдущей задачи. Также можно выполнить это задание для любого другого проекта, над которым мы работаем, или придумать новый. Это нужно, если мы будем публиковать библиотеку для других разработчиков: добавив больше данных, мы дадим дополнительную информацию о библиотеке. Дополнительная информация будет включать лицензию вашей библиотеки, подробное описание, классификаторы и ключевые слова.

    * Лицензия: выберите подходящую лицензию для своей библиотеки и добавьте ее в файл setup.py. Выбирайте из MIT, BSD, Apache License 2.0 и GPL или используйте свою. Добавьте лицензию непосредственно в функцию setup().

    * Подробное описание: создайте файл README.md в корневом каталоге вашего проекта и напишите подробное описание вашей библиотеки. Затем измените файл setup.py, чтобы включить это подробное описание при упаковке библиотеки. Вы можете использовать функции open() и read() для чтения содержимого файла README.md.

    * Классификаторы: Классификаторы — это способ категоризировать вашу библиотеку. Вы можете добавить классификаторы, чтобы указать целевую аудиторию, статус разработки, язык программирования и многое другое. Доступные параметры см. в списке классификаторов PyPI.

    * Ключевые слова: добавьте список ключевых слов, описывающих основные функции и возможности вашей библиотеки. Это поможет пользователям найти вашу библиотеку в указателях пакетов.


**Ответ**

([код](/projects/code_to_lib/useful_utils/improved_setup.py)):

```python
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='useful-utils',
    version='1.0.0',
    packages=find_packages(),
    description='Utils to make life easier',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specify the type of long description
    author='Your Name',
    author_email='your_name@example.com',
    url='https://github.com/your_username/your_repository',
    install_requires=[
        'pytest',  
    ],
    license='MIT',  # Add your library's license here
    classifiers=[
        # Add classifiers that describe your library
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='python library example',  # Add keywords that describe your library
)
```

### Задача 3


Напишите makefile, который будет автоматизировать некоторые процедуры, которые мы осуществляем с библиотекой. Определите следующие задачи (target):

    * Задача **install** устанавливает зависимости проекта, указанные в файле requirements.txt.
    * Задача **test** запускает тесты с помощью pytest.
    * Задача **clean** удаляет временные файлы, созданные в процессе упаковки.


**Ответ**

([код](/projects/code_to_lib/useful_utils/makefile)):

```makefile
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

```

### Задача 4

Напишите комментарии в виде docstring, которые описывают работу функций и параметры. Помните, что в некоторых случаях порядок параметров неважен, например, при сложении, поэтому можно описать их как первое число и второе число. В других случаях, например, при вычитании, порядок важен, и мы должны описать числа соответствующим образом, даже если интуитивно понятно, что из первого вычитается второе. Написать docstring нужно для функции в модуле math_operations.py:

    * add(a, b): принимает два аргумента a и b и возвращает их сумму.
    * subtract(a, b): принимает два аргумента a и b и возвращает их разницу.
    * multiply(а, b): принимает два аргумента a и b и возвращает их произведение.
    * devide(а, b): принимает два аргумента a и b и возвращает результат деления a на b.

Добавьте задачу **docs** в makefile  для сборки документации с помощью [pdoc](https://pdoc.dev/docs/pdoc.html). Собранная документация не должна попасть в репозиторий git, поэтому нужно модифицировать задачу **clean**.

**Ответ**

([код](/projects/code_to_lib/useful_utils/useful_utils/math_operations_docstring.py)):

```
def add(a, b):
    """
    Return the sum of two numbers.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Return the difference between two numbers.

    Parameters:
        a (int or float): The minuend.
        b (int or float): The subtrahend.

    Returns:
        int or float: The result of subtracting b from a.
    """
    return a - b

def multiply(a, b):
    """
    Return the product of two numbers.

    Parameters:
        a (int or float): The first factor.
        b (int or float): The second factor.

    Returns:
        int or float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Return the result of dividing two numbers.

    Parameters:
        a (int or float): The dividend.
        b (int or float): The divisor.

    Returns:
        int or float: The result of dividing a by b.

    Raises:
        ValueError: If b is zero (0).
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

```

Содержимое `makefile`:

([код](/projects/code_to_lib/useful_utils/makefile_docstring)):

```makefile
PACKAGE_NAME := useful-utils
PYTHON := python3
DOCS_DIR := docs

.PHONY: install test clean package docs

install:
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install -r requirements.txt

test:
	@echo "Running tests..."
	$(PYTHON) -m pytest

clean:
	@echo "Cleaning up..."
	rm -rf dist/ build/ docs/ *.egg-info

docs:
	@echo "Generating documentation..."
	pdoc --html $(PACKAGE_NAME) --output-dir $(DOCS_DIR) --force
```
