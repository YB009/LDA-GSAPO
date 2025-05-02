# User Guide: Enhanced LDA Sentiment Analysis Tool

## Getting Started
1. **Installation**:
   - Clone the repository
   - Set up Python backend: `pip install -r backend/requirements.txt`
   - Install frontend dependencies: `npm install`

2. **Running the Application**:
   - Start backend: `python backend/app.py`
   - Start frontend: `npm start`

## Using the Application
### Uploading Data
1. Navigate to the Demo page
2. Click "Choose File" and select your customer reviews file (CSV, JSON, or TXT)
3. Click "Analyze" to process the file

### Viewing Results
The analysis results include:
- **Topic Coherence Score**: Overall quality metric (higher is better)
- **Discovered Topics**: List of topics with their top words
- **Topic Visualization**: Bar chart showing word weights per topic

### Interpreting Results
- Each topic represents a common theme in customer feedback
- Words are weighted by their importance to the topic
- Higher coherence scores indicate more meaningful topics

## Best Practices
1. **Data Preparation**:
   - Ensure text is in the first column of CSV/JSON files
   - For large datasets (>10,000 reviews), consider sampling

2. **Analysis**:
   - Start with default settings (10 topics)
   - Adjust number of topics based on coherence scores

3. **Troubleshooting**:
   - For processing errors, check file format
   - For unclear topics, try adjusting preprocessing settings