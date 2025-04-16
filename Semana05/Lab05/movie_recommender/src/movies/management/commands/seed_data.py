import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from movies.models import (
    Director, Actor, Genre, Movie, MovieActor, UserProfile, Rating
)

class Command(BaseCommand):
    """Command to seed the database with sample data"""
    help = 'Seeds the database with sample data for testing and development'
    
    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Rating.objects.all().delete()
        MovieActor.objects.all().delete()
        Movie.objects.all().delete()
        Director.objects.all().delete()
        Actor.objects.all().delete()
        Genre.objects.all().delete()
        
        # Create sample directors
        self.stdout.write('Creating directors...')
        directors = [
            Director(
                name="Christopher Nolan",
                birth_date=date(1970, 7, 30),
                biography="British-American filmmaker known for his cerebral, often nonlinear, storytelling."
            ),
            Director(
                name="Steven Spielberg",
                birth_date=date(1946, 12, 18),
                biography="American filmmaker, considered one of the founding pioneers of the New Hollywood era."
            ),
            Director(
                name="Greta Gerwig",
                birth_date=date(1983, 8, 4),
                biography="American actress and filmmaker known for her roles in mumblecore films."
            ),
            Director(
                name="Denis Villeneuve",
                birth_date=date(1967, 10, 3),
                biography="Canadian filmmaker known for his atmospheric, visually striking films."
            ),
        ]
        Director.objects.bulk_create(directors)
        
        # Create sample actors
        self.stdout.write('Creating actors...')
        actors = [
            Actor(
                name="Leonardo DiCaprio",
                birth_date=date(1974, 11, 11),
                biography="American actor known for his intense, unconventional roles."
            ),
            Actor(
                name="Meryl Streep",
                birth_date=date(1949, 6, 22),
                biography="American actress often described as the 'best actress of her generation'."
            ),
            Actor(
                name="Tom Hanks",
                birth_date=date(1956, 7, 9),
                biography="American actor and filmmaker, known for both comedic and dramatic roles."
            ),
            Actor(
                name="Viola Davis",
                birth_date=date(1965, 8, 11),
                biography="American actress and producer, known for her powerful performances."
            ),
            Actor(
                name="Timothée Chalamet",
                birth_date=date(1995, 12, 27),
                biography="American actor known for his roles in independent films."
            ),
            Actor(
                name="Saoirse Ronan",
                birth_date=date(1994, 4, 12),
                biography="Irish and American actress known for her roles in period dramas."
            ),
        ]
        Actor.objects.bulk_create(actors)
        
        # Create sample genres
        self.stdout.write('Creating genres...')
        genres = [
            Genre(name="Action", description="Action films emphasize spectacular physical action."),
            Genre(name="Comedy", description="Comedy films are designed to provoke laughter."),
            Genre(name="Drama", description="Drama films are serious in tone, focusing on personal development."),
            Genre(name="Science Fiction", description="Science fiction films deal with imaginative and futuristic concepts."),
            Genre(name="Horror", description="Horror films seek to elicit fear or disgust from the audience."),
            Genre(name="Romance", description="Romance films focus on love and romantic relationships."),
            Genre(name="Thriller", description="Thriller films maintain high levels of suspense and excitement."),
        ]
        Genre.objects.bulk_create(genres)
        
        # Get all created objects
        directors = list(Director.objects.all())
        actors = list(Actor.objects.all())
        genres = list(Genre.objects.all())
        
        # Create sample movies
        self.stdout.write('Creating movies...')
        movies = [
            Movie(
                title="Inception",
                release_date=date(2010, 7, 16),
                plot="A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into someone's mind.",
                runtime=148,
                director=directors[0]  # Christopher Nolan
            ),
            Movie(
                title="Jurassic Park",
                release_date=date(1993, 6, 11),
                plot="A pragmatic paleontologist visiting a theme park is amazed when its cloned dinosaurs are created, but things soon turn dangerous when they escape.",
                runtime=127,
                director=directors[1]  # Steven Spielberg
            ),
            Movie(
                title="Little Women",
                release_date=date(2019, 12, 25),
                plot="The lives of the March sisters as they navigate love, loss, and the pressures of growing up in 19th-century Massachusetts.",
                runtime=135,
                director=directors[2]  # Greta Gerwig
            ),
            Movie(
                title="Dune",
                release_date=date(2021, 10, 22),
                plot="A noble family becomes embroiled in a war for control over the galaxy's most valuable asset while its heir becomes troubled by visions of a dark future.",
                runtime=155,
                director=directors[3]  # Denis Villeneuve
            ),
            Movie(
                title="Interstellar",
                release_date=date(2014, 11, 7),
                plot="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                runtime=169,
                director=directors[0]  # Christopher Nolan
            ),
        ]
        for movie in movies:
            movie.save()
            
            # Add genres to movies
            if movie.title == "Inception":
                movie.genres.add(genres[3], genres[6])  # Sci-Fi, Thriller
            elif movie.title == "Jurassic Park":
                movie.genres.add(genres[0], genres[3])  # Action, Sci-Fi
            elif movie.title == "Little Women":
                movie.genres.add(genres[2], genres[5])  # Drama, Romance
            elif movie.title == "Dune":
                movie.genres.add(genres[0], genres[3])  # Action, Sci-Fi
            elif movie.title == "Interstellar":
                movie.genres.add(genres[2], genres[3])  # Drama, Sci-Fi
        
        # Create MovieActor relationships
        self.stdout.write('Creating movie-actor relationships...')
        movie_actors = [
            # Inception
            MovieActor(movie=movies[0], actor=actors[0], character_name="Dom Cobb", is_lead=True),
            
            # Jurassic Park
            MovieActor(movie=movies[1], actor=actors[2], character_name="Dr. Alan Grant", is_lead=True),
            
            # Little Women
            MovieActor(movie=movies[2], actor=actors[5], character_name="Jo March", is_lead=True),
            MovieActor(movie=movies[2], actor=actors[4], character_name="Laurie", is_lead=False),
            
            # Dune
            MovieActor(movie=movies[3], actor=actors[4], character_name="Paul Atreides", is_lead=True),
            
            # Interstellar
            MovieActor(movie=movies[4], actor=actors[0], character_name="Cooper", is_lead=True),
        ]
        MovieActor.objects.bulk_create(movie_actors)
        
        # Create users
        self.stdout.write('Creating users...')
        users = []
        for i in range(1, 6):
            username = f"user{i}"
            user = User.objects.create_user(
                username=username,
                email=f"{username}@example.com",
                password="password123"
            )
            users.append(user)
            
            # Create user profile
            profile = UserProfile.objects.create(user=user, bio=f"Bio for {username}")
            
            # Add favorite genres
            profile.favorite_genres.add(*random.sample(list(Genre.objects.all()), 2))
        
        # Create ratings
        self.stdout.write('Creating ratings...')
        ratings = []
        for user in users:
            # Each user rates 2-4 random movies
            for movie in random.sample(list(Movie.objects.all()), random.randint(2, 4)):
                rating = Rating(
                    user=user,
                    movie=movie,
                    value=random.randint(1, 10),
                    comment=f"Rating comment from {user.username} for {movie.title}"
                )
                ratings.append(rating)
        
        Rating.objects.bulk_create(ratings)
        
        # Update average ratings
        for movie in Movie.objects.all():
            movie.update_avg_rating()
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
