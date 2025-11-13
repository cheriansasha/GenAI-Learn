# To run this script:
# 1. pip install -r requirements.txt
# 2. set GROQ_API_KEY=your_actual_groq_api_key_here
# 3. python chat_ai.py

from groq import Groq
import os

# Initialize Groq client with API key from environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": question}],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        question = input("Ask me anything (or 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        answer = ask_ai(question)
        print(f"AI: {answer}\n")