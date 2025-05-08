import React from 'react';
import '../styles/main.css';

const AboutPage = () => {
    return (
        <div className="about-page">
            <h1>About the Enhanced LDA Framework</h1>
            
            <section className="about-section">
                <h2>Project Overview</h2>
                <p>
                    Our enhanced LDA framework couples Gibbs Sampling with Perplexity optimization
                    to provide more refined topic distribution and increased model accuracy in
                    customer sentiment analysis. By incorporating topic coherence metrics as an
                    evaluation mechanism, our method improves over standard LDA in capturing
                    semantically consistent and sentiment-aligned topics from customer reviews.
                </p>
            </section>
            
            <section className="technical-section">
                <h2>Technical Approach</h2>
                <ul>
                    <li>
                        <strong>Gibbs Sampling:</strong> A Markov Chain Monte Carlo (MCMC) technique
                        to refine topic allocation through iterative sampling of the word distributions.
                    </li>
                    <li>
                        <strong>Perplexity Optimization:</strong> Algorithm that reduces model perplexity
                        and increases interpretability, addressing limitations of high-perplexity models.
                    </li>
                    <li>
                        <strong>Topic Coherence Metrics:</strong> Ensures generated topics are not only
                        statistically robust but also meaningful and aligned with sentiment themes.
                    </li>
                </ul>
            </section>
            
            <section className="benefits-section">
                <h2>Key Benefits</h2>
                <div className="benefits-grid">
                    <div className="benefit-card">
                        <h3>Improved Accuracy</h3>
                        <p>Significantly better than standard LDA in terms of topic coherence</p>
                    </div>
                    <div className="benefit-card">
                        <h3>Actionable Insights</h3>
                        <p>Provides clearer understanding of customer sentiment themes</p>
                    </div>
                    <div className="benefit-card">
                        <h3>User-Friendly</h3>
                        <p>Interactive interface for exploring analysis results</p>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default AboutPage;