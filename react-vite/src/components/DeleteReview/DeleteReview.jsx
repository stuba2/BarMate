import { useEffect } from "react";
import { useDispatch } from "react-redux";
import './DeleteReview.css'
import * as reviewActions from "../../redux/reviews"

const DeleteReview = ({reviewId, setIsBeingDeleted, recipeId}) => {
  const dispatch = useDispatch()

  useEffect(() => {

  }, [dispatch])

  const handleDelete = (e) => {
    e.preventDefault()

    dispatch(reviewActions.deleteReviewThunk(reviewId, recipeId))
    setIsBeingDeleted(false)
    // setCounter(+counter+1)
  }

  const handleDiscard = () => {
    setIsBeingDeleted(false)
  }

  return (
    <div className="delete-container">
      <div className="delete-top-row">
        <div></div>
        <h1 className="delete-header">Delete review?</h1>
        <button onClick={handleDiscard} className="delete-x">X</button>
      </div>
      <p className="delete-p">Deleting a review is forever. There is no undo.</p>
      <button onClick={handleDelete} className="delete-button">Delete review</button>
    </div>
  )
}

export default DeleteReview
