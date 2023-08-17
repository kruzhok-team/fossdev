 # Культура и инструменты open source разработки

## Оглавление

* Раздел 1. Введение, подходы к программированию
  - [Терминология](/educational_materials/terms/content.md)
  - [Командная строка как универсальный способ взаимодействия с любым компьютером](/educational_materials/bash/content.md)
    - [Задачи](/educational_materials/bash/exercises.md)
    - [Вопросы](/educational_materials/bash/quiz.md)
  - [Система контроля версий git. Основные понятия. Работа с локальным репозиторием. Локальное использование](/educational_materials/git_base/content.md)
  - Git как инструмент командной работы. Работа с удаленными репозиториями.
  - Знакомство с платформами размещения исходного кода программ на примере Github
  - [Среды разработки. Основные возможности](/educational_materials/ide/content.md)
  - [Оформление кода. Виды стилей. Автоматические средства для форматирование](/educational_materials/styles/content.md)
    - [Задачи](/educational_materials/styles/exercises.md)
    - [Вопросы](/educational_materials/styles/quiz.md)
  - [Зачем нужно документирование. Учимся читать и использовать в своем проекте чужой код с Github](/educational_materials/github/content.md)
* Раздел 2. Работа над проектом
  - [Стадии жизни проекта](/educational_materials/stages/content.md)
  - [Работа над MVP. Этапы разработки и проверка гипотез](/educational_materials/mvp/content.md)
  - [UML диаграммы](/educational_materials/uml/content.md)
    - [Задачи](/educational_materials/uml/exercises.md)
    - [Вопросы](/educational_materials/uml/quiz.md)
  - [Код -> Библиотека](/educational_materials/code_to_lib/content.md)
    - [Задачи](/educational_materials/code_to_lib/exercises.md)
    - [Вопросы](/educational_materials/code_to_lib/quiz.md)
  - [Основы Open Source](/educational_materials/open_source/content.md)
  - [Обзор открытых лицензий и типов проектов, для которых они подходят](/educational_materials/open_license/content.md)
  - [Создаем свой первый статичный сайт на GitHub Pages](/educational_materials/github_pages/content.md)
    - [Задачи](/educational_materials/github_pages/exercises.md)
    - [Вопросы](/educational_materials/github_pages/quiz.md)
* Раздел 3. Инструменты
  - [Знакомство с рабочим окружением. Системное окружение. Создание виртуального окружения venv для проекта](/educational_materials/path_venv/content.md)
    - [Задачи](/educational_materials/path_venv/exercises.md)
    - [Вопросы](/educational_materials/path_venv/quiz.md)
  - [Стандарты составления документации к коду и приложению](/educational_materials/docs/content.md)
    - [Задачи](/educational_materials/docs/exercises.md)
    - [Вопросы](/educational_materials/docs/quiz.md)
  - [Автотесты и культура разработки кода test-driven-development](/educational_materials/testing/content.md)
    - [Задачи](/educational_materials/testing/exercises.md)
    - [Вопросы](/educational_materials/testing/quiz.md)
  - [Логирование работы приложения](/educational_materials/logging/content.md)
    - [Задачи](/educational_materials/logging/exercises.md)
    - [Вопросы](/educational_materials/logging/quiz.md)
  - [Менеджеры пакетов Python. Сборка проекта](/educational_materials/packaging/content.md)
    - [Задачи](/educational_materials/packaging/exercises.md)
    - [Вопросы](/educational_materials/packaging/quiz.md)
  - [Управление вызовом приложений: автоматизация процессов посредством планировщика задач crontab и systemctl](/educational_materials/managers/content.md)
    - [Задачи](/educational_materials/managers/exercises.md)
    - [Вопросы](/educational_materials/managers/quiz.md)
  - [Контейнеризация на примере Docker.](/educational_materials/docker_base/content.md)
    - Задачи
    - [Вопросы](/educational_materials/docker_base/quiz.md)
  - Практическое использование Docker
* Дополнительные материалы
  - [Концепция сети в Docker](/educational_materials/docker_network/content.md)
  - [Реестр Docker](/educational_materials/docker_hub/content.md)

## Сборка 

Создайте виртуальное окружение (опционально):

```bash
conda create -n sphinx_md python=3.10
conda activate sphinx_md
```

Установите sphinx и поддержку markdown:

```bash 
pip install sphinx
pip install --upgrade myst-parser

```

Соберите html (находясь в корневой директории проекта):

```bash
make html
```

В корневой директории появится папка build, где будет находиться собранная документация.

Для сборки pdf установите latexmk и поддержку кириллицы:

```bash
sudo apt install latexmk
sudo apt install texlive-lang-cyrillic
make latexpdf
```


