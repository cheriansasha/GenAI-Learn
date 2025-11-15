"""AI chat module for generating news article summaries."""

from groq import Groq  # AI/LLM client for generating text completions
import requests  # HTTP library for making web requests
from bs4 import BeautifulSoup  # HTML parser for extracting text from web pages
from secrets import get_secret  # Custom module to retrieve API keys from AWS Secrets Manager
import json  # Built-in library for parsing JSON data

try:
    secret_data = json.loads(get_secret())
    groq_api_key = secret_data.get("groq_api_key")
except:
    groq_api_key = None

if not groq_api_key:
    raise SystemExit("Error: GROQ API key not found in secrets manager")

client = Groq(api_key=groq_api_key)

def extract_article_text(soup):
    """Extract article text from HTML, trying multiple selectors."""
    selectors = ['p', 'div.article-content', 'div.story-body', 'article', 'div.content', 'div.post-content']
    
    for selector in selectors:
        elements = soup.select(selector)
        if elements:
            text = ' '.join([el.get_text().strip() for el in elements])
            if len(text) > 100:  # Only return if substantial content found
                return text
    
    # Fallback to all text if no specific selectors work
    return soup.get_text()

def ask_ai(news_url):
    """Generate 100-word summary of news article from URL."""
    try:
        # fetch the HTML content from the provided news URL using requests.get()
        response = requests.get(news_url)
        # create a BeautifulSoup object to parse the HTML content for easier extraction
        soup = BeautifulSoup(response.content, 'html.parser')
        
        article_text = extract_article_text(soup)        
        
        prompt = f"Summarize this news article in exactly 100 words: {article_text}"
        
        # make an API call to the Groq LLM service to generate a text completion
        ai_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.3,  # Lower = more focused, Higher = more creative (0.0-2.0)
            top_p=0.9        # Nucleus sampling - considers top 90% probability mass (0.0-1.0)
        )
        
        # returns the AI-generated completion response
        return ai_response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error: {e}"