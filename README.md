# Культура и инструменты open source разработки

## Оглавление

* Раздел 1. Введение, подходы к программированию
  - [Терминология](/educational_materials/terms/content.md)
  - [Командная строка как универсальный способ взаимодействия с любым компьютером](/educational_materials/bash/content.md)
    - [Вопросы](/educational_materials/bash/quiz.md)
    - [Задачи](/educational_materials/bash/exercises.md)
  - Система контроля версий git. Основные понятия. Работа с локальным репозиторием. Локальное использование
  - Git как инструмент командной работы. Работа с удаленными репозиториями.
  - Знакомство платформами размещения исходного кода программ на примере Github
  - Знакомство с рабочим окружением. Системное окружение. Создание виртуального окружения venv для проекта
  - [Среды разработки. Основные возможности](/educational_materials/ide/content.md)
  - [Оформление кода. Виды стилей. Автоматические средства для форматирование](/educational_materials/styles/content.md)
    - [Вопросы](/educational_materials/styles/quiz.md)
    - [Задачи](/educational_materials/styles/exercises.md)
  - Зачем нужно документирование. Учимся читать и использовать в своем проекте чужой код с Github
* Раздел 2. Работа над проектом
  - [Стадии жизни проекта](/educational_materials/stages/content.md)
  - Работа над MVP. Этапы разработки и проверка гипотез
  - UML диаграммы
  - [Код -> Библиотека](/educational_materials/code_to_lib/content.md)
    - [Задачи](/educational_materials/code_to_lib/exercises.md)
    - [Вопросы](/educational_materials/code_to_lib/quiz.md)
  - Основы опенсорс
  - Обзор открытых лицензий и типов проектов для которых они подходят.
  - Создаем свой первый статичный сайт на GitHub Pages
* Раздел 3. Инструменты
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
  - Docker. Концепция сети в Docker


## Оглавление (obsolete)

* Основы программного обеспечения с открытым исходным кодом
  - [Основы Open Source](01_open_source/main.md)
  - [Обзор открытых лицензий и типов проектов для которых они подходят.](02_open_license/main.md)
  - [Стадии жизни проекта и инструменты для их достижения.](01_stages/main.md)
  - [Работа над MVP. Этапы разработки и проверка гипотез](04_mvp/main.md)
* Раздел 2. Инструменты разработчика
  - [Система контроля версий git. Основные понятия. Работа с локальным репозиторием. Локальное использование](05_git_base/main.md)
  - Основные сценарии использования git. Работа с удаленными репозиториями
  - Знакомство с репозиториями и платформами размещения исходного кода программ на примере Github
  - [Стандарты составления документации к коду и приложению](12_docs/main.md)
  - [Работа в командной строке](16_bash/main.md)
  - [Знакомство с рабочим окружением. Системное окружение. Создание виртуального окружения venv для проекта](17_path_venv)
  - [Менеджеры пакетов Python. Сборка проекта](10_packages/main.md)
  - [Среды разработки. Основные возможности](22_ide/main.md)
  - [Виртуализация и контейнеризация в чем тут разница на примере Docker. Создаем контейнер на базе Linux и настраиваем там рабочее окружение для проекта Python](25_docker_base/main.md)
* Раздел 3. Культура разработки
  - [Оформление кода. Виды стилей. Автоматические средства для форматирование.](14_styles)
  - [Создаем переиспользуемый код. Собираем библиотеку для использования в других проектах.](09_code_to_lib/main.md)
  - [Учимся читать и использовать в своем проекте чужой код с Github](06_github/main.md)
  - [Автотесты и культура разработки кода test-driven-development](23_testing/main.md)
  - [Логирование работы приложения.](24_logging)
  - Управление вызовом приложений - автоматизация процессов, посредством планировщика задач crontab и systemctl
* Раздел 4. Факультативы по оформлению проекта
  - [Создаем свой первый статичный сайт на GitHub Pages](36_git_hub_pages)
  - [Средства для сборки документации](12_docs/main.md#sphinx)
* Невошедшее
  - [Концепция сети в Docker](32_docker_network/main.md)
  - [Реестр Doсker](33_dockerhub/main.md)
  - [UML диаграммы](13_uml/main.md)


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


