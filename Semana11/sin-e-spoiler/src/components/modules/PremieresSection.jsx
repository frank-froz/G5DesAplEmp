import { useState } from "react";
import usePremieres from '../../hooks/usePremieres';
import PremieresSlider from "./PremieresSlider";
import { notifyFavorite } from "../../utils/notifyFavorite";
import LoadingSkeleton from "../widgets/LoadingSkeleton";

export default function PremieresSection() {
  const { premieres, loading, error } = usePremieres();
  const [favorites, setFavorites] = useState([]);

  const handleSelect = movie => {
    const added = !favorites.some(f => f.id === movie.id);
    const updated = added
      ? [...favorites, movie]
      : favorites.filter(f => f.id !== movie.id);
    setFavorites(updated);
    notifyFavorite(movie, added);
  };

  if (error) return <p className="text text--lg c-danger">Error loading premieres.</p>;

  return (
    <section id="premieres" className="section">
      <div className="container">
        <h2 className="title c-primary t-align-center">Estrenos 🎉</h2>
        {loading
          ? <LoadingSkeleton count={4} height={250} />
          : <PremieresSlider items={premieres} loading={loading} onSelect={handleSelect} />}
      </div>
    </section>
  );
}
