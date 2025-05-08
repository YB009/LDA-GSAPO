import React, { useState } from 'react';
import UploadPanel from './UploadPanel/UploadPanel.jsx';
import ResultsView from './ResultsView/ResultsView.jsx';
import TopicVisualization from './ResultsView/TopicVisualization.jsx';

const DemoPage = () => {
    const [results, setResults] = useState(null);

    const handleAnalysisComplete = (data) => {
        setResults(data);
    };

    return (
        <div className="demo-page">
            <h1>Enhanced LDA Sentiment Analysis</h1>
            <div className="demo-container">
                <div className="upload-section">
                    <UploadPanel onAnalysisComplete={handleAnalysisComplete} />
                </div>
                {results && (
                    <div className="results-section">
                        <h2>Analysis Results</h2>
                        <div className="coherence-score">
                            <strong>Topic Coherence Score:</strong> {results.coherence_score.toFixed(3)}
                        </div>
                        <ResultsView topics={results.topics} />
                        <TopicVisualization topics={results.topics} />
                    </div>
                )}
            </div>
        </div>
    );
};

export default DemoPage;