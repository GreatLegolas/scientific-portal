import React, { useState, useEffect } from 'react';
import { getArticles } from '../services/api';
import './ArticleList.css';

function ArticleList() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchArticles();
  }, []);

  const fetchArticles = async () => {
    try {
      const response = await getArticles();
      setArticles(response.data.results);
      setLoading(false);
    } catch (err) {
      setError('Failed to fetch articles');
      setLoading(false);
    }
  };

  if (loading) return <div className="loading">Loading articles...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="article-list-container">
      <h2>Scientific Articles</h2>
      <div className="articles-grid">
        {articles.map((article) => (
          <div key={article.id} className="article-card">
            <h3>{article.title}</h3>
            <div className="article-meta">
              <span className="author">By: {article.author_name}</span>
              <span className="status">{article.status}</span>
            </div>
            <p className="abstract">{article.abstract.substring(0, 200)}...</p>
            <div className="keywords">
              {article.keywords_list.map((keyword, idx) => (
                <span key={idx} className="keyword-tag">{keyword}</span>
              ))}
            </div>
            <div className="article-stats">
              <span>👁 {article.view_count} views</span>
              <span>📝 {article.reviews_count} reviews</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ArticleList;
