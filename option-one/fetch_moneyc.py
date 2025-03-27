import os
import json
import requests
from bs4 import BeautifulSoup


with open("insurance_articles.json", "r", encoding="utf-8") as file:
    articles = json.load(file)

scraped_articles = []
headers = {"User-Agent": "Mozilla/5.0"}


for article in articles:
    link = article.get("link")
    
    if not link:
        print(f"⚠️ Skipping '{article['headline']}' - No link found.")
        continue  

    print(f"🔄 Fetching: {link}")

    try:
        response = requests.get(link, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"❌ Failed to fetch {link} - Status Code: {response.status_code}")
            continue  

        soup = BeautifulSoup(response.text, "html.parser")

       
        title_tag = soup.find("h1", class_="article_title")
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

        
        desc_tag = soup.find("h2", class_="article_desc")
        desc = desc_tag.get_text(strip=True) if desc_tag else "N/A"

        
        paragraphs = []
        for p in soup.find_all("p"):
            if not p.attrs:  
                text = p.get_text(strip=True)
                if text:
                    paragraphs.append(text)

        print(f"✅ Successfully scraped '{title}' ({len(paragraphs)} paragraphs)")

        scraped_articles.append({
            "headline": title,
            "description": desc,
            "link": link,
            "content": paragraphs
        })

    except Exception as e:
        print(f"⚠️ Error processing {link}: {str(e)}")


with open("monecsites.json", "w", encoding="utf-8") as file:
    json.dump(scraped_articles, file, indent=4, ensure_ascii=False)

print("✅ Scraping complete! Data saved to monecsites.json")
