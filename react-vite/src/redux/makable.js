import { MAKABLE_RECIPES } from "./actionTypes";

const getMakableRecipes = (data) => {
  return {
    type: MAKABLE_RECIPES,
    payload: data
  }
}

export const getMakableRecipesThunk = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/makable`)

    const data = await response.json()
    dispatch(getMakableRecipes(data))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

const initialState = {}

const makableReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case MAKABLE_RECIPES:
      newState = {}
      const makableRecipesArr = action.payload.ret
      makableRecipesArr.map((obj) => newState[obj.id] = obj)
      return newState
    default:
      return state
  }
}

export default makableReducer
