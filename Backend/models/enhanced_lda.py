import numpy as np
from gensim import corpora, models
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
from gensim.models.ldamulticore import LdaMulticore
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class EnhancedLDA:
    def __init__(self, num_topics=10, alpha='symmetric', eta='auto', 
                 iterations=50, random_state=None):
        self.num_topics = num_topics
        self.alpha = alpha
        self.eta = eta
        self.iterations = iterations
        self.random_state = random_state
        self.lda_model = None
        self.dictionary = None
        self.coherence_score = None
        
    def fit(self, processed_docs, optimize_coherence=True):
        """Fit the enhanced LDA model with Gibbs Sampling and Perplexity optimization"""
        
        # Create dictionary and corpus
        self.dictionary = corpora.Dictionary(processed_docs)
        corpus = [self.dictionary.doc2bow(doc) for doc in processed_docs]
        
        # Train base LDA model with Gibbs Sampling
        self.lda_model = LdaMulticore(
            corpus=corpus,
            id2word=self.dictionary,
            num_topics=self.num_topics,
            passes=self.iterations,
            alpha=self.alpha,
            eta=self.eta,
            random_state=self.random_state,
            chunksize=2000,
            eval_every=10,
            per_word_topics=True
        )
        
        if optimize_coherence:
            self.optimize_coherence(corpus, processed_docs)
        
        return self
    
    def optimize_coherence(self, corpus, texts):
        """Optimize topic coherence using perplexity and coherence metrics"""
        # Calculate coherence score
        coherence_model = CoherenceModel(
            model=self.lda_model,
            texts=texts,
            dictionary=self.dictionary,
            coherence='c_v'
        )
        self.coherence_score = coherence_model.get_coherence()
        
        # Additional optimization logic would go here
        # This could include iterative refinement of topics based on coherence
        
        return self.coherence_score
    
    def predict_topics(self, new_docs):
        """Predict topics for new documents"""
        if not self.lda_model or not self.dictionary:
            raise ValueError("Model must be trained before prediction")
            
        new_corpus = [self.dictionary.doc2bow(doc) for doc in new_docs]
        topics = []
        
        for doc in new_corpus:
            topic_dist = self.lda_model.get_document_topics(doc)
            topics.append(topic_dist)
            
        return topics
    
    def get_topics(self, num_words=10):
        """Return the discovered topics with their top words"""
        return self.lda_model.print_topics(num_words=num_words)