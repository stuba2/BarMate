import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <ul className="navigation-container">
      <div className="nav-left">
        <NavLink  to="/"><img className="nav-logo" src="../../../public/wholeLogoCropped2.jpg"/></NavLink>
        <div><NavLink to="/recipes" className="nav-link">Cocktails</NavLink></div>
        <div><NavLink to="/ingredients" className="nav-link">Ingredients</NavLink></div>
        <div><NavLink to="/account/myBar" className="nav-link">My Bar</NavLink></div>
        <div><NavLink to='/account/myCocktails' className="nav-link">My Cocktails</NavLink></div>
      </div>

      <div className="nav-right">
        <ProfileButton />
      </div>
    </ul>
  );
}

export default Navigation;
