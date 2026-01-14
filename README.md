# Scientific Portal

A scientific publication and peer review portal prototype built with Django (backend) and React (frontend).

## Features

### User Management
- User registration with email verification placeholder
- ORCID account linking placeholder
- User profiles with statistics and analytics

### Article Management
- Submit scientific articles with title, abstract, and keywords
- Article metadata storage in database
- Article view count tracking
- Status tracking (draft, submitted, under review, accepted, rejected, published)

### Anonymous Peer Review
- Anonymous review process protecting both author and reviewer identities
- Review status tracking (in progress, completed)
- Recommendations (accept, minor revision, major revision, reject)
- Confidential comments for editors

### User Profiles & Analytics
- View authored articles
- View contributed reviews
- Statistics dashboard:
  - Total articles authored
  - Articles published
  - Reviews given and completed
  - Total article views
  - Articles under review

### Administration
- Django Admin interface for database management
- View and manage all users, articles, and reviews

## Tech Stack

**Backend:**
- Python 3.12
- Django 4.2.9
- Django REST Framework 3.14.0
- PostgreSQL (with SQLite fallback for development)

**Frontend:**
- React 18
- React Router DOM
- Axios for API calls

## Project Structure

```
scientific-portal/
├── backend/                 # Django backend
│   ├── backend/            # Project settings
│   ├── users/              # User management app
│   ├── articles/           # Article management app
│   ├── reviews/            # Review management app
│   ├── db.sqlite3          # SQLite database (development)
│   ├── manage.py           # Django management script
│   └── create_seed_data.py # Script to create demo data
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── services/      # API service layer
│   │   ├── App.js         # Main app component
│   │   └── App.css        # Main app styles
│   └── package.json
└── requirements.txt        # Python dependencies
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 14+ and npm
- PostgreSQL (optional, SQLite is used by default)

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/GreatLegolas/scientific-portal.git
cd scientific-portal
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Navigate to backend directory:
```bash
cd backend
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create demo data (includes admin and test users):
```bash
python create_seed_data.py
```

6. Start the Django development server:
```bash
python manage.py runserver
```

The backend API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install npm dependencies:
```bash
npm install
```

3. Start the React development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## Demo Credentials

After running `create_seed_data.py`, you can use these credentials:

**Admin:**
- Username: `admin`
- Password: `admin123`
- Admin Panel: `http://localhost:8000/admin/`

**Test Users:**
- Username: `john_doe` / Password: `password123`
- Username: `jane_smith` / Password: `password123`
- Username: `bob_wilson` / Password: `password123`

## API Endpoints

### Users
- `POST /api/users/register/` - Register new user
- `GET /api/users/profile/` - Get current user profile
- `PUT /api/users/profile/` - Update user profile
- `GET /api/users/stats/` - Get user statistics
- `GET /api/users/<id>/` - Get user details

### Articles
- `GET /api/articles/` - List all articles
- `POST /api/articles/` - Create new article
- `GET /api/articles/<id>/` - Get article details
- `PUT /api/articles/<id>/` - Update article
- `DELETE /api/articles/<id>/` - Delete article
- `GET /api/articles/my-articles/` - Get user's articles
- `POST /api/articles/submit/` - Submit article for review

### Reviews
- `GET /api/reviews/` - List all reviews
- `POST /api/reviews/` - Create new review
- `GET /api/reviews/<id>/` - Get review details
- `PUT /api/reviews/<id>/` - Update review
- `DELETE /api/reviews/<id>/` - Delete review
- `GET /api/reviews/my-reviews/` - Get user's reviews
- `GET /api/reviews/article/<article_id>/` - Get reviews for article (anonymous for authors)

## Database Configuration

By default, the application uses SQLite for easy development. To use PostgreSQL:

1. Update `backend/backend/settings.py`:
```python
# Set USE_SQLITE environment variable to 'false'
import os
os.environ['USE_SQLITE'] = 'false'
```

2. Configure your PostgreSQL database:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'scientific_portal',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Development Notes

- The frontend is configured to connect to the backend at `http://localhost:8000`
- CORS is configured to allow requests from `http://localhost:3000`
- Email verification is a placeholder feature (not implemented)
- ORCID integration is a placeholder feature (not implemented)

## Future Enhancements

- Implement actual email verification
- Integrate ORCID authentication
- Add file upload for article PDFs
- Implement real-time notifications
- Add search and filtering capabilities
- Implement user authentication with JWT tokens
- Add article versioning
- Implement discussion threads for reviews
- Add DOI assignment for published articles

## License

This is a prototype project for demonstration purposes.
