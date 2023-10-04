# api_final
api final
Финальный проект Спринта №11 API для Yatube

Проект предназначен для демонстрации и закрепления знаний 
о технологии Django Rest Framework

Для запуска проекта необходимо:

1. Клонировать репозиторий и перейти в него в командной строке:

    git clone https://github.com/gbolezin/api_final_yatube.git
    cd api_final_yatube

2. Cоздать и активировать виртуальное окружение:

    python3 -m venv venv
    source venv/bin/activate

3. Установить зависимости из файла requirements.txt:

    python3 -m pip install --upgrade pip
    pip install -r requirements.txt

4. Выполнить миграции:

    python3 manage.py migrate

5. Запустить проект:

    python3 manage.py runserver


Документация по проекту доступна после запуска проекта по ссылке:
    
    http://127.0.0.1:8000/redoc/

Примеры запросов:
 - GET http://127.0.0.1:8000/api/v1/posts/ - получение всех публикаций
 
 Ожидаемый формат ответа:
 {
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}

 - POST http://127.0.0.1:8000/api/v1/follow/ - оформление подписки на пользователя
 параметры запроса:
 {
    "following": "string"
 }

 Ожидаемый формат ответа:
 {
    "user": "string",
    "following": "string"
 }

Использованные технологии:
 - Python
 - Django
 - Django Rest Framework
 - Djoser JWT

 Автор: Георгий Болезин, g.bolezin@icloud.com, tg:@gbolezin
