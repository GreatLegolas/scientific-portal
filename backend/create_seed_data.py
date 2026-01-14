"""
Script to create initial demonstration data for the scientific portal
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from articles.models import Article
from reviews.models import Review
from django.utils import timezone

User = get_user_model()

def create_seed_data():
    print("Creating seed data...")
    
    # Create superuser
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@scientificportal.com',
            password='admin123',
            email_verified=True
        )
        print(f"Created superuser: admin / admin123")
    
    # Create regular users
    users_data = [
        {
            'username': 'john_doe',
            'email': 'john@example.com',
            'password': 'password123',
            'bio': 'Research scientist specializing in quantum physics',
            'affiliation': 'MIT',
            'email_verified': True
        },
        {
            'username': 'jane_smith',
            'email': 'jane@example.com',
            'password': 'password123',
            'bio': 'Professor of Computer Science',
            'affiliation': 'Stanford University',
            'email_verified': True
        },
        {
            'username': 'bob_wilson',
            'email': 'bob@example.com',
            'password': 'password123',
            'bio': 'PhD candidate in Biochemistry',
            'affiliation': 'Harvard University',
            'email_verified': True
        }
    ]
    
    created_users = []
    for user_data in users_data:
        if not User.objects.filter(username=user_data['username']).exists():
            user = User.objects.create_user(**user_data)
            created_users.append(user)
            print(f"Created user: {user.username}")
    
    # Get all users for article creation
    john = User.objects.get(username='john_doe')
    jane = User.objects.get(username='jane_smith')
    bob = User.objects.get(username='bob_wilson')
    
    # Create articles
    articles_data = [
        {
            'title': 'Quantum Entanglement in High-Energy Physics',
            'abstract': 'This paper explores the phenomenon of quantum entanglement in high-energy particle collisions. We present new experimental results from the Large Hadron Collider that demonstrate previously unknown correlations between entangled particles.',
            'keywords': 'quantum physics, entanglement, particle physics, LHC',
            'author': john,
            'status': 'submitted',
            'view_count': 45,
            'submitted_at': timezone.now()
        },
        {
            'title': 'Machine Learning Applications in Climate Modeling',
            'abstract': 'We propose a novel machine learning approach for improving the accuracy of climate prediction models. Our method combines deep learning with traditional physics-based models to achieve better long-term forecasts.',
            'keywords': 'machine learning, climate science, deep learning, prediction',
            'author': jane,
            'status': 'under_review',
            'view_count': 78,
            'submitted_at': timezone.now()
        },
        {
            'title': 'Novel Protein Folding Mechanisms in Alzheimer\'s Disease',
            'abstract': 'This study identifies new protein folding pathways that may contribute to the development of Alzheimer\'s disease. We used advanced imaging techniques to observe protein misfolding at the molecular level.',
            'keywords': 'biochemistry, protein folding, Alzheimer, neuroscience',
            'author': bob,
            'status': 'submitted',
            'view_count': 32,
            'submitted_at': timezone.now()
        },
        {
            'title': 'Advances in Renewable Energy Storage',
            'abstract': 'This paper presents a comprehensive review of current renewable energy storage technologies and proposes new approaches for improving efficiency and reducing costs.',
            'keywords': 'renewable energy, energy storage, sustainability, batteries',
            'author': john,
            'status': 'published',
            'view_count': 156,
            'submitted_at': timezone.now()
        }
    ]
    
    created_articles = []
    for article_data in articles_data:
        if not Article.objects.filter(title=article_data['title']).exists():
            article = Article.objects.create(**article_data)
            created_articles.append(article)
            print(f"Created article: {article.title}")
    
    # Create reviews
    if len(created_articles) >= 2:
        # Jane reviews John's quantum physics paper
        article1 = Article.objects.get(title='Quantum Entanglement in High-Energy Physics')
        if not Review.objects.filter(article=article1, reviewer=jane).exists():
            review1 = Review.objects.create(
                article=article1,
                reviewer=jane,
                status='completed',
                recommendation='minor_revision',
                comments='The experimental methodology is sound, but the paper would benefit from additional discussion of the theoretical implications. Please expand the conclusion section.',
                confidential_comments='This is a strong paper that should be accepted with minor revisions.',
                completed_at=timezone.now()
            )
            print(f"Created review by {jane.username} for article: {article1.title}")
        
        # Bob reviews John's quantum physics paper
        if not Review.objects.filter(article=article1, reviewer=bob).exists():
            review2 = Review.objects.create(
                article=article1,
                reviewer=bob,
                status='in_progress',
                comments='',
                confidential_comments='Need more time to review the statistical analysis.'
            )
            print(f"Created review by {bob.username} for article: {article1.title}")
        
        # John reviews Jane's climate modeling paper
        article2 = Article.objects.get(title='Machine Learning Applications in Climate Modeling')
        if not Review.objects.filter(article=article2, reviewer=john).exists():
            review3 = Review.objects.create(
                article=article2,
                reviewer=john,
                status='completed',
                recommendation='accept',
                comments='Excellent work combining ML with traditional climate models. The validation results are convincing and the approach is innovative.',
                confidential_comments='This is publishable as-is. Highly recommend acceptance.',
                completed_at=timezone.now()
            )
            print(f"Created review by {john.username} for article: {article2.title}")
    
    print("\nSeed data creation completed!")
    print("\nCredentials:")
    print("Admin: admin / admin123")
    print("User 1: john_doe / password123")
    print("User 2: jane_smith / password123")
    print("User 3: bob_wilson / password123")

if __name__ == '__main__':
    create_seed_data()
