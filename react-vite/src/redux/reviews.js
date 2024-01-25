import {GET_REVIEWS, POST_REVIEW, EDIT_REVIEW, DELETE_REVIEW} from './actionTypes'

const getReviews = (data) => {
  return {
    type: GET_REVIEWS,
    payload: data
  }
}

// const getOneRecipe = (data) => {
//   return {
//     type: GET_A_RECIPE,
//     payload: data
//   }
// }

// const createRecipe = (data) => {
//   return {
//     type: POST_RECIPE,
//     payload: data
//   }
// }

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

// export const getRecipesThunkAll = () => async (dispatch) => {
//   try {
//     const response = await fetch(`/api/recipes/`)

//     const data = await response.json()
//     dispatch(getRecipes(data))
//   } catch (error) {
//     console.log('error: ', error)
//     return error
//   }
// }

// export const getOneRecipeThunk = (recipeId) => async (dispatch) => {
//   try {
//     const response = await fetch(`/api/recipes/${+recipeId}`)

//     const data = await response.json()
//     dispatch(getOneRecipe(data))
//   } catch (error) {
//     console.log('error: ', error)
//     return error
//   }
// }

// export const createRecipeThunk = (recipeForm) => async (dispatch) => {
//   try {
//     const response = await fetch(`/api/recipes/`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json"
//       },
//       body: JSON.stringify(recipeForm)
//     })
//     console.log('thunk response: ', response)

//     const data = await response.json()
//     console.log('thunk data: ', data)
//     dispatch(createRecipe(data))
//     return data
//   } catch (error) {
//     console.log('error: ', error)
//     return error
//   }

//     // const response = await fetch(`/api/recipes/`, {
//     //   method: "POST",
//     //   headers: {
//     //     "Content-Type": "application/json"
//     //   },
//     //   body: JSON.stringify(recipeForm)
//     // })
//     // console.log('thunk response: ', response)

//     // if (response.ok) {
//     //   const data = await response.json()
//     //   console.log('thunk data: ', data)
//     //   dispatch(createRecipe(data))
//     //   return data
//     // }
//     // if (!response.ok) {
//     //   // const error = await response.json()
//     //   // return error
//     //   console.log('not ok response: ', response)
//     //   return response
//     // }
// }

// export const addRecipeIngredientsThunk = (RIObj) => async (dispatch) => {
//   console.log('add RI thunk')
//   try {
//     console.log('add RI try')
//     const response = await fetch(`/api/recipe_ingredients/`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json"
//       },
//       body: JSON.stringify(RIObj)
//     })
//     console.log('add RI response: ', response)

//     const data = await response.json()
//     console.log('add RI data: ', data)

//   } catch (error) {
//     console.log('error: ', error)
//     return error
//   }
// }

const initialState = {}

const reviewReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case GET_REVIEWS:
      newState = {...state}
      const reviewsArr = action.payload.Reviews
      reviewsArr.map((reviewObj) => newState[reviewObj.id] = reviewObj)
      return newState
    // case GET_A_RECIPE:
    //   newState = {...state}
    //   const recipeArr = action.payload.Recipe
    //   recipeArr.map((recipeObj) => newState[recipeObj.id] = recipeObj)
    //   return newState
    // case POST_RECIPE:
    //   newState = {...state}
    //   const newRecipe = action.payload
    //   newState[newRecipe.id] = newRecipe
    //   return newState
    default:
      return state
  }
}

export default reviewReducer
