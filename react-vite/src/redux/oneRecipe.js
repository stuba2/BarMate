import {GET_A_RECIPE} from './actionTypes'

const getOneRecipe = (data) => {
  return {
    type: GET_A_RECIPE,
    payload: data
  }
}

export const getOneRecipeThunk = (recipeId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/${+recipeId}`)

    const data = await response.json()
    dispatch(getOneRecipe(data))
    return data
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

const initialState = {}

const oneRecipeReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case GET_A_RECIPE:
      newState = {...state}
      const recipeArr = action.payload.Recipe
      recipeArr.map((recipeObj) => newState[recipeObj.id] = recipeObj)
      return newState
    case 'ERROR':
      newState = {}
      const error = action.payload
      newState['Errors'] = error.Errors
      return newState
    default:
      return state
  }
}

export default oneRecipeReducer
