    import { useEffect, useState } from "react";
    import { useParams, useNavigate } from "react-router-dom";
    import HeaderComponent from "../components/HeaderComponent";
    import axios from "axios";

    const initData = {
    cod: '',
    nom: '',
    cat: '',  // guardará el id de la categoría
    img: null, // para almacenar el archivo de imagen seleccionado
    };

    function SerieFormPage() {
    const { idserie } = useParams();
    const navigate = useNavigate();

    const [data, setData] = useState(initData);
    const [categories, setCategories] = useState([]);

    // Cargar categorías al montar el componente
    useEffect(() => {
        async function fetchCategories() {
        try {
            const resp = await axios.get('http://localhost:8000/series/api/v1/categories/');
            setCategories(resp.data);
        } catch (error) {
            console.error('Error al cargar categorías:', error);
        }
        }
        fetchCategories();
    }, []);

    // Si hay idserie, cargar datos para edición
    useEffect(() => {
        if (idserie) {
        async function fetchSerie() {
            try {
            const resp = await axios.get(`http://localhost:8000/series/api/v1/series/${idserie}/`);
            setData({
                cod: resp.data.cod,
                nom: resp.data.nom,
                cat: resp.data.cat, // ID de la categoría
                img: null,          // Imagen nueva se selecciona aparte
            });
            } catch (error) {
            console.error('Error al cargar serie:', error);
            }
        }
        fetchSerie();
        }
    }, [idserie]);

    // Manejo de cambios en inputs
    const onChangeNombre = (e) => setData({ ...data, nom: e.target.value });
    const onChangeCod = (e) => setData({ ...data, cod: e.target.value });
    const onChangeCategoria = (e) => setData({ ...data, cat: e.target.value });
    const onChangeImage = (e) => {
        if (e.target.files.length > 0) {
        setData({ ...data, img: e.target.files[0] });
        }
    };

    // Enviar formulario
    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append('cod', data.cod);
        formData.append('nom', data.nom);
        formData.append('cat', data.cat);
        if (data.img) {
        formData.append('img', data.img);
        }

        try {
        if (idserie) {
            // Actualizar serie existente
            await axios.put(`http://localhost:8000/series/api/v1/series/${idserie}/`, formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
            });
        } else {
            // Crear nueva serie
            await axios.post('http://localhost:8000/series/api/v1/series/', formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
            });
        }
        navigate('/series'); // Redirigir tras guardar
        } catch (error) {
        console.error('Error guardando la serie:', error);
        }
    };

    return (
        <>
        <HeaderComponent />
        <div className="container mt-3">
            <div className="border-bottom pb-3 mb-3">
            <h3>{idserie ? 'Editar Serie' : 'Nueva Serie'}</h3>
            </div>
            <form onSubmit={handleSubmit} className="row">
            <div className="col-md-4">
                <img
                className="card-img-top"
                src={data.img ? URL.createObjectURL(data.img) : "https://dummyimage.com/400x250/000/fff"}
                alt="Serie"
                />
            </div>
            <div className="col-md-8">
                <div className="mb-3">
                <label htmlFor="inputCod" className="form-label">Código</label>
                <input
                    type="number"
                    className="form-control"
                    id="inputCod"
                    value={data.cod}
                    onChange={onChangeCod}
                    required
                />
                </div>
                <div className="mb-3">
                <label htmlFor="inputName" className="form-label">Nombre</label>
                <input
                    type="text"
                    className="form-control"
                    id="inputName"
                    value={data.nom}
                    onChange={onChangeNombre}
                    required
                />
                </div>
                <div className="mb-3">
                <label htmlFor="inputCategory" className="form-label">Categoría</label>
                <select
                    id="inputCategory"
                    className="form-select"
                    value={data.cat}
                    onChange={onChangeCategoria}
                    required
                >
                    <option value="">Seleccione una opción</option>
                    {categories.map(cat => (
                    <option key={cat.id} value={cat.id}>{cat.nombre}</option>
                    ))}
                </select>
                </div>
                <div className="mb-3">
                <label htmlFor="inputImage" className="form-label">Imagen</label>
                <input
                    type="file"
                    className="form-control"
                    id="inputImage"
                    onChange={onChangeImage}
                />
                </div>
                <div className="mb-3">
                <button className="btn btn-primary">{idserie ? 'Actualizar' : 'Guardar'}</button>
                </div>
            </div>
            </form>
        </div>
        </>
    );
    }

    export default SerieFormPage;
