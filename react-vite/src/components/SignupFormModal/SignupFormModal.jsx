import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import "./SignupForm.css";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";

function SignupFormModal() {
  const dispatch = useDispatch();
  const [ email, setEmail ] = useState("");
  const [ username, setUsername ] = useState("");
  const [ dob, setDob ] = useState()
  const [ password, setPassword ] = useState("");
  const [ confirmPassword, setConfirmPassword ] = useState("");
  const [ errors, setErrors ] = useState({});
  const [ hasSubmitted, setHasSubmitted ] = useState(false)
  const { closeModal } = useModal();

  const getAge = (birthdate) => {
    let today = new Date()
    let dob = new Date(new Date(birthdate).getTimezoneOffset()*60000 + new Date(birthdate).getTime())
    let age = today.getFullYear() - dob.getFullYear()
    let month = today.getMonth() - dob.getMonth()
    if (month < 0 || (month === 0 && today.getDate() < dob.getDate())) age--
    if (age < 21) return false
    return true
  }

  useEffect(() => {
    const errors = {}
    if (!(email.includes('@') && email.includes('.'))) errors['email'] = 'Invalid Email'
    if (!email) errors['email'] = 'Email is required'
    if (email.length > 255) errors['email'] = 'Email is too long'
    if (email.length < 8) errors['email'] = 'Email must be at least 8 characters'
    if (!username) errors['username'] = 'Username is required'
    if (username.length > 64) errors['username'] = 'Username is too long'
    if (username.length < 4) errors['username'] = 'Username must be at least 4 characters'
    if (!dob) errors['dob'] = 'Date of birth is required'
    if (!getAge(dob)) errors['dob'] = 'You must be 21 to use this site'
    if (!password) errors['password'] = 'Date of birth is required'
    if (password.length > 255) errors['password'] = 'Password is too long'
    if (!confirmPassword) errors['confirmPassword'] = 'Date of birth is required'
    if (confirmPassword.length > 255) errors['confirmPassword'] = 'Password is too long'
    if (password.length < 8) errors['password'] = 'Password must be at least 8 characters'
    if (password !== confirmPassword) errors['confirmPassword'] = 'Passwords must match'

    setErrors(errors)
  },[email, username, dob, password, confirmPassword])


  const handleSubmit = async (e) => {
    e.preventDefault();
    setHasSubmitted(true)

    if (!(Object.values(errors).length)) {
      const serverResponse = await dispatch(
        thunkSignup({
          email,
          username,
          dob,
          password,
        })
      );

      if (serverResponse) {
        setErrors(serverResponse);
      } else {
        closeModal();
      }
    }
  };

  return (
    <div className="signup-modal-container">
      <h1 className="signup-h1">Sign Up</h1>
      {errors.server && <p>{errors.server}</p>}

      <form onSubmit={handleSubmit} className="signup-form">

        <label className="signup-email">
          <div className="signup-email-name-val">
            <div className="signup-email-name">Email</div>
            <div className="validation-error">
              {hasSubmitted && errors.email && `*${errors.email}`}
            </div>
          </div>

          <input
            type="text"
            className="signup-email-input"
            placeholder="email@example.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            maxLength='255'
            minLength='8'
          />
        </label>

        <label className="signup-username">
          <div className="signup-username-name-val">
            <div className="signup-username-name">Username</div>
            <div className="validation-error">
              {hasSubmitted && errors.username && `*${errors.username}`}
            </div>
          </div>

          <input
            type="text"
            className="signup-username-input"
            placeholder="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            maxLength='64'
            minLength='4'
          />
        </label>

        <label className="signup-dob">
          <div className="signup-dob-name-val">
            <div className="signup-dob-name">Date of Birth</div>
            <div className="validation-error">
              {hasSubmitted && errors.dob && `*${errors.dob}`}
            </div>
          </div>

          <input
            type="date"
            className="signup-dob-input"
            value={dob}
            onChange={(e) => setDob(e.target.value)}
            required
          />
        </label>

        <label className="signup-password">
          <div className="signup-password-name-val">
            <div className="signup-password-name">Password</div>
            <div className="validation-error">
              {hasSubmitted && errors.password && `*${errors.password}`}
            </div>
          </div>

          <input
            type="password"
            className="signup-password-input"
            placeholder="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            maxLength='255'
            minLength='8'
          />
        </label>

        <label className="signup-confirm-password">
          <div className="signup-confirm-password-name-val">
            <div className="signup-confirm-password-name">Confirm Password</div>
            <div className="validation-error">
              {hasSubmitted && errors.confirmPassword && `*${errors.confirmPassword}`}
            </div>
          </div>

          <input
            type="password"
            className="signup-confirm-password-input"
            placeholder="confirm password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
            maxLength='255'
            minLength='8'
          />
        </label>

        <div className="signup-button-container"><button type="submit" className="signup-button">Sign Up</button></div>

        <div className="signup-no-account">Already have an account?
          <OpenModalMenuItem
            itemText='Log in!'
            modalComponent={<LoginFormModal />}
          />
        </div>
      </form>
    </div>
  );
}

export default SignupFormModal;
