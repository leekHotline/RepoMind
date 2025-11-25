"""
演示如何使用MCP服务的客户端示例
"""

import asyncio
from fastmcp import FastMCP

async def demo_mcp_service():
    """演示MCP服务的实际使用"""

    # 创建客户端连接到我们的MCP服务
    async with FastMCP.client("http://localhost:8000") as client:

        print("=== MCP服务演示 ===\n")

        # 1. 使用搜索工具
        print("1. 使用搜索工具:")
        search_results = await client.call_tool("search_web", {"query": "weather forecast"})
        print(f"搜索结果: {search_results}\n")

        # 2. 使用时间工具
        print("2. 使用时间工具:")
        current_time = await client.call_tool("get_current_time", {"timezone": "Asia/Shanghai"})
        print(f"当前时间: {current_time}\n")

        # 3. 使用运费计算工具
        print("3. 使用运费计算工具:")
        shipping_cost = await client.call_tool("calculate_shipping_cost", {
            "weight": 2.5,
            "destination": "China",
            "express": True
        })
        print(f"运费计算: {shipping_cost}\n")

        # 4. 使用资源
        print("4. 使用天气资源:")
        weather_info = await client.get_resource("weather://beijing")
        print(f"天气信息: {weather_info}\n")

# 模拟AI模型调用MCP工具的场景
async def simulate_ai_model_using_tools():
    """模拟AI模型如何调用MCP工具"""

    print("=== AI模型使用MCP工具的场景模拟 ===\n")

    # 场景1: 用户询问天气和时间的组合查询
    print("场景1: 用户询问'现在北京的时间和天气如何？'")

    async with FastMCP.client("http://localhost:8000") as client:
        # AI模型会决定需要调用哪些工具
        time_result = await client.call_tool("get_current_time", {"timezone": "Asia/Shanghai"})
        weather_result = await client.get_resource("weather://beijing")

        print(f"AI调用工具结果:")
        print(f"- 时间: {time_result}")
        print(f"- 天气: {weather_result}")
        print(f"AI可以回答: 当前时间是{time_result}，北京的天气是{weather_result}\n")

    # 场景2: 用户需要计算国际运费
    print("场景2: 用户询问'从中国寄2公斤包裹到美国，加急需要多少钱？'")

    async with FastMCP.client("http://localhost:8000") as client:
        shipping_result = await client.call_tool("calculate_shipping_cost", {
            "weight": 2.0,
            "destination": "USA",
            "express": True
        })

        print(f"AI调用工具结果:")
        print(f"- 运费计算: {shipping_result}")
        print(f"AI可以回答: 从中国寄2公斤包裹到美国，加急运费为${shipping_result['total_cost']:.2f}，预计{shipping_result['estimated_days']}天到达\n")

if __name__ == "__main__":
    print("注意: 请先运行 MCP 服务 (python mcp/web_search.py)")
    print("然后取消注释下面的代码来运行演示")

    # 取消注释以下代码来运行演示
    # asyncio.run(demo_mcp_service())
    # asyncio.run(simulate_ai_model_using_tools())