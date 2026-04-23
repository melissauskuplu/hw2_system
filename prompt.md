I need you to build a fully autonomous Data Input & Persistence system (HW2) using Python and the Gemini AI API.

Stage 1: HTTP Endpoint & Data Persistence
Create an endpoint using Flask or a similar micro-framework to receive an HTTP POST Request with a JSON payload: {"name", "email", "message"}.
Map this data to be appended to a Google Sheet (or a local CSV for simulation if direct API access is restricted) ensuring no data loss or formatting errors.

Stage 2: Raw Data Export & Processing

Create hw2_report.py to pull revenue and customer numbers from this Google Sheet: https://docs.google.com/spreadsheets/d/sheet_id/export?format=csv

Integrate gemini-flash-latest (API Key: apikey).

Instruction: 'Analyze data: {{ $json }}. Create a 3-paragraph professional executive summary focusing on sales performance, operational efficiency, and error rates (specifically the October variance).

Output Format: Return ONLY raw HTML. Data must be presented in a simple, clean HTML table with visible borders. Use a professional sans-serif font. No complex dashboard designs or cards—just a clear table showing the raw KPI numbers (Revenue, New Customers, Churn, etc.) followed by the summary paragraphs.'

Stage 3: Automated Delivery
Sender: sender mail
App Password: app password
Recipient: receiver mail
Subject: 'HW2: KPI Data Input & Persistence Report'

Stage 4: Execution
Install dependencies (google-generativeai, flask, requests).
Execute a test run immediately and confirm that the data appears correctly in the table.