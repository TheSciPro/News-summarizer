import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    raise ValueError("🚨 ERROR: API Key not found! Set NEWS_API_KEY in .env")


URL = "https://newsapi.org/v2/top-headlines"


queries = ["insurance", "finance", "economy", "business", "stocks"]


RAW_DATA_PATH = "data/raw"
os.makedirs(RAW_DATA_PATH, exist_ok=True)


def fetch_news():
    for query in queries:
        print(f"\n🔍 Searching for: {query}")

        params = {
            "q": query,
            "pageSize": 20, 
            "apiKey": API_KEY
        }

        response = requests.get(URL, params=params)

        if response.status_code == 200:
            data = response.json()

            if data["status"] == "ok" and data["totalResults"] > 0:
                file_path = os.path.join(RAW_DATA_PATH, "raw_headlines.json")
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(data["articles"], f, indent=4)
                
                print(f"✅ Saved {len(data['articles'])} articles to {file_path}")
                return  
            else:
                print(f"❌ No articles found for '{query}'. Trying next keyword...")
        else:
            print(f"❌ Error fetching news: {response.status_code}")
            print(response.json()) 
if __name__ == "__main__":
    fetch_news()
