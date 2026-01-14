import React, { useState, useEffect } from 'react';
import { getUserStats, getMyArticles, getMyReviews } from '../services/api';
import './UserProfile.css';

function UserProfile() {
  const [stats, setStats] = useState(null);
  const [articles, setArticles] = useState([]);
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchProfileData();
  }, []);

  const fetchProfileData = async () => {
    try {
      const [statsRes, articlesRes, reviewsRes] = await Promise.all([
        getUserStats(),
        getMyArticles(),
        getMyReviews()
      ]);
      setStats(statsRes.data);
      setArticles(articlesRes.data);
      setReviews(reviewsRes.data);
      setLoading(false);
    } catch (err) {
      setError('Failed to load profile data. Please login first.');
      setLoading(false);
    }
  };

  if (loading) return <div className="loading">Loading profile...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="profile-container">
      <h2>User Profile</h2>
      
      <div className="stats-section">
        <h3>Statistics</h3>
        <div className="stats-grid">
          <div className="stat-card">
            <div className="stat-value">{stats.articles_authored}</div>
            <div className="stat-label">Articles Authored</div>
          </div>
          <div className="stat-card">
            <div className="stat-value">{stats.articles_published}</div>
            <div className="stat-label">Articles Published</div>
          </div>
          <div className="stat-card">
            <div className="stat-value">{stats.reviews_given}</div>
            <div className="stat-label">Reviews Given</div>
          </div>
          <div className="stat-card">
            <div className="stat-value">{stats.reviews_completed}</div>
            <div className="stat-label">Reviews Completed</div>
          </div>
          <div className="stat-card">
            <div className="stat-value">{stats.total_article_views}</div>
            <div className="stat-label">Total Article Views</div>
          </div>
          <div className="stat-card">
            <div className="stat-value">{stats.articles_under_review}</div>
            <div className="stat-label">Under Review</div>
          </div>
        </div>
      </div>

      <div className="articles-section">
        <h3>My Articles</h3>
        {articles.length === 0 ? (
          <p>No articles yet.</p>
        ) : (
          <div className="list">
            {articles.map((article) => (
              <div key={article.id} className="list-item">
                <h4>{article.title}</h4>
                <div className="item-meta">
                  <span>Status: {article.status}</span>
                  <span>Views: {article.view_count}</span>
                  <span>Reviews: {article.reviews_count}</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="reviews-section">
        <h3>My Reviews</h3>
        {reviews.length === 0 ? (
          <p>No reviews yet.</p>
        ) : (
          <div className="list">
            {reviews.map((review) => (
              <div key={review.id} className="list-item">
                <h4>{review.article_title}</h4>
                <div className="item-meta">
                  <span>Status: {review.status}</span>
                  <span>Recommendation: {review.recommendation || 'N/A'}</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default UserProfile;
