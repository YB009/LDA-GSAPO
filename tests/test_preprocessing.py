import pytest
from backend.models.preprocessing import TextPreprocessor

@pytest.fixture
def preprocessor():
    return TextPreprocessor()

def test_clean_text(preprocessor):
    dirty_text = "This is a TEST text! With 123 numbers and #hashtags."
    clean_text = preprocessor.clean_text(dirty_text)
    assert clean_text == "this is a test text with numbers and hashtags"

def test_lemmatize_text(preprocessor):
    text = "running runs ran"
    lemmatized = preprocessor.lemmatize_text(text)
    assert "run" in lemmatized

def test_remove_stopwords(preprocessor):
    tokens = ["this", "is", "a", "test", "sentence"]
    filtered = preprocessor.remove_stopwords(tokens)
    assert len(filtered) == 2  # "test" and "sentence"

def test_process_text(preprocessor):
    text = "The products are amazing and work perfectly!"
    processed = preprocessor.process_text(text)
    assert "product" in processed  # lemmatized
    assert "amazing" in processed
    assert "perfectly" in processed
    assert "the" not in processed  # stopword removed