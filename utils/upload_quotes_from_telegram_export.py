import json
import requests

# Path to the JSON file
quotes_file = 'quotes.json'

# URL of the FastAPI application endpoint
api_url = 'http://192.168.0.200:8000/quotes/'

# Function to load quotes from the JSON file
def load_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        messages = data.get("messages", [])
        quotes = []
        for msg in messages:
            if msg["type"] == "message" and "text_entities" in msg:
                quote = ''.join(entity["text"] if isinstance(entity, dict) else entity for entity in msg["text_entities"])
                quotes.append(quote)
    return quotes

# Function to upload a single quote to the FastAPI application
def upload_quote(quote_text):
    response = requests.post(api_url, json={"text": quote_text})
    if response.status_code == 200:
        print(f'Successfully uploaded quote: {quote_text}')
    else:
        print(f'Failed to upload quote: {quote_text}. Status code: {response.status_code}')

# Main function to load quotes and upload them
def main():
    quotes = load_quotes(quotes_file)
    for quote in quotes:
        upload_quote(quote)

if __name__ == '__main__':
    main()

