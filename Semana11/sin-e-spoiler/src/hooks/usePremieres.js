import { useState, useEffect, useRef } from "react";
import { tmdbNowPlayingMock } from "../data/movies.data";

const usePremieres = (delay = 500) => {
  const [premieres, setPremieres] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const timerRef = useRef();

  useEffect(() => {
    setLoading(true);

    timerRef.current = setTimeout(() => {
      try {
        setPremieres(tmdbNowPlayingMock.results.slice(0, 10));
      } catch (e) {
        setError(e);
      } finally {
        setLoading(false);
      }
    }, delay);

    return () => {
      clearTimeout(timerRef.current);
    };
  }, [delay]);

  return { premieres, loading, error };
};

export default usePremieres;
