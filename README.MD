# Запуск приложения
# Поднять зависмости
 ```shell
make docker.up
```

# Подождать когда поднимутся зависимости и накатить миграции:
```shell
make migrate.up
```
# Запустить приложение:
```shell
make run.local
```




# Планы на доработку:
- написать тесты
- причесывать к чистой архитектуре
- добавление работы не только access token , но так же работы с refresh token