import os
import requests
import json
import time
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")


NEWS_API_URL = "https://newsapi.org/v2/top-headlines"


QUERIES = ["insurance", "climate policy", "finance trends"]
CATEGORY = "business"
COUNTRY = "us"
PAGE_SIZE = 20  
MAX_RETRIES = 3  

def fetch_headlines(query, category=CATEGORY, country=COUNTRY, page_size=PAGE_SIZE, page=1):
    """Fetch top news headlines for a given query and save them."""
    params = {
        "apiKey": API_KEY,
        "category": category,
        "country": country,
        "q": query,
        "pageSize": page_size,
        "page": page
    }

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(NEWS_API_URL, params=params)
            response.raise_for_status()  # Handle HTTP errors
            
            data = response.json()
            articles = data.get("articles", [])

            # Save data to JSON file
            raw_data_path = f"data/raw/raw_headlines_{query.replace(' ', '_')}.json"
            os.makedirs(os.path.dirname(raw_data_path), exist_ok=True)

            with open(raw_data_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            print(f"✅ {len(articles)} articles saved for query: {query}")
            return data

        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching news for '{query}' (Attempt {attempt+1}/{MAX_RETRIES}): {e}")
            time.sleep(2 ** attempt)  # Exponential backoff
    
    print(f"⚠️ Failed to fetch news for '{query}' after {MAX_RETRIES} retries.")
    return None

if __name__ == "__main__":
    for query in QUERIES:
        fetch_headlines(query)
