import numpy as np
from gensim.models import CoherenceModel
import matplotlib.pyplot as plt
import seaborn as sns

class ModelEvaluator:
    @staticmethod
    def calculate_coherence(model, texts, dictionary, coherence='c_v'):
        coherence_model = CoherenceModel(
            model=model,
            texts=texts,
            dictionary=dictionary,
            coherence=coherence
        )
        return coherence_model.get_coherence()
    
    @staticmethod
    def evaluate_topic_quality(topics):
        """Evaluate topic quality based on topic diversity and term uniqueness"""
        # Calculate topic diversity
        unique_words = set()
        for topic in topics:
            for word in topic:
                unique_words.add(word)
        diversity = len(unique_words) / sum(len(topic) for topic in topics)
        
        # Calculate term uniqueness
        word_counts = {}
        for topic in topics:
            for word in topic:
                word_counts[word] = word_counts.get(word, 0) + 1
        uniqueness = sum(1 for count in word_counts.values() if count == 1) / len(word_counts)
        
        return {
            'topic_diversity': diversity,
            'term_uniqueness': uniqueness
        }
    
    @staticmethod
    def visualize_topics(topics, num_words=10):
        """Create visualization of topics with their top words"""
        plt.figure(figsize=(12, 8))
        for i, topic in enumerate(topics):
            plt.subplot(2, 5, i+1)  # Assuming 10 topics
            words = [word for word, _ in topic[:num_words]]
            weights = [weight for _, weight in topic[:num_words]]
            sns.barplot(x=weights, y=words)
            plt.title(f'Topic {i+1}')
            plt.tight_layout()
        return plt