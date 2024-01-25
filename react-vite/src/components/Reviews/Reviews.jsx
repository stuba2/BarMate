import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import * as reviewActions from "../../redux/reviews"
import Toasts from "../Toasts/Toasts";

const hourArr = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

const Reviews = () => {
  const dispatch = useDispatch()
  const reviews = useSelector((state) => state.reviews)
  const { recipeId } = useParams()
  const { user } = useSelector(state => state.session)

  const reviewsArr = Object.values(reviews)
  console.log('reviewsArr: ', reviewsArr)




  useEffect(() => {
    dispatch(reviewActions.getReviewsThunk(+recipeId))
  }, [dispatch])

  if (!reviews) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <>
      <div>
        <div>{reviewsArr.map((review) => {
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

          return (
            <div>
              <div>{review.reviewer_details.username}</div>
              <div>{review.review_text}</div>
              <div><i class="fa-solid fa-star"></i> {review.rating}</div>
              <div>{dateMonth} {dateDate} at {postedHour}:{postedMinute} {meridiem}</div>

            </div>
          )
        })}</div>
      </div>
      </>
    );
  }
}

export default Reviews;
