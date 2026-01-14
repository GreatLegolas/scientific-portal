import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Register from './components/Register';
import ArticleList from './components/ArticleList';
import SubmitArticle from './components/SubmitArticle';
import SubmitReview from './components/SubmitReview';
import UserProfile from './components/UserProfile';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <div className="header-content">
            <h1>Scientific Portal</h1>
            <nav className="nav-menu">
              <Link to="/">Home</Link>
              <Link to="/register">Register</Link>
              <Link to="/submit-article">Submit Article</Link>
              <Link to="/submit-review">Submit Review</Link>
              <Link to="/profile">Profile</Link>
            </nav>
          </div>
        </header>
        <main className="App-main">
          <Routes>
            <Route path="/" element={<ArticleList />} />
            <Route path="/register" element={<Register />} />
            <Route path="/submit-article" element={<SubmitArticle />} />
            <Route path="/submit-review" element={<SubmitReview />} />
            <Route path="/profile" element={<UserProfile />} />
          </Routes>
        </main>
        <footer className="App-footer">
          <p>© 2026 Scientific Portal - Peer Review System</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
