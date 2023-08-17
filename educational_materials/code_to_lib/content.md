# Код -> Библиотека

## Мотивация 

Каждый, кто пишет код, рано или поздно упирается в необходимость использовать свои наработки в нескольких проектах. Мы можем просто копировать участки кода каждый раз в новый проект, но это несет в себе большие издержки, так как мы теряем единую точку "входа", т.е. возможность внести изменения в одном месте и получить их везде, где мы используем этот код. Поэтому мы хотим сделать из нашего кода библиотеку, которая может быть полезна как нам, так и сторонним разработчикам, которую мы сможем поддерживать, функции которой будут описаны, а также автоматически тестироваться, чтобы уменьшить вероятность ошибок. В этом уроке мы поговорим о том, что должно быть в проекте помимо кода, чтобы его можно было назвать библиотекой, а в следующем — рассмотрим, как упаковать наш код, чтобы его могли устанавливать себе другие разработчики. 

## Определяем функциональность библиотеки

Например, мы пишем функцию, которая будет сообщать нам, сколько памяти потребляет та или иная функция. Воспользуемся [документацией](https://docs.python.org/3/library/tracemalloc.html) к библиотеке `tracemalloc`. Она позволит нам отследить выделенное место. Также можно использовать библиотеку `sys`, которая позволит определить только ту память, которую занимает непосредственно объект с данными.

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

Мы видим, что даже пустой массив занимает какое-то место в памяти (для 64-разрядной системы это 72 байта), и не каждое добавление элементов вызывает выделение памяти. Оговоримся, что в зависимости от того, как заполнять данные, результат будет разным. Ниже приведены примеры кода, которые дадут несколько другой вывод при том же результирующем массиве.

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

Мы не будет обсуждать разницу в выводе, она связана с особенностями реализации списков в Python и способе создания конкретного списка. Для наших задач необязательно знать точные числа, но нужно иметь оценку объема памяти, выделяемой на те или иные операции, для того чтобы разбить полный массив данных на части (`chunk`) и обрабатывать так, чтобы все умещалось в памяти. Практически всегда можно сделать оценку потребляемой памяти вручную, но такой подход требует погружения в детали задачи. 

Давайте попробуем разделить код выше на функциональную часть, которая делает что-то полезное для нас, и ту, которая оценивает память:

([код](/projects/code_to_lib/split_functionality.py)):

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

Теперь можно попробовать сделать `execute_and_get_memory_usage` более универсальным, так, чтобы эта функция могла работать с любой функцией, а не только с `do_something_usefull`. Так как мы не знаем, какие аргументы будут у функций, нужен способ, который позволит не ограничиваться определенным количеством аргументов. Для этого в Python используются `*args` и `**kwargs`. 

([код](/projects/code_to_lib/split_functionality_args.py)):

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

Мы видим, что `sys.getsizeof()` не информативен для вложенных объектов, поэтому оставим только tracemalloc. *Примечание: функции типа `execute_and_get_memory_usage` в Python называются декораторы, мы не будем подробно на этом останавливаться, так как этот курс не про само программирование и изучение языка. Вы можете легко найти материалы для изучения самостоятельно, наподобие [таких](https://www.programiz.com/python-programming/decorator) или [таких](https://www.geeksforgeeks.org/decorators-in-python/).

Мы получили инструмент для оценки памяти, которая требуется для выполнения той или иной функции с определенным набором входных данных. Теперь мы хотим использовать ее в других наших проектах. Возможно даже, она будет интересна другим разработчикам, поэтому нужно оформить все как принято при распространении кода. Здесь мы пока не будем говорить о менеджерах установки, таких как `pip` или `apt` (используется в Ubuntu), поговорим пока о том, что должно быть помимо кода, чтобы кодом можно было воспользоваться.

1. Первое, что должно сопровождать код, — это файл **README**.md. Мы будем использовать Markdown для разметки, также часто используется `reStructedText`, тогда вы увидите `README.rst` в списке файлов проекта. Файл README нужен для того, чтобы понять, будет ли полезен данный проект тому, кто его читает. В README могут содержаться короткие примеры того, как использовать API библиотеки, и другая полезная информация, которую разработчик пожелал добавить. [Пункты](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/), которые обычно включает README:

  * название проекта;
  * описание;
  * содержание для удобной навигации;
  * инструкции по установке;
  * примеры использования приложения;
  * упоминание участников, которые внесли вклад в проект;
  * информация о лицензии (текст лицензии содержится в отдельном файле);
  * бейджи;
  * способы поучаствовать в проекте.

![badges](/graphics/badge.png)

Научиться писать хороший README можно только через практику и примеры, которые вы сами считаете хорошими. [Здесь](https://github.com/matiassingers/awesome-readme) собран список проектов, которые, по мнению авторов списка, являются хорошими, обратитесь к нему и составьте свое мнение о том, что должен включать это файл. 

2. Далее проект должен содержать файл **LICENSE** с текстом лицензии. По лицензиям в курсе есть [отдельный материал](https://github.com/kruzhok-team/fossdev/blob/devel/educational_materials/open_license/content.md), посмотрите его и выберите подходящую.

3. Как мы уже говорили ранее, в README должны быть инструкции по установке. Установка может быть как полностью ручная, так и с той или иной степенью автоматизации. Например, в проектах на Python часто содержится файл `setup.py`, в котором прописан код для установки. Тогда инструкция по установке выглядит как одна строка:

```bash
python setup.py
```

4. Любой код использует другой код, поэтому в проекте нужно прописать список используемых библиотек, **зависимостей**. Его можно как вести вручную, например, в файле `requirements.txt`, который используется `pip` для установки зависимостей, так и автоматически, если мы используем другой инструмент, например, `poetry`.

5. Каталог, который содержит код проекта. Для разных языков программирования он будет называть по-разному. Для проектов на Python название каталога совпадает с названием проекта. В С++ это будут `src` и `include`. 

6. Очень хорошая идея иметь тесты в проекте, это поможет понять пользователю вашей библиотеки, что код выполнился штатно, хотя бы для тестовых данных. Файлы с тестами будут иметь разную структуру для разных языков программирования.

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

*Примечание: `__init__.py` нужен для того, чтобы Python воспринимал каталог как пакет*

## Собираем проект 

Напишем файл для установки `setup.py`, для данного примера воспользуемся библиотекой `setuptools`.

([код](/projects/mtracker/setup.py)):

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

Мы устанавливаем пакет `mtracker`, `install_requires` пустое, поскольку мы не используем зависимости не из стандартной библиотеки Python. `extras_require` содержат модули, которые не нужны при работе приложения, но понадобятся, если мы захотим прогнать тесты для проекта. Также указываем версию Python, под которой проект должен запуститься.


README можно посмотреть на [странице](https://github.com/standlab/mtracker) проекта на GitHub. 

От кода, который мы разрабатывали выше, оставим только часть с `tracemalloc`

([код](/projects/mtracker/mtracker/mtracker.py)):

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

И снабдим наш проект тестом. Здесь мы написали всего один тест, который проверит, не ломает ли наш трекер работу функций, на примере функции, которая возвращает список.

([код](/projects/mtracker/test/test_mtracker.py)):

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

Мы снабдили написанную нами функцию необходимыми файлами, чтобы ее можно было выложить в открытый доступ и позволить другим разработчикам устанавливать ее себе и использовать ее API. 
