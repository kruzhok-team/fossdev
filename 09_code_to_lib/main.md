# Код -> Библиотека

## Мотивация 

Каждый, кто пишет код, рано или поздно упирается в необходимость использовать свои наработки в нескольких проектах. Мы можем просто копировать участки код каждый раз в новый проект, но это несет с собой большие издержки, так как мы теряем единую точку "входа", т.е. так чтобы внести изменения в одном месте и получить их везде где мы используем этот код. Поэтому мы хотим сделать из нашего кода библиотеку, которая может быть полезна как нам так и сторонним разработчикам, которую мы сможем поддерживать, функции которой будут описаны, а так же автоматически тестироваться, чтобы уменьшить вероятность ошибок. В этом уроке мы поговорим о том, что должно быть в проекте помимо кода, что бы его можно было назвать библиотекой, а в следующем рассмотрим как упаковать наш код, чтобы его могли устанавливать себе другие разработчики. 

## Определяем функциональность библиотеки

Например, мы пишем функцию, которая будет сообщать нам, сколько памяти потребляет та или иная функция. Воспользуемся [документацией](https://docs.python.org/3/library/tracemalloc.html) к библиотеке `tracemalloc`. Она позволит нам отследить выделенное место. Также можно использовать библиотеку `sys`, которая позволит узнать только ту память, которую занимает непосредственно объект с данными.

 ```python   
import tracemalloc
import sys

data = list()
print(f"According to sys: {sys.getsizeof(data)}")
for i in range(10):
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()
    data.append(1)
    after = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"According to tracemalloc: {after[1] - before[1]}")
    print(f"According to sys: {sys.getsizeof(data)}")
```

Пример вывода:

```sh
According to sys: 72
According to tracemalloc: 32
According to sys: 104
According to tracemalloc: 0
According to sys: 104
According to tracemalloc: 0
According to sys: 104
According to tracemalloc: 0
According to sys: 104
According to tracemalloc: 64
According to sys: 136
According to tracemalloc: 0
According to sys: 136
According to tracemalloc: 0
According to sys: 136
According to tracemalloc: 0
According to sys: 136
According to tracemalloc: 128
According to sys: 200
According to tracemalloc: 0
According to sys: 200
```

Мы видим, что даже пустой массив занимает какое-то место в памяти (для 64-разрядной системы это 72 байта) и не каждое добавление элементов вызывает выделение памяти. Оговоримся, что в зависимости от того, как заполнять данные, результат будет разным. Ниже приведены примеры кода, которые дадут несколько другой вывод при том же результирующем массиве.

Альтернативный пример:

 ```python
import tracemalloc
import sys

for i in range(10):
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()
    data = [1] * i
    after = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"According to tracemalloc: {after[1] - before[1]}")
    print(f"According to sys: {sys.getsizeof(data)}")
```

Еще альтернативный пример:

``` python
import tracemalloc
import sys

for i in range(10):
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()
    data = [1 for _ in range(i)]
    after = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"According to tracemalloc: {after[1] - before[1]}")
    print(f"According to sys: {sys.getsizeof(data)}")
```

Мы не будет обсуждать разницу в выводе, она связана с особенностями реализации списков в Python и способе его создания. Для наших задач необязательно иметь точные числа, но нужно иметь оценку объема памяти выделяемой на те или иные операции для того, чтобы разбить полный массив данных на части (`chunk`) и обрабатывать так, чтобы все умещалось в памяти. Практически всегда можно сделать оценку потребляемой памяти вручную, но такой подход требует погружения в детали задачи. 

Давайте попробуем разделить код выше на функциональную часть, которая делает что-то полезное для нас, и ту, которая оценивает память:

``` python
import tracemalloc
import sys

def do_something_usefull(n):
    data = [1 for _ in range(n)]    
    return data
    
def execute_and_get_memory_usage(function, n):
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()
    data = function(i)
    after = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"According to tracemalloc: {after[1] - before[1]}")
    print(f"According to sys: {sys.getsizeof(data)}")
    return data 
    
for i in range(10):
    execute_and_get_memory_usage(do_something_usefull, i)
```

Теперь можно попробовать попробовать сделать `execute_and_get_memory_usage` более универсальным, так, чтобы эта функция могла работать с любой функцией, а не только с `do_something_usefull`. Так как мы не знаем, какие аргументы будут у функций, нужен способ, который позволит не ограничиваться определенным количеством аргументов, для этого в python используются `*args` и `**kwargs`. 

``` python
import tracemalloc
import sys

def do_something_usefull(n):
    data = [1 for _ in range(n)]    
    return data

def do_something_else_usefull(n, m, step=1):
    data = [[1 for _ in range(n)] for _ in range(0, m, step)]
    return data
    
def execute_and_get_memory_usage(function, *args, **kwargs):
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()
    result = function(*args, **kwargs)
    after = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"According to tracemalloc: {after[1] - before[1]}")
    print(f"According to sys: {sys.getsizeof(data)}")
    return result

print('1D example:')
execute_and_get_memory_usage(do_something_usefull, 10)

print('\n2D example:')
execute_and_get_memory_usage(do_something_else_usefull, 10, 10, step=2)
```

Пример вывода:

```sh
1D example:
According to tracemalloc: 320
According to sys: 200

2D example:
According to tracemalloc: 1112
According to sys: 136
```   

Мы видим, что `sys.getsizeof()` не информативен для вложенных объектов, поэтому оставим только tracemalloc. *Примечание: функции типа `execute_and_get_memory_usage` в python называются декораторы, мы не будем подробно на этом останавливаться, так как этот курс не про само программирования и изучение языка. Вы можете легко найти материалы для изучения самостоятельно наподобие [таких](https://www.programiz.com/python-programming/decorator) или [таких](https://www.geeksforgeeks.org/decorators-in-python/).

Мы получили инструмент для оценки памяти, которая требуется для выполнения той или иной функции и определенным набором входных данных. Теперь мы хотим использовать ее в других наших проектах. Возможно, даже она будет интересна другим разработчикам, поэтому нужно оформить все как принято при распространении кода. Здесь мы пока не будем говорить о менеджерах установки таких как `pip` или `apt` (используется в Ubuntu), поговорим пока о том, что должен быть помимо кода для того, чтобы кодом можно было воспользоваться:

1. Первое, что должно сопровождать код, - это файл **README**.md. Мы будем использовать markdown для разметки, так же часто используется `reStructedText`, тогда вы увидите `README.rst` в списке файлов проекта. Файл README нужен для того, чтобы понять, будет ли полезен данный проект тому, кто его читает. В README могут содержаться короткие примеры того, как использовать API библиотеки и другая полезная информация, которую разработчик пожелал добавить. [Пункты](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/), которые обычно включает README:

  * название проекта;
  * описание;
  * содержание для удобной навигации;
  * инструкции по установке;
  * примеры использования приложения;
  * упоминание участников, которые внесли вклад в проект;
  * информация о лицензии (текст лицензии содержится в отдельном файле);
  * бейджи;
  * способы как поучаствовать в проекте.

![badges](./img/badge.png)

Научиться писать хороший README можно только через практику и примеры, которые Вы сами считаете хорошими. [Здесь](https://github.com/matiassingers/awesome-readme) собран список проектов, которые, по мнению авторов списка, являются хорошими, обратитесь к нему и составьте свое мнение о том, что должен включать это файл. 

2. Далее проект должен содержать файл **LICENSE** с текстом лицензии. По лицензиям в курсе есть (PASTE_LINK) отдельный материал, посмотрите его и выберите подходящую.

3. Как мы уже говорили ранее, в README должны быть инструкции по установке. Установка может быть как полностью ручная, так и с той или иной степенью автоматизации. Например, в проектах на Python часто содержится файл `setup.py` в котором прописан код для установки. Тогда инструкция по установке выглядит как одна строка:

```bash
python setup.py
```

4. Любой код использует другой код, поэтому в проекте нужно прописать список используемых библиотек, **зависимостей**. Его можно как вести вручную, например, в файле `requirements.txt`, который используется `pip` для установки зависимостей, так и автоматически, если мы используем другой инструмент, например `poetry`.

5. Каталог, который содержит код проекта. Для разных языков программирования он будет называть по-разному. Для проектов на python название каталога совпадает с названием проекта. В С++ это будут `src` и `include`. 

6. Очень хорошая идея иметь тесты в проекте, это поможет понять пользователю вашей библиотеки, что код выполнился штатно хотя бы для тестовых данных. Файлы с тестами будут иметь разную структуру для разных языков программирования.

Для Python:

``` sh
my_project
├── mtracker
│   ├── utils
│   │   ├── __init__.py
│   │   └── futils.py
│   ├── __init__.py
│   └── mtracker.py
└── test
    ├── utils
    │   ├── __init__.py
    │   └── test_futils.py
    ├── __init__.py
    └── test_mtracker.py
```

*Примечание: `__init__.py` нужен для того чтобы Python воспринимал каталог как пакет*

## Собираем проект 

Напишем файл для установки `setup.py`, для данного примера воспользуемся библиотекой `setuptools`.

``` python
from setuptools import setup

setup(
   name='mtraker',
   version='1.0',
   description='Provides a decorator for memory usage tracking. The part of FOSS course.',
   license='MIT',
   author='Artem Vesnin',
   author_email='artemvesnin@gmail.com',
   url='https://github.com/standlab/mtracker',
   packages=['mtracker'],
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
```

Мы устанавливаем пакет `mtracker`, `install_requires` пустое, поскольку мы не используем зависимости не из стандартной библиотеки Python. `extras_require` содержат модули, которые не нужны при работе приложения, но понадобятся, если мы захотим прогнать тесты для проекта. Также, указываем версию Python, под которой проект должен запуститься.


README можно посмотреть на [странице](https://github.com/standlab/mtracker) проекта на GitHub. 

От кода, который мы разрабатывали выше, оставим только часть с `tracemalloc`

```python
import tracemalloc

def execute_and_get_memory_usage(function, *args, **kwargs):
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()
    result = function(*args, **kwargs)
    after = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"According to tracemalloc: {after[1] - before[1]}")
    return result
```

И снабдим наш проект тестом. Здесь мы написали всего один тест, который проверит, не ломает ли наш трекер работу функций на примере функции, которая возвращает список.

```python
import pytest
from mtracker.mtracker import execute_and_get_memory_usage

def _generate_list(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst

def test_no_change():
    n = 10
    lst1 = _generate_list(n)
    lst2 = execute_and_get_memory_usage(_generate_list, n)
    assert len(lst1) == len(lst2)
    for l1, l2 in zip(lst1, lst2):
        assert l1 == l2
```

Проверим тесты:

``` sh
artem@pc:~/foss/mtracker$ pytest
    ============================= test session starts ==============================
    platform linux -- Python 3.7.4, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
    rootdir: /home/artem/swdev/gitrepo/edu/toolchain_proj/mtracker
    plugins: doctestplus-0.4.0, arraydiff-0.3, remotedata-0.3.2, openfiles-0.4.0
    collected 1 item                                                               
    
    test/test_mtracker.py .                                                  [100%]
    
    ============================== 1 passed in 0.04s ===============================
```
Устанавливаем:

``` sh
artem@pc:~/foss/mtracker$ pip install .
    Processing /home/artem/foss/mtracker
    Building wheels for collected packages: mtracker
    ...
    Successfully installed mtracker-1.0
```  

Проверяем:

``` python   
>>> from mtracker import mtracker
>>> mtracker.execute_and_get_memory_usage
<function execute_and_get_memory_usage at 0x7effef7b1cb0>
```
Проверяем установку как в README:

``` sh
artem@pc:~$ pip install git+https://github.com/standlab/mtracker.git#egg=mtracker
    Collecting mtracker from git+https://github.com/standlab/mtracker.git#egg=mtracker
    ...
    Installing collected packages: mtracker
    Successfully installed mtracker-1.0
```

## Выводы

Мы снабдили написанную нами функцию необходимыми файлами, чтобы её можно было выложить в открытый доступ и позволить другим разработчикам, устанавливать её себе и использовать её API. 

## Задачи 

### Задачa 1 

1. Организуйте код библиотеки `useful_utils`, который содержит модули для математических операций и работы со строками в виде библиотеки.

    * Определите модули и их функциональность: в структуре каталогов создайте отдельные файлы модулей для представления различных функций вашей библиотеки: math_operations.py и string_utils.py.

    * Функции в math_operations.py:

        * add(a, b): принимает два аргумента a и b и возвращает их сумму.
        * subtract(a, b): принимает два аргумента a и b и возвращает их разницу.
        * multiply(а, b): принимает два аргумента a и b и возвращает их произведение.
        * devide(а, b): принимает два аргумента a и b и возвращает результат деления a на b
        *   .
    * Функции для string_utils.py:
        * concatenate(a, b): принимает две строки a и b и возвращает их конкатенацию.
        * reverse(s): принимает строку s и возвращает ее реверс.
        * substring(s, i, j): принимает строку s и возвращает подстроку.

    * Создайте файл `__init__.py`: и напишите содержимое так что бы функции из модулей были доступны, когда кто-то импортирует вашу библиотеку, т.е. чтобы можно было выполнить импорт nfrbv образом 

        ```python
        from useful_utils import add, subtract, multiply, divide, concatenate, reverse
        ```

    * Протестируйте свой код: создайте отдельный каталог тестов для написания тестовых случаев для вашей библиотеки. Реализуйте тесты для каждой функции.
    * Напишите `setup.py`
    * Добавьте README: Создайте файл README.md с кратким описанием вашей библиотеки, инструкциями по ее установке и использованию и примерами использования каждой функции.
]

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

Содержимое `__init__.py`:

```python
# __init__.py

# Import functions from math_operations.py
from .math_operations import add, subtract, multiply, divide

# Import functions from string_utils.py
from .string_utils import concatenate, reverse, substring
```

Содержимое `setup.py`:

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

Добавьте дополнительных данных в setup.py.

В этой задаче вы улучшите файл setup.py, который писали для предыдущей задачи. Так же можно сделать это задание для любого другого проекта, над которым мы работаем, или придумать новый. Это нужно если мы будем публиковать библиотеку для других разработчиков, добавив больше данных мы дадим дополнительную информацию о библиотеке. Дополнительная информация будет включать лицензию вашей библиотеки, подробное описание, классификаторы и ключевые слова.

    * Лицензия: выберите подходящую лицензию для своей библиотеки и добавьте ее в файл setup.py. Выбирайте из MIT, BSD, Apache License 2.0 и GPL или используйте свою. Добавьте лицензию непосредственно в функцию setup().

    * Подробное описание: создайте файл README.md в корневом каталоге вашего проекта и напишите подробное подробное описание вашей библиотеки. Затем измените файл setup.py, чтобы включить это подробное описание при упаковке библиотеки. Вы можете использовать функции open() и read() для чтения содержимого файла README.md.

Классификаторы: Классификаторы — это способ категоризировать вашу библиотеку. Вы можете добавить классификаторы, чтобы указать целевую аудиторию, статус разработки, язык программирования и многое другое. Доступные параметры см. в списке классификаторов PyPI.

Ключевые слова: добавьте список ключевых слов, описывающих основные функции и возможности вашей библиотеки. Это поможет пользователям найти вашу библиотеку в указателях пакетов.


**Ответ**

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


Напишите makefile, который будет автоматизировать некоторые процедуры, которые мы делаем с библиотекой. Определите следующие задачи (target):

    * Задача **install** устанавливает зависимости проекта, указанные в файле requirements.txt.
    * Задача **test** запускает тесты с помощью pytest.
    * Задача **clean** удаляет временные файлы, созданные в процессе упаковки.


**Ответ**

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

Напишите комментарии в виде docstring которые описывают работу функций и описывают параметры. Помните, что в некоторых случаях порядок параметров неважен, например при сложении, поэтому можно описать их как первое число и второе число. В других случаях, например при вычитании, порядок важен, и мы должны описать числа соответствующим образом, даже если интуитивно понятно что из первого отнимается второе. Написать docstring нужно для функции в модуле math_operations.py:

    * add(a, b): принимает два аргумента a и b и возвращает их сумму.
    * subtract(a, b): принимает два аргумента a и b и возвращает их разницу.
    * multiply(а, b): принимает два аргумента a и b и возвращает их произведение.
    * devide(а, b): принимает два аргумента a и b и возвращает результат деления a на b

Добавьте задачу **docs** в makeifle  для сборки документации с помощью [pdoc](https://pdoc.dev/docs/pdoc.html). Собранная документация не должна попасть в репозиторий git, поэтому нужно модифицировать задачу **clean**.

**Ответ**


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

