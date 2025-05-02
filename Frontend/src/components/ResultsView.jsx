import React from 'react';
import { Table } from 'react-bootstrap';

const ResultsView = ({ topics }) => {
    return (
        <div className="results-view">
            <h3>Discovered Topics</h3>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>Topic #</th>
                        <th>Top Words</th>
                    </tr>
                </thead>
                <tbody>
                    {topics.map((topic, index) => (
                        <tr key={index}>
                            <td>Topic {index + 1}</td>
                            <td>
                                {topic.split(' + ').map((word, i) => (
                                    <span key={i} className="topic-word">
                                        {word.split('*')[1].replace(/"/g, '')}
                                    </span>
                                ))}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </div>
    );
};

export default ResultsView;