## Что реализованно

* Главная страница
* Страница туров
* Страница направлений

![MVP](mvp.gif)

#### Установка проекта

- установить версию python 3.8
  
- создать виртуальное окружение 
```shell script
python3.8 -m venv venv
```

- активировать виртуальное окружение
```shell script
source venv/bin/activate
```

- установить зависимости
```shell script
pip install -r requirements.txt
```

- запустить django-проект
```shell script
gunicorn django_tours.wsgi
```

- открыть в браузере http://localhost:8000 
