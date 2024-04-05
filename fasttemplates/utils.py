import os
import shutil
import tempfile
import stat

from fasttemplates.constants import WORKING_DIR, SETTINGS_DIR


def copy_files(src_dir, dst_dir, ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = []

    for item in os.listdir(src_dir):
        if item in ignore_dirs:
            continue

        src_item = os.path.join(src_dir, item)
        dst_item = os.path.join(dst_dir, item)

        if os.path.isdir(src_item):
            os.makedirs(dst_item, exist_ok=True)
            copy_files(src_item, dst_item, ignore_dirs)
        else:
            shutil.copy2(src_item, dst_item)


def cout_settings_properties() -> int:
    settings_path = os.path.join(WORKING_DIR, "app\\settings.py")
    with open(settings_path, "r") as f:
        lines = f.readlines()

    return (
        len(
            [
                line
                for line in lines
                if line.strip() and not line.strip().startswith("#")
            ]
        )
        + 1
    )


def add_property_to_settings(_K: str, _T: type, _V: str) -> None:
    settings_path = os.path.join(WORKING_DIR, SETTINGS_DIR)
    with open(settings_path, "r") as f:
        lines = f.readlines()

    NUMBER_OF_PROPERTIES = cout_settings_properties()
    lines.insert(NUMBER_OF_PROPERTIES, f"    {_K}: {_T.__name__} = {_V}\n")

    with open(settings_path, "w") as f:
        f.writelines(lines)


def add_mongo_uri_to_settings():
    add_property_to_settings("MONGO_URI", str, "'mongodb://localhost:27017'")


def add_redis_uri_to_settings():
    add_property_to_settings("REDIS_URI", str, "'redis://localhost:6379/0'")


def on_rm_error(func, path, exc_info) -> None:
    "Error handler for `shutil.rmtree`"
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def clone_and_copy(repo_url: str) -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.system(f"git clone {repo_url} {tmpdirname}")
        shutil.rmtree(os.path.join(tmpdirname, ".git"), onerror=on_rm_error)
        copy_files(tmpdirname, WORKING_DIR)
