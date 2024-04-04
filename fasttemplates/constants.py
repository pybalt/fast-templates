import os

MONGO_DIR_NAME = 'mongo'
REDIS_DIR_NAME = 'redis'

MONGO_PROMPT = "MongoDB database"
REDIS_PROMPT = "Redis database"

WORKING_DIR = os.getcwd()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

"BASE LAYOUT"
BASE_LAYOUT = os.path.join(BASE_DIR, "templates\\baselayout")

"SETTINGS LOCATION"
SETTINGS_DIR = "app\\settings.py"

SETTINGS_CLASS_DEFINITION = 'class Settings(BaseSettings):'

"EXTRAS"
DB_DIR = "app\\db"
DB_TREE = os.path.join(BASE_DIR, "templates\\extras\\db")
REDIS_CACHE_TREE = os.path.join(BASE_DIR, "templates\\extras\\cache\\redis")

"Repositories"
FASTAPI_FS = 'FastAPI Fullstack Template by Tiangolo'
FASTAPI_DJANGO_ORM = 'FastAPI with Django ORM by Uhttred'
FASTAPI_FULLSTACK = 'https://github.com/tiangolo/full-stack-fastapi-template.git'
FASTAPI_WITH_DJANGO_ORM = 'https://github.com/uhttred/fastapi-with-django-orm-template.git'

docker_compose_dict = {
    'version': '3.8',
    'services': {
      'backend': {
        'build': '.',
        'command': 'uvicorn app.main:app --host 0.0.0.0 --port 80 --reload --log-level debug',
        'volumes': ['.:/app'],
        'ports': ['8000:80'],
        'env_file': ['.env'],
        },
    },
    'volumes':{
    }
}
mongo_service = {
  'db': {
    'image': 'mongo:latest',
    'ports': ['27017:27017'],
    'volumes': ['mongodb_data_container:/data/db']
  }
}
redis_service = {
  'redis': {
    'image': 'redis:latest',
    'ports': ['6379:6379'],
    'volumes': ['redis_data_container:/data/db']
  }
}
mongo_volume = {
  'mongodb_data_container': {}
}
redis_volume = {
  'redis_data_container': {}
}