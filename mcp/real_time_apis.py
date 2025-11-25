from fastmcp import FastMCP
import httpx
import json
from typing import Dict, List, Optional
from datetime import datetime

mcp = FastMCP("RealTimeAPIs")

@mcp.tool()
async def get_crypto_price(symbol: str = "BTC") -> Dict:
    """
    Get real-time cryptocurrency price from CoinGecko API.

    Args:
        symbol: Cryptocurrency symbol (e.g., BTC, ETH, ADA)

    Returns:
        Current price and market data
    """
    try:
        async with httpx.AsyncClient() as client:
            # Get coin ID from symbol
            response = await client.get("https://api.coingecko.com/api/v3/coins/list")
            coins = response.json()

            coin_id = None
            for coin in coins:
                if coin['symbol'].lower() == symbol.lower():
                    coin_id = coin['id']
                    break

            if not coin_id:
                return {"error": f"Cryptocurrency {symbol} not found"}

            # Get price data
            price_response = await client.get(
                f"https://api.coingecko.com/api/v3/coins/{coin_id}",
                params={"localization": "false", "tickers": "false", "market_data": "true"}
            )

            data = price_response.json()
            market_data = data.get('market_data', {})

            return {
                "symbol": symbol.upper(),
                "name": data.get('name', ''),
                "current_price": market_data.get('current_price', {}).get('usd', 0),
                "price_change_24h": market_data.get('price_change_24h', 0),
                "price_change_percentage_24h": market_data.get('price_change_percentage_24h', 0),
                "market_cap": market_data.get('market_cap', {}).get('usd', 0),
                "last_updated": market_data.get('last_updated', '')
            }
    except Exception as e:
        return {"error": f"Failed to fetch crypto price: {str(e)}"}

@mcp.tool()
async def get_news_headlines(category: str = "general", country: str = "us") -> List[Dict]:
    """
    Get latest news headlines from NewsAPI.

    Args:
        category: News category (general, business, technology, etc.)
        country: Country code for news (us, gb, cn, etc.)

    Returns:
        List of news articles
    """
    try:
        # Note: You'll need to get a free API key from https://newsapi.org
        api_key = "YOUR_NEWS_API_KEY_HERE"  # Replace with your actual API key

        if api_key == "YOUR_NEWS_API_KEY_HERE":
            # Return mock data for demonstration
            return [
                {
                    "title": "Latest Technology Breakthrough",
                    "description": "Scientists announce major AI breakthrough",
                    "url": "https://example.com/news/1",
                    "publishedAt": datetime.now().isoformat(),
                    "source": "Example News"
                },
                {
                    "title": "Global Markets Update",
                    "description": "Stock markets show mixed performance",
                    "url": "https://example.com/news/2",
                    "publishedAt": datetime.now().isoformat(),
                    "source": "Financial Times"
                }
            ]

        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://newsapi.org/v2/top-headlines",
                params={
                    "country": country,
                    "category": category,
                    "apiKey": api_key
                }
            )

            data = response.json()
            articles = data.get('articles', [])

            return [
                {
                    "title": article.get('title', ''),
                    "description": article.get('description', ''),
                    "url": article.get('url', ''),
                    "publishedAt": article.get('publishedAt', ''),
                    "source": article.get('source', {}).get('name', '')
                }
                for article in articles[:5]  # Return top 5 articles
            ]
    except Exception as e:
        return [{"error": f"Failed to fetch news: {str(e)}"}]

@mcp.tool()
async def get_weather_by_city(city: str, country_code: str = "") -> Dict:
    """
    Get current weather for a city using OpenWeatherMap API.

    Args:
        city: City name
        country_code: Optional country code (e.g., 'us', 'cn')

    Returns:
        Current weather information
    """
    try:
        # Note: You'll need to get a free API key from https://openweathermap.org
        api_key = "YOUR_OPENWEATHER_API_KEY_HERE"  # Replace with your actual API key

        if api_key == "YOUR_OPENWEATHER_API_KEY_HERE":
            # Return mock data for demonstration
            return {
                "city": city,
                "temperature": 22.5,
                "description": "clear sky",
                "humidity": 65,
                "wind_speed": 3.2,
                "pressure": 1013,
                "country": country_code or "Unknown"
            }

        location = f"{city},{country_code}" if country_code else city

        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={
                    "q": location,
                    "appid": api_key,
                    "units": "metric"
                }
            )

            data = response.json()

            return {
                "city": data.get('name', ''),
                "temperature": data['main']['temp'],
                "description": data['weather'][0]['description'],
                "humidity": data['main']['humidity'],
                "wind_speed": data['wind']['speed'],
                "pressure": data['main']['pressure'],
                "country": data.get('sys', {}).get('country', '')
            }
    except Exception as e:
        return {"error": f"Failed to fetch weather: {str(e)}"}

@mcp.tool()
async def get_stock_price(symbol: str) -> Dict:
    """
    Get real-time stock price using Alpha Vantage API.

    Args:
        symbol: Stock symbol (e.g., AAPL, GOOGL, TSLA)

    Returns:
        Current stock price and market data
    """
    try:
        # Note: You'll need to get a free API key from https://www.alphavantage.co
        api_key = "YOUR_ALPHA_VANTAGE_API_KEY_HERE"  # Replace with your actual API key

        if api_key == "YOUR_ALPHA_VANTAGE_API_KEY_HERE":
            # Return mock data for demonstration
            mock_prices = {
                "AAPL": 175.25,
                "GOOGL": 142.80,
                "TSLA": 245.15,
                "MSFT": 330.45
            }

            price = mock_prices.get(symbol.upper(), 100.0)
            return {
                "symbol": symbol.upper(),
                "price": price,
                "change": price * 0.01,  # Mock 1% change
                "change_percent": 1.0,
                "volume": 1000000,
                "last_updated": datetime.now().isoformat()
            }

        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://www.alphavantage.co/query",
                params={
                    "function": "GLOBAL_QUOTE",
                    "symbol": symbol,
                    "apikey": api_key
                }
            )

            data = response.json()
            quote = data.get('Global Quote', {})

            return {
                "symbol": symbol.upper(),
                "price": float(quote.get('05. price', 0)),
                "change": float(quote.get('09. change', 0)),
                "change_percent": float(quote.get('10. change percent', '0%').replace('%', '')),
                "volume": int(quote.get('06. volume', 0)),
                "last_updated": quote.get('07. latest trading day', '')
            }
    except Exception as e:
        return {"error": f"Failed to fetch stock price: {str(e)}"}

@mcp.tool()
async def search_github_repos(query: str, language: str = "") -> List[Dict]:
    """
    Search GitHub repositories using GitHub API.

    Args:
        query: Search query
        language: Programming language filter

    Returns:
        List of GitHub repositories
    """
    try:
        search_params = {"q": query}
        if language:
            search_params["q"] += f" language:{language}"

        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.github.com/search/repositories",
                params=search_params
            )

            data = response.json()
            repos = data.get('items', [])

            return [
                {
                    "name": repo.get('name', ''),
                    "full_name": repo.get('full_name', ''),
                    "description": repo.get('description', ''),
                    "url": repo.get('html_url', ''),
                    "stars": repo.get('stargazers_count', 0),
                    "forks": repo.get('forks_count', 0),
                    "language": repo.get('language', ''),
                    "updated_at": repo.get('updated_at', '')
                }
                for repo in repos[:5]  # Return top 5 results
            ]
    except Exception as e:
        return [{"error": f"Failed to search GitHub: {str(e)}"}]

if __name__ == "__main__":
    mcp.run()