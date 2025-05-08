import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home/Home';  // Changed from './pages/Home'
import Demo from './pages/Demo/Demo';  // Changed from './pages/Demo'
import NavBar from './components/NavBar/NavBar';  // Changed from './components/NavBar'
import './styles/main.css';

function App() {
  return (
    <Router>
      {/* NavBar should wrap around Routes to appear on all pages */}
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/demo" element={<Demo />} />
      </Routes>
    </Router>
  );
}

export default App;