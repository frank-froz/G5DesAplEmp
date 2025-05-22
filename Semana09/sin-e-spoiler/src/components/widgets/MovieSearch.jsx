import { useState, useEffect } from "react";

const MovieSearch = ({ onSearch }) => {
  const [query, setQuery] = useState("");
  const [debouncedQuery, setDebouncedQuery] = useState("");

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedQuery(query);
    }, 300);

    return () => clearTimeout(handler);
  }, [query]);

  useEffect(() => {
    onSearch(debouncedQuery.toLowerCase());
  }, [debouncedQuery, onSearch]);

  return (
    <input
      type="text"
      value={query}
      placeholder="Search movies..."
      className="form__input"
      aria-label="Search movies"
      onChange={(e) => setQuery(e.target.value)}
    />
  );
};

export default MovieSearch;
