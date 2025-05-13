# GitHub Actions: автоматизация сборки и тестирования

## Введение

GitHub Actions — это инструмент для автоматизации процессов в репозиториях GitHub. Он позволяет настроить CI/CD (Continuous Integration / Continuous Deployment) для проектов, что упрощает процессы сборки, тестирования и развертывания приложения. В этом документе мы рассмотрим, как настроить GitHub Actions для автоматической сборки и тестирования вашего проекта.

## 1. Что такое GitHub Actions?

GitHub Actions позволяет вам автоматизировать рабочие процессы с использованием **workflow** файлов. Эти файлы могут запускать действия при различных событиях, таких как создание pull request, push изменений в репозиторий или создание релиза.

## 2. Основные компоненты GitHub Actions

- **Workflow** — описание процесса автоматизации. Хранится в `.github/workflows` директории.
- **Job** — набор шагов, которые выполняются в одном окружении.
- **Step** — отдельная команда или действие, которое выполняется в рамках job.
- **Action** — действие, которое может быть использовано в шаге для выполнения задачи (например, установка зависимостей, тестирование, сборка документации).

## 3. Пример настройки GitHub Actions

В следующем примере мы настроим GitHub Actions для проекта на Python, чтобы автоматически устанавливать зависимости, запускать тесты и собирать документацию с помощью Sphinx.

### 1. Создайте файл workflow

В корневой директории вашего репозитория создайте директорию `.github/workflows`, если она ещё не существует, и файл, например, `python.yml`:

```bash
mkdir -p .github/workflows
nano .github/workflows/python.yml
```

### 2. Пример конфигурации workflow:

```yaml
name: Python CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest tests/

      - name: Build documentation
        run: |
          cd docs
          make html

      - name: Upload documentation artifacts
        uses: actions/upload-artifact@v2
        with:
          name: docs
          path: docs/_build/html
```

### 3. Объяснение конфигурации:

- **name**: Имя workflow.
- **on**: Указывает события, при которых workflow будет запущен. В данном случае при push в ветку `main` и при pull request.
- **jobs**: Рабочие процессы, которые должны быть выполнены. Здесь настроен один job — `build`, который выполняется на виртуальной машине с Ubuntu.
- **steps**: Шаги, которые выполняются в рамках этого job:
  - `actions/checkout@v2`: Проверка репозитория.
  - `actions/setup-python@v2`: Установка Python.
  - Установка зависимостей с помощью `pip install`.
  - Запуск тестов с использованием `pytest`.
  - Сборка документации с помощью Sphinx.
  - Загрузка собранной документации как артефакт.

## 4. Проверка работы GitHub Actions

После того как вы добавите файл `.github/workflows/python.yml` в репозиторий, GitHub Actions будет автоматически запускаться на каждое изменение в ветке `main` или на pull request. Вы можете увидеть статус сборки и тестов в разделе "Actions" вашего репозитория.

## 5. Полезные ссылки

- [Документация GitHub Actions](https://docs.github.com/en/actions)
- [Actions for Python](https://github.com/actions/setup-python)
- [GitHub Actions: Введение](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions)
