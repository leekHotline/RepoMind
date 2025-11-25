from fastmcp import FastMCP
import httpx
from typing import List, Dict
import json

mcp = FastMCP("WebSearch")


@mcp.tool()
def search_web(query: str, max_results: int = 5) -> List[Dict]:
    """
    Search the web for information using a search engine.

    Args:
        query: The search query
        max_results: Maximum number of results to return

    Returns:
        List of search results with title, url, and snippet
    """
    # 在实际应用中，这里会调用真实的搜索引擎API
    # 这里使用模拟数据来演示

    # 模拟搜索逻辑
    if "weather" in query.lower():
        return [
            {
                "title": "Weather Forecast",
                "url": "https://weather.com/forecast",
                "snippet": "Current weather conditions and 7-day forecast"
            }
        ]
    elif "news" in query.lower():
        return [
            {
                "title": "Latest News Headlines",
                "url": "https://news.example.com",
                "snippet": "Breaking news and current events"
            }
        ]
    else:
        return [
            {
                "title": f"Search Results for: {query}",
                "url": f"https://search.example.com?q={query}",
                "snippet": f"Information about {query}"
            }
        ]


@mcp.tool()
def get_current_time(timezone: str = "UTC") -> str:
    """
    Get the current time in the specified timezone.

    Args:
        timezone: Timezone identifier (e.g., 'Asia/Shanghai', 'UTC', 'America/New_York')

    Returns:
        Current time string
    """
    from datetime import datetime
    import pytz

    try:
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz)
        return current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def calculate_shipping_cost(weight: float, destination: str, express: bool = False) -> Dict:
    """
    Calculate shipping cost based on weight and destination.

    Args:
        weight: Package weight in kilograms
        destination: Destination country/region
        express: Whether to use express shipping

    Returns:
        Shipping cost details
    """
    base_rate = 10.0  # Base shipping cost
    weight_rate = 5.0  # Cost per kg

    if express:
        base_rate *= 2
        weight_rate *= 1.5

    total_cost = base_rate + (weight * weight_rate)

    return {
        "weight_kg": weight,
        "destination": destination,
        "express": express,
        "base_cost": base_rate,
        "weight_cost": weight * weight_rate,
        "total_cost": total_cost,
        "estimated_days": 3 if express else 7
    }


@mcp.resource("weather://{city}")
def get_weather(city: str) -> str:
    """
    Get current weather information for a city.

    Args:
        city: City name

    Returns:
        Weather information
    """
    # 模拟天气数据
    weather_data = {
        "beijing": "Sunny, 25°C",
        "shanghai": "Cloudy, 22°C",
        "new york": "Rainy, 18°C",
        "london": "Foggy, 15°C"
    }

    city_key = city.lower()
    if city_key in weather_data:
        return f"Weather in {city}: {weather_data[city_key]}"
    else:
        return f"Weather data not available for {city}"


if __name__ == "__main__":
    mcp.run()
