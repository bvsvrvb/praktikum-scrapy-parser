# Асинхронный парсер документации Python
Учебный проект Яндекс Практикум (курс Python-разработчик плюс).

## Описание
Парсер на базе фреймворка Scrapy, который собирает информацию о [документах PEP](https://peps.python.org/) в два файла .csv:
1. В первый файл выводится список всех PEP: Номер, Название и Статус.
2. Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (Статус, Количество).  

## Технологии
[![Python](https://img.shields.io/badge/Python-3.9-3776AB?logo=python)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/Scrapy-2.5.1-60a839)](https://scrapy.org/)

## Запуск проекта
Клонировать репозиторий и перейти в директорию проекта:
```bash
git clone https://github.com/bvsvrvb/praktikum-scrapy-parser.git
```
```bash
cd praktikum-scrapy-parser
```
Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
Запустить парсер:
```bash
scrapy crawl pep
```
