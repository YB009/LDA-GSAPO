from flask import Flask, request, jsonify
from models.enhanced_lda import EnhancedLDA
from models.preprocessing import TextPreprocessor
import os

app = Flask(__name__)

# Initialize components
preprocessor = TextPreprocessor()
lda_model = EnhancedLDA(num_topics=10)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Save and process the file
    filepath = os.path.join('data/raw_reviews', file.filename)
    file.save(filepath)
    
    # Preprocess and analyze
    processed_text = preprocessor.process_file(filepath)
    lda_model.fit(processed_text)
    
    # Get results
    topics = lda_model.get_topics()
    coherence = lda_model.coherence_score
    
    return jsonify({
        'topics': topics,
        'coherence_score': coherence,
        'message': 'Analysis completed successfully'
    })

@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    processed_text = preprocessor.process_text(text)
    topics = lda_model.predict_topics([processed_text])
    
    return jsonify({
        'topics': topics,
        'message': 'Text analyzed successfully'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)