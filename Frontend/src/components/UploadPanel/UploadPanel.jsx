import React, { useState } from 'react';
import axios from 'axios';
import './UploadPanel.css';

const UploadPanel = ({ onAnalysisComplete }) => {
    const [file, setFile] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setError(null); // Clear error when new file selected
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) {
            setError('Please select a CSV, TXT, or JSON file');
            return;
        }

        setIsLoading(true);
        setError(null);

        try {
            const formData = new FormData();
            formData.append('file', file);

            const response = await axios.post(
                'http://localhost:5000/api/upload', 
                formData, 
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    },
                    timeout: 30000 // 30-second timeout
                }
            );
            
            if (response.data.error) {
                throw new Error(response.data.error);
            }
            
            onAnalysisComplete(response.data);
        } catch (err) {
            console.error('Upload error:', err);
            setError(err.response?.data?.error || 
                    err.message || 
                    'Analysis failed. Please try again.');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="upload-container">
            <h2>Upload Customer Reviews</h2>
            <p className="instructions">
                Supported formats: CSV, JSON, or TXT with review text
            </p>
            
            <form onSubmit={handleSubmit} className="upload-form">
                <div className="file-input-container">
                    <label htmlFor="file-upload" className="file-label">
                        {file ? file.name : 'Choose File'}
                    </label>
                    <input
                        id="file-upload"
                        type="file"
                        onChange={handleFileChange}
                        accept=".csv,.json,.txt"
                        className="file-input"
                    />
                </div>
                
                <button 
                    type="submit" 
                    disabled={isLoading || !file}
                    className={`analyze-btn ${isLoading ? 'loading' : ''}`}
                >
                    {isLoading ? (
                        <>
                            <span className="spinner"></span>
                            Processing...
                        </>
                    ) : (
                        'Analyze Reviews'
                    )}
                </button>
            </form>

            {error && (
                <div className="error-message">
                    ⚠️ {error}
                </div>
            )}
        </div>
    );
};

export default UploadPanel;