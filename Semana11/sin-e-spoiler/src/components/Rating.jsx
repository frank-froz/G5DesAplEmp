// components/Rating.jsx - Star rating display
const Rating = ({ value, maxValue = 5 }) => {
  const fullStars = Math.floor(value);
  const hasHalfStar = value % 1 !== 0;
  const emptyStars = maxValue - Math.ceil(value);
  
  return (
    <div className="rating">
      {/* Full stars */}
      {[...Array(fullStars)].map((_, index) => (
        <span key={`full-${index}`} className="rating__star">★</span>
      ))}
      
      {/* Half star */}
      {hasHalfStar && (
        <span className="rating__star rating__star--half">★</span>
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
