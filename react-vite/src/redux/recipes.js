import {GET_RECIPES, GET_A_RECIPE, GET_USER_RECIPES, POST_RECIPE, POST_RECIPE_IMAGE, EDIT_RECIPE, DELETE_RECIPE, RANDOM_RECIPE} from './actionTypes'

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

const getRandomRecipe = (data) => {
  return {
    type: RANDOM_RECIPE,
    payload: data
  }
}

const createRecipe = (data) => {
  return {
    type: POST_RECIPE,
    payload: data
  }
}

const getUsersRecipes = (data) => {
  return {
    type: GET_USER_RECIPES,
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
    console.log('error: ', error)
    return error
  }
}

export const getRecipesThunkAll = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/`)

    const data = await response.json()
    dispatch(getRecipes(data))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

export const getUsersRecipesTHunk = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/user`)

    const data = await response.json()
    dispatch(getUsersRecipes(data))
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
    return data
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

export const getRandomRecipeThunk = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/random`)

    const data = await response.json()
    dispatch(getRandomRecipe(data))
    return data
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
    console.log('thunk response: ', response)

    const data = await response.json()
    console.log('thunk data: ', data)
    dispatch(createRecipe(data))
    return data
  } catch (error) {
    console.log('error: ', error)
    return error
  }

    // const response = await fetch(`/api/recipes/`, {
    //   method: "POST",
    //   headers: {
    //     "Content-Type": "application/json"
    //   },
    //   body: JSON.stringify(recipeForm)
    // })
    // console.log('thunk response: ', response)

    // if (response.ok) {
    //   const data = await response.json()
    //   console.log('thunk data: ', data)
    //   dispatch(createRecipe(data))
    //   return data
    // }
    // if (!response.ok) {
    //   // const error = await response.json()
    //   // return error
    //   console.log('not ok response: ', response)
    //   return response
    // }
}

export const addRecipeIngredientsThunk = (RIObj) => async (dispatch) => {
  console.log('add RI thunk')
  try {
    console.log('add RI try')
    const response = await fetch(`/api/recipe_ingredients/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(RIObj)
    })
    console.log('add RI response: ', response)

    const data = await response.json()
    console.log('add RI data: ', data)

  } catch (error) {
    console.log('error: ', error)
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
    console.log('error: ', error)
    return error
  }
}

export const editRecipeIngredientsThunk = (rIId, rIObj) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipe_ingredients/${rIId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(rIObj)
    })
    console.log('RI response: ', response)

    const data = await response.json()
    console.log('RI data: ', data)
  } catch (error) {
    console.log('error: ', error)
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
    case EDIT_RECIPE:
      newState = {...state}
      const recipe = action.payload
      newState[recipe.id] = recipe
      return newState
    case GET_USER_RECIPES:
      newState = {...state}
      const UsersRecipesArr = action.payload.Recipes
      UsersRecipesArr.map((recipeObj) => newState[recipeObj.id] = recipeObj)
      return newState
    case RANDOM_RECIPE:
      newState = {...state}
      const randRec = action.payload.Recipe
      randRec.map((recipeObj) => newState[recipeObj.id] = recipeObj)
      return newState
    case DELETE_RECIPE:
      newState = {...state}
      const recipeId = action.payload
      delete newState[recipeId]
      return newState
    default:
      return state
  }
}

export default recipeReducer
