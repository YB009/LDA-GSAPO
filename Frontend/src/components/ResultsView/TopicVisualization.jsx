import React, { useEffect, useRef } from 'react';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const TopicVisualization = ({ topics }) => {
    const chartRef = useRef(null);
    const chartInstance = useRef(null);

    useEffect(() => {
        if (topics && chartRef.current) {
            // Destroy previous chart if exists
            if (chartInstance.current) {
                chartInstance.current.destroy();
            }

            // Prepare data for chart
            const labels = topics.map((_, index) => `Topic ${index + 1}`);
            const wordsData = topics.map(topic => 
                topic.split(' + ').map(item => {
                    const parts = item.split('*');
                    return {
                        word: parts[1].replace(/"/g, ''),
                        weight: parseFloat(parts[0])
                    };
                })
            );

            // Get top 3 words for each topic
            const datasets = [];
            for (let i = 0; i < 3; i++) {
                datasets.push({
                    label: `Top ${i + 1} Word`,
                    data: wordsData.map(topic => topic[i]?.weight || 0),
                    backgroundColor: `hsl(${i * 120}, 70%, 50%)`,
                });
            }

            // Create new chart
            const ctx = chartRef.current.getContext('2d');
            chartInstance.current = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: datasets,
                },
                options: {
                    responsive: true,
                    scales: {
                        x: {
                            stacked: true,
                        },
                        y: {
                            stacked: true,
                            beginAtZero: true,
                        },
                    },
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const topicIndex = context.dataIndex;
                                    const wordIndex = context.datasetIndex;
                                    const word = wordsData[topicIndex][wordIndex]?.word || '';
                                    return `${word}: ${context.raw}`;
                                }
                            }
                        }
                    }
                },
            });
        }

        return () => {
            if (chartInstance.current) {
                chartInstance.current.destroy();
            }
        };
    }, [topics]);

    return (
        <div className="topic-visualization">
            <h3>Topic Word Weights</h3>
            <canvas ref={chartRef}></canvas>
        </div>
    );
};

export default TopicVisualization;