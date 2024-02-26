import { RANDOM_RECIPE } from "./actionTypes";

const getRandomRecipe = (data) => {
  return {
    type: RANDOM_RECIPE,
    payload: data
  }
}

export const getRandomRecipeThunk = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/random`)

    const data = await response.json()
    dispatch(getRandomRecipe(data))
    return data
  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

const initialState = {}

const randRecReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case RANDOM_RECIPE:
      newState = {...state}
      const randRec = action.payload.Recipe
      randRec.map((recipeObj) => newState[recipeObj.id] = recipeObj)
      return newState
    default:
      return state
  }
}

export default randRecReducer
