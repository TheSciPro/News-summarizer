import subprocess
import time
import logging
import schedule

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def run_script(script_name):
    """Run a Python script and log errors"""
    logging.info(f"🚀 Running {script_name}...")

    try:
        subprocess.run(["python", script_name], check=True)
        logging.info(f"✅ {script_name} completed successfully!\n")
    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Error while running {script_name}: {e}")
        print(f"❌ Error while running {script_name}. Check pipeline.log for details.")
        exit(1)  

def run_pipeline():
    """Runs the full scraping and reporting pipeline"""
    start_time = time.time()

    # Step 1: Scrape latest headlines
    run_script("moneyc.py")

    # Step 2: Fetch content from URLs
    run_script("fetch_moneyc.py")

    # Step 3: Generate structured report
    run_script("generate_insurance_report.py")

    # Total execution time
    end_time = time.time()
    execution_time = round(end_time - start_time, 2)
    logging.info(f"🎯 Full pipeline executed in {execution_time} seconds!\n")
    print(f"🎯 Full pipeline executed in {execution_time} seconds!")

# Schedule the script to run every day at 9 AM
schedule.every().day.at("09:00").do(run_pipeline)

if __name__ == "__main__":
    logging.info("🚀 Starting the scheduled pipeline...")

    # Run pipeline immediately on start
    run_pipeline()

    # Keep the script running for scheduling
    while True:
        schedule.run_pending()
        time.sleep(60)  
