import MovieCard from "./MovieCard";

const MovieList = ({ movies, favorites = {}, onToggleFavorite }) => {
  return (
    <section className="section section--movies">
      <div className="container">
        <div className="g-layout g-layout--auto-fit-columns g-6">
          {movies.map((movie) => (
            <MovieCard
              key={movie.id}
              movie={movie}
              isFavorite={!!favorites[movie.id]}
              onToggleFavorite={() => onToggleFavorite(movie.id)}
            />
          ))}
        </div>
      </div>
    </section>
  );
};

export default MovieList;
