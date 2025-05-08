import React from 'react';
import './ResultsView.css';

const ResultsView = ({ data }) => {
    return (
        <div className="results-view">
            <div className="metrics-section">
                <div className="metric-card">
                    <h3>Topic Coherence</h3>
                    <p className="metric-value">
                        {data.coherence_score?.toFixed(3) || 'N/A'}
                    </p>
                </div>
            </div>

            <div className="topics-section">
                <h3>Discovered Topics</h3>
                <div className="topics-grid">
                    {data.topics?.map((topic, index) => (
                        <div key={index} className="topic-card">
                            <h4>Topic {index + 1}</h4>
                            <ul>
                                {topic.split(' + ').map((word, i) => (
                                    <li key={i}>
                                        {word.split('*')[1].replace(/"/g, '')}
                                    </li>
                                ))}
                            </ul>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default ResultsView;