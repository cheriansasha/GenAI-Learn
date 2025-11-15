"""News API module for fetching top article URLs."""

import requests
import json
from secrets import get_secret

def is_url_valid(url):
    """Check if URL is accessible."""
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except:
        return False

def get_top_articles():
    """Fetch top 5 US news article URLs from NewsAPI."""
    try:
        secret_data = json.loads(get_secret())
        api_key = secret_data.get("news_api_key")
    except:
        api_key = None
    
    if not api_key:
        return []
    
    url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=5&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["status"] == "ok":
            valid_urls = []
            for article in data["articles"]:
                if is_url_valid(article['url']):
                    valid_urls.append(article['url'])
            return valid_urls
        else:
            return []
    except Exception as e:
        return []