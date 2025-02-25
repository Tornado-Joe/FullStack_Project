import os
from flask import Flask, jsonify, render_template
from supabase import create_client, Client

app = Flask(__name__, static_folder='', template_folder='')

# Supabase Zugangsdaten
SUPABASE_URL = 'https://xrjwfmgowboaorbvkbdp.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhyandmbWdvd2JvYW9yYnZrYmRwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MDQyNDcwMiwiZXhwIjoyMDU2MDAwNzAyfQ.i6m1JqWHlm09j-da4tSlJfTeS0fzvOhLIFUKP4CY2hQ'

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_names', methods=['GET'])
def get_names():
    try:
        result = supabase.table('Personal').select('Name').execute()
        print(result)  # Debugging: Zeigt das Ergebnis in der Konsole
        data = result.data
        return jsonify(data)
    except Exception as e:
        print("Fehler:", e)  # Zeigt die genaue Fehlerursache
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
