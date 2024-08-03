from flask import Flask, jsonify
from flask_cors import CORS
import random
import os

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render'ın sağladığı PORT'u al
    app.run(host='0.0.0.0', port=port)
