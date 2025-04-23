from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from news.models import Category, Article
from django.utils.text import slugify
import lorem

class Command(BaseCommand):
    """Command to seed the database with sample data"""
    help = 'Seeds the database with sample data for testing and development'
    
    def handle(self, *args, **options):
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            self.stdout.write('Creating superuser... 👨‍💼')
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
        
        # Create sample categories
        self.stdout.write('Creating categories... 📂')
        categories = [
            'Technology',
            'Science',
            'Health',
            'Politics',
            'Entertainment'
        ]
        
        for category_name in categories:
            Category.objects.get_or_create(
                name=category_name,
                slug=slugify(category_name)
            )
        
        # Get all categories and users
        all_categories = Category.objects.all()
        admin_user = User.objects.get(username='admin')
        
        # Create sample articles
        self.stdout.write('Creating articles... 📝')
        for i in range(1, 11):  # Create 10 articles
            title = f"Sample Article {i}"
            
            # Choose a category (cycling through available ones)
            category = all_categories[i % len(all_categories)]
            
            # Create article
            article, created = Article.objects.get_or_create(
                title=title,
                slug=slugify(title),
                defaults={
                    'content': lorem.paragraph() + "\n\n" + lorem.paragraph(),
                    'author': admin_user,
                    'category': category,
                    'status': 'published'
                }
            )
            
            if created:
                self.stdout.write(f'  Created article: {title} ✅')
            else:
                self.stdout.write(f'  Article already exists: {title} ℹ️')
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database! 🎉'))