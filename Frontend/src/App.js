import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/Home';
import AboutPage from './pages/About';
import DemoPage from './pages/Demo';
import NavBar from './components/NavBar';
import './styles/main.css';

function App() {
    return (
        <Router>
            <div className="app">
                <NavBar />
                <main>
                    <Routes>
                        <Route path="/" element={<HomePage />} />
                        <Route path="/about" element={<AboutPage />} />
                        <Route path="/demo" element={<DemoPage />} />
                    </Routes>
                </main>
                <footer>
                    <p>© {new Date().getFullYear()} Enhanced LDA Sentiment Analysis Project</p>
                </footer>
            </div>
        </Router>
    );
}

export default App;