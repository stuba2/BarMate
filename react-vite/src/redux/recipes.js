import {GET_RECIPES, GET_A_RECIPE, GET_USER_RECIPES, POST_RECIPE, POST_RECIPE_IMAGE, EDIT_RECIPE, DELETE_RECIPE} from './actionTypes'

const getRecipes = (data) => {
  return {
    type: GET_RECIPES,
    payload: data
  }
}

const getOneRecipe = (data) => {
  return {
    type: GET_A_RECIPE,
    payload: data
  }
}

const createRecipe = (data) => {
  return {
    type: POST_RECIPE,
    payload: data
  }
}

export const getRecipesThunk = (page) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/index/${+page}`)

    const data = await response.json()
    dispatch(getRecipes(data))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

export const getOneRecipeThunk = (recipeId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/${+recipeId}`)

    const data = await response.json()
    dispatch(getOneRecipe(data))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

export const createRecipeThunk = (recipeForm) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(recipeForm)
    })

    const data = await response.json()
    dispatch(createRecipe(data))
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
      const recipesArr = action.payload.Recipes
      recipesArr.map((recipeObj) => newState[recipeObj.id] = recipeObj)
      return newState
    case GET_A_RECIPE:
      newState = {...state}
      const recipeArr = action.payload.Recipe
      recipeArr.map((recipeObj) => newState[recipeObj.id] = recipeObj)
      return newState
    case POST_RECIPE:
      newState = {...state}
      const newRecipe = action.payload
      newState[newRecipe.id] = newRecipe
      return newState
    default:
      return state
  }
}

export default recipeReducer
