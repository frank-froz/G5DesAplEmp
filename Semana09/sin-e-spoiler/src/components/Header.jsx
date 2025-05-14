// components/Header.jsx - Navigation header
import React from 'react';

const Header = () => {
  return (
    <header className="header">
      <nav className="nav container">
        <div className="nav__wrapper d-flex a-items-center j-content-between">
          <a href="/" className="nav__logo">
            <h1 className="nav__title c-primary">Sin E Spoiler 🎬</h1>
          </a>
          
          <ul className="list list--menu d-flex g-4">
            <li className="list__item">
              <a href="#movies" className="nav__link c-white">Movies</a>
            </li>
            <li className="list__item">
              <a href="#coming-soon" className="nav__link c-white">Coming Soon</a>
            </li>
            <li className="list__item">
              <a href="#promotions" className="nav__link c-white">Promotions</a>
            </li>
            <li className="list__item">
              <a href="#contact" className="nav__link c-white">Contact</a>
            </li>
          </ul>
        </div>
      </nav>
    </header>
  );
};

export default Header;
