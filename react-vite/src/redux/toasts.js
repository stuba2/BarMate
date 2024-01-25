import { GET_TOASTS, POST_TOASTS, DELETE_TOASTS } from './actionTypes'

const getToasts = (data) => {
  return {
    type: GET_TOASTS,
    payload: data
  }
}


export const getToastsThunk = (recipeId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/${+recipeId}/toasts`)

    const data = await response.json()
    dispatch(getToasts(data))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

const initialState = {}

const toastReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case GET_TOASTS:
      newState = {...state}
      const toastsArr = action.payload.Toasts
      toastsArr.map((toastObj) => newState[toastObj.id] = toastObj)
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

export default toastReducer
