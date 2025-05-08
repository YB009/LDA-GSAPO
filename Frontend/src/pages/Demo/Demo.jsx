import React, { useState } from 'react';
import UploadPanel from '../../components/UploadPanel/UploadPanel';
import ResultsView from '../../components/ResultsView/ResultsView';
import './Demo.css';

const Demo = () => {
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleAnalysisComplete = (data) => {
        setResults(data);
    };

    return (
        <div className="demo-page">
            <header className="demo-header">
                <h1>Customer Sentiment Analysis</h1>
                <p>Upload customer reviews to discover key topics and sentiments</p>
            </header>
            
            <main className="demo-content">
                <div className="upload-section">
                    <UploadPanel 
                        onAnalysisComplete={handleAnalysisComplete}
                    />
                </div>
                
                {loading && (
                    <div className="loading-overlay">
                        <div className="spinner"></div>
                        <p>Analyzing your reviews...</p>
                    </div>
                )}

                {results && (
                    <div className="results-section">
                        <h2>Analysis Results</h2>
                        <ResultsView data={results} />
                    </div>
                )}
            </main>
        </div>
    );
};

export default Demo;