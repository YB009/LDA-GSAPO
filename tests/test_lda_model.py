import pytest
from backend.models.enhanced_lda import EnhancedLDA
from backend.models.preprocessing import TextPreprocessor

@pytest.fixture
def sample_docs():
    return [
        ["customer", "service", "good", "experience"],
        ["product", "quality", "poor", "return"],
        ["delivery", "fast", "shipping", "time"],
        ["price", "high", "value", "money"],
        ["website", "easy", "use", "interface"]
    ]

def test_lda_initialization():
    lda = EnhancedLDA(num_topics=5)
    assert lda.num_topics == 5
    assert lda.lda_model is None

def test_lda_fit(sample_docs):
    lda = EnhancedLDA(num_topics=3)
    lda.fit(sample_docs)
    assert lda.lda_model is not None
    assert lda.dictionary is not None
    assert lda.coherence_score is not None

def test_predict_topics(sample_docs):
    lda = EnhancedLDA(num_topics=3)
    lda.fit(sample_docs)
    new_docs = [["customer", "happy", "service"], ["product", "broken"]]
    topics = lda.predict_topics(new_docs)
    assert len(topics) == 2
    for topic in topics:
        assert len(topic) == 3  # num_topics