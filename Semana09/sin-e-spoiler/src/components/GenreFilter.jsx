import React from 'react';

const GenreFilter = ({ genres, activeGenre, onGenreChange }) => {
  return (
    <div className='container'>
      <div className="card__body">
        <div className="genre-filter">
          {genres.map(genre => (
            <button
              key={genre}
              className={`button btn ${activeGenre === genre ? 'btn--active' : ''}`}
              onClick={() => onGenreChange(genre)}
            >
              {genre}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default GenreFilter;
