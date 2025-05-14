// components/Rating.jsx - Star rating display
import React from 'react';

const Rating = ({ value, maxValue = 5 }) => {
  const fullStars = Math.floor(value);
  const hasHalfStar = value % 1 !== 0;
  const emptyStars = maxValue - Math.ceil(value);
  
  return (
    <div className="rating d-flex a-items-center g-1">
      {/* Full stars */}
      {[...Array(fullStars)].map((_, index) => (
        <span key={`full-${index}`} className="rating__star c-warning">★</span>
      ))}
      
      {/* Half star */}
      {hasHalfStar && (
        <span className="rating__star rating__star--half c-warning">★</span>
      )}
      
      {/* Empty stars */}
      {[...Array(emptyStars)].map((_, index) => (
        <span key={`empty-${index}`} className="rating__star rating__star--empty">☆</span>
      ))}
      
      <span className="rating__value">{value.toFixed(1)}</span>
    </div>
  );
};

export default Rating;
