import os

MONGO_DIR_NAME = 'mongo'
REDIS_DIR_NAME = 'redis'

MONGO_PROMPT = "MongoDB database"
REDIS_PROMPT = "Redis database"

WORKING_DIR = os.getcwd()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

"BASE LAYOUT"
BASE_LAYOUT = os.path.join(BASE_DIR, "templates\\baselayout")


"EXTRAS"
DB_TREE = os.path.join(BASE_DIR, "templates\\extras\\db")
DB_DIR = os.path.join(BASE_LAYOUT, "app\\db")
REDIS_CACHE_TREE = os.path.join(BASE_DIR, "templates\\extras\\cache\\redis")

"Repositories"
FASTAPI_FS = 'FastAPI Fullstack Template by Tiangolo'
FASTAPI_DJANGO_ORM = 'FastAPI with Django ORM by Uhttred'
FASTAPI_FULLSTACK = 'https://github.com/tiangolo/full-stack-fastapi-template.git'
FASTAPI_WITH_DJANGO_ORM = 'https://github.com/uhttred/fastapi-with-django-orm-template.git'

DOCKER_COMPOSE_YML = """    depends_on:
        - db
    environment:
        - MONGO_URI: mongodb://db:27017
  db:
    image: mongo:latest
    ports:
      - "27017:27017" # This config is to expose the port to the host machine. 
      # We could delete this line and the app would still be able to connect to the db container
    volumes:
      - mongodb_data_container:/data/db
volumes:
  mongodb_data_container:
"""
