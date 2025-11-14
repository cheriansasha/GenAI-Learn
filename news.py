# To run this script:
# 1. pip install -r requirements.txt
# 2. set NEWS_API_KEY=your_news_api_key_here
# 3. python news.py

import requests
import os

def is_url_valid(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except:
        return False

def get_top_articles():
    api_key = os.getenv("NEWS_API_KEY")
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

# if __name__ == "__main__":
#     print("Top 5 Article URLs Today:")
#     print("=" * 40)
#     print(get_top_headlines())