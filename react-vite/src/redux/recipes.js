import {GET_RECIPES, GET_A_RECIPE, GET_USER_RECIPES, POST_RECIPE, EDIT_RECIPE, DELETE_RECIPE} from './actionTypes'

const getRecipes = (data) => {
  return {
    type: GET_RECIPES,
    payload: data
  }
}

const createRecipe = (data) => {
  return {
    type: POST_RECIPE,
    payload: data
  }
}

const editRecipe = (data) => {
  return {
    type: EDIT_RECIPE,
    payload: data
  }
}

const deleteRecipe = (data) => {
  return {
    type: DELETE_RECIPE,
    payload: data
  }
}

export const getRecipesThunk = (page) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/index/${+page}`)

    const data = await response.json()
    dispatch(getRecipes(data))
  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

export const getRecipesThunkAll = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/`)

    const data = await response.json()
    dispatch(getRecipes(data))
  } catch (error) {
    // console.log('error: ', error)
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

    if (response.ok) {
      const data = await response.json()
      dispatch(createRecipe(data))
      return data
    }
    if (!response.ok) {
      const err = await response.json()
      dispatch({
        type: 'ERROR',
        payload: err
      })
    }


  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

export const addRecipeIngredientsThunk = (RIObj) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipe_ingredients/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(RIObj)
    })

    const data = await response.json()

  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

export const editRecipeThunk = (recipeId, recipeForm) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/${recipeId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(recipeForm)
    })

    const data = await response.json()
    dispatch(editRecipe(data))
    return data
  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

export const editRecipeIngredientsThunk = (rIId, rIObj) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipe_ingredients/${+rIId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(rIObj)
    })

    const data = await response.json()
  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

export const deleteRecipeThunk = (recipeId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/${recipeId}`, {
      method: "DELETE"
    })

    const data = await response.json()
    dispatch(deleteRecipe(recipeId))
  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

export const addRecipeImageThunk = (recipeId, imgForm) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/${+recipeId}/image`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(imgForm)
    })

    const data = await response.json()
  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

export const editRecipeImageThunk = (recipeId, imgForm) => async (dispatch ) => {
  try {
    const response = await fetch(`/api/recipes/${recipeId}/image`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(imgForm)
    })

    const data = await response.json()
  } catch (error) {
    // console.log('error: ', error)
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
    case POST_RECIPE:
      newState = {...state}
      const newRecipe = action.payload
      newState[newRecipe.id] = newRecipe
      return newState
    case EDIT_RECIPE:
      newState = {...state}
      const recipe = action.payload
      newState[recipe.id] = recipe
      return newState
    case DELETE_RECIPE:
      newState = {...state}
      const recipeId = action.payload
      delete newState[recipeId]
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

export default recipeReducer
