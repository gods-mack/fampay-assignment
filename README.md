
# FamTube


### Run Server
 - create virtualenv `python3 -m virtualenv venv` and activate
 - install python Libs `pip install -r requirements.txt`
 - `python manage.py makemigrations`
 - `python manage.py migrate`
 - run Django App `python3 manage.py runserver 0:8001`
 

 ### Scheduler:
  - Celery-beat - `celery -A FamTube beat -l info`
  - Celery-Worker - `celery -A FamTube worker -l info`
  - start Redis - `redis.server`




