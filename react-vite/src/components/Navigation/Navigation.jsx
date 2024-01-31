import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import { useSelector } from "react-redux";

function Navigation() {
  const { user } = useSelector(state => state.session)

  let newRecClass
  let navLinkClass
  if (!user) {
    newRecClass = 'nav-create hidden'
    navLinkClass = 'nav-link-special hidden'
  } else {
    newRecClass = 'nav-create'
    navLinkClass = 'nav-link-special'
  }

  return (
    <ul className="navigation-container">
      <div className="nav-left">
        <NavLink  to="/"><img className="nav-logo" src="../../../wholeLogoCropped2.jpg"/></NavLink>
        <div><NavLink to="/recipes/index/1" className="nav-link">Cocktails</NavLink></div>
        <div><NavLink to="/recipes/makable" className="nav-link">What Can You Make?</NavLink></div>
        <div><NavLink to="/account/myBar" className="nav-link">My Bar</NavLink></div>
        <div><NavLink to='/account/myCocktails' className="nav-link">My Cocktails</NavLink></div>
      </div>

      <div className="nav-right">
        <div className={newRecClass}><NavLink to={`/recipes/new`} className={navLinkClass}>Create a Cocktail</NavLink></div>
        <ProfileButton />
      </div>
    </ul>
  );
}

export default Navigation;
