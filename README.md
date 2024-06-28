# ProductManagement
Тестовое задание

# Запуск
Устанавливаем [Git](https://git-scm.com/downloads) и [Docker](https://www.docker.com/products/docker-desktop/)
```
git clone https://github.com/Noloquideus/ProductManagement.git
```
```
docker-compose up --build
```

# Стек
- Python
- - Sqlalchemy + asyncpg, alembic
- - Sqladmin
- - прочие зависимости
- Docker, docker-compose
- Redis (keydb)

# F.A.Q
- ```Poetry```использован исключительно для фиксации зависимостей и их связей - как по мне, его не удобно использовать в докере.
- Система уровней доступа - быстрее и проще, чем роли и разрешения.
- Реализована кастомная фильтрация для продуктов, хотя можно было использовать **[Fastapi-filter](https://github.com/arthurio/fastapi-filter)**
- Настроено логирование в консоль (просто как пример)
- Пытался выдержать чистую архитектуру
- Мониторинг, nginx отсутствует aka зачем
