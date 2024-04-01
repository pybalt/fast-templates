import os

import typer
import questionary

from constants import *
from utils import *

app = typer.Typer()


def custom() -> None:
    options = questionary.checkbox("What do you want to add?", choices=[
        REDIS_PROMPT, MONGO_PROMPT]).ask()
    mongo_present = MONGO_PROMPT in options
    redis_present = REDIS_PROMPT in options
    add_base_layout()

    if mongo_present:
        add_mongo()
        print("MongoDB database added")
    if redis_present:
        add_redis()
        print("Redis database added")
        cache = questionary.confirm("Do you want to use Redis as cache?").ask()
        if cache:
            add_cache_with_redis()
            print("Redis cache added")


def popular() -> None:
    "Clones the popular template from the github repository"

    optionLambdas = {
        FASTAPI_FS: lambda: os.system(f'git clone {FASTAPI_FULLSTACK} {WORKING_DIR}'),
        FASTAPI_DJANGO_ORM: lambda: os.system(
            f'git clone {FASTAPI_WITH_DJANGO_ORM} {WORKING_DIR}')
    }

    option = questionary.select("Which popular template do you want to clone?", choices=[
        FASTAPI_FS, FASTAPI_DJANGO_ORM]).ask()

    optionLambdas[option]()

    print("Popular template added")


@app.command()
def main() -> None:
    popular_or_simplified_functions = {
        'Popular': popular,
        'Custom': custom
    }
    popular_or_simplified = questionary.select("Popular templates or custom templates?", choices=[
        'Popular', 'Custom']).ask()
    popular_or_simplified_functions[popular_or_simplified]()


def add_base_layout() -> None:
    os.makedirs(WORKING_DIR, exist_ok=True)
    copy_files(BASE_LAYOUT, WORKING_DIR)


def add_mongo() -> None:
    MONGO_DIR = os.path.join(WORKING_DIR, DB_DIR)
    os.makedirs(MONGO_DIR, exist_ok=True)
    copy_files(DB_TREE, MONGO_DIR, ignore_dirs=[REDIS_DIR_NAME])

    # Add dnspython & pymongo to requirements.txt
    with open(os.path.join(WORKING_DIR, "requirements.txt"), "a") as f:
        f.write("\ndnspython\npymongo\n")

    # Modify docker-compose.yml
    with open(os.path.join(WORKING_DIR, "docker-compose.yml"), "a") as f:
        f.write(DOCKER_COMPOSE_YML)

    add_mongo_uri_to_settings()


def add_redis() -> None:
    REDIS_DIR = os.path.join(WORKING_DIR, DB_DIR)
    os.makedirs(REDIS_DIR, exist_ok=True)
    copy_files(DB_TREE, REDIS_DIR, ignore_dirs=[MONGO_DIR_NAME])


def add_cache_with_redis() -> None:
    os.makedirs(WORKING_DIR, exist_ok=True)
    copy_files(REDIS_CACHE_TREE, WORKING_DIR)


if __name__ == "__main__":
    app()
