"""
演示真实API调用的MCP服务使用示例
"""

import asyncio
from fastmcp import FastMCP

async def demo_real_time_apis():
    """演示真实API调用的MCP服务"""

    print("=== 真实API调用MCP服务演示 ===\n")

    async with FastMCP.client("http://localhost:8000") as client:

        # 1. 获取加密货币价格
        print("1. 获取加密货币价格:")
        btc_price = await client.call_tool("get_crypto_price", {"symbol": "BTC"})
        print(f"比特币价格: ${btc_price.get('current_price', 'N/A')}")
        print(f"24小时变化: {btc_price.get('price_change_percentage_24h', 'N/A')}%\n")

        # 2. 获取新闻头条
        print("2. 获取最新新闻:")
        news = await client.call_tool("get_news_headlines", {"category": "technology"})
        for article in news[:2]:  # 显示前2条新闻
            print(f"- {article.get('title', 'N/A')}")
        print()

        # 3. 获取天气信息
        print("3. 获取天气信息:")
        weather = await client.call_tool("get_weather_by_city", {"city": "Beijing"})
        print(f"北京天气: {weather.get('temperature', 'N/A')}°C, {weather.get('description', 'N/A')}")
        print()

        # 4. 获取股票价格
        print("4. 获取股票价格:")
        stock = await client.call_tool("get_stock_price", {"symbol": "AAPL"})
        print(f"苹果股票: ${stock.get('price', 'N/A')} (变化: {stock.get('change_percent', 'N/A')}%)")
        print()

        # 5. 搜索GitHub仓库
        print("5. 搜索GitHub仓库:")
        repos = await client.call_tool("search_github_repos", {"query": "machine learning", "language": "python"})
        for repo in repos[:2]:
            print(f"- {repo.get('name', 'N/A')}: {repo.get('description', 'N/A')}")

async def simulate_ai_with_real_time_data():
    """模拟AI使用实时数据回答复杂问题"""

    print("\n=== AI使用实时数据回答复杂问题 ===\n")

    async with FastMCP.client("http://localhost:8000") as client:

        # 场景1: 投资建议
        print("场景1: 用户询问'今天适合投资加密货币吗？'")

        # AI会调用多个工具来收集信息
        btc_data = await client.call_tool("get_crypto_price", {"symbol": "BTC"})
        eth_data = await client.call_tool("get_crypto_price", {"symbol": "ETH"})
        news_data = await client.call_tool("get_news_headlines", {"category": "business"})

        print(f"AI收集的数据:")
        print(f"- 比特币: ${btc_data.get('current_price', 'N/A')} ({btc_data.get('price_change_percentage_24h', 'N/A')}%)")
        print(f"- 以太坊: ${eth_data.get('current_price', 'N/A')} ({eth_data.get('price_change_percentage_24h', 'N/A')}%)")
        print(f"- 相关新闻: {len(news_data)} 条")
        print("AI可以基于这些实时数据提供投资建议\n")

        # 场景2: 旅行规划
        print("场景2: 用户询问'下周去北京旅游，天气怎么样？有什么技术新闻？'")

        weather_data = await client.call_tool("get_weather_by_city", {"city": "Beijing"})
        tech_news = await client.call_tool("get_news_headlines", {"category": "technology"})

        print(f"AI收集的数据:")
        print(f"- 北京天气: {weather_data.get('temperature', 'N/A')}°C, {weather_data.get('description', 'N/A')}")
        print(f"- 最新技术新闻: {len(tech_news)} 条")
        for news in tech_news[:1]:
            print(f"  * {news.get('title', 'N/A')}")
        print("AI可以结合天气和新闻提供旅行建议\n")

        # 场景3: 开发者查询
        print("场景3: 开发者询问'有哪些热门的Python机器学习项目？'")

        github_repos = await client.call_tool("search_github_repos", {
            "query": "machine learning",
            "language": "python"
        })

        print(f"AI收集的数据:")
        for repo in github_repos[:3]:
            print(f"- {repo.get('name', 'N/A')} (⭐ {repo.get('stars', 0)})")
            print(f"  {repo.get('description', 'N/A')}")
        print("AI可以推荐最热门的机器学习项目")

if __name__ == "__main__":
    print("启动真实API MCP服务:")
    print("python mcp/real_time_apis.py")
    print("\n然后取消注释下面的代码来运行演示:")

    # 取消注释以下代码来运行演示
    # asyncio.run(demo_real_time_apis())
    # asyncio.run(simulate_ai_with_real_time_data())