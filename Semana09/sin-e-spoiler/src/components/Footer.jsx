// components/Footer.jsx - Footer with cinema information
import React from 'react';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer__content">
          <div className="footer__section">
            <h3 className="footer__title c-primary">Sin E Spoiler</h3>
            <p className="footer__text">
              Your trusted source for spoiler-free movie experiences.
            </p>
          </div>
          
          <div className="footer__section">
            <h4 className="footer__subtitle">Quick Links</h4>
            <ul className="list">
              <li><a href="#movies" className="footer__link">Now Showing</a></li>
              <li><a href="#coming-soon" className="footer__link">Coming Soon</a></li>
              <li><a href="#promotions" className="footer__link">Promotions</a></li>
              <li><a href="#about" className="footer__link">About Us</a></li>
            </ul>
          </div>
          
          <div className="footer__section">
            <h4 className="footer__subtitle">Contact</h4>
            <address className="footer__address">
              <p>📍 123 Cinema Street, Movie City</p>
              <p>📧 info@sinespoiler.com</p>
              <p>📱 (555) 123-4567</p>
            </address>
          </div>
        </div>
        
        <div className="footer__bottom">
          <p className="footer__copyright">
            &copy; {currentYear} Sin E Spoiler. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
