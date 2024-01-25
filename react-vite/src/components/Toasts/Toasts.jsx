import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import * as toastActions from "../../redux/toasts"

const hourArr = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

const Toasts = () => {
  const dispatch = useDispatch()
  // const reviews = useSelector((state) => state.reviews)
  const { recipeId } = useParams()
  const { user } = useSelector(state => state.session)
  const toasts = useSelector(state => state.toasts)

  let numToasts = Object.keys(toasts).length



  useEffect(() => {
    dispatch(toastActions.getToastsThunk(+recipeId))
  }, [dispatch])

  if (!toasts) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <>
      <div>
        <div><i class="fa-solid fa-champagne-glasses"></i> {numToasts}</div>
      </div>
      </>
    );
  }
}

export default Toasts;
