from flask import Flask, jsonify, render_template
from supabase import create_client, Client

app = Flask(__name__, static_folder='', template_folder='')

# Verbindung zur Supabase-Datenbank
SUPABASE_URL = 'https://xrjwfmgowboaorbvkbdp.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhyandmbWdvd2JvYW9yYnZrYmRwIiwicm9sZSIsInNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MDQyNDcwMiwiZXhwIjoyMDU2MDAwNzAyfQ.i6m1JqWHlm09j-da4tSlJfTeS0fzvOhLIFUKP4CY2hQ'
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    return render_template('index.html')  # Lädt die HTML-Seite

@app.route('/get_names', methods=['GET'])
def get_names():
    # Nur die Spalte "Name" aus der Tabelle "Personal" abrufen
    result = supabase.table('Personal').select('Name').execute()
    data = result.data  # Extrahierte Daten
    return jsonify(data)  # Daten als JSON zurückgeben

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Nutzt Port 5001
