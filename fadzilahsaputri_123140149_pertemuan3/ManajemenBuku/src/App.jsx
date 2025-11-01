import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home/Home';
import Stats from './pages/Stats/Stats';
import './App.css';

function App() {
  return (
    <div className="app">
      <nav className="navbar">
        <div className="nav-container">
          <Link to="/" className="nav-brand">
            📚 Manajemen Buku
          </Link>
          <div className="nav-links">
            <Link to="/" className="nav-link">
              Koleksi
            </Link>
            <Link to="/stats" className="nav-link">
              Statistik
            </Link>
          </div>
        </div>
      </nav>

      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stats" element={<Stats />} />
        </Routes>
      </main>

      <footer className="footer">
        <p>&copy; 2024 Manajemen Buku Pribadi</p>
      </footer>
    </div>
  );
}

export default App;