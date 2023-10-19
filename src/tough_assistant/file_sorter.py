import os
import shutil
import unicodedata
import re

def normalize(name):
    # Normalize folder names to a compatible form
    sanitized_name = unicodedata.normalize('NFKD', name)
    sanitized_name = re.sub(r'[\/:*?"<>|]', '_', sanitized_name)  # Remove illegal characters
    sanitized_name = sanitized_name.lower()
    sanitized_name = re.sub(r'[^a-z0-9._ ]', '', sanitized_name)  # Remove unsupported characters
    return sanitized_name

def move_file(source_file, destination_folder):
    name, ext = os.path.splitext(source_file)
    ext_folder = os.path.join(destination_folder, ext[1:])  # Remove the dot from the extension
    os.makedirs(ext_folder, exist_ok=True)
    dest_file = os.path.join(ext_folder, normalize(os.path.basename(source_file)))
    shutil.move(source_file, dest_file)

def sort_and_rename_files(folder_path):
    destination_folder = os.path.join(folder_path, "sorted_and_renamed_files")
    os.makedirs(destination_folder, exist_ok=True)

    for root, dirs, files in os.walk(folder_path, topdown=True):
        for file in files:
            source_file = os.path.join(root, file)
            move_file(source_file, destination_folder)
            print(f"Moved file: {source_file} -> {destination_folder}")

        for dir in dirs:
            source_dir = os.path.join(root, dir)
            dest_dir = os.path.join(destination_folder, normalize(dir))

            if not os.listdir(source_dir):
                os.rmdir(source_dir)  # Delete empty directory
                print(f"Deleted empty folder: {source_dir}")

    print("Files sorted, renamed, and empty folders removed.")

if __name__ == "__main":
    folder_path = input("Enter the folder path: ")
    sort_and_rename_files(folder_path)
