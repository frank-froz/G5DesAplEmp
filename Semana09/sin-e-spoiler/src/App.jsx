// App.jsx - Main application component
import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import MovieList from './components/MovieList';
import Footer from './components/Footer';
import './css/index.css';

const App = () => {
  // Sample movie data for week 9
  const movies = [
    {
      id: 1,
      title: "Interstellar",
      rating: 4.5,
      genre: "Sci-Fi",
      duration: "169 min",
      image: "https://via.placeholder.com/300x450/234B96/FEFEFE?text=Interstellar",
      description: "A team of explorers travel through a wormhole in space.",
      showTimes: ["2:30 PM", "5:45 PM", "9:00 PM"]
    },
    {
      id: 2,
      title: "Inception",
      rating: 4.8,
      genre: "Thriller",
      duration: "148 min",
      image: "https://via.placeholder.com/300x450/23B5E8/FEFEFE?text=Inception",
      description: "A skilled thief enters people's dreams to steal secrets.",
      showTimes: ["1:00 PM", "4:15 PM", "7:30 PM", "10:45 PM"]
    },
    {
      id: 3,
      title: "The Matrix",
      rating: 4.7,
      genre: "Action",
      duration: "136 min",
      image: "https://via.placeholder.com/300x450/23B58B/FEFEFE?text=Matrix",
      description: "A computer hacker learns about the true nature of reality.",
      showTimes: ["3:00 PM", "6:15 PM", "9:30 PM"]
    }
  ];

  return (
    <div className="app">
      <Header />
      <main className="main">
        <Hero />
        <MovieList movies={movies} />
      </main>
      <Footer />
    </div>
  );
};

export default App;
