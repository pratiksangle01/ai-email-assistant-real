import requests
import os

# IMPORTANT: Store your API key as environment variable
API_KEY = os.getenv("OPENAI_API_KEY")

def generate_reply(email):
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a professional email assistant."},
            {"role": "user", "content": email}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"

def main():
    print("=== AI Email Assistant (Real API) ===\n")
    
    email = input("Enter client email:\n")
    
    reply = generate_reply(email)
    
    print("\n--- AI Generated Reply ---\n")
    print(reply)

if __name__ == "__main__":
    main()
