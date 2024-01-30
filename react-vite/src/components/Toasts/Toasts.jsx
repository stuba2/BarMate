import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import * as toastActions from "../../redux/toasts"
import './Toasts.css'

const Toasts = ({  }) => {
  const dispatch = useDispatch()
  const { recipeId } = useParams()
  const { user } = useSelector(state => state.session)
  const toasts = useSelector(state => state.toasts)


  useEffect(() => {
    dispatch(toastActions.getToastsThunk(+recipeId))
  }, [dispatch])

  let numToasts = Object.keys(toasts).length

  let toastsArr = Object.values(toasts)
  let toast = toastsArr.find(obj => obj.user_id === user.id)

  const handleToast = () => {
    const toastObj = {
      user_id: user.id,
      recipe_id: recipeId
    }

    if (!toast) {
        dispatch(toastActions.postToastThunk(recipeId, toastObj))
        numToasts++
    }else {
        dispatch(toastActions.deleteToastThunk(recipeId, toast.id))
        numToasts--
      }
  }


  if (!toasts) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <>
      <div>
        <div>
          <button className="toast-button" onClick={handleToast}><i className="fa-solid fa-champagne-glasses"></i> {numToasts}</button>
        </div>
      </div>
      </>
    );
  }
}

export default Toasts;
