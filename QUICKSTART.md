# Quick Start Guide

## Running the Scientific Portal Locally

### 1. Start the Backend (Django)

```bash
# Navigate to the backend directory
cd backend

# Run migrations (if not already done)
python3 manage.py migrate

# Create demo data (if not already done)
python3 create_seed_data.py

# Start the Django server
python3 manage.py runserver
```

Backend will be available at: `http://localhost:8000`

### 2. Start the Frontend (React)

Open a new terminal:

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies (first time only)
npm install

# Start the React development server
npm start
```

Frontend will be available at: `http://localhost:3000`

### 3. Access the Application

- **Frontend**: http://localhost:3000
- **API**: http://localhost:8000/api/
- **Django Admin**: http://localhost:8000/admin/

### 4. Login Credentials

**Admin Account:**
- Username: `admin`
- Password: `admin123`

**Test User Accounts:**
- `john_doe` / `password123`
- `jane_smith` / `password123`
- `bob_wilson` / `password123`

## Features to Test

### User Registration
1. Go to http://localhost:3000/register
2. Fill in the registration form
3. Submit to create a new user

### Browse Articles
1. The homepage shows all published articles
2. Each article displays title, abstract, keywords, views, and review count

### Submit Article
1. Go to http://localhost:3000/submit-article
2. Fill in title, abstract, and keywords
3. Submit (note: requires authentication)

### Submit Review
1. Go to http://localhost:3000/submit-review
2. Enter article ID, comments, and recommendation
3. Submit anonymous review

### View Profile & Analytics
1. Go to http://localhost:3000/profile
2. View statistics (articles, reviews, views)
3. See your authored articles and reviews

### Django Admin
1. Go to http://localhost:8000/admin/
2. Login with admin credentials
3. Manage users, articles, and reviews
4. View all database records

## API Endpoints Testing

You can test the API endpoints using curl or any API client:

```bash
# List all articles
curl http://localhost:8000/api/articles/

# Get specific article
curl http://localhost:8000/api/articles/1/

# Register new user
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "testpass123",
    "password2": "testpass123"
  }'
```

## Notes

- The application uses SQLite by default for easy development
- Email verification and ORCID integration are placeholders
- For production use, configure PostgreSQL and implement proper authentication
- CORS is configured to allow localhost:3000 for development
