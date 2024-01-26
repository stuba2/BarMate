import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import * as reviewActions from "../../redux/reviews"
// import './CreateCommentComponent.css'

const CreateReview = ({ recipeId }) => {
  const dispatch = useDispatch()
  const { user } = useSelector(state => state.session)
  const [ reviewText, setReviewText ] = useState('')
  const [ numStars, setNumStars ] = useState()
  const [ isStar1Clicked, setIsStar1Clicked ] = useState(false)
  const [ isStar2Clicked, setIsStar2Clicked ] = useState(false)
  const [ isStar3Clicked, setIsStar3Clicked ] = useState(false)
  const [ isStar4Clicked, setIsStar4Clicked ] = useState(false)
  const [ isStar5Clicked, setIsStar5Clicked ] = useState(false)
  const [ validationErrors, setValidationErrors ] = useState({})
  const [ selected, setSelected ] = useState(false)
  const [ textValidity, setTextValidity ] = useState(false)
  const [ starsValidity, setStarsValidity ] = useState(false)
  const [ validity, setValidity ] = useState(true)

  // const initials = `${user.first_name[0]}${user.last_name[0]}`

console.log('validity: ', validity)
console.log('selected: ', selected)
  useEffect(() => {
    if (reviewText.length < 1001 && numStars > 0) setValidity(true)
    else setValidity(false)
  }, [reviewText])

  useEffect(() => {
    const errors = {}

    if (reviewText.length >= 1001) {
      errors.review_text = 'Comment must be 1000 characters or less'
      setValidity(false)
    }
    setValidationErrors(errors)

  }, [reviewText])

  let buttonClass
  if (!selected) {
    buttonClass = "create-review-save-hidden"
  }
  if (selected) {
    buttonClass = "create-review-save"
  }
  if (selected && reviewText && numStars > 0) {
    buttonClass = "create-review-save-enabled"
  }
  if (validationErrors.review_text) {
    buttonClass = "create-review-save"
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    const reviewForm = {
      review_text: reviewText,
      rating: numStars,
      user_id: user.id,
      recipe_id: +recipeId
    }

    if (!Object.values(validationErrors).length) {
      dispatch(reviewActions.createReviewThunk(reviewForm, recipeId))
    }


    setReviewText('')
    setIsStar1Clicked(false)
    setIsStar2Clicked(false)
    setIsStar3Clicked(false)
    setIsStar4Clicked(false)
    setIsStar5Clicked(false)
    setSelected(false)
  }

  const reviewLengthErrorClass = 'review-length-error' + ((reviewText.length < 1001) ? '' : '-error')


  const star1ClassName = (isStar1Clicked ? 'fa-solid fa-star' : 'fa-regular fa-star')
  const star2ClassName = (isStar2Clicked ? 'fa-solid fa-star' : 'fa-regular fa-star')
  const star3ClassName = (isStar3Clicked ? 'fa-solid fa-star' : 'fa-regular fa-star')
  const star4ClassName = (isStar4Clicked ? 'fa-solid fa-star' : 'fa-regular fa-star')
  const star5ClassName = (isStar5Clicked ? 'fa-solid fa-star' : 'fa-regular fa-star')


  return (
    <div className="create-review-container">

      <form onSubmit={handleSubmit} className="create-review-form">
        <div className="create-review-form">
          <div className="create-review-text-container">
            <textarea
              id= "review-text"
              className="create-review-text"
              type="text"
              onChange={e => setReviewText(e.target.value)}
              onClick={() => setSelected(true)}
              value={reviewText}
              placeholder="Write a review..."
            />
          </div>


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

          <div className="button-validation-combo">
            <div className={reviewLengthErrorClass}>Comment must be 1000 characters or less</div>
            <button className={buttonClass} disabled={!validity ? true : false}>Save</button>
          </div>

        </div>
      </form>

    </div>
  )
}

export default CreateReview
