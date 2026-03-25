import requests
from datetime import timedelta
from email.utils import parsedate_to_datetime


url = input("Enter website URL (include https://): ")

try:
    response = requests.get(url, timeout=5)

    print("\n--- RESULT ---")
    print("Status Code:", response.status_code)

    if response.url.startswith("https://"):
        print("HTTPS: Yes")
    else:
        print("HTTPS: No")



    headers = response.headers
    from datetime import timedelta
    from email.utils import parsedate_to_datetime

    TIME_HEADERS = ["date", "expires", "last-modified"]

    print("\n--- HEADERS (SMART TIME HANDLING) ---")

    for key, value in headers.items():
        if key.lower() in TIME_HEADERS:
            try:
                gmt_time = parsedate_to_datetime(value)
                uzb_time = gmt_time + timedelta(hours=5)
                print(f"{key} (UZT): {uzb_time.strftime('%Y-%m-%d %H:%M:%S')}")
            except:
                print(f"{key}: {value} (could not parse)")
        else:
            print(f"{key}: {value}")


    print("\n--- SECURITY HEADERS ---")

    if "Content-Security-Policy" in headers:
        print("CSP: Present")
    else:
        print("CSP: Missing")

    if "X-Frame-Options" in headers:
        print("X-Frame-Options: Present")
    else:
        print("X-Frame-Options: Missing")

    if "X-Content-Type-Options" in headers:
        print("X-Content-Type-Options: Present")
    else:
        print("X-Content-Type-Options: Missing")

    if "Referrer-Policy" in headers:
        print("Referrer-Policy: Present")
    else:
        print("Referrer-Policy: Missing")

    risk = "LOW"

    if "Content-Security-Policy" not in headers:
        risk = "HIGH"

    elif "Strict-Transport-Security" not in headers:
        risk = "MEDIUM"

    print("\n--- SECURITY RISK ---")
    print("Risk Level:", risk)

    if "Strict-Transport-Security" in headers:
        print("HSTS: Present")
    else:
        print("HSTS: Missing")
except:
    print("Error: Could not connect to the website")

