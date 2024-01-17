import {GET_RECIPES, GET_A_RECIPE, GET_USER_RECIPES, POST_RECIPE, POST_RECIPE_IMAGE, EDIT_RECIPE, DELETE_RECIPE} from './actionTypes'

const getRecipes = (data) => {
  return {
    type: GET_RECIPES,
    payload: data
  }
}

export const getRecipesThunk = () => async (dispatch) => {
  console.log('in thunk')
  try {
    console.log('in try')
    const response = await fetch(`/api/recipes`)
    console.log('response: ', response)

    const data = await response.json()
    console.log('data: ', data)
    dispatch(getRecipes(data))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

const initialState = {}

const recipeReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case GET_RECIPES:
      newState = {...state}
      const recipeArr = action.payload.Recipes
      recipeArr.map((recipeObj) => newState[recipeObj.id] = recipeObj)
      return newState
    default:
      return state
  }
}

export default recipeReducer
