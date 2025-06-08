import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import LoginPage from './pages/LoginPage'
import HomePage from './pages/HomPage'
import CategoryPage from './pages/CategoryPage'
import SeriePage from './pages/SeriePage'
import SerieFormPage from './pages/SerieFormPage'
import CategoryFormPage from './pages/category/CategoryFormPage'
import CategoryEditFormPage from './pages/category/CategoryEditFormPage'

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element ={<LoginPage />} />
        <Route path='/home' element ={< HomePage />} />
        <Route path='/categories' element ={< CategoryPage />} />
        <Route path='/categories/new' element ={< CategoryFormPage />} />
        <Route path='/categories/edit/:id' element ={< CategoryEditFormPage />} />
        <Route path='/series' element ={< SeriePage />} />
        <Route path='/series/new' element ={< SerieFormPage />} />
        <Route path='/series/edit/:idserie' element ={< SerieFormPage />} />
      </Routes>
        
    </BrowserRouter>
  )
}

export default App
