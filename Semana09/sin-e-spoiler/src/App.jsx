// App.jsx - Main application component
import React, { useState } from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import MovieList from './components/MovieList';
import Footer from './components/Footer';
import { getMovies } from './data/movies';
import GenreFilter from './components/GenreFilter';
import './css/index.css';

const App = () => {
  // Get movies from our data file
  const movies = getMovies();

const genres = ["All", ...Array.from(new Set(movies.map(movie => movie.genre)))];
const [activeGenre, setActiveGenre] = useState("All");

const handleGenreChange = genre => {
  setActiveGenre(genre);
};

const filteredMovies = activeGenre === "All"
  ? movies
  : movies.filter(movie => movie.genre === activeGenre);



  return (
    <div>
      <Header />
      <main className="main">
        <Hero />
        <GenreFilter genres={genres} activeGenre={activeGenre} onGenreChange={handleGenreChange} />
        <MovieList movies={filteredMovies} />
      </main>
      <Footer />
    </div>
  );
};

export default App;
