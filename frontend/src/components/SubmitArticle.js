import React, { useState } from 'react';
import { submitArticle } from '../services/api';
import './SubmitArticle.css';

function SubmitArticle() {
  const [formData, setFormData] = useState({
    title: '',
    abstract: '',
    keywords: ''
  });
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('');
    setError('');

    try {
      await submitArticle(formData);
      setMessage('Article submitted successfully!');
      setFormData({
        title: '',
        abstract: '',
        keywords: ''
      });
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to submit article. Please login first.');
    }
  };

  return (
    <div className="submit-article-container">
      <h2>Submit Article</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Title:</label>
          <input
            type="text"
            name="title"
            value={formData.title}
            onChange={handleChange}
            required
            placeholder="Enter article title"
          />
        </div>
        <div className="form-group">
          <label>Abstract:</label>
          <textarea
            name="abstract"
            value={formData.abstract}
            onChange={handleChange}
            required
            placeholder="Enter article abstract"
            rows="8"
          />
        </div>
        <div className="form-group">
          <label>Keywords (comma-separated):</label>
          <input
            type="text"
            name="keywords"
            value={formData.keywords}
            onChange={handleChange}
            required
            placeholder="e.g., machine learning, AI, neural networks"
          />
        </div>
        <button type="submit">Submit Article</button>
      </form>
      {message && <div className="success-message">{message}</div>}
      {error && <div className="error-message">{error}</div>}
    </div>
  );
}

export default SubmitArticle;
