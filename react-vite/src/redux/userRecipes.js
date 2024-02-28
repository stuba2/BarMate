import {GET_USER_RECIPES} from './actionTypes'


const getUsersRecipes = (data) => {
  return {
    type: GET_USER_RECIPES,
    payload: data
  }
}

export const getUsersRecipesThunk = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/user`)

    const data = await response.json()
    dispatch(getUsersRecipes(data))
  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

const initialState = {}

const userRecipeReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case GET_USER_RECIPES:
      newState = {}
      const UsersRecipesArr = action.payload.Recipes
      UsersRecipesArr.map((recipeObj) => newState[recipeObj.id] = recipeObj)
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

export default userRecipeReducer
