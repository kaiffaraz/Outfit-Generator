import os
import random
import webbrowser
import threading
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load pretrained CNN
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Define a simple color palette for "fashion logic"
STYLE_PAIRS = {
    "White": ["Black", "Navy Blue", "Grey"],
    "Light Blue": ["Charcoal", "Black", "Beige"],
    "Pink": ["Grey", "Navy Blue"],
    "Sky Blue": ["Navy", "Dark Grey"],
    "Black": ["Beige", "White", "Light Grey"],
    "Navy Blue": ["Grey", "Khaki"],
    "Grey": ["Maroon", "Navy Blue", "White"]
}

def extract_features(img_path):
    """Extract features for possible future fashion model usage."""
    img = Image.open(img_path).convert('RGB').resize((224, 224))
    img_data = np.expand_dims(np.array(img), axis=0)
    img_data = preprocess_input(img_data)
    features = model.predict(img_data, verbose=0)
    return features.flatten()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        shirts = request.files.getlist('shirts')
        pants = request.files.getlist('pants')

        if not shirts or not pants:
            return jsonify({'error': 'Please upload both shirts and pants.'}), 400

        shirt_paths, pant_paths = [], []
        for file in shirts:
            filename = secure_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)
            shirt_paths.append(path)

        for file in pants:
            filename = secure_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)
            pant_paths.append(path)

        outfits = []
        color_keys = list(STYLE_PAIRS.keys())

        for i in range(min(6, len(shirt_paths))):
            shirt_color = random.choice(color_keys)
            pant_color = random.choice(STYLE_PAIRS[shirt_color])

            shirt_img = shirt_paths[i % len(shirt_paths)]
            pant_img = pant_paths[i % len(pant_paths)]

            outfits.append({
                "shirt": "/" + shirt_img.replace("\\", "/"),
                "pant": "/" + pant_img.replace("\\", "/"),
                "description": f"{shirt_color} Shirt with {pant_color} Pants"
            })

        return jsonify({'outfits': outfits})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/static/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)
