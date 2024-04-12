# Запуск с помощью докера

### Создайте файл .env и добавьте в него следующие значения
```
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
```

### Запустите докер  
`docker-compose up --build`

### Создайте простое меню
`docker-compose exec backend python manage.py createmenu`

### Вы можете создать суперпользователя и добавить в админке еще несколько меню
`docker-compose exec backend python manage.py createsuperuser`

### откройте сайт по ссылке http://localhost

# Запуск без докера

### Установите значение STATICFILES_DIRS и уберите STATIC_ROOT в settings.py
```
# STATIC_ROOT = 'static'

STATICFILES_DIRS = ['static']
```

### Поменяйте базу данных на sqlite3 в settings.py
```
DATABASES = {
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    },

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Установите зависимости
```
pip install -r requirements.txt
pip install psycopg2
```

### Мигрируйте изменения в бд и запустите сервер
```
python manage.py migrate
python manage.py runserver
```

# Как нарисовать меню в любом шаблоне
```
{% load draw_menu %}
{% draw_menu 'Россия' %}
```