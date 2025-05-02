import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy
import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nlp = spacy.load('en_core_web_sm')

class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.custom_stopwords = ['product', 'service', 'company', 'would', 'could', 'also']
        
    def clean_text(self, text):
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
        # Convert to lowercase
        text = text.lower()
        # Remove extra whitespace
        text = re.sub(' +', ' ', text).strip()
        return text
    
    def lemmatize_text(self, text):
        doc = nlp(text)
        return ' '.join([token.lemma_ for token in doc])
    
    def remove_stopwords(self, tokens):
        return [token for token in tokens if token not in self.stop_words 
                and token not in self.custom_stopwords and len(token) > 2]
    
    def process_text(self, text):
        # Clean text
        text = self.clean_text(text)
        # Lemmatize
        text = self.lemmatize_text(text)
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stopwords
        tokens = self.remove_stopwords(tokens)
        return tokens
    
    def process_file(self, file_path):
        # Read different file types
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
            texts = df.iloc[:, 0].tolist()  # Assuming text is in first column
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
            texts = df.iloc[:, 0].tolist()
        else:  # txt file
            with open(file_path, 'r') as f:
                texts = f.readlines()
        
        processed_docs = [self.process_text(text) for text in texts]
        return processed_docs