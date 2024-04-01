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
