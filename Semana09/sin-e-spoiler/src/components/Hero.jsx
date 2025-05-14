// components/Hero.jsx - Hero section with featured content
const Hero = () => {
  return (
    <section className="hero">
      <div className="container">
        <h1 className="hero__title">
          Watch Without Spoilers
        </h1>
        <p className="hero__paragraph">
          Experience movies the way they're meant to be seen. 
          AI-powered reviews that preserve the magic.
        </p>
        
        <div className="hero__cta">
          <button className="button button--primary">
            Browse Movies
          </button>
          <button className="button">
            Coming Soon
          </button>
        </div>
      </div>
    </section>
  );
};

export default Hero;

