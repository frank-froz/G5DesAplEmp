import { useState } from "react";
import Header from "./components/Header";
import Hero from "./components/Hero";
import GenreFilter from "./components/GenreFilter";
import MovieList from "./components/MovieList";
import MovieSearch from "./components/widgets/MovieSearch";
import Footer from "./components/Footer";
import { getMovies } from "./utils/movie.utils";

function App() {
  const movies = getMovies();
  const genres = ["All", ...new Set(movies.map((m) => m.genre))];
  const [activeGenre, setActiveGenre] = useState("All");
  const [favorites, setFavorites] = useState({});
  const [searchQuery, setSearchQuery] = useState("");

  const toggleFavorite = (movieId) => {
    setFavorites((prev) => ({
      ...prev,
      [movieId]: !prev[movieId],
    }));
  };

  const handleSearch = (query) => {
    setSearchQuery(query);
  };
  // cambia el género activo seleccionado en el filtro aña
  const handleGenreChange = (genre) => {
    setActiveGenre(genre);
  };

  const filteredMovies = movies.filter((movie) => {
    const matchesGenre = activeGenre === "All" || movie.genre === activeGenre;
    const matchesSearch = movie.title.toLowerCase().includes(searchQuery);
    return matchesGenre && matchesSearch;
  });

  // Obtiene solo las películas marcadas como favoritas
  const favoriteMovies = movies.filter((movie) => favorites[movie.id]);

  return (
    <>
      <Header />
      <main className="main d-flex f-direction-column g-8">
        <Hero />
        <MovieSearch onSearch={handleSearch} />
        <GenreFilter
          genres={genres}
          activeGenre={activeGenre}
          onGenreChange={handleGenreChange}
        />
        <MovieList
          movies={filteredMovies}
          favorites={favorites}
          onToggleFavorite={toggleFavorite}
        />
        {favoriteMovies.length > 0 && (
          <>
            <h2 className="title c-primary t-align-center m-top-6">
              Your Favorites ❤️
            </h2>
            <MovieList
              movies={favoriteMovies}
              favorites={favorites}
              onToggleFavorite={toggleFavorite}
            />
          </>
        )}
      </main>
      <Footer />
    </>
  );
}

export default App;
