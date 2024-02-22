import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import * as reviewActions from "../../redux/reviews"
import './EditReview.css'

const EditReview = ({reviewId, setIsBeingEdited, recipeId}) => {

  const dispatch = useDispatch()
  const { user } = useSelector(state => state.session)
  const reviews = useSelector(state => state.reviews)
  const [ reviewText, setReviewText ] = useState('')
  const [ numStars, setNumStars ] = useState()
  const [ isStar1Clicked, setIsStar1Clicked ] = useState(false)
  const [ isStar2Clicked, setIsStar2Clicked ] = useState(false)
  const [ isStar3Clicked, setIsStar3Clicked ] = useState(false)
  const [ isStar4Clicked, setIsStar4Clicked ] = useState(false)
  const [ isStar5Clicked, setIsStar5Clicked ] = useState(false)
  const [ validationErrors, setValidationErrors ] = useState({})
  const [ selected, setSelected ] = useState(false)
  const [ validity, setValidity ] = useState(false)


  const review = reviews[+reviewId]

  useEffect(() => {
    setReviewText(review.review_text)
    setNumStars(review.rating)
    if (review.rating === 1) {
      setIsStar1Clicked(true)
      setIsStar2Clicked(false)
      setIsStar3Clicked(false)
      setIsStar4Clicked(false)
      setIsStar5Clicked(false)
    }
    if (review.rating === 2) {
      setIsStar1Clicked(true)
      setIsStar2Clicked(true)
      setIsStar3Clicked(false)
      setIsStar4Clicked(false)
      setIsStar5Clicked(false)
    }
    if (review.rating === 3) {
      setIsStar1Clicked(true)
      setIsStar2Clicked(true)
      setIsStar3Clicked(true)
      setIsStar4Clicked(false)
      setIsStar5Clicked(false)
    }
    if (review.rating === 4) {
      setIsStar1Clicked(true)
      setIsStar2Clicked(true)
      setIsStar3Clicked(true)
      setIsStar4Clicked(true)
      setIsStar5Clicked(false)
    }
    if (review.rating === 5) {
      setIsStar1Clicked(true)
      setIsStar2Clicked(true)
      setIsStar3Clicked(true)
      setIsStar4Clicked(true)
      setIsStar5Clicked(true)
    }
  }, [dispatch])

  useEffect(() => {
    if (reviewText.length < 1001 && numStars > 0) setValidity(true)
    else setValidity(false)
  }, [reviewText])

  useEffect(() => {
    const errors = {}

    if (reviewText.length >= 1001) {
      errors.review = 'Review must be 1000 characters or less'
      setValidity(false)
    }
    if (reviewText.length <= 0) {
      errors.review = 'Review cannot be 0 characters'
      setValidity(false)
    }

    setValidationErrors(errors)

  }, [reviewText])

  let buttonClass
  if (!selected) {
    buttonClass = "create-review-save-enabled"
  }
  if (selected) {
    buttonClass = "create-review-save-enabled"
  }
  if (validationErrors.review) {
    buttonClass = "create-review-save"
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    const reviewForm = {
      id: reviewId,
      review_text: reviewText,
      rating: numStars,
      user_id: user.id,
      recipe_id: +recipeId
    }

    if (!Object.values(validationErrors).length) {
      dispatch(reviewActions.editReviewThunk(recipeId, reviewId, reviewForm))
    }

    setIsBeingEdited(false)
  }

  const handleDiscard = async (e) => {
    e.preventDefault()
    setIsBeingEdited(false)
  }

  const reviewLengthErrorClass = 'review-length-error' + (validity ? '' : '-error')

  const star1ClassName = (isStar1Clicked ? 'fa-solid fa-star' : 'fa-regular fa-star')
  const star2ClassName = (isStar2Clicked ? 'fa-solid fa-star' : 'fa-regular fa-star')
  const star3ClassName = (isStar3Clicked ? 'fa-solid fa-star' : 'fa-regular fa-star')
  const star4ClassName = (isStar4Clicked ? 'fa-solid fa-star' : 'fa-regular fa-star')
  const star5ClassName = (isStar5Clicked ? 'fa-solid fa-star' : 'fa-regular fa-star')


  return (
    // <div className="edit-review-container">

      <form onSubmit={handleSubmit} className="edit-review-form-container">
        <div className="edit-review-form">

          {/* <div className="create-review-text-container"> */}
            <textarea
              id= "review-text"
              className="edit-review-text"
              type="text"
              onChange={e => setReviewText(e.target.value)}
              onClick={() => setSelected(true)}
              value={reviewText}
              placeholder="Write a review..."
            />
          {/* </div> */}

          <div className="post-review-stars">
          <span className="rate">
            <i
              className={star1ClassName}
              onClick={e => {
                setNumStars(1)
                setIsStar1Clicked(true)
                setIsStar2Clicked(false)
                setIsStar3Clicked(false)
                setIsStar4Clicked(false)
                setIsStar5Clicked(false)
              }}
            />
            <i
              className={star2ClassName}
              onClick={e => {
                setNumStars(2)
                setIsStar1Clicked(true)
                setIsStar2Clicked(true)
                setIsStar3Clicked(false)
                setIsStar4Clicked(false)
                setIsStar5Clicked(false)
              }}
            />
            <i
              className={star3ClassName}
              onClick={e => {
                setNumStars(3)
                setIsStar1Clicked(true)
                setIsStar2Clicked(true)
                setIsStar3Clicked(true)
                setIsStar4Clicked(false)
                setIsStar5Clicked(false)
              }}
            />
            <i
              className={star4ClassName}
              onClick={e => {
                setNumStars(4)
                setIsStar1Clicked(true)
                setIsStar2Clicked(true)
                setIsStar3Clicked(true)
                setIsStar4Clicked(true)
                setIsStar5Clicked(false)
              }}
            />
            <i
              className={star5ClassName}
              onClick={e => {
                setNumStars(5)
                setIsStar1Clicked(true)
                setIsStar2Clicked(true)
                setIsStar3Clicked(true)
                setIsStar4Clicked(true)
                setIsStar5Clicked(true)
              }}
            />
          </span> Stars
        </div>

          <div className="edit-button-validation-combo">
            <button className={buttonClass} disabled={!validity ? true : false}>Save</button>
            <button className="edit-review-discard" onClick={handleDiscard}>Discard changes</button>
            {/* <div className={reviewLengthErrorClass}>Review must be 1000 characters or less</div> */}
            <div className="validation-error">{validationErrors.review}</div>
          </div>

        </div>
      </form>

    // </div>
  )
}

export default EditReview
