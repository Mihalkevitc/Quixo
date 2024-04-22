# Используем базовый образ Python
FROM python:3.9

# Устанавливаем переменную окружения для отображения вывода Python в консоль
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости приложения (requirements.txt) в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости приложения
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . /app/

# Команда для запуска приложения (замените на вашу команду)
CMD ["python", "Quixo.py"]
