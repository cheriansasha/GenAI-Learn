"""Main application for fetching news and generating AI summaries."""

from news import get_top_articles
from chat_ai import ask_ai

def main():
    """Fetch top news articles and generate AI summaries for each."""
    news_array = get_top_articles()
    
    for url in news_array:
        summary = ask_ai(url)
        print(f"Summary: {summary}\n")
        
if __name__ == "__main__":
   main()