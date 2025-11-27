import os
from loguru import logger
from pathlib import Path


def read_file(name: str) -> str:
    "read and save the text from file"
    # 1. 检查是否存在
    if not os.path.exists(name):
        return f"Error: File '{name}' not found."
    
    # 2. 检查是不是目录（关键！）
    if os.path.isdir(name):
        return f"Skip: '{name}' is a directory, cannot read context."
        
    try:
        with open(name, 'rb') as f:
            content = f.read()
        # 尝试解码，方便 Agent 理解
        try:
            return content.decode('utf-8')
        except UnicodeDecodeError:
            return f"Binary file content (size: {len(content)} bytes)"
    except Exception as e:
        # 捕获所有其他异常，别让程序崩
        logger.error(f"Error reading {name}: {str(e)}")
        return f"System Error: {str(e)}"
    
    
def list_files(directory: str = '.') -> list[str]:
    """
    list files in the specific directory. 
    Args:
        directory: The path to list. defaults to current working directory.
    """
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except Exception as e:
        return [f"Error: {str(e)}"]

def rename_file(name: str):
    "rename the name of file, bullshit comment"
    filename = name + '1'
    os.rename(name, filename)


if __name__ == "__main__" :
    # logger.info(rename_file('a'))
    logger.info(list_files())