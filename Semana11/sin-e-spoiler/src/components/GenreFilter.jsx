import React from 'react';
import Button from './widgets/Button';

const GenreFilter = ({ genres, activeGenre, onGenreChange }) => {
  return (
    <div className='container'>
      <div className="card__body">
        <div className="genre-filter" style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
          {genres.map(genre => (
            <Button
              key={genre}
              text={genre}
              variant={activeGenre === genre ? 'primary' : 'outline-primary'}
              onClick={() => onGenreChange(genre)}
              ariaLabel={`Filter movies by genre ${genre}`}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default GenreFilter;
