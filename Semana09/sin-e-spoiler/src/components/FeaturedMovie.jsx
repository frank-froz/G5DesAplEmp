import React from 'react';

const FeaturedMovie = ({ movie }) => {
  return (
    <div className="featured-movie">
      <div className="featured-movie__backdrop">
        <img src={movie.backdrop} alt={movie.title} />
      </div>
      <div className="featured-movie__content">
        <h2>{movie.title}</h2>
        <p>{movie.description}</p>
        <button className="btn btn--large">Book Now</button>
      </div>
    </div>
  );
};

export default FeaturedMovie;
