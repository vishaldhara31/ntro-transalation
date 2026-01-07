# backend/app.py
import os
import pytesseract
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
# 1. Import the official Google Cloud library
from google.cloud import translate_v2 as translate

# 2. Set up the credentials. The library will automatically find 'credentials.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'
translate_client = translate.Client()

# 3. Set the Tesseract path (this is still needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
CORS(app)

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        file = request.files.get('file')
        if not file:
            return jsonify({"error": "No file provided"}), 400

        # --- Step A: Perform OCR (same as before) ---
        image = Image.open(file.stream)
        original_text = pytesseract.image_to_string(image, lang='nep+sin')

        if not original_text.strip():
            return jsonify({"error": "OCR failed to extract any text from the image."}), 500
        
        print(f"Successfully extracted text: {original_text[:100]}...")

        # --- Step B: Translate using the powerful Google Translate API ---
        result = translate_client.translate(original_text, target_language='en')
        final_translation = result['translatedText']

        print(f"Successfully translated text: {final_translation[:100]}...")
        
        return jsonify({
            'originalText': original_text,
            'translatedText': final_translation
        })

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)