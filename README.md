
# FamTube


### Run Server
 - create virtualenv `python3 -m virtualenv venv` and activate
 - install python Libs `pip install -r requirements.txt`
 - `python manage.py makemigrations`
 - `python manage.py migrate`
 - run Django App `python3 manage.py runserver 0:8000`
 

 ### Celery/Scheduler and Redis cmds:
  - Celery-beat - `celery -A FamTube beat -l info`
  - Celery-Worker - `celery -A FamTube worker -l info`
  - start Redis - `redis.server`

### Docker setups (Pending)
  - docker-compose -up build
  
  
### API Contracts
  - Get All Video -> `http://0.0.0.0:8000/api/video/`
  - Search Video by title -> `http://0.0.0.0:8000/api/search/?title=maroon`
  - Search by description -> `http://0.0.0.0:8000/api/search/?desc=maroon`
  - Search by Partial Query ("How to make tea" -> "tea how") -> `http://0.0.0.0:8000/api/search/?partial_query=how tea`






