import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Users API
export const registerUser = (userData) => api.post('/users/register/', userData);
export const getUserProfile = () => api.get('/users/profile/');
export const getUserStats = () => api.get('/users/stats/');
export const updateUserProfile = (userData) => api.put('/users/profile/', userData);

// Articles API
export const getArticles = (params) => api.get('/articles/', { params });
export const getArticle = (id) => api.get(`/articles/${id}/`);
export const createArticle = (articleData) => api.post('/articles/', articleData);
export const submitArticle = (articleData) => api.post('/articles/submit/', articleData);
export const updateArticle = (id, articleData) => api.put(`/articles/${id}/`, articleData);
export const deleteArticle = (id) => api.delete(`/articles/${id}/`);
export const getMyArticles = () => api.get('/articles/my-articles/');

// Reviews API
export const getReviews = (params) => api.get('/reviews/', { params });
export const getReview = (id) => api.get(`/reviews/${id}/`);
export const createReview = (reviewData) => api.post('/reviews/', reviewData);
export const updateReview = (id, reviewData) => api.put(`/reviews/${id}/`, reviewData);
export const getArticleReviews = (articleId) => api.get(`/reviews/article/${articleId}/`);
export const getMyReviews = () => api.get('/reviews/my-reviews/');

export default api;
