import os

class Config:
    # Data paths
    RAW_DATA_PATH = os.path.join('data', 'raw_reviews')
    PROCESSED_DATA_PATH = os.path.join('data', 'processed')
    RESULTS_PATH = os.path.join('data', 'results')
    
    # Model parameters
    DEFAULT_NUM_TOPICS = 10
    DEFAULT_ITERATIONS = 50
    DEFAULT_RANDOM_STATE = 42
    
    # File upload settings
    ALLOWED_EXTENSIONS = {'csv', 'txt', 'json'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    
    @staticmethod
    def ensure_directories_exist():
        """Create necessary directories if they don't exist"""
        os.makedirs(Config.RAW_DATA_PATH, exist_ok=True)
        os.makedirs(Config.PROCESSED_DATA_PATH, exist_ok=True)
        os.makedirs(Config.RESULTS_PATH, exist_ok=True)

# Initialize directories
Config.ensure_directories_exist()