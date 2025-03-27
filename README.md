# Insurance News Agent 🚀
## Overview
This agent fetches the latest insurance news and generates structured summary reports under key domains such as:

* Climate Risk

* InsureTech

* Regulation & Policies

* Industry Trends

The generated reports are tailored for professionals in the Insurance and Reinsurance business to stay updated with impactful events.

## Why This Approach?
* ✅ No External Frameworks (e.g., LangChain) → Making it more secure for enterprise integration.
* ✅ Automated News Aggregation → Runs daily at 9 AM, fetching and summarizing news without manual intervention.
* ✅ Multi-Source News Extraction → Ensures diverse perspectives by pulling from multiple sources.

## Approaches to Identify Insurance News
### Approach 1: MoneyControl
Extracts the latest insurance-related news from MoneyControl. 
MoneyControl is part of the Network 18 group, owned by Reliance Group. A scheduled pipeline runs every morning at 9 AM, fetching content and generating a summary report.

### Approach 2: NewsAPI.org
Uses NewsAPI.org to pull the latest global insurance news. This API acts as a wrapper around Google News for comprehensive coverage.

## Setup & Installation
### 1️⃣ Generate API Keys and Create a Virtual Environment
* Generate API key from your Groq account
* Generate API key from newsapi.org
* Add the API keys in the following format in your .env format
```
GROQ_API_KEY =
NEWS_API_KEY =
```

#### Virtual Environment
```python -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```
### 3️⃣ Run the Pipeline (MoneyControl Approach)

```
cd option-one
python pipeline.py
```
💡 After running, a structured summary report (report.txt) will be generated.

### Demo
![{734E6BD0-9189-434E-9277-CF79B72D53EB}](https://github.com/user-attachments/assets/deaf1fb1-ece5-4e2c-a671-d392da04ada1)


## How It Works 🚀
This pipeline follows a multi-step process:

* 1️⃣ moneyc.py → Scrapes headlines & URLs of insurance news from MoneyControl.
* 2️⃣ fetch_moneyc.py → Fetches full articles using the extracted URLs.
* 3️⃣ generate_insurance_report.py → Uses Groq’s LLM to generate structured summaries.
* 4️⃣ Scheduling & Logging → The pipeline automatically runs daily with logs for monitoring.

🔹 Reports are saved in report.txt with categorized insights!

#### NOTE
* If you want to know the source from which the report was generated add this function in your generate_insurance_report.py
```
# Process each article
for article in articles:
    headline = article.get("headline", "Unknown Title")
    link = article.get("link", "No Link Provided")
    content = " ".join(article.get("content", []))  # Convert list to string

    if not content.strip():
        print(f"⚠️ Skipping '{headline}' - No content available.")
        continue  # Skip empty articles

    print(f"📌 Analyzing: {headline}")

    structured_summary = categorize_and_summarize(content)

    if structured_summary:
        structured_summaries.append(f"🔹 **{headline}**\n🔗 {link}\n{structured_summary}\n\n")
        print(f"✅ Processed: {headline}")
    else:
        print(f"❌ Failed to process '{headline}'")

# Generate structured insurance report
report_content = (
    "📌 **INSURANCE MARKET REPORT**\n"
    "----------------------------------------\n\n"
    + "\n".join(structured_summaries)
)

# Save report to a text file
with open("insurance_report.txt", "w", encoding="utf-8") as file:
    file.write(report_content)

print("✅ Report generated: insurance_report.txt")
```
### Next Steps 🚀

* Have multiple approaches
    * Local LLM Integration
    * Framework Integration
    * Research and experimentation on different Agentic architectures

* Dashboard Integration → Convert reports into real-time visual insights.

* Multi-Source Aggregation → Combine MoneyControl and NewsAPI for richer coverage.
