import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate, useParams } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as barActions from "../../redux/bars"

const MyBar = () => {
  const dispatch = useDispatch()
  const userBar = useSelector((state) => state.recipes)


  useEffect(() => {
    dispatch(barActions.getBarThunk())
  }, [dispatch])


  if (!true) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <>
      <div>
        hi
      </div>
      </>
    );
  }
}

export default MyBar;
