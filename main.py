# import argparse
# import asyncio
# import logging
# import shutil
# from pathlib import Path

# parser = argparse.ArgumentParser(description="Sort files by extension")
# parser.add_argument('source', help='Path to source folder')
# parser.add_argument('destination', help='Path to destination folder')
# args = parser.parse_args()


# source = Path(args.source)
# destination = Path(args.destination )

# for path in source.iterdir():
#     if path.is_file():
#         folder_name = path.suffix[1:] if path.suffix else "no_extension"
#         target_dir = destination / folder_name

#         target_dir.mkdir(exist_ok=True)
#         shutil.copy(path, target_dir / path.name)
#         print(target_dir.name)

import argparse
import shutil
from pathlib import Path


parser = argparse.ArgumentParser(description="Sort files by extension")
parser.add_argument("source", help="Path to source folder")
parser.add_argument("destination", help="Path to destination folder")
args = parser.parse_args()

source = Path(args.source)
destination = Path(args.destination)


# def read_folder(source):
#     if not source.exists() or not source.is_dir():
#         print("Source folder does not exist or is not a directory")
#         exit()

#     result = []  # список

#     for path in source.rglob("*"):
#         if path.is_file():
#             folder_name = path.suffix[1:] if path.suffix else "no_extension"
#             result.append(folder_name)  

#     return result

def read_folder(source):
    if not source.exists() or not source.is_dir():
        print("Source folder does not exist or is not a directory")
        exit()

    result = []

    for path in source.rglob("*"):
        if path.is_file():
            folder_name = path.suffix[1:] if path.suffix else "no_extension"
            result.append((path, folder_name))  # 🔥 кортеж

    return result

# def create_folder(destination, result):
#     created_dirs = []
#     for folder_name in result:
#         target_dir = destination / folder_name
#         target_dir.mkdir(parents=True, exist_ok=True)
#         created_dirs.append(target_dir)
#     return created_dirs

def create_folder(destination, result):
    created_dirs = {}

    for _, folder_name in result:
        target_dir = destination / folder_name
        target_dir.mkdir(parents=True, exist_ok=True)
        created_dirs[folder_name] = target_dir

    return created_dirs

# def copy_file(target_dir, path):
#     shutil.copy2(path, target_dir / path.name)
#     print(f"Copied: {path.name} -> {target_dir}")

# def copy_file(files, folders):
#     for path, folder_name in files:
#         target_dir = folders[folder_name]
#         shutil.copy2(path, target_dir / path.name)
#         print(f"Copied: {path.name} -> {target_dir}")


# if __name__ == "__main__":
#     folder_names = read_folder(source)
#     create_folder(destination, folder_names)
#     # copy_file(source_folder, destination)   

if __name__ == "__main__":
    files = read_folder(source)
    folders = create_folder(destination, files)
    # copy_file(files, folders)