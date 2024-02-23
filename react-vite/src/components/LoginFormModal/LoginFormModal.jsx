import { useEffect, useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import SignupFormModal from "../SignupFormModal";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const [ hasSubmitted, setHasSubmitted ] = useState(false)
  const { closeModal } = useModal();

  useEffect(() => {
    const errors = {}

    if (!email) errors['email'] = 'Email is required'
    if (!password) errors['password'] = 'Password is required'

    setErrors(errors)
  },[email, password])

  const handleSubmit = async (e) => {
    e.preventDefault();
    setHasSubmitted(true)

    if (!(Object.values(errors).length)) {
      const serverResponse = await dispatch(
        thunkLogin({
          email,
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

  const handleDemoLogin = async (e) => {
    e.preventDefault()

    const serverResponse = await dispatch(
      thunkLogin({
        email: 'kyle@mooney.io',
        password: 'password',
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  }

  return (
    <div className="login-modal-container">
      <h1 className="login-h1">Log In</h1>

      <form onSubmit={handleSubmit} className="login-form">

          <label className="login-email">
            <input
              type="text"
              className="login-email-input"
              placeholder="email@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />

            <div className="validation-error">
              {hasSubmitted && errors.email && `*${errors.email}`}
            </div>
          </label>


          <label className="login-password">
            <input
              type="password"
              className="login-password-input"
              placeholder="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />

            <div className="validation-error">
              {hasSubmitted && errors.password && `*${errors.password}`}
            </div>
          </label>

        <div className="login-button-container"><button type="submit" className="login-button">Log In</button></div>

        <div className="login-demo-button-container"><button onClick={handleDemoLogin} className="demo-button">Demo Log In</button></div>

        <div className="login-no-account">Don't have an account?
          <OpenModalMenuItem
            itemText='Sign up!'
            modalComponent={<SignupFormModal />}
          />
        </div>
      </form>
    </div>
  );
}

export default LoginFormModal;
