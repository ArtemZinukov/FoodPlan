# FoodPlan

## Описание

Этот проект представляет собой сервис, который позволяет наслаждаться домашней кухней на уровне ресторанного качества. 
Система разработана с использованием Django и предоставляет клиентам возможность приобретать подписку на ежедневные рецепты.

Ссылка на рабочий сайт [FoodPlan](http://194.169.192.82/)
## Установка

Python3 должен быть уже установлен. Затем используйте pip 
(или pip3, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

Далее необходимо создать файл с разрешением .env и внести в него параметры:

   1. DEBUG="по умолчанию False"
   2. DJANGO_SECRET="ваш джанго ключ" 
   3. ALLOWED_HOSTS="по умолчанию ['127.0.0.1', 'localhost']"
   4. YOOKASSA_SECRET_KEY= "ключ для магаза"
   5. YOOKASSA_SHOP_ID= "айди магаза"


Для получения YOOKASSA_SECRET_KEY и YOOKASSA_SHOP_ID необходимо перейти по ссылке
[Юкасса](https://yookassa.ru/connection/), пройти регистрацию и записать полученные ключи в файл env. 

## Запуск

Создайте миграции и примените их:

```
python manage.py makemigrations

python manage.py migrate
```

Создайте суперпользователя для доступа к админке:

```
python manage.py createsuperuser
```

Запустите сервер разработки:

```
python manage.py runserver
```