import requests
import datetime
import time

URL = "https://app-selenium-chrome-ybznwqgr6a2k7hsxs6vutq.streamlit.app"

def main():
    now = datetime.datetime.utcnow()
    print(f"[{now}] Cron job started - pinging Streamlit app...")
    try:
        response = requests.get(URL, timeout=15)
        print(f"✅ Request completed with status {response.status_code}")
        print("Response length:", len(response.text))
    except Exception as e:
        print("Error while requesting:", e)
    print(f"Finished at {datetime.datetime.utcnow()} UTC\n")

if __name__ == "__main__":
    main()
