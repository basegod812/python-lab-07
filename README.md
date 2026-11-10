# Лабораторная работа №7 — Работа с СУБД в Python

**ФИО:** Шкловский Герман Вячеславович  
**Группа:** 221141  
**Вариант:** 2  
**Номер лабораторной:** 7

## Задания варианта №2
- Среднее №2 — вставка записи в таблицу SQLite через INSERT.
- Среднее №4 — обновление записи через UPDATE.
- Среднее №7 — создание нескольких связанных таблиц (`groups`, `students`).
- Повышенное №2 — операции CRUD через SQLAlchemy ORM, сущности `Department` и `Employee`.
- Повышенное №6 — работа с сервером PostgreSQL через psycopg2, SQL-запрос к серверу.

## Запуск
```bash
python -m pip install -r requirements.txt
python main.py
python -m unittest discover -s tests -v
```
Требуется Python 3.11+. SQLite и ORM-пример работают без отдельного сервера.

## Подключение PostgreSQL
Установи сервер PostgreSQL и создай базу и пользователя. Укажи строку подключения в переменной окружения (не сохраняй пароль в репозитории):

PowerShell:
```powershell
$env:POSTGRES_DSN="host=localhost dbname=postgres user=postgres password=YOUR_PASSWORD"
python main.py
```
При отсутствии `POSTGRES_DSN` внешний тест корректно пропускается. Реальное подключение PostgreSQL должно быть проверено на машине с сервером.
