// components/Hero.jsx - Hero section with featured content
import React from 'react';

const Hero = () => {
  return (
    <section className="hero">
      <div className="container">
        <h1 className="hero__title">
          Watch Without Spoilers
        </h1>
        <p className="hero__paragraph c-secondary">
          Experience movies the way they're meant to be seen. 
          AI-powered reviews that preserve the magic.
        </p>
        
        <div className="hero__cta d-flex j-content-center g-4">
          <button className="btn btn--primary">
            Browse Movies
          </button>
          <button className="btn btn--secondary">
            Coming Soon
          </button>
        </div>
      </div>
    </section>
  );
};

export default Hero;
