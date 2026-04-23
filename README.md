# 📊 Data Input, Persistence & AI Reporting System (HW2)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![AI](https://img.shields.io/badge/AI-Gemini%20Flash-orange.svg)](https://aistudio.google.com/)
[![Status](https://img.shields.io/badge/Status-Completed-green.svg)](https://github.com/)

An autonomous data pipeline developed for **HW2 – Data Input & Persistence**. This system bridges the gap between raw data entry and professional AI-powered reporting.

## 📝 Project Overview
The system is designed to handle two critical operational stages:
1. **Data Persistence:** Capturing incoming JSON payloads through a dedicated HTTP endpoint.
2. **Automated Analysis:** Processing live KPI metrics from Google Sheets using Generative AI to produce a structured executive report.

## 🏗️ System Architecture

- **Stage 1: HTTP Endpoint & Persistence**
  - Uses **Flask** to host an endpoint that listens for `POST` requests.
  - Accepts JSON payloads: `{"name", "email", "message"}`.
  - Maps and appends data to a local persistence log (CSV) with 100% integrity to ensure no data loss.

- **Stage 2: AI Analysis & Processing**
  - **Data Source:** Fetches live CSV data from a remote Google Sheet.
  - **AI Engine:** Integrates **Gemini 1.5 Flash** to perform a professional analysis of Sales, Efficiency, and Error Rates.
  - **Focus:** Diagnostic analysis of the October variance.

- **Stage 3: Automated Delivery**
  - Generates a **Simple HTML Table** of raw KPI numbers.
  - Sends the report via a secure SMTP gateway with professional formatting.

## 🛠️ Technical Stack
- **Backend:** Python (Flask)
- **AI:** Google Generative AI (Gemini API)
- **Networking:** Requests (with secure headers)
- **Email:** SMTPLib (MIME HTML rendering)

## 📂 Deliverables
- `app.py`: The HTTP endpoint script for data persistence.
- `hw2_report.py`: The AI reporting and email delivery engine.
- `persistence_log.csv`: The local storage for incoming data payloads.

## 🔧 Installation & Execution

1. **Install Dependencies:**
   ```bash
   pip install flask google-generativeai requests
