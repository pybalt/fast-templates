import os
import shutil


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
