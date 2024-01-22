import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <ul className="navigation-container">
      <div className="nav-left">
        <img className="nav-logo" src="../../../dist/assets/wholeLogoCropped2.jpg"/>
        <div><NavLink to="/" className="nav-link">Home</NavLink></div>
        <div><NavLink to="/myBar" className="nav-link">My Bar</NavLink></div>
        <div><NavLink to="/recipes" className="nav-link">Cocktails</NavLink></div>
        <div><NavLink to="/ingredients" className="nav-link">Ingredients</NavLink></div>
      </div>

      <div className="nav-right">
        <ProfileButton />
      </div>
    </ul>
  );
}

export default Navigation;
