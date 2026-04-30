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

if not source.exists() or not source.is_dir():
    print("Source folder does not exist or is not a directory")
    exit()

destination.mkdir(parents=True, exist_ok=True)

for path in source.rglob("*"):
    if path.is_file():
        folder_name = path.suffix[1:] if path.suffix else "no_extension"
        target_dir = destination / folder_name
        target_dir.mkdir(parents=True, exist_ok=True)

        shutil.copy2(path, target_dir / path.name)
        print(f"Copied: {path.name} -> {target_dir}")