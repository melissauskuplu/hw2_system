import requests
import csv
import io
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import google.generativeai as genai

# Configuration
CSV_URL = "google sheet url"
GEMINI_API_KEY = "gemini api key"
SENDER_EMAIL = "sender mail"
APP_PASSWORD = "google app pasword"
RECIPIENT_EMAIL = "receiver mail"
SUBJECT = "HW2: KPI Data Input & Persistence Report"

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def process_with_gemini(csv_data):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-flash-latest')
    
    prompt = f"""
    Analyze data: {csv_data}. 
    Create a 3-paragraph professional executive summary focusing on sales performance, operational efficiency, and error rates (specifically the October variance).
    
    Output Format: Return ONLY raw HTML. Data must be presented in a simple, clean HTML table with visible borders. 
    Use a professional sans-serif font. No complex dashboard designs or cards—just a clear table showing the raw KPI numbers 
    (Revenue, New Customers, Churn, etc.) followed by the summary paragraphs.
    """
    
    response = model.generate_content(prompt)
    # Clean up the response to ensure it's just HTML
    html_content = response.text.replace('```html', '').replace('```', '').strip()
    return html_content

def send_email(html_content):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = SUBJECT
    
    msg.attach(MIMEText(html_content, 'html'))
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)

def main():
    print("Fetching data...")
    csv_text = fetch_data(CSV_URL)
    
    print("Processing with Gemini...")
    html_report = process_with_gemini(csv_text)
    
    print("Full HTML Report Output:\n")
    print(html_report)
    
    print("\nSending email...")
    send_email(html_report)
    print("Email sent successfully!")

if __name__ == "__main__":
    main()
