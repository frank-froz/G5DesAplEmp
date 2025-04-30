from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from blog.models import Category, Tag, Post, Comment
import random
from datetime import timedelta


class Command(BaseCommand):
    """Command to seed the database with sample data"""
    help = 'Seeds the database with sample data for development and testing'
    
    def handle(self, *args, **options):
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            self.stdout.write('Creating superuser... 👤')
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
        
        # Create regular user if it doesn't exist
        if not User.objects.filter(username='user').exists():
            self.stdout.write('Creating regular user... 👤')
            User.objects.create_user(
                username='user',
                email='user@example.com',
                password='user123'
            )
        
        # Create categories
        self.stdout.write('Creating categories... 📂')
        categories = [
            ('Programming', 'Posts about programming languages and software development.'),
            ('Data Science', 'Articles related to data analysis, machine learning, and statistics.'),
            ('Web Development', 'Content about web technologies, frameworks, and best practices.'),
            ('DevOps', 'Topics covering deployment, infrastructure, and operations.'),
            ('Career', 'Career advice, industry insights, and professional development.'),
        ]
        
        for name, description in categories:
            Category.objects.get_or_create(
                name=name,
                defaults={
                    'slug': slugify(name),
                    'description': description
                }
            )
        
        # Create tags
        self.stdout.write('Creating tags... 🏷️')
        tags = [
            'Python', 'JavaScript', 'Django', 'React', 'Docker',
            'APIs', 'Database', 'Security', 'Testing', 'Performance',
            'Git', 'Frontend', 'Backend', 'Cloud', 'Mobile'
        ]
        
        created_tags = []
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(
                name=tag_name,
                defaults={'slug': slugify(tag_name)}
            )
            created_tags.append(tag)
        
        # Get users
        admin_user = User.objects.get(username='admin')
        regular_user = User.objects.get(username='user')
        
        # Create posts
        self.stdout.write('Creating posts... 📝')
        post_data = [
            {
                'title': 'Getting Started with Django ORM',
                'content': '''
                Django's Object-Relational Mapping (ORM) is a powerful tool that allows you to interact with your database using Python code instead of raw SQL.
                
                In this post, we'll explore the basics of the Django ORM and how to use it effectively in your projects.
                
                ## Key Features of Django ORM
                
                Django ORM provides several key features that make database interactions simpler:
                
                1. **Model Definition**: Define database tables as Python classes
                2. **QuerySet API**: Intuitive interface for database queries
                3. **Migrations**: Track and apply database schema changes
                4. **Relationship Management**: Easily handle related data
                
                ## Basic Usage
                
                Here's a simple example of how to retrieve data using the Django ORM:
                
                ```python
                # Get all published posts
                published_posts = Post.objects.filter(status='published')
                
                # Get a specific post
                post = Post.objects.get(id=1)
                
                # Get related data
                comments = post.comments.all()
                ```
                
                In future posts, we'll dive deeper into more advanced ORM features like annotations, aggregations, and complex filtering.
                ''',
                'status': 'published',
                'category': 'Programming',
                'tags': ['Python', 'Django', 'Database'],
                'author': admin_user,
            },
            {
                'title': 'Understanding Django Model Relationships',
                'content': '''
                One of the most powerful features of Django's ORM is its ability to define and work with relationships between models.
                
                ## Types of Relationships
                
                Django supports three main types of relationships:
                
                ### One-to-Many (ForeignKey)
                
                The most common type of relationship. For example, a Post has many Comments:
                
                ```python
                class Comment(models.Model):
                    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
                ```
                
                ### Many-to-Many
                
                When records in one table can be related to multiple records in another table, and vice versa. For example, Posts and Tags:
                
                ```python
                class Post(models.Model):
                    tags = models.ManyToManyField(Tag, related_name='posts')
                ```
                
                ### One-to-One
                
                When a record in one table corresponds to exactly one record in another table. For example, User and Profile:
                
                ```python
                class Profile(models.Model):
                    user = models.OneToOneField(User, on_delete=models.CASCADE)
                ```
                
                ## Working with Related Objects
                
                Django makes it easy to navigate relationships in both directions:
                
                ```python
                # Forward (following the relationship)
                comments = post.comments.all()
                
                # Backward (reverse relationship)
                posts = tag.posts.all()
                ```
                
                Understanding these relationships is crucial for designing effective data models and writing efficient queries.
                ''',
                'status': 'published',
                'category': 'Programming',
                'tags': ['Python', 'Django', 'Database'],
                'author': admin_user,
            },
            {
                'title': 'Advanced Queries with Django ORM',
                'content': '''
                Beyond basic CRUD operations, Django's ORM provides powerful tools for complex queries.
                
                ## Using Q Objects for Complex Filters
                
                The Q objects allow for complex queries with logical operators:
                
                ```python
                from django.db.models import Q
                
                # Posts containing "Django" OR "Python" in the title
                posts = Post.objects.filter(
                    Q(title__icontains='Django') | Q(title__icontains='Python')
                )
                
                # Posts published in the last week but NOT in category "News"
                one_week_ago = timezone.now() - timedelta(days=7)
                posts = Post.objects.filter(
                    Q(published_at__gte=one_week_ago) & ~Q(category__name='News')
                )
                ```
                
                ## Annotations and Aggregations
                
                Add computed fields or summarize data:
                
                ```python
                from django.db.models import Count, Avg
                
                # Annotate posts with comment count
                posts = Post.objects.annotate(comment_count=Count('comments'))
                
                # Get average number of comments per post
                avg_comments = Post.objects.aggregate(avg_comments=Avg(Count('comments')))
                ```
                
                ## Query Optimization
                
                Optimize database access with:
                
                ```python
                # Select specific fields
                posts = Post.objects.values('title', 'published_at')
                
                # Prefetch related objects
                posts = Post.objects.prefetch_related('comments')
                
                # Join related models
                posts = Post.objects.select_related('author', 'category')
                ```
                
                These advanced features help you build efficient, powerful applications without writing raw SQL.
                ''',
                'status': 'published',
                'category': 'Programming',
                'tags': ['Python', 'Django', 'Database', 'Performance'],
                'author': admin_user,
            },
            {
                'title': 'Frontend Integration with Django',
                'content': '''
                Integrating modern frontend frameworks with Django backends can create powerful web applications.
                
                ## Options for Frontend Integration
                
                There are several ways to integrate frontend frameworks with Django:
                
                1. **Django Templates with JavaScript**: Use Django's template system with sprinkles of JavaScript
                2. **Django as an API + Separate Frontend**: Django REST Framework + React/Vue/Angular
                3. **Hybrid Approach**: Django templates for some parts, API for others
                
                ## Django REST Framework
                
                For API-based approaches, Django REST Framework (DRF) is essential:
                
                ```python
                from rest_framework import serializers
                
                class PostSerializer(serializers.ModelSerializer):
                    class Meta:
                        model = Post
                        fields = ['id', 'title', 'content', 'author', 'published_at']
                ```
                
                ## CORS Configuration
                
                When using separate frontend applications, configure CORS:
                
                ```python
                INSTALLED_APPS = [
                    # ...
                    'corsheaders',
                ]
                
                MIDDLEWARE = [
                    'corsheaders.middleware.CorsMiddleware',
                    # ...
                ]
                
                CORS_ALLOWED_ORIGINS = [
                    "http://localhost:3000",
                ]
                ```
                
                Choose the approach that best fits your project requirements and team skills.
                ''',
                'status': 'published',
                'category': 'Web Development',
                'tags': ['JavaScript', 'React', 'APIs', 'Frontend'],
                'author': regular_user,
            },
            {
                'title': 'Docker for Django Development',
                'content': '''
                Containerizing your Django application with Docker can simplify development and deployment.
                
                ## Benefits of Docker
                
                - **Consistent environments**: Same setup across all developer machines
                - **Isolation**: Dependencies are contained and don't conflict
                - **Easy onboarding**: New team members can start quickly
                - **Production parity**: Dev environment matches production
                
                ## Basic Docker Setup
                
                A simple `Dockerfile` for Django:
                
                ```dockerfile
                FROM python:3.10-slim
                
                WORKDIR /app
                
                COPY requirements.txt .
                RUN pip install --no-cache-dir -r requirements.txt
                
                COPY . .
                
                CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
                ```
                
                ## Docker Compose
                
                For multi-container setups with databases:
                
                ```yaml
                version: '3'
                
                services:
                  web:
                    build: .
                    ports:
                      - "8000:8000"
                    depends_on:
                      - db
                    environment:
                      - DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
                
                  db:
                    image: postgres:13
                    environment:
                      - POSTGRES_PASSWORD=postgres
                ```
                
                Docker simplifies development workflow and deployment, making it an essential tool for modern Django projects.
                ''',
                'status': 'published',
                'category': 'DevOps',
                'tags': ['Docker', 'DevOps', 'Backend'],
                'author': regular_user,
            },
            {
                'title': 'Custom Model Managers in Django',
                'content': '''
                Django models come with a default manager, but you can create custom managers to encapsulate common queries.
                
                ## What is a Manager?
                
                A manager is the interface through which database queries are provided to Django models. Every model has at least one manager.
                
                ## Creating Custom Managers
                
                There are two main approaches to creating custom managers:
                
                ### 1. Adding Extra Methods
                
                ```python
                class PublishedManager(models.Manager):
                    def published(self):
                        return self.filter(status='published')
                    
                    def by_category(self, category_slug):
                        return self.filter(category__slug=category_slug)
                ```
                
                ### 2. Modifying Initial QuerySet
                
                ```python
                class PublishedManager(models.Manager):
                    def get_queryset(self):
                        return super().get_queryset().filter(status='published')
                ```
                
                ## Using Custom Managers
                
                Add your custom manager to your model:
                
                ```python
                class Post(models.Model):
                    # fields...
                    
                    objects = models.Manager()  # Default manager
                    published = PublishedManager()  # Custom manager
                ```
                
                Then use it in your code:
                
                ```python
                # Using the custom manager
                published_posts = Post.published.all()
                
                # Using a method from the custom manager
                category_posts = Post.published.by_category('django')
                ```
                
                Custom managers help keep your code DRY and maintainable by centralizing query logic.
                ''',
                'status': 'draft',
                'category': 'Programming',
                'tags': ['Python', 'Django', 'Database'],
                'author': admin_user,
            },
        ]
        
        for data in post_data:
            # Get or create category
            category = Category.objects.get(name=data['category'])
            
            # Set published_at for published posts
            published_at = None
            if data['status'] == 'published':
                published_at = timezone.now() - timedelta(days=random.randint(1, 30))
            
            # Create post
            post, created = Post.objects.get_or_create(
                title=data['title'],
                defaults={
                    'slug': slugify(data['title']),
                    'content': data['content'],
                    'status': data['status'],
                    'author': data['author'],
                    'category': category,
                    'published_at': published_at,
                }
            )
            
            if created:
                # Add tags
                for tag_name in data['tags']:
                    tag = Tag.objects.get(name=tag_name)
                    post.tags.add(tag)
                
                self.stdout.write(f"  Created post: {post.title} ✅")
            else:
                self.stdout.write(f"  Post already exists: {post.title} ℹ️")
        
        # Create comments
        self.stdout.write('Creating comments... 💬')
        
        comment_contents = [
            "Great article! Thanks for sharing this information.",
            "I've been looking for this explanation for a while. Very helpful!",
            "Could you elaborate more on the second point? I'm a bit confused about it.",
            "Looking forward to more content like this. Very insightful!",
            "I think you missed mentioning an important aspect of this topic.",
            "This is exactly what I needed to understand. Thanks!",
            "I'm going to implement this in my project right away!",
            "Well explained with clear examples. Easy to follow.",
        ]
        
        published_posts = Post.objects.filter(status='published')
        for post in published_posts:
            # Create 3-5 random comments per post
            num_comments = random.randint(3, 5)
            for i in range(num_comments):
                comment_content = random.choice(comment_contents)
                author = admin_user if i % 2 == 0 else regular_user
                is_approved = random.choice([True, True, False])  # 2/3 chance of being approved
                
                Comment.objects.get_or_create(
                    post=post,
                    author=author,
                    content=comment_content,
                    defaults={
                        'is_approved': is_approved,
                    }
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database! 🎉'))