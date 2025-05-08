import React from 'react';
import { Link } from 'react-router-dom';
import '../../styles/main.css';;

const HomePage = () => {
    return (
        <div className="home-page">
            <header className="hero-section">
                <h1>Enhanced LDA for Customer Sentiment Analysis</h1>
                <p>
                    A novel approach combining Gibbs Sampling and Perplexity optimization 
                    for more coherent topic modeling in customer feedback analysis.
                </p>
                <Link to="/demo" className="cta-button">
                    Try the Demo
                </Link>
            </header>
            
            <section className="features-section">
                <div className="feature">
                    <h3>Gibbs Sampling</h3>
                    <p>Refined topic allocation through iterative sampling of word distributions</p>
                </div>
                <div className="feature">
                    <h3>Perplexity Optimization</h3>
                    <p>Reduced model perplexity for increased interpretability</p>
                </div>
                <div className="feature">
                    <h3>Topic Coherence</h3>
                    <p>Semantically consistent and sentiment-aligned topics</p>
                </div>
            </section>
        </div>
    );
};

export default HomePage;