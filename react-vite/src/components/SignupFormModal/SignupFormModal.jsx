import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import "./SignupForm.css";

function SignupFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [dob, setDob] = useState()
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      return setErrors({
        confirmPassword:
          "Confirm Password field must be the same as the Password field",
      });
    }

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
  };

  return (
    <div className="signup-modal-container">
      <h1 className="signup-h1">Sign Up</h1>
      {errors.server && <p>{errors.server}</p>}
      <form onSubmit={handleSubmit} className="signup-form">
        <label className="signup-email">
          <div>Email</div>
          <input
            type="text"
            className="signup-email-input"
            placeholder="email@example.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        {errors.email && <p>{errors.email}</p>}
        <label className="signup-username">
          <div>Username</div>
          <input
            type="text"
            className="signup-username-input"
            placeholder="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
        {errors.username && <p>{errors.username}</p>}
        <label className="signup-dob">
          <div>Date of Birth</div>
          <input
            type="date"
            className="signup-dob-input"
            value={dob}
            onChange={(e) => setDob(e.target.value)}
            required
          />
        </label>
        {errors.dob && <p>{errors.dob}</p>}
        <label className="signup-password">
          <div>Password</div>
          <input
            type="password"
            className="signup-password-input"
            placeholder="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        {errors.password && <p>{errors.password}</p>}
        <label className="signup-confirm-password">
          <div>Confirm Password</div>
          <input
            type="password"
            className="signup-confirm-password-input"
            placeholder="confirm password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </label>
        {errors.confirmPassword && <p>{errors.confirmPassword}</p>}
        <div className="signup-button-container"><button type="submit" className="signup-button">Sign Up</button></div>
      </form>
    </div>
  );
}

export default SignupFormModal;
