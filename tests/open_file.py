from loguru import logger
# pythonic passionic
# 劲 力 激励 

# 基础控制流
str = "apple_pen"
result = 100 if str == "apple" else 0
logger.info(result)

# 列表推导式
nums = [1,2,3,4,5,6]
list = [i**2 for i in nums if i%2 == 0]
logger.info(list)

# with自动管理资源
with open("file.txt", 'w') as f:
    f.write("hello world")


# 类与对象 面向对象
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        return f"Hello:{self.name}"
    
user = User()
