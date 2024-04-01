import os

import typer
import questionary

from constants import *
from utils import *

app = typer.Typer()


@app.command()
def main():
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


def add_base_layout():
    os.makedirs(WORKING_DIR, exist_ok=True)
    copy_files(BASE_LAYOUT, WORKING_DIR)


def add_mongo():
    MONGO_DIR = os.path.join(WORKING_DIR, DB_DIR)
    os.makedirs(MONGO_DIR, exist_ok=True)
    copy_files(DB_TREE, MONGO_DIR, ignore_dirs=[REDIS_DIR_NAME])


def add_redis():
    REDIS_DIR = os.path.join(WORKING_DIR, DB_DIR)
    os.makedirs(REDIS_DIR, exist_ok=True)
    copy_files(DB_TREE, REDIS_DIR, ignore_dirs=[MONGO_DIR_NAME])


def add_cache_with_redis():
    os.makedirs(WORKING_DIR, exist_ok=True)
    copy_files(REDIS_CACHE_TREE, WORKING_DIR)


if __name__ == "__main__":
    app()
