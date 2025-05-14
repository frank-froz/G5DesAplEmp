// App.jsx - Main application component
import React, { useState } from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import MovieList from './components/MovieList';
import Footer from './components/Footer';
import { getMovies } from './data/movies';
import GenreFilter from './components/GenreFilter';
import FeaturedMovie from './components/FeaturedMovie';
import './css/index.css';

const App = () => {
  // Get movies from our data file
  const movies = getMovies();


  // Extraer géneros únicos para el filtro
  const genres = Array.from(new Set(movies.map(movie => movie.genre)));

  // Estado para el género activo
  const [activeGenre, setActiveGenre] = useState(null);

  // Manejar cambio de género
  const handleGenreChange = genre => {
    setActiveGenre(genre === activeGenre ? null : genre); // toggle para quitar filtro
  };

  // Filtrar películas según género activo
  const filteredMovies = activeGenre
    ? movies.filter(movie => movie.genre === activeGenre)
    : movies;

  // Tomar la primera película filtrada como destacada
  const featuredMovie = filteredMovies[0] || null;

  return (
    <div>
      <Header />
      <main className="main">
        <Hero />
        <GenreFilter genres={genres} activeGenre={activeGenre} onGenreChange={handleGenreChange} />
        {featuredMovie && <FeaturedMovie movie={featuredMovie} />}
        <MovieList movies={filteredMovies} />
      </main>
      <Footer />
    </div>
  );
};

export default App;
