# Культура и инструменты open source разработки

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


