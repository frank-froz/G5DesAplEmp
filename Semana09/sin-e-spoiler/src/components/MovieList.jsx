// components/MovieList.jsx - Movie grid container
import React from 'react';
import MovieCard from './MovieCard';

const MovieList = ({ movies }) => {
  return (
    <section id="movies" className="section section--movies">
      <div className="container">
        <h2 className="section__title c-primary">Now Showing</h2>
        
        <div className="movies__grid">
          {movies.map(movie => (
            <MovieCard key={movie.id} movie={movie} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default MovieList;
