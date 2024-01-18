import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <ul>
      <li><NavLink to="/">Home</NavLink></li>
      <li><NavLink to="/myBar">My Bar</NavLink></li>
      <li><NavLink to="/recipes">Cocktails</NavLink></li>

      <li>
        <ProfileButton />
      </li>
    </ul>
  );
}

export default Navigation;
