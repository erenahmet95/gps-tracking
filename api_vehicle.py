from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import random
import os
import nc_py_api

app = Flask(__name__, static_folder='static')  # Static folder olarak 'static' klasörü belirtilmiştir
CORS(app)  # CORS'u etkinleştir

# Nextcloud giriş bilgileri ve hedef klasör
NC_URL = "https://cloud.mt-kabelbau.de"
NC_USER = "Eren Isik"
NC_PASS = "A+b=123456789"
TARGET_DIR = "Projekte/WestNetz/Rüthen-Upgrade/99_sonstiges/Baustelle Fotos und Videos/59602 Rüthen"
OUTPUT_JS_PATH = "static/photos.js"  # static dizinine kaydet

# Nextcloud istemcisi oluşturma
nc = nc_py_api.Nextcloud(nextcloud_url=NC_URL, nc_auth_user=NC_USER, nc_auth_pass=NC_PASS)

def list_photos(directory):
    """Verilen dizindeki tüm fotoğraf dosyalarını listele."""
    photo_files = []
    for node in nc.files.listdir(directory):
        if node.is_dir:
            photo_files.extend(list_photos(node.user_path))
        elif node.user_path.endswith(('.jpg', '.jpeg', '.png')):
            photo_files.append(node.user_path)
    return photo_files

def create_photos_js(photo_list):
    """Fotoğraf dosyası listesinden photos.js dosyasını oluştur."""
    js_content = "const photoFiles = [\n"
    for photo in photo_list:
        js_content += f'    "{photo}",\n'
    js_content += "];\n"

    with open(OUTPUT_JS_PATH, "w", encoding="utf-8") as js_file:
        js_file.write(js_content)
    print(f"photos.js başarıyla oluşturuldu: {OUTPUT_JS_PATH}")

def update_photos_js():
    """Nextcloud'dan en son fotoğrafları alarak photos.js dosyasını güncelle."""
    try:
        photos = list_photos(TARGET_DIR)
        create_photos_js(photos)
    except Exception as e:
        print(f"Hata: photos.js güncellenemedi - {e}")

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

@app.route('/api/update-photos', methods=['GET'])
def update_photos():
    update_photos_js()
    return jsonify({
        "status": "photos.js başarıyla güncellendi"
    })

# Statik photos.js dosyasını sunma
@app.route('/static/photos.js')
def serve_photos_js():
    return send_from_directory(app.static_folder, 'photos.js')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render'ın sağladığı PORT'u al
    update_photos_js()  # Başlangıçta photos.js'yi güncelle
    app.run(host='0.0.0.0', port=port)
