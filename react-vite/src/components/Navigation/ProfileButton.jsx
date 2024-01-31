import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkLogout } from "../../redux/session";
import { useNavigate } from "react-router-dom";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import './ProfileButton.css'

function ProfileButton() {
  const dispatch = useDispatch();
  const navigate = useNavigate()
  const [ showMenu, setShowMenu ] = useState(false);
  const user = useSelector(store => store.session.user);
  const ulRef = useRef();

  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    setShowMenu(!showMenu);
  };

   useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  const logout = (e) => {
    e.preventDefault();
    dispatch(thunkLogout());
    closeMenu();
    navigate('/')
  };

  let loginClass
  let signupClass
  let logoutClass

  if (!user) {
    loginClass = 'profile-login'
    signupClass = 'profile-signup'
    logoutClass = 'profile-logout hidden'
  } else {
    loginClass = 'profile-login hidden'
    signupClass = 'profile-signup hidden'
    logoutClass = 'profile-logout'
  }


  return (
    <>
      <div className="log-sign-container">
        <div className={loginClass}>
          <OpenModalMenuItem
            itemText="Log In"
            onItemClick={closeMenu}
            modalComponent={<LoginFormModal />}
          />
        </div>
        <div className={signupClass}>
          <OpenModalMenuItem
            itemText="Sign Up"
            onItemClick={closeMenu}
            modalComponent={<SignupFormModal />}
          />
        </div>
        <div className={logoutClass}>
          <button onClick={logout} className="profile-logout-button">Log Out</button>
        </div>
      </div>
    </>
  );
}

export default ProfileButton;
