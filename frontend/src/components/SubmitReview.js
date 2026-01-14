import React, { useState } from 'react';
import { createReview } from '../services/api';
import './SubmitReview.css';

function SubmitReview() {
  const [formData, setFormData] = useState({
    article: '',
    comments: '',
    confidential_comments: '',
    recommendation: ''
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
      await createReview(formData);
      setMessage('Review submitted successfully!');
      setFormData({
        article: '',
        comments: '',
        confidential_comments: '',
        recommendation: ''
      });
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to submit review. Please login first.');
    }
  };

  return (
    <div className="submit-review-container">
      <h2>Submit Anonymous Review</h2>
      <p className="info-text">Your identity will remain anonymous to the article author.</p>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Article ID:</label>
          <input
            type="number"
            name="article"
            value={formData.article}
            onChange={handleChange}
            required
            placeholder="Enter the article ID"
          />
        </div>
        <div className="form-group">
          <label>Comments (visible to author):</label>
          <textarea
            name="comments"
            value={formData.comments}
            onChange={handleChange}
            placeholder="Your review comments that will be shared with the author"
            rows="6"
          />
        </div>
        <div className="form-group">
          <label>Confidential Comments (only for editors):</label>
          <textarea
            name="confidential_comments"
            value={formData.confidential_comments}
            onChange={handleChange}
            placeholder="Confidential comments for editors only"
            rows="4"
          />
        </div>
        <div className="form-group">
          <label>Recommendation:</label>
          <select
            name="recommendation"
            value={formData.recommendation}
            onChange={handleChange}
            required
          >
            <option value="">Select a recommendation</option>
            <option value="accept">Accept</option>
            <option value="minor_revision">Minor Revision</option>
            <option value="major_revision">Major Revision</option>
            <option value="reject">Reject</option>
          </select>
        </div>
        <button type="submit">Submit Review</button>
      </form>
      {message && <div className="success-message">{message}</div>}
      {error && <div className="error-message">{error}</div>}
    </div>
  );
}

export default SubmitReview;
