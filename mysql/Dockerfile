# Используем базовый образ MySQL
FROM mysql:5.7

# Устанавливаем переменные окружения для создания пользователя и базы данных
ENV MYSQL_DATABASE=standings \
    MYSQL_USER=user \
    MYSQL_PASSWORD=password \
    MYSQL_ROOT_PASSWORD=rootpassword

# Копируем дамп базы данных, если необходимо
# COPY mydatabase.sql /docker-entrypoint-initdb.d/

# Прописываем правильную кодировку
# ENV LANG=C.UTF-8

# Устанавливаем часовой пояс
# ENV TZ=UTC

# Пример изменения конфигурации MySQL (необязательно)
# COPY my.cnf /etc/mysql/conf.d/

# Порт по умолчанию для MySQL
EXPOSE 3306
