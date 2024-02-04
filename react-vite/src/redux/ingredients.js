import {GET_INGREDIENTS, GET_AN_INGREDIENT, POST_INGREDIENT, POST_INGREDIENT_IMAGE } from './actionTypes'

const getIngredients = (data) => {
  return {
    type: GET_INGREDIENTS,
    payload: data
  }
}

const postIngredient = (data) => {
  return {
    type: POST_INGREDIENT,
    payload: data
  }
}


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

export const postIngredientThunk = (ingredientObj) => async (dispatch) => {
  try {
    let ingredient = {
      name: ingredientObj.name
    }

    const response = await fetch(`/api/ingredients/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(ingredient)
    })

    const data = await response.json()
    dispatch(postIngredient(data))
    return data

    let ingredientImage = {
      ingredient_id: data.id,
      url: ingredientObj.url
    }
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

export const postIngredientImageThunk = (ingImgObj, id) => async (dispatch) => {
  try {
    const response = await fetch(`/api/ingredients/${id}/image`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(ingImgObj)
    })

    // const thisIngredient = await fetch(`/api/ingredients/${}/`)

    const data = await response.json()
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}


const initialState = {}

const ingredientReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case GET_INGREDIENTS:
      newState = {...state}
      const ingredientArr = action.payload.Ingredients
      ingredientArr.map((ingredientObj) => newState[ingredientObj.id] = ingredientObj)
      return newState
    case POST_INGREDIENT:
      newState = {...state}
      const newIng = action.payload
      newState[newIng.id] = newIng
      return newState
    default:
      return state
  }
}

export default ingredientReducer
