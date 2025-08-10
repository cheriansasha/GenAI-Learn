import openai

# Set your OpenAI API key (get free credits at openai.com)
openai.api_key = "your_openai_api_key_here"

def ask_ai(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Cheapest model
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
