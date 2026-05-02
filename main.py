import argparse
import asyncio
import logging
import shutil
from pathlib import Path


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d %(module)5s:%(lineno)-3d %(levelname)-7s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def parse_args():
    parser = argparse.ArgumentParser(description="Sort files by extension")
    parser.add_argument("source", help="Path to source folder")
    parser.add_argument("destination", help="Path to destination folder")
    return parser.parse_args()


async def read_folder(source: Path):
    if not source.exists() or not source.is_dir():
        raise ValueError("Source folder does not exist or is not a directory")

    return await asyncio.to_thread(
        lambda: [path for path in source.rglob("*") if path.is_file()]
    )


async def create_folder(destination: Path, file_path: Path):
    folder_name = file_path.suffix[1:] if file_path.suffix else "no_extension"
    target_dir = destination / folder_name

    await asyncio.to_thread(target_dir.mkdir, parents=True, exist_ok=True)

    return target_dir


async def copy_file(file_path: Path, target_dir: Path):
    await asyncio.to_thread(shutil.copy2, file_path, target_dir / file_path.name)
    logging.info(f"Copied: {file_path.name} -> {target_dir}")


async def process_file(file_path: Path, destination: Path):
    try:
        target_dir = await create_folder(destination, file_path)
        await copy_file(file_path, target_dir)
    except Exception as error:
        logging.error(f"Error processing {file_path}: {error}")


async def main():
    args = parse_args()

    source = Path(args.source)
    destination = Path(args.destination)

    logging.info(f"Start processing: {source} -> {destination}")

    try:
        files = await read_folder(source)
        logging.info(f"Found {len(files)} files")

        tasks = [process_file(file_path, destination) for file_path in files]
        await asyncio.gather(*tasks)

        logging.info("Processing finished")

    except Exception as error:
        logging.error(error)


if __name__ == "__main__":
    configure_logging()
    asyncio.run(main())
