import os
import shutil

from fastapitemplatewizard.constants import WORKING_DIR


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


def add_mongo_uri_to_settings():
    # Add MONGO_URI to Settings class
    settings_path = os.path.join(WORKING_DIR, "app\\settings.py")
    with open(settings_path, "r") as f:
        lines = f.readlines()

    # Find the line with the class definition
    class_def_index = next(i for i, line in enumerate(
        lines) if 'class Settings(BaseSettings):' in line)

    # Insert the new line after the class definition
    lines.insert(class_def_index + 3, '    MONGO_URI:  str = None\n')

    # Write the modified lines back to the file
    with open(settings_path, "w") as f:
        f.writelines(lines)
