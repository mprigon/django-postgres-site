## Задача
Необходимо создать сайт с админ панелью и 2-мя кабинетами
на Flask или Django. На сайте помимо админки должны быть
два кабинета заказчика и исполнителя.
Минимальный набор полей в профилях (имя, контактные данные,
опыт). БД PostgreSQL

## БД, запуск
БД на DockerHub
TODO: образ на Hub (с образом уже созданной базы)
если загрузить контейнер только с PostgreSQL (например, 12),
то создать в нем базу

docker run --name postgres:12 -p 5432:5432 -d -e POSTGRES_PASSWORD=hello postgres12
docker exec -it postgres12 psql -U postgres -h localhost

CREATE DATABASE django_site;
CREATE USER django_user WITH PASSWORD 'django';
GRANT ALL PRIVILEGES ON DATABASE django_site TO django_user;

в терминале запустить:
docker run --name postgres12 -p 5432:5432 -d -e POSTGRES_PASSWORD=hello mprigon/postgres:12
docker start postgres12
пользователь и пароль к БД уже заданы в settings.py

## Сайт на Django
pip intall requirements
python manage.py runserver

Можно регистрироваться как через сайт, так и через admin
В личном кабинете можно просматривать свои данные и обновлять часть.

Superuser: admin - admin
Заказчик и Исполнитель:
masha - masha12345
ivanov_ivan - ivanov12345
