from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64
from scan import DocScanner
import cv2

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins


@app.route('/scan', methods=['POST'])
def scan_image():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # If user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Save the uploaded file to a temporary location
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        # Initialize the document scanner
        scanner = DocScanner()

        # Scan the uploaded image
        try:
            scanned_image = scanner.scan(file_path)
            os.remove(file_path)  # Remove the temporary file

            # Encode the scanned image to base64
            _, buffer = cv2.imencode('.jpg', scanned_image)
            base64_image = base64.b64encode(buffer).decode('utf-8')
            
            return jsonify({'success': True, 'image': base64_image})
        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070, debug=True)
