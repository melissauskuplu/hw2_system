import csv
import os
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

CSV_FILE = 'submissions.csv'

# Ensure CSV file exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Name', 'Email', 'Message'])

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        data = request.get_json()
        
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        if not all([name, email, message]):
            return jsonify({"error": "Missing required fields: name, email, message"}), 400
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Append to CSV
        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, name, email, message])
            
        return jsonify({"status": "success", "message": "Data appended to CSV"}), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
