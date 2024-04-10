# TP2024
CalDAV task manager app

## Build
```bash
$ cp .env.example .env
$ docker-compose build
```

## Run
```bash
$ docker-compose up -d
```
При первом включении нужно:
1. Перейти на web-панель Nextcloud http://127.0.0.1:80
2. Ввести логин и пароль в соотвестии с .env файлом (```NEXTCLOUD_ADMIN_LOGIN```, ```NEXTCLOUD_ADMIN_PASSWORD```).
3. На следующем окне выбрать "Установить рекомендуемые приложения"


## Stop
```bash
$ docker-compose down
```