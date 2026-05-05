import os
import shutil

BASE_PATH = "./output"   # local folder (safe for testing)


def create_folder(*paths):
    full_path = os.path.join(BASE_PATH, *paths)
    os.makedirs(full_path, exist_ok=True)
    return full_path


def move_file(src, dest_folder):
    file_name = os.path.basename(src)
    dest = os.path.join(dest_folder, file_name)

    if os.path.exists(dest):
        print("Duplicate skipped:", file_name)
        return

    shutil.move(src, dest)