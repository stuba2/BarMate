import {GET_REVIEWS, POST_REVIEW, EDIT_REVIEW, DELETE_REVIEW} from './actionTypes'

const getReviews = (data) => {
  return {
    type: GET_REVIEWS,
    payload: data
  }
}

const createReview = (data) => {
  return {
    type: POST_REVIEW,
    payload: data
  }
}

const editReview = (data) => {
  return {
    type: EDIT_REVIEW,
    payload: data
  }
}

export const getReviewsThunk = (recipeId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/reviews/${+recipeId}/reviews`)

    const data = await response.json()
    dispatch(getReviews(data))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

export const createReviewThunk = (reviewForm, recipeId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/${recipeId}/reviews`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(reviewForm)
    })

    const data = await response.json()
    dispatch(createReview(data))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

export const editReviewThunk = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/${recipeId}/reviews/${reviewId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(reviewForm)
    })

    const data = response.json()
    dispatch(editReview(data))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}


const initialState = {}

const reviewReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case GET_REVIEWS:
      newState = {...state}
      const reviewsArr = action.payload.Reviews
      reviewsArr.map((reviewObj) => newState[reviewObj.id] = reviewObj)
      return newState
    case POST_REVIEW:
      newState = {...state}
      const newReview = action.payload
      newState[newReview.id] = newReview
      return newState
    case EDIT_REVIEW:
      newState = {...state}
      const review = action.payload
      newState[review.id] = review
      return newState
    default:
      return state
  }
}

export default reviewReducer
