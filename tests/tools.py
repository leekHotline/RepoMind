import os
from loguru import logger
from pathlib import Path


def read_file( name : str) -> str:
    "read and save the text from file"
    try:
        with open(name, 'rb') as f:
            content = f.read()
        return content
    except Exception as e:
        logger.error(f"Error Memssages:{str(e)}")


def list_files() -> list[str] :
    "list all the name of file"
    dir_name = os.listdir('.')
    return dir_name


def rename_file(name: str):
    "rename the name of file, bullshit comment"
    filename = name + '1'
    os.rename(name, filename)


if __name__ == "__main__" :
    # logger.info(rename_file('a'))
    logger.info(list_files())