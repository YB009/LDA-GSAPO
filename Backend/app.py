from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from models.enhanced_lda import EnhancedLDA
from models.preprocessing import TextPreprocessor
import os
import logging
from werkzeug.utils import secure_filename
import nltk
import json


# Ensure downloads happen even if someone runs app.py first
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
# Configure logging
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO
)

# Initialize Flask app with CORS
app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for all routes

# Configuration
UPLOAD_FOLDER = os.path.join('data', 'raw_reviews')
ALLOWED_EXTENSIONS = {'csv', 'txt', 'json'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config.update({
    'UPLOAD_FOLDER': UPLOAD_FOLDER,
    'MAX_CONTENT_LENGTH': 16 * 1024 * 1024  # 16MB
})

# Initialize models
preprocessor = TextPreprocessor()
lda_model = EnhancedLDA(num_topics=10)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """Root endpoint to verify backend is running"""
    return jsonify({
        "status": "running",
        "message": "LDA Backend API",
        "endpoints": {
            "upload": "/api/upload (POST)",
            "analyze": "/api/analyze (POST)"
        },
        "instructions": "Upload CSV with 'review' column to /api/upload"
    })

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Handle file upload and processing"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Allowed formats: CSV, TXT, JSON'}), 400

    try:
        # Secure save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Process and analyze
        processed_text = preprocessor.process_file(filepath)
        lda_model.fit(processed_text)
        
        return jsonify({
            'status': 'success',
            'filename': filename,
            'topics': lda_model.get_topics(),
            'coherence_score': lda_model.coherence_score
        })

    except Exception as e:
        logging.error(f"Processing failed: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    """Direct text analysis endpoint"""
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing text parameter'}), 400

        processed_text = preprocessor.process_text(data['text'])
        topics = lda_model.predict_topics([processed_text])
        
        return jsonify({
            'status': 'success',
            'topics': topics
        })

    except Exception as e:
        logging.error(f"Analysis failed: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files (like favicon)"""
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    # Create required directories
    os.makedirs('data/raw_reviews', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    
    # Run the app
    app.run(host='0.0.0.0', port=5000, debug=True)