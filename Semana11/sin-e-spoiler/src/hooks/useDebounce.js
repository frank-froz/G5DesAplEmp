import { useState, useEffect } from "react";

const useDebounce = (value, delay = 300) => {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const id = setTimeout(() => {
      setDebounced(value);
    }, delay);

    return () => {
      clearTimeout(id);
    };
  }, [value, delay]);

  return debounced;
};

export default useDebounce;