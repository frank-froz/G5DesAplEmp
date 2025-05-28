import { useState } from "react";
import Rating from "./Rating"; // dentro de components
import Button from "./widgets/Button";

const MovieCard = ({ movie, isFavorite = false, onToggleFavorite }) => {
  const { title, rating, genre, duration, image, description, showTimes } = movie;
  const [animating, setAnimating] = useState(false);

  const handleFavoriteClick = () => {
    if (animating) return;
    setAnimating(true);
    onToggleFavorite(movie.id);
    setTimeout(() => setAnimating(false), 500);
  };

  return (
    <article className="card card--movie">
      <div className="card__header p-relative">
        <img
          src={image}
          alt={`${title} poster`}
          className="card__image"
          loading="lazy"
        />

        <span className="badge badge--primary p-absolute t-2 r-2">{genre}</span>

        {/* Aquí va el botón favorito */}
        <button
          aria-label={isFavorite ? `Remove ${title} from favorites` : `Add ${title} to favorites`}
          onClick={handleFavoriteClick}
          className={`favorite-button p-absolute t-2 l-2 ${animating ? "animate" : ""}`}
        >
          {isFavorite ? "❤️" : "🤍"}
        </button>
      </div>

      <div className="card__body d-flex f-direction-column g-2">
        <h3 className="card__title">{title}</h3>
        <div className="d-flex a-items-center g-2">
          <Rating value={rating} />
          <span className="card__duration">{duration}</span>
        </div>
        <p className="card__description">
          {description.length > 150 ? description.slice(0, 147) + "..." : description}
        </p>

        <div className="card__showtimes">
          <h4 className="card__subtitle">Today's Showtimes</h4>
          <div className="d-flex f-wrap g-2">
            {showTimes.map((time, i) => (
              <Button
                key={i}
                text={time}
                variant="outline-primary"
                ariaLabel={`Showtime ${time} for ${title}`}
              />
            ))}
          </div>
        </div>
      </div>
    </article>
  );
};

export default MovieCard;
