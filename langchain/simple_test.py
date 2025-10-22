import os
from loguru import logger
from dotenv import load_dotenv


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 自动加载env环境文件
load_dotenv()

# 从环境变量中获取刚刚设置好的apikey
api_key = os.getenv("DEEPSEEK_API_KEY")

# 初始化大模型
llm = ChatOpenAI(
    model = "deepseek-chat",
    api_key= api_key,
    base_url="https://api.deepseek.com"
)

# 创建一个提示模板
prompt = ChatPromptTemplate.from_template(
 "我想开一家以{themes}为主题的餐馆,帮我想3个有创造力的名字"
)

# 创建一个简单的输出解析器，它会把模型的输出直接变成一个字符串
output_parser = StrOutputParser()

# 创建一个链 用lcel管道符来创建链 意思是提示词到模型到解析器
chain  = prompt | llm | output_parser

# 运行链并获得结果
my_themes = "cyberpunk"

print(f"正在为“{my_themes}”主题的店请求创意名字...")

response = chain.invoke({"themes":  my_themes})

#打印响应结果
print("\nDeepSeek 模型给出的建议是：")
logger.info(response)