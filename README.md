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
### 1️⃣ Create a Virtual Environment

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

## How It Works 🚀
This pipeline follows a multi-step process:

* 1️⃣ moneyc.py → Scrapes headlines & URLs of insurance news from MoneyControl.
* 2️⃣ fetch_moneyc.py → Fetches full articles using the extracted URLs.
* 3️⃣ generate_insurance_report.py → Uses Groq’s LLM to generate structured summaries.
* 4️⃣ Scheduling & Logging → The pipeline automatically runs daily with logs for monitoring.

🔹 Reports are saved in report.txt with categorized insights!

### Next Steps 🚀
* Enhance Summarization → Improve structuring using domain-specific LLM prompts.

* Dashboard Integration → Convert reports into real-time visual insights.

* Multi-Source Aggregation → Combine MoneyControl and NewsAPI for richer coverage.