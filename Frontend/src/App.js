import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/Home';
import DemoPage from './pages/Demo';
import NavBar from './components/NavBar';
import './styles/main.css';

function App() {
  return (
    <Router>
      {/* NavBar should wrap around Routes to appear on all pages */}
      <NavBar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/demo" element={<DemoPage />} />
      </Routes>
    </Router>
  );
}

export default App;