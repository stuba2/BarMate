import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import * as reviewActions from "../../redux/reviews"
import EditReview from "../EditReview/EditReview";
import DeleteReview from "../DeleteReview/DeleteReview";
import './Reviews.css'

const hourArr = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

const Reviews = () => {
  const dispatch = useDispatch()
  const reviews = useSelector(state => state.reviews)
  const { recipeId } = useParams()
  const { user } = useSelector(state => state.session)
  const [ isBeingEdited, setIsBeingEdited ] = useState(false)
  const [ focusedReviewId, setFocusedReviewId ] = useState()
  const [ isBeingDeleted, setIsBeingDeleted ] = useState(false)

  const reviewsArr = Object.values(reviews).reverse()




  useEffect(() => {
    dispatch(reviewActions.getReviewsThunk(+recipeId))
  }, [dispatch])

  if (!reviews) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div className="review-super-container">
        <div className="rev-lesser-container">{reviewsArr.map((review) => {
          let updatedDateSplit = new Date(review.updated_at).toDateString().split(' ')
          let updatedTimeSplit = new Date(review.updated_at).toTimeString().split(' ')
          let dateMonth = updatedDateSplit[1]
          let dateDate = updatedDateSplit[2]
          let timeTimeSplit = updatedTimeSplit[0].split(':')
          let timeHour = timeTimeSplit[0]
          let postedHour
          let meridiem
          if (timeHour < 12) {
            postedHour = hourArr[+timeHour]
            meridiem = 'AM'
          } else {
            postedHour = hourArr[+timeHour - 12]
            meridiem = 'PM'
          }
          let postedMinute = timeTimeSplit[1]

          let editDeleteButtonClass
          let deleteButtonClass

          if (user && review.user_id !== user.id) {
            editDeleteButtonClass = 'review-edit-delete-hidden'
          } else {
            editDeleteButtonClass = 'review-edit-delete'
          }

          if (isBeingDeleted) {
            deleteButtonClass = 'review-delete-shown'
          } else {
            deleteButtonClass = 'review-delete-hidden'
          }

          if (isBeingEdited && focusedReviewId === review.id) {
            return <EditReview key={review.id} reviewId={review.id} setIsBeingEdited={setIsBeingEdited} recipeId={recipeId}/>
          } else if (isBeingDeleted && focusedReviewId === review.id) {
            return (
              // if review is being deleted
              <div className="rev-container">

                <div className="rev-name-time">
                  <div className="review-username">{review.reviewer_details.username}</div>
                  <div className="review-timestamp">{dateMonth} {dateDate} at {postedHour}:{postedMinute} {meridiem}</div>
                </div>

                <div className="review-text">{review.review_text}</div>

                <div className="review-rating-edit-delete">
                  <div className="review-rating"><i className="fa-solid fa-star"></i> {review.rating}</div>
                  <div className={editDeleteButtonClass}>
                    <div>
                      <button className="review-edit" onClick={() => {
                        setIsBeingEdited(true)
                        setFocusedReviewId(review.id)
                      }}>Edit</button>
                    </div>
                    <div className="review-dot">·</div>
                    <div>
                    <button className='review-delete' onClick={() => {
                        setIsBeingDeleted(true)
                        setFocusedReviewId(review.id)
                      }}>Delete</button>
                      <div className='review-delete-shown'>
                        <DeleteReview reviewId={review.id} setIsBeingDeleted={setIsBeingDeleted} recipeId={recipeId}/>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
            )
          } else {
            return (
              // standard review setup
              <div className="rev-container">

                <div className="rev-name-time">
                  <div className="review-username">{review.reviewer_details.username}</div>
                  <div className="review-timestamp">{dateMonth} {dateDate} at {postedHour}:{postedMinute} {meridiem}</div>
                </div>

                <div className="review-text">{review.review_text}</div>

                <div className="review-rating-edit-delete">
                  <div className="review-rating"><i className="fa-solid fa-star"></i> {review.rating}</div>
                  <div className={editDeleteButtonClass}>
                    <div>
                      <button className="review-edit" onClick={() => {
                        setIsBeingEdited(true)
                        setFocusedReviewId(review.id)
                      }}>Edit</button>
                    </div>
                    <div className="review-dot">·</div>
                    <div>
                    <button className='review-delete' onClick={() => {
                        setIsBeingDeleted(true)
                        setFocusedReviewId(review.id)
                      }}>Delete</button>
                      <div className='review-delete-hidden'>
                        <DeleteReview reviewId={review.id} setIsBeingDeleted={setIsBeingDeleted} recipeId={recipeId}/>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
            )
          }
        })}</div>
        </div>
    );
  }
}

export default Reviews;
