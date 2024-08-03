from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # CORS izinlerini ekleyin

# Rüthen şehrinde başlangıç konumu
vehicle_location = {
    "latitude": 51.492856993695966,  # Rüthen şehir merkezi civarında bir konum
    "longitude": 8.43100790583464
}

# Konum bilgisini güncelleyen ve döndüren API
@app.route('/api/vehicle-location', methods=['GET'])
def get_vehicle_location():
    # Simülasyon için konumu biraz değiştiriyoruz
    vehicle_location['latitude'] += random.uniform(-0.0005, 0.0005)
    vehicle_location['longitude'] += random.uniform(-0.0005, 0.0005)

    # Konsola koordinatları yazdır
    print(f"Updated Vehicle Location: Latitude = {vehicle_location['latitude']}, Longitude = {vehicle_location['longitude']}")

    return jsonify(vehicle_location)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Flask uygulamasını 5000 portunda çalıştırıyoruz
