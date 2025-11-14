from news import get_top_articles
from chat_ai import ask_ai

def main():
    news_array = get_top_articles()
    
    for url in news_array:
        summary = ask_ai(url)
        print(f"Summary: {summary}\n")
        
if __name__ == "__main__":
   main()