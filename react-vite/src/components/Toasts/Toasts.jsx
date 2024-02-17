import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import * as toastActions from "../../redux/toasts"
import './Toasts.css'

const Toasts = ({ recipe }) => {
  const dispatch = useDispatch()
  const { recipeId } = useParams()
  const { user } = useSelector(state => state.session)
  const toasts = useSelector(state => state.toasts)


  useEffect(() => {
    dispatch(toastActions.getToastsThunk(+recipeId))
  }, [dispatch])

  let numToasts = Object.keys(toasts).length

  let toastsArr = Object.values(toasts)
  let toast = toastsArr.find(obj => user ? obj.user_id === user.id : undefined)

  const handleToast = () => {
    if (!user) {
      return
    }
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

  let toastClass
  if (user && recipe && user.id === recipe.user_id) {
    toastClass = 'toast-button hidden'
  } else toastClass = 'toast-button'

  if (!toasts) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <>
      <div>
        <div className="toast-container">
          <button className={toastClass} onClick={handleToast}>Toast it!</button>
          <div><i className="fa-solid fa-champagne-glasses"></i> {numToasts}</div>
        </div>
      </div>
      </>
    );
  }
}

export default Toasts;
