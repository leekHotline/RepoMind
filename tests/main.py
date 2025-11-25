import os
from pydantic_ai.models.google import GoogleModel
from pydantic_ai import Agent
from . import tools
# 导入当前目录 这样可以导入当前目录其它文件的函数
from dotenv import load_dotenv
from loguru import logger

load_dotenv()# 默认就导入密钥了 无需手动传递
api_key = os.getenv('GEMINI_API_KEY') 

model = GoogleModel("gemini-2.5-pro")
# gemini-2.5-falsh-preview-04-07
agent = Agent(model
              , system_prompt = 'you are an experienced programer'
              , tools = [tools.read_file, tools.list_files, tools.rename_file])



def main(): 
    logger.info(api_key)
    user_prompt = input("pleas input your prompt:")
    response = agent.run_sync(user_prompt)
    logger.info(response)

if __name__ == "__main__":
    main()