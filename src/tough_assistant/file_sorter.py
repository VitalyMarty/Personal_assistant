import os
import shutil
import zipfile
import re
import string


def normalize(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9.]', '_', name)
    return name

def process_archive(source_path, destination_path):
    with zipfile.ZipFile(source_path, 'r') as archive:
        archive.extractall(destination_path)


def sort_and_rename_files(folder_path):
    ignored_folders = {'archives', 'video', 'audio', 'documents', 'images'}

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    dirs = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]

    destination_folder = os.path.join(folder_path, "sorted_and_renamed_files")
    os.makedirs(destination_folder, exist_ok=True)

    for dir in dirs:
        if dir not in ignored_folders:
            source_dir = os.path.join(folder_path, dir)
            dest_dir = os.path.join(destination_folder, normalize(dir))
            shutil.move(source_dir, dest_dir)

    for file in files:
        name, ext = os.path.splitext(file)
        source_file = os.path.join(folder_path, file)

        if ext == '.zip':
            dest_folder = os.path.join(destination_folder, 'archives', normalize(name))
            os.makedirs(dest_folder, exist_ok=True)
            process_archive(source_file, dest_folder)
        else:
            latin_name = normalize(name)
            dest_file = os.path.join(destination_folder, latin_name + ext)
            shutil.move(source_file, dest_file)

    # Remove empty directories
    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
        for dirname in dirnames:
            dir_to_check = os.path.join(dirpath, dirname)
            if not os.listdir(dir_to_check) and dirname != 'sorted_and_renamed_files':
                os.rmdir(dir_to_check)

    print("Files sorted, renamed, and normalized successfully!")



