import { useEffect } from "react"
import { useParams } from "react-router-dom"
import HeaderComponent from "../components/HeaderComponent"

function SerieFormPage(){
    const series = [
        {cod:1, nom:"Friends", cat:"Comedy", img:"friends.png"},
        {cod:2, nom:"Law & Order", cat:"Drama", img:"law-and-order.png"},
        {cod:3, nom: "The Big Bang Theory", cat:"Comedy", img:"the-big-bang-theory.png"},
        {cod:4, nom:"Stranger Things", cat:"Horror", img:"stranger-things.png"},
        {cod:5, nom:"Dr. House", cat:"Drama", img:"dr-house.png"},
        {cod:6, nom:"The X-Files", cat: "Drama", img:"the-x-files.png"},
    ];
    const { idserie } = useParams();
    const setDataForm = (codigo) => {
        for (const item of series) {
            if(item.cod==codigo){
            console.log(item);
                document.getElementById('inputName').value = item.nom;
                document.getElementById('inputCategory').value = item.cat;
                document.getElementById('fileImg').src= "https://dummyimage.com/400x250/000/fff&text="+item.img
                break;
            }
        }
    }    
    useEffect(()=> { 
        setDataForm(idserie);
    },[]);
    return (
        <>
            <HeaderComponent />
            <div className="container mt-3">
                <div className="border-bottom pb-3 mb-3">
                    <h3>Nuevo - Serie</h3>
                </div>
                <form className="row">
                    <div className="col-md-4">
                        <img 
                            id="fileImg"
                            className="card-img-top" 
                            src={"https://dummyimage.com/400x250/000/fff"} 
                            alt="img" />
                    </div>
                    <div className="col-md-8">
                        <div className="mb-3">
                            <label htmlFor="inputName" className="form-label">Nombre</label>
                            <input type="text" className="form-control" id="inputName" required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="inputCategory" className="form-label">Categoria</label>
                            <select className="form-select" id="inputCategory" required >
                                <option value="">Seleccione una opción</option>
                                <option value="Horror">Horror</option>
                                <option value="Comedy">Comedy</option>
                                <option value="Action">Action</option>
                                <option value="Drama">Drama</option>
                            </select>
                        </div>
                        <div className="mb-3">
                            <label htmlFor="inputImage" className="form-label">Imagen</label>
                            <input type="file" className="form-control" id="inputImage" required />
                        </div>
                        <div className="mb-3">
                            <button className="btn btn-primary">Guardar</button>
                        </div>
                    </div>
                </form>
            </div>
        </>
    )
}


export default SerieFormPage
