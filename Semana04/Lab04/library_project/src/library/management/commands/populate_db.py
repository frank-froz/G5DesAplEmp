from django.core.management.base import BaseCommand
from django.utils import timezone
from library.models import Author, AuthorProfile, Category, Publisher, Book, Publication
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populates the database with sample data'
    
    def handle(self, *args, **options):
        # Clear existing data 🧹
        self.stdout.write('Clearing existing data...')
        Publication.objects.all().delete()
        Book.objects.all().delete()
        Category.objects.all().delete()
        AuthorProfile.objects.all().delete()
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        
        # Create categories 🏷️
        self.stdout.write('Creating categories...')
        categories = [
            Category(name="Science Fiction", description="Imaginative fiction that explores advanced science and technology"),
            Category(name="Fantasy", description="Fiction with magical or supernatural elements"),
            Category(name="Mystery", description="Fiction dealing with the solution of a crime or puzzle"),
            Category(name="Romance", description="Fiction that focuses on romantic relationships"),
            Category(name="Non-fiction", description="Information based on facts and reality"),
            Category(name="Biography", description="An account of someone's life written by someone else"),
        ]
        
        for category in categories:
            category.save()
        
        # Create authors 👨‍🎨
        self.stdout.write('Creating authors...')
        authors = [
            Author(name="J.K. Rowling", birth_date=date(1965, 7, 31), 
                  biography="British author best known for the Harry Potter series."),
            Author(name="George Orwell", birth_date=date(1903, 6, 25), 
                  biography="English novelist, essayist, and critic known for works like '1984' and 'Animal Farm'."),
            Author(name="Jane Austen", birth_date=date(1775, 12, 16), 
                  biography="English novelist known for works such as 'Pride and Prejudice' and 'Sense and Sensibility'."),
        ]
        
        for author in authors:
            author.save()
        
        # Create author profiles 👤
        self.stdout.write('Creating author profiles...')
        profiles = [
            AuthorProfile(author=authors[0], website="https://www.jkrowling.com", twitter_handle="@jk_rowling"),
            AuthorProfile(author=authors[1], website="", twitter_handle=""),
            AuthorProfile(author=authors[2], website="", twitter_handle=""),
        ]
        
        for profile in profiles:
            profile.save()
        
        # Create publishers 🏢
        self.stdout.write('Creating publishers...')
        publishers = [
            Publisher(name="Penguin Books", website="https://www.penguin.com", email="info@penguin.com"),
            Publisher(name="HarperCollins", website="https://www.harpercollins.com", email="info@harpercollins.com"),
            Publisher(name="Bloomsbury", website="https://www.bloomsbury.com", email="info@bloomsbury.com"),
        ]
        
        for publisher in publishers:
            publisher.save()
        
        # Create books 📚
        self.stdout.write('Creating books...')
        books = [
            Book(title="Harry Potter and the Philosopher's Stone", author=authors[0],
                 isbn="9780747532743", publication_date=date(1997, 6, 26),
                 summary="The first book in the Harry Potter series."),
                 
            Book(title="1984", author=authors[1],
                 isbn="9780451524935", publication_date=date(1949, 6, 8),
                 summary="A dystopian novel set in a totalitarian society."),
                 
            Book(title="Pride and Prejudice", author=authors[2],
                 isbn="9780141439518", publication_date=date(1813, 1, 28),
                 summary="A romantic novel that follows the character development of Elizabeth Bennet."),
                 
            Book(title="Harry Potter and the Chamber of Secrets", author=authors[0],
                 isbn="9780747538486", publication_date=date(1998, 7, 2),
                 summary="The second book in the Harry Potter series."),
        ]
        
        for book in books:
            book.save()
        
        # Add categories to books 🔗
        self.stdout.write('Adding categories to books...')
        books[0].categories.add(categories[1])  # Harry Potter - Fantasy
        books[1].categories.add(categories[0])  # 1984 - Science Fiction
        books[1].categories.add(categories[4])  # 1984 - Non-fiction
        books[2].categories.add(categories[3])  # Pride and Prejudice - Romance
        books[3].categories.add(categories[1])  # Harry Potter 2 - Fantasy
        
        # Create publications 📰
        self.stdout.write('Creating publications...')
        publications = [
            Publication(book=books[0], publisher=publishers[2], date_published=date(1997, 6, 26), country="United Kingdom"),
            Publication(book=books[0], publisher=publishers[0], date_published=date(1998, 9, 1), country="United States"),
            Publication(book=books[1], publisher=publishers[0], date_published=date(1949, 6, 8), country="United Kingdom"),
            Publication(book=books[2], publisher=publishers[1], date_published=date(1813, 1, 28), country="United Kingdom"),
            Publication(book=books[3], publisher=publishers[2], date_published=date(1998, 7, 2), country="United Kingdom"),
        ]
        
        for publication in publications:
            publication.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database! 🎉'))
