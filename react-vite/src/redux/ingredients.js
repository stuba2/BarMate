import {GET_INGREDIENTS, GET_AN_INGREDIENT, POST_INGREDIENT, POST_INGREDIENT_IMAGE } from './actionTypes'

const getIngredients = (data) => {
  return {
    type: GET_INGREDIENTS,
    payload: data
  }
}

// const getOneRecipe = (data) => {
//   return {
//     type: GET_A_RECIPE,
//     payload: data
//   }
// }x

export const getIngredientsThunk = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/ingredients/`)

    const data = await response.json()
    dispatch(getIngredients(data))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

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

const initialState = {}

const ingredientReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case GET_INGREDIENTS:
      newState = {...state}
      const ingredientArr = action.payload.Ingredients
      ingredientArr.map((ingredientObj) => newState[ingredientObj.id] = ingredientObj)
      return newState
    default:
      return state
  }
}

export default ingredientReducer
