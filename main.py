from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import cv2
import numpy as np
from scan import DocScanner # Assuming you saved the DocScanner class in scan.py

app = Flask(__name__)
CORS(app)

@app.route('/scan', methods=['POST'])
def scan_image():
    try:
        data = request.get_json()
        if not data or 'file' not in data:
            return jsonify({'error': 'No image data provided'})

        base64_image = data['file']
        img_bytes = base64.b64decode(base64_image)
        img_array = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if img is None:
            return jsonify({'error': 'Invalid image data'})

        scanner = DocScanner()
        scanned_base64 = scanner.scan(img) #image object passed in.

        return jsonify({'success': True, 'image': scanned_base64})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070, debug=True)