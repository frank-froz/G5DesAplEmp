import React from 'react';

const GenreFilter = ({ genres, activeGenre, onGenreChange }) => {
  return (
    <div className="genre-filter">
      {genres.map(genre => (
        <button
          key={genre}
          className={`btn ${activeGenre === genre ? 'btn--active' : ''}`}
          onClick={() => onGenreChange(genre)}
        >
          {genre}
        </button>
      ))}
    </div>
  );
};

export default GenreFilter;
