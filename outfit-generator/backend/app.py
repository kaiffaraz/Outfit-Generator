from flask import Flask, request, jsonify, send_from_directory, render_template_string
from flask_cors import CORS
import os
import random
import webbrowser
import threading

app = Flask(__name__, static_folder="../frontend", static_url_path="/")
CORS(app)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Serve the frontend index.html
@app.route("/")
def serve_frontend():
    index_path = os.path.join(app.static_folder, "index.html")
    if os.path.exists(index_path):
        return send_from_directory(app.static_folder, "index.html")
    return "❌ index.html not found. Make sure it's inside the 'frontend' folder."

# Upload shirts and pants
@app.route("/upload", methods=["POST"])
def upload_files():
    shirts = request.files.getlist("shirts")
    pants = request.files.getlist("pants")

    if not shirts or not pants:
        return jsonify({"error": "Please upload both shirts and pants"}), 400

    shirt_paths, pant_paths = [], []

    # Save shirts
    for file in shirts:
        filename = "shirt_" + file.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)
        shirt_paths.append(f"/{path}")

    # Save pants
    for file in pants:
        filename = "pant_" + file.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)
        pant_paths.append(f"/{path}")

    # Generate outfit combinations
    outfits = []
    color_combos = [
        ("#ffffff", "#000000"),  # White shirt + Black pant
        ("#00008B", "#808080"),  # Navy shirt + Gray pant
        ("#C0C0C0", "#2F4F4F"),  # Light gray shirt + Dark gray pant
        ("#4682B4", "#000000"),  # Steel blue + Black
        ("#E6E6FA", "#2E2E2E"),  # Lavender + Charcoal
        ("#708090", "#1C1C1C"),  # Slate gray + Black
    ]

    for i in range(min(len(shirt_paths), len(pant_paths))):
        shirt_color, pant_color = random.choice(color_combos)
        outfit = {
            "name": f"Outfit {i + 1}",
            "shirt": shirt_paths[i % len(shirt_paths)],
            "pant": pant_paths[i % len(pant_paths)],
            "shirtColor": shirt_color,
            "pantColor": pant_color
        }
        outfits.append(outfit)

    return jsonify({"outfits": outfits})

# Serve static files (uploads + mannequin)
@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

# Auto open browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
