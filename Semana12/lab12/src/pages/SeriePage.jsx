import { useEffect, useState } from "react";
import axios from "axios";
import HeaderComponent from "../components/HeaderComponent";
import SerieComponent from "../components/SerieComponent";

function SeriePage() {
  const [series, setSeries] = useState([]);
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const [seriesResp, categoriesResp] = await Promise.all([
          axios.get('http://localhost:8000/series/api/v1/series/'),
          axios.get('http://localhost:8000/series/api/v1/categories/'),
        ]);
        setSeries(seriesResp.data);
        setCategories(categoriesResp.data);
      } catch (error) {
        console.error('Error al cargar datos:', error);
      }
    }
    fetchData();
  }, []);

  return (
    <>
      <HeaderComponent />
      <div className="container mt-3">
        <div className="d-flex justify-content-between border-bottom pb-3 mb-3">
          <h3>Series</h3>
          <div>
            <a className="btn btn-primary" href="/series/new">Nuevo</a>
          </div>
        </div>
        <div className="row">
          {series.map((serie) => {
            // Buscamos el nombre de la categoría en base al id
            const categoriaNombre = categories.find(c => c.id === serie.cat)?.nombre || "Sin categoría";

            return (
              <div key={serie.cod} className="col-md-3 mb-3">
                <SerieComponent
                  codigo={serie.cod}
                  nombre={serie.nom}
                  categoria={categoriaNombre}
                  imagen={serie.img}
                />
              </div>
            );
          })}
        </div>
      </div>
    </>
  );
}

export default SeriePage;
