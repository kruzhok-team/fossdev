# Сборка проекта и установка пакета на примере Python

## Зачем вообще нужна упаковка проекта

Мы уже умеем хранить код в Git-репозитории, клонировать его, переключаться между ветками и отправлять изменения. Но этого недостаточно, чтобы проектом было удобно пользоваться как библиотекой. Когда мы пишем:

```python
import lib_name
lib_name.do_something()
```

мы выступаем не как авторы библиотеки, а как её пользователи. Значит, у нас должен быть понятный и воспроизводимый способ получить библиотеку, её зависимости и совместимую версию в своё окружение.

Мы уже использовали `setup.py` для целей установки проекта. Более современная версия точки входа для сборки проекта - это `pyproject.toml`. Именно там описывается, как проект собирать, какие у него метаданные и какие зависимости ему нужны во время выполнения. Для библиотек это лучше, чем разносить ключевую информацию по разным файлам и тем более лучше, чем собирать зависимости вручную из lock-файлов. Сравненние pyproject.toml и setup.py приведено в конце урока.

## Неправильные и неудобные способы использовать чужой код

### Ctrl-C / Ctrl-V

Самый наивный путь — просто скопировать нужную функцию или модуль себе в проект.

Почему это плохо:

* вы отрываете код от его истории и перестаёте получать исправления;
* легко потерять скрытые зависимости между модулями;
* вы не видите, какие версии зависимостей нужны проекту;
* вы не получаете нормальный путь обновления;
* вы не воспроизводите реальную установку и реальное окружение пользователя.

### Клонировать репозиторий и руками править `sys.path`

Это уже лучше, потому что у вас есть исходники, тесты и структура проекта, но по-прежнему неудобно:

* установка превращается в ручную процедуру;
* проект подключается через “костыль” в коде или через `PYTHONPATH`;
* обновление и повторяемость окружения остаются проблемой;
* сам способ использования библиотеки получается неестественным.

Такой путь полезно показать студентам как промежуточный шаг в понимании проблемы, но не как целевую практику.

## Как выглядит installable Python-проект

Минимальная структура проекта:

```text
mtracker/
├── pyproject.toml или setup.py
├── README.md
├── LICENSE
├── Makefile
├── src/
│   └── mtracker/
│       ├── __init__.py
│       └── ...
└── tests/
    └── ...
```

Ключевой файл здесь — `pyproject.toml`. PyPA рекомендует иметь его в корне проекта (**не репозитория** - помним про организацию в виде моноропозитория), а стандартным инструментом для сборки source distribution и wheel считает `build`. Напрямую вызывать `python setup.py sdist` и `python setup.py bdist_wheel` не нужно. ([Python Packaging][3])

## Что должен уметь пользователь проекта

Для пользователя библиотеки есть четыре базовых сценария:

### 1. Установка из PyPI

```bash
python -m pip install mtracker
```

Это самый обычный сценарий: `pip` находит пакет в индексе и устанавливает его.

### 2. Установка из локального исходного дерева

```bash
python -m pip install .
```

Так устанавливают проект из текущего каталога. Это ближе всего к реальной установке и полезно для CI, сборки и проверок перед публикацией. ([Pip Documentation][4])

### 3. Editable install для разработки

```bash
python -m pip install -e .
```

Editable install не копирует файлы проекта в site-packages, а подключает исходное дерево напрямую. Это удобно именно для разработки: код меняется, и изменения сразу видны без переустановки. При этом важно помнить, что поведение editable install и обычной установки может отличаться, поэтому перед релизом полезно проверять и “обычную” установку тоже. ([Pip Documentation][4])

### 4. Установка собранного wheel

```bash
python -m pip install dist/*.whl
```

Wheel — это готовый дистрибутив для установки. PyPA рекомендует публиковать и wheel, и sdist: wheel ускоряет установку, а sdist нужен как исходный дистрибутив и резервный путь для систем, где готового wheel нет. ([Python Packaging][5])

## Установка прямо из GitHub

Иногда пакет ещё не опубликован в PyPI, но репозиторий уже оформлен как installable-проект. Тогда `pip` умеет ставить пакет прямо из Git-репозитория. Общая форма — `ProjectName @ VCS_URL`. Для Git это выглядит так: ([Pip Documentation][6])

```bash
python -m pip install "mtracker @ git+https://github.com/standlab/mtracker.git"
#python -m pip install "mtracker @ git+https://github.com/ORG/mtracker.git@v1.0.0"
#python -m pip install "mtracker @ git+https://github.com/ORG/mtracker.git@main"
```

Практическое замечание: для воспроизводимости лучше ставить не `main`, а конкретный тег релиза или commit/tag, который вы контролируете. Кроме того, если подходящая версия уже установлена, `pip` не обязан переустанавливать пакет только потому, что изменился commit; в таких случаях может понадобиться `--upgrade`. ([Pip Documentation][7])

## Отдельно: установка пакета из монорепозитория

Если Python-пакет лежит не в корне репозитория, а внутри подпроекта, `pip` умеет установить его через `#subdirectory=...`. Это официальный сценарий для VCS URL. ([Pip Documentation][7])

Пример структуры монорепозитория:

```text
repo/
├── libs/
│   └── mtracker/
│       ├── pyproject.toml
│       └── src/
└── apps/
    └── analytics_api/
        ├── pyproject.toml
        └── src/
```

Установка пакета из подпапки такого репозитория:

```bash
python -m pip install \
  "ndfl @ git+https://github.com/vesninam/test-git-fossdev3.git@master#subdirectory=testing/tdd"
```

Это стоит вынести в отдельный подраздел занятия, потому что студентам часто кажется, что installable-проект обязан лежать в корне репозитория. На практике это не так: главное, чтобы в указанной подпапке был полноценный Python-проект со своим `pyproject.toml`.

## Что хранить в `pyproject.toml`

* `[build-system]` описывает backend сборки;
* `[project]` хранит основные метаданные и runtime-зависимости;
* dev-инструменты собраны в Poetry group.

Poetry поддерживает runtime-зависимости в `project.dependencies` по PEP 621, а dev-зависимости — через dependency groups. Для Poetry 2 это хороший и современный вариант. ([Poetry][8])

Пример:

```toml
[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

[project]
name = "mtracker"
version = "1.0.0"
description = "Simple tracker package used in course examples"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "matplotlib>=3.8,<4.0"
]

[tool.poetry.group.dev.dependencies]
pytest = "^8.0.0"
ruff = "^0.11.0"
mypy = "^1.10.0"
build = "^1.2.0"
twine = "^6.1.0"
```

Поле `requires-python` важно показывать отдельно: именно оно ограничивает допустимые версии Python для установки. Одних classifiers для этого недостаточно. ([Python Packaging][9])

## Сборка проекта

Сегодня стандартный путь сборки — это:

```bash
python -m build
```

Эта команда вызывает backend, описанный в `pyproject.toml`, и по умолчанию собирает и source distribution, и wheel. Именно этот путь PyPA рекомендует вместо прямых вызовов `python setup.py sdist` и `python setup.py bdist_wheel`. ([Python Packaging][1])

После сборки в каталоге `dist/` обычно появляются два файла:

* `mtracker-1.0.0.tar.gz` — sdist;
* `mtracker-1.0.0-py3-none-any.whl` — wheel.

Для pure-Python проекта wheel часто имеет вид `py3-none-any`, то есть не привязан к платформе и конкретной реализации Python 3. ([Python Packaging][5])

## Публикация в TestPyPI

Для учебного проекта лучше сначала публиковать пакет в TestPyPI, а не в основной индекс. PyPA рекомендует использовать для загрузки `twine`, а не `python setup.py upload`. ([Python Packaging][1])

Проверка и публикация:

```bash
python -m twine check dist/*
python -m twine upload --repository testpypi dist/*
```

Установка из TestPyPI:

```bash
python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  mtracker
```

`--extra-index-url` полезен, если у вашего тестового пакета есть зависимости, которых нет в TestPyPI, но которые есть в основном PyPI. Именно такой сценарий рекомендует документация PyPA. ([Python Packaging][13])

## Что важно запомнить

1. Git-репозиторий и installable-пакет — это не одно и то же.
2. Для современного Python-проекта центральный файл — `pyproject.toml`.
3. `setup.py` как конфиг ещё допустим, но запускать `python setup.py ...` напрямую не надо.
4. Runtime-зависимости библиотеки должны жить в метаданных проекта, а не извлекаться из `requirements.txt` или lock-файла.
5. Для разработки полезен editable install, но перед публикацией нужно отдельно проверить обычную установку или установку wheel.
6. Пакет можно ставить не только из PyPI, но и прямо из Git-репозитория.
7. Если пакет лежит внутри монорепозитория, `pip` умеет ставить его через `#subdirectory=...`. ([Python Packaging][3])


## Доп. материал (сравненние pyproject.toml и setup.py)

Чтобы было понятнее в чем сходства и различия в `setup.py` и `pyproject.toml` соберем их в одной таблице.

| Назначение                                                                                                                                     | `setup.py`                                         | `pyproject.toml`                                                                                      | Кем / для чего используется                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Модель описания проекта**: в одном случае можно программно описывать логику, в другом — декларативно описывать метаданные и параметры сборки | Императивный подход: исполняемый Python-скрипт     | Декларативный подход: статический TOML-файл                                                           | `setuptools`, `distutils` (исторически), современные build frontend’ы и backend’ы |
| **Основные метаданные проекта**: имя, версия, авторы, описание, лицензия, Python version requirement и т.д.                                    | Аргументы `setup(...)`                             | Таблица `[project]`                                                                                   | `pip`, PyPI, `build`, `Poetry`, `Flit`, `Hatch`, `setuptools`                     |
| **Основные зависимости**: какие библиотеки нужны для работы пакета                                                                             | `install_requires`                                 | `dependencies`                                                                                        | `pip`, `Poetry`, `PDM`, build backend’ы                                           |
| **Необязательные группы зависимостей**: например, `dev`, `test`, `docs`                                                                        | `extras_require`                                   | `optional-dependencies`                                                                               | `pip install .[dev]`, `Poetry`, `setuptools`                                      |
| **Описание системы сборки**: какой backend использовать и какие пакеты нужны для сборки проекта                                                | Отдельного стандартного механизма нет              | `[build-system]`                                                                                      | `pip`, `python -m build`, другие build frontend’ы                                 |
| **CLI и точки входа**: сопоставление имени команды и Python-функции                                                                            | `entry_points`, `console_scripts`                  | `[project.scripts]`, `[project.entry-points]`                                                         | `pip`, `setuptools`, `Poetry`, `Flit`                                             |
| **Централизация настроек инструментов**: линтеры, форматтеры, тесты, type checker’ы                                                            | Обычно нужны отдельные файлы конфигурации          | `[tool.*]`                                                                                            | `Ruff`, `Black`, `pytest`, `mypy`, `coverage` и др.                               |
| **Кастомная логика сборки**: генерация кода, C/C++-расширения, нестандартные шаги сборки                                                       | Очень гибкий: можно писать произвольный Python-код | Более ограниченный и предсказуемый; сложная логика обычно переносится в build backend или его плагины | Чаще всего `setuptools`, Cython, backend-specific plugins                         |
| **Editable install**: установка в режиме разработки без переустановки после каждого изменения                                                  | Поддерживается исторически                         | Поддерживается современным стандартом через backend hooks                                             | `pip install -e .`, PEP 660                                                       |
| **Статус в экосистеме**: современный способ описывать Python-проект                                                                            | Прямой запуск `python setup.py ...` устарел        | Текущий рекомендуемый стандарт                                                                        | Весь современный packaging ecosystem                                              |
                                         

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="my-cool-app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    extras_require={
        "dev": ["pytest", "black"],
    },
    entry_points={
        "console_scripts": [
            "cool-cli = my_app.main:run",
        ],
    },
)
```

```
# pyproject.toml

[build-system]
# This replaces the need for a setup.py script
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my-cool-app"
version = "0.1.0"
description = "A modern example project"
dependencies = [
    "requests>=2.25.1",
]

[project.optional-dependencies]
dev = ["pytest", "black"]

[project.scripts]
# This replaces entry_points
cool-cli = "my_app.main:run"

[tool.black]
# You can now put tool configs here instead of separate files!
line-length = 88
target-version = ['py39']

```

[1]: https://packaging.python.org/guides/tool-recommendations/ "Tool recommendations - Python Packaging User Guide"
[2]: https://packaging.python.org/en/latest/specifications/pyproject-toml/?utm_source=chatgpt.com "pyproject.toml specification"
[3]: https://packaging.python.org/en/latest/discussions/setup-py-deprecated/ "Is setup.py deprecated? - Python Packaging User Guide"
[4]: https://pip.pypa.io/en/stable/topics/local-project-installs/ "Local project installs - pip documentation v26.0.1"
[5]: https://packaging.python.org/en/latest/discussions/package-formats/ "Package Formats - Python Packaging User Guide"
[6]: https://pip.pypa.io/en/stable/topics/vcs-support/ "VCS Support - pip documentation v26.0.1"
[7]: https://pip.pypa.io/en/latest/_sources/topics/vcs-support.md.txt "pip.pypa.io"
[8]: https://python-poetry.org/docs/managing-dependencies/ "
Managing dependencies | Documentation | Poetry - Python dependency management and packaging made easy
"
[9]: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/ "Writing your pyproject.toml - Python Packaging User Guide"
[10]: https://packaging.python.org/discussions/install-requires-vs-requirements/ "install_requires vs requirements files - Python Packaging User Guide"
[11]: https://python-poetry.org/docs/managing-dependencies/?utm_source=chatgpt.com "Managing dependencies | Documentation"
[12]: https://python-poetry.org/docs/main/faq/?utm_source=chatgpt.com "FAQ | main | Documentation | Poetry - Python dependency ..."
[13]: https://packaging.python.org/guides/using-testpypi/ "Using TestPyPI - Python Packaging User Guide"
