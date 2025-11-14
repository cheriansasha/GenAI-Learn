# To run this script:
# 1. pip install -r requirements.txt
# 2. set GROQ_API_KEY=your_actual_groq_api_key_here
# 3. python chat_ai.py

from groq import Groq
from news import get_top_articles
import os
import requests
from bs4 import BeautifulSoup

# Initialize Groq client with API key from environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(news_url):
    try:
        response = requests.get(news_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text() for p in paragraphs])
        
        prompt = f"Summarize this news article in exactly 100 words: {article_text}"
        
        ai_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return ai_response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
    
# if __name__ == "__main__":
#     while True:
#         question = input("Ask me anything (or 'quit' to exit): ")
#         if question.lower() == 'quit':
#             break
#         answer = ask_ai(question)
#         print(f"AI: {answer}\n")