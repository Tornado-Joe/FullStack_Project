from flask import Flask, jsonify, render_template
from supabase import create_client, Client
import os
from dotenv import load_dotenv  # NEU: Lädt Umgebungsvariablen aus .env

# .env-Datei laden
load_dotenv()

app = Flask(__name__, static_folder='', template_folder='')

# Supabase Zugangsdaten aus der .env-Datei holen
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Verbindung zur Supabase-Datenbank
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_personal', methods=['GET'])
def get_personal():
    try:
        result = supabase.table('Personal').select('Name, Position').execute()
        data = result.data  # Extrahierte Daten aus Supabase
        print("Daten aus Supabase:", data)  # Debugging
        return jsonify(data)  # JSON an das Frontend zurückgeben
    except Exception as e:
        print("Fehler:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
