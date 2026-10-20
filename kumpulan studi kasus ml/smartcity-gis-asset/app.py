from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_NAME = 'database/assets.db'

def init_db():
    os.makedirs('database', exist_ok=True)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS public_assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_name TEXT NOT NULL,
            category TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/assets', methods=['GET'])
def get_assets():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public_assets")
    rows = cursor.fetchall()
    conn.close()
    
    assets = [dict(row) for row in rows]
    return jsonify(assets)

@app.route('/api/assets', methods=['POST'])
def add_asset():
    data = request.json
    asset_name = data.get('asset_name')
    category = data.get('category')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO public_assets (asset_name, category, latitude, longitude)
        VALUES (?, ?, ?, ?)
    ''', (asset_name, category, latitude, longitude))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Aset/Laporan berhasil disubmit ke Cloud!"}), 201

if __name__ == '__main__':
    init_db()
    app.run(port=5000)
