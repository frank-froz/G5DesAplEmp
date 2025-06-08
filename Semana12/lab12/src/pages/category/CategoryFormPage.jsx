import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";
import HeaderComponent from "../../components/HeaderComponent";


const initData = {
    id: '',
    nombre: '',
}


function CategoryFormPage(){
    
    const urlApi = 'http://localhost:8000/series/api/v1/categories/';
    const navigate = useNavigate();
    const [data, setData] = useState(initData);


    const onChangeNombre = (e) => {
        const nData = {...data, nombre: e.target.value}
        setData(nData);
    };


    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post(urlApi, data);
        navigate("/categories");
    };


    return (
        <>
            <HeaderComponent />
            <div className="container mt-3">
                <div className="border-bottom pb-3 mb-3">
                    <h3>Nueva - Categoría</h3>
                </div>
                <form onSubmit={handleSubmit} className="row">
                    <div className="mb-3">
                        <label htmlFor="inputName" className="form-label">Nombre</label>
                        <input type="text" onChange={onChangeNombre} className="form-control" required />
                    </div>
                    <div className="mb-3">
                        <button className="btn btn-primary me-2">Guardar</button>
                        <Link className="btn btn-secondary" to="/categories">Cancelar</Link>
                    </div>
                </form>
            </div>
        </>
    )
}


export default CategoryFormPage
