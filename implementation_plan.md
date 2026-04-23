# Implementation Plan - HW2: Data Input & Persistence System

This plan outlines the creation of a fully autonomous system for receiving data via HTTP, persisting it to a local CSV, generating a KPI report using Gemini AI, and delivering the report via email.

## User Review Required

> [!IMPORTANT]
> The system uses a hardcoded Gemini API Key and Gmail App Password as provided in the request. These should be treated as sensitive information.

> [!NOTE]
> Stage 1 (Persistence) will use a local CSV (`submissions.csv`) for simulation as suggested, to avoid complex Google Sheets API authentication setup for this homework.

## Proposed Changes

### Project Structure
- `app.py`: Flask server for data input and persistence.
- `hw2_report.py`: Script to fetch data, generate AI summary, and send email.
- `submissions.csv`: Local storage for Stage 1 data.

---

### [Component] Stage 1: Flask Server
#### [NEW] [app.py]
- Setup Flask with a POST route `/data`.
- Receive `name`, `email`, and `message`.
- Append to `submissions.csv` with a timestamp.

### [Component] Stage 2 & 3: Reporting and Emailing
#### [NEW] [hw2_report.py]
- Download CSV from the provided Google Sheets link.
- Parse CSV and format for Gemini.
- Call Gemini 1.5 Flash to generate executive summary (raw HTML).
- Construct email with the HTML report.
- Send email via Gmail SMTP using provided credentials.

---

## Verification Plan

### Automated Tests
1. **Dependency Installation**: `pip install flask requests google-generativeai`
2. **Flask Testing**: Send a test POST request to `http://localhost:5000/data` and verify `submissions.csv` is updated.
3. **Report Generation**: Run `python hw2_report.py` and check the console output (HTML) and the sent email.

### Manual Verification
- Verify the email receipt at `receiver mail`.
- Check the HTML table formatting and AI summary content.
