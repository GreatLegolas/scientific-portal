import React, { useState } from 'react';
import { registerUser } from '../services/api';
import './Register.css';

function Register() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    password2: '',
    bio: '',
    affiliation: ''
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
      const response = await registerUser(formData);
      setMessage(response.data.message);
      setFormData({
        username: '',
        email: '',
        password: '',
        password2: '',
        bio: '',
        affiliation: ''
      });
    } catch (err) {
      setError(err.response?.data?.message || 'Registration failed');
    }
  };

  return (
    <div className="register-container">
      <h2>User Registration</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Username:</label>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Password:</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Confirm Password:</label>
          <input
            type="password"
            name="password2"
            value={formData.password2}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Bio:</label>
          <textarea
            name="bio"
            value={formData.bio}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Affiliation:</label>
          <input
            type="text"
            name="affiliation"
            value={formData.affiliation}
            onChange={handleChange}
          />
        </div>
        <button type="submit">Register</button>
      </form>
      {message && <div className="success-message">{message}</div>}
      {error && <div className="error-message">{error}</div>}
    </div>
  );
}

export default Register;
