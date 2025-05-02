import React, { useState } from 'react';
import axios from 'axios';

const UploadPanel = ({ onAnalysisComplete }) => {
    const [file, setFile] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) {
            setError('Please select a file first');
            return;
        }

        setIsLoading(true);
        setError(null);

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:5000/api/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            onAnalysisComplete(response.data);
        } catch (err) {
            setError(err.response?.data?.error || 'An error occurred during analysis');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="upload-panel">
            <h2>Upload Customer Reviews</h2>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} accept=".csv,.txt,.json" />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Analyzing...' : 'Analyze'}
                </button>
            </form>
            {error && <div className="error-message">{error}</div>}
        </div>
    );
};

export default UploadPanel;