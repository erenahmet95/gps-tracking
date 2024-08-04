from flask import Flask, jsonify
from flask_cors import CORS
import random
import os
import nc_py_api

app = Flask(__name__)
CORS(app)  # Enable CORS

# Nextcloud credentials and target directory
NC_URL = "https://cloud.mt-kabelbau.de"
NC_USER = "Eren Isik"
NC_PASS = "A+b=123456789"
TARGET_DIR = "Projekte/WestNetz/Rüthen-Upgrade/99_sonstiges/Baustelle Fotos und Videos/59602 Rüthen"
OUTPUT_JS_PATH = "photos.js"

# Create a Nextcloud client instance
nc = nc_py_api.Nextcloud(nextcloud_url=NC_URL, nc_auth_user=NC_USER, nc_auth_pass=NC_PASS)

def list_photos(directory):
    """List all photo files in the given directory."""
    photo_files = []
    for node in nc.files.listdir(directory):
        if node.is_dir:
            photo_files.extend(list_photos(node.user_path))
        elif node.user_path.endswith(('.jpg', '.jpeg', '.png')):
            photo_files.append(node.user_path)
    return photo_files

def create_photos_js(photo_list):
    """Create a photos.js file from the list of photo files."""
    js_content = "const photoFiles = [\n"
    for photo in photo_list:
        js_content += f'    "{photo}",\n'
    js_content += "];\n"

    with open(OUTPUT_JS_PATH, "w", encoding="utf-8") as js_file:
        js_file.write(js_content)
    print(f"photos.js successfully created: {OUTPUT_JS_PATH}")

def update_photos_js():
    """Update the photos.js file with the latest photos from Nextcloud."""
    try:
        photos = list_photos(TARGET_DIR)
        create_photos_js(photos)
    except Exception as e:
        print(f"Error updating photos.js: {e}")

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
        "status": "photos.js updated successfully"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get the PORT provided by Render
    update_photos_js()  # Initial update of photos.js
    app.run(host='0.0.0.0', port=port)
