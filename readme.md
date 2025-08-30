
## Содержание:  
Задача: **API-сервис для вопросов и ответов**  
Описание задачи: [docs/challenge.md](docs/challenge.md)  
[Быстрый старт](#быстрый-старт)  
[Архитектура и подход](#архитектура-и-подход)  
[Источники](#источники)  


# Быстрый старт

## Рекомендуемый способ (Docker Compose)

Самый простой способ запустить приложение - использовать Docker Compose:

```bash
docker compose up
```

Этот способ автоматически поднимет все необходимые сервисы, включая базу данных PostgreSQL.

## Альтернативный способ (локально)

### 1. Настройка базы данных

Убедитесь, что PostgreSQL установлен и запущен.

### 2. Переменные окружения

Скопируйте шаблон и отредактируйте настройки подключения к базе данных:

```bash
cp .env.dist .env
```

### 3. Установка зависимостей

Создайте виртуальное окружение и установите зависимости:

```bash
uv venv .venv
source .venv/bin/activate
pip install .
```

### 4. Запуск приложения

```bash
cd src
python -m app
```

> **Примечание:** Docker Compose предпочтительнее — все сервисы и зависимости настраиваются автоматически.


# Архитектура и подход

Чтобы реализовать этот проект в рамках технического задания, я выбрал **чистую архитектуру** в качестве основы структуры проекта. Это позволяет выполнить некоторые [критерии](docs/challenge.md#критерии-оценки) должным образом. Сама задача не содержит сложной бизнес-логики, поэтому, исходя из этого и того, что это тестовое задание, я не стал углубляться в сложные паттерны разработки, такие как `Repository` или `Value Object`, а также не реализовал подробные описания ошибок на каждом слое.

Тем не менее, **чистая архитектура** невозможна без этих приемов, поэтому вы можете увидеть реализацию `Unity Of Code` и описательный `Gateway`, но без разделения на чтение и запись.

Соблюдается **Dependency Rule**: каждая зависимость оборачивается в вызываемую функцию, например, в файлах [**main**.py](src/app/__main__.py) и [providers.py](src/app/infrastructure/persistence/providers.py).

Есть и нарушения **Dependency Rule** в слое `/interface`. Например, каждый интерактор получает в качестве зависимости `pydantic` модели. Я сделал это спорное решение, чтобы продемонстрировать свои навыки использовании этих же `pydantic` моделей (о них говорилось в кейсе). Сейчас можно обойтись без них и использовать зависимости из [dto.py](src/app/application/common/dto.py).

В [техническом задании](docs/challenge.md) было сказано что приветствуется, так и подпадает по критерии оценивание наличие миграций и тестов. Все это присутствует. Но относительно тестов - я тестировал на позитивные и негативные тесты, как unit. При этом не хватает двух тестов для эндпоинтов из [answers.py](src/app/interface/routes/answers.py).

Для валидации данных я проверяю в самом де эндпоинте. А на деле, их стоило вынести в паттерн `Value Objecy`, в слой бизнес логики. Но в силу сказанного, я оставил этот как есть.


# Источники
Источники, на которые я часто опираюсь, это проекты людей python-сообществ, а так же популярные статьи.

- [Explicit Architecture - Symfony Demo Application](https://github.com/hgraca/explicit-architecture-php)
- [Explicit Architecture – DDD, Hexagonal, Onion, Clean, CQRS](https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/#application-core-organisation)
- [Litestar Dishka Faststream](https://github.com/Sehat1137/litestar-dishka-faststream)
- [FastAPI Clean Example](https://github.com/ivan-borovets/fastapi-clean-example)
- [Pure Architecture FastAPI](https://github.com/Maclovi/pure-architecture-fastapi)
- [User Service](https://github.com/SamWarden/user_service)