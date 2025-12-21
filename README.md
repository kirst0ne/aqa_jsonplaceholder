# API Testing Project

Проект для тестирования REST API (JSONPlaceholder) с использованием Pytest и Allure.

## Структура проекта
**project/**  
├── **data/** - JSON-файлы с тестовыми данными  
│   ├── albums.json  
│   ├── comments.json  
│   ├── posts.json  
│   └── users.json  
├── **helpers/** - Вспомогательные модули  
│   ├── api_client.py - Клиент для работы с API  
│   ├── config.py - Конфигурация  
│   ├── logger.py - Логирование  
│   ├── utils.py - Утилиты  
│   └── validators.py - Валидаторы ответов  
├── **tests/** - Тесты  
│   ├── **api/** - API-тесты  
│   │   ├── conftest.py - Фикстуры Pytest  
│   │   ├── test_posts.py - Тесты для /posts  
│   │   └── test_users.py - Тесты для /users  
│   ├── **ui/** - UI-тесты (заготовка)  
│   └── **unit/** - Unit-тесты (заготовка)  
├── **allure-results/** - Результаты Allure (генерируется)  
├── **reports/** - Отчёты (заготовка)  
├── **requirements.txt** - Зависимости Python  
└── **README.md** - Этот файл 

## Установка

1. Установите зависимости:

```bash
pip install -r requirements.txt
```

2. Установите Allure Commandline (отдельно от Python)

## Запуск тестов

- Запуск всех API-тестов
```bash
python -m pytest tests/api/
```
- Запуск конкретного модуля
```bash
python -m pytest tests/api/test_posts.py
```
- Запуск с генерацией Allure-отчёта
```bash
python -m pytest tests/api/ --alluredir=./allure-results
```
## Просмотр Allure-отчёта

1. После запуска тестов с --alluredir выполните:
```bash
allure serve allure-results
```
2. Отчёт откроется автоматически в браузере на http://localhost:8080


## Используемые технологии

- Python 3.x + pytest — фреймворк тестирования
- requests — HTTP-запросы к API
- allure-pytest — интеграция с Allure
- JSONPlaceholder — Mock REST API

## Примечания

- Тестовые данные находятся в папке data/
- Результаты Allure сохраняются в allure-results/ (не коммитить в git)
- Для очистки результатов: rm -rf allure-results/
