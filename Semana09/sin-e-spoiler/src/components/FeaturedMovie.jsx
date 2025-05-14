import React from 'react';

const FeaturedMovie = ({ movie }) => {
  return (
    <div className="featured-movie">
      <div className="featured-movie__content">
        <button className="btn btn--large">Book Now</button>
      </div>
    </div>
  );
};

export default FeaturedMovie;
