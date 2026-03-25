# Website-security-check
Many websites lack essential security headers, which may expose them to risks such as:
	•	Cross-Site Scripting (XSS)
	•	Clickjacking
	•	Insecure content loading
This tool:
	•	Sends a request to a website
	•	Extracts HTTP response headers
	•	Checks for key security headers
	•	Provides a basic risk assessment (LOW / HIGH)

🔍 Security Checks Included
	•	HTTPS enforcement
	•	Content-Security-Policy (CSP)
	•	X-Frame-Options
	•	Strict-Transport-Security (HSTS)
	•	X-Content-Type-Options
	•	Referrer-Policy

⚠️ Important Note

This tool provides basic security analysis only.
It does not guarantee that a website is fully secure.

Example:
--- SECURITY HEADERS ---
CSP: Present
X-Frame-Options: Present
X-Content-Type-Options: Present
Referrer-Policy: Missing

--- SECURITY RISK ---
Risk Level: LOW

How to run: 
pip install requests
python scanner.py

These indicate that YouTube has basic security policies. 

The program will ask you to enter the URL of the website, and it will automatically give you the report. The URL should be https://example.com  in this format, you can change https with http and .com with .org. 

🎯 Purpose
This project was built to:
	•	improve awareness of basic web security
	•	practice building cybersecurity tools
	•	explore security gaps in real-world websites

🧠 Future Improvements
	•	Web interface (UI)
	•	Automated scanning of multiple sites
	•	More advanced vulnerability checks
