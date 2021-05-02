# fastapi_auth_service
Simple FastAPI app for authorization

# Инструкция для локального запуска в dev-режиме

## Подготовка окружения 

#### Версия Python
python3.9.1

#### Установка виртуального окружения
`python3 -m venv venv`

#### Применение виртуального окружения
`source venv/bin/activate`

#### Установка зависимостей
`pip install -r requirements.txt`

## Развертывание локальной инфраструктры
### Поднять все контейнеры

`cd deployment && docker-compose up -d`