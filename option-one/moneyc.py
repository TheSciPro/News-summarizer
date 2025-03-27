import requests
import json
from bs4 import BeautifulSoup


URL = "https://www.moneycontrol.com/news/tags/insurance.html"
headers = {"User-Agent": "Mozilla/5.0"}


response = requests.get(URL, headers=headers)

data = []

if response.status_code == 200:
  
    soup = BeautifulSoup(response.text, "html.parser")

    
    for h2 in soup.find_all("h2"):
        h2_text = h2.get_text(strip=True)
        link_tag = h2.find("a")  
        h2_link = link_tag["href"] if link_tag and "href" in link_tag.attrs else None

        paragraphs = []
        for p in h2.find_all_next("p"):
            if not p.attrs:  
                p_text = p.get_text(strip=True)
                if p_text: 
                    paragraphs.append(p_text)

            
            if p.find_next("h2"):
                break

        if paragraphs:
            data.append({
                "headline": h2_text,
                "link": h2_link,
                "paragraphs": paragraphs
            })

    with open("insurance_articles.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("✅ Data saved to insurance_articles.json successfully!")
else:
    print(f"❌ Failed to fetch the page, status code: {response.status_code}")
