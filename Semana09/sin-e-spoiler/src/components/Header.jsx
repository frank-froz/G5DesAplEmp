// components/Header.jsx - Navigation header
const Header = () => {
  return (
    <header className="header">
      <nav className="nav container">
        <div className="nav__wrapper">
          <a href="/" className="nav__logo">
            <h1 className="nav__title">Sin E Spoiler 🎬</h1>
          </a>
          
          <ul className="nav__menu">
            <li className="nav__item">
              <a href="#movies" className="nav__link">Movies</a>
            </li>
            <li className="nav__item">
              <a href="#coming-soon" className="nav__link">Coming Soon</a>
            </li>
            <li className="nav__item">
              <a href="#promotions" className="nav__link">Promotions</a>
            </li>
            <li className="nav__item">
              <a href="#contact" className="nav__link">Contact</a>
            </li>
          </ul>
        </div>
      </nav>
    </header>
  );
};

export default Header;
