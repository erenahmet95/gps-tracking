from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # CORS'u etkinleştir

def get_random_coordinates():
    latitude = 51.49268579318188 + (random.random() - 0.5) * 0.01
    longitude = 8.431149492160445 + (random.random() - 0.5) * 0.01
    return latitude, longitude

@app.route('/api/vehicle-location', methods=['GET'])
def vehicle_location():
    lat, lon = get_random_coordinates()
    return jsonify({
        "latitude": lat,
        "longitude": lon
    })

# app.run() çağrısını kaldırın
