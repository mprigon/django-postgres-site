## Задача
Необходимо создать сайт с админ панелью и 2-мя кабинетами
на Flask или Django. На сайте помимо админки должны быть
два кабинета заказчика и исполнителя.
Минимальный набор полей в профилях (имя, контактные данные,
опыт). БД PostgreSQL.

## БД, запуск
БД PostgreSQL выгружена с помощью pd_dumpall

Файл копии БД в папке postgres_dump: psql12

Восстановить копию БД:
Если в контейнере (например, Postgres:12), то

docker run --name postgres12 -p 5432:5432 -d -e POSTGRES_PASSWORD=hello postgres:12

docker exec -it postgres12 /bin/bash

psql -U postgres -w -f psql12 postgres

Если postgres12 был остановлен, то в терминале запустить:

docker start postgres12

пользователь и пароль к БД уже заданы в settings.py

## Сайт на Django
pip intall requirements
python manage.py runserver

Можно регистрироваться как через сайт, так и через admin.
В личном кабинете можно просматривать свои данные и обновлять часть.

Superuser: admin - admin

Два пользователя (Заказчик и Исполнитель):

masha - masha12345

ivanov_ivan - ivanov12345
