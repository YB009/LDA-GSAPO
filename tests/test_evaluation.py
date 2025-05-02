import pytest
from backend.models.evaluation import ModelEvaluator

@pytest.fixture
def sample_topics():
    return [
        ['service', 'support', 'help', 'team'],
        ['product', 'quality', 'material', 'design'],
        ['price', 'cost', 'value', 'expensive']
    ]

def test_calculate_coherence():
    # Mock model and data would be needed
    pass

def test_evaluate_topic_quality(sample_topics):
    quality = ModelEvaluator.evaluate_topic_quality(sample_topics)
    assert 0 <= quality['topic_diversity'] <= 1
    assert 0 <= quality['term_uniqueness'] <= 1

def test_visualize_topics(sample_topics):
    # Test returns matplotlib figure
    fig = ModelEvaluator.visualize_topics(sample_topics)
    assert hasattr(fig, 'savefig')