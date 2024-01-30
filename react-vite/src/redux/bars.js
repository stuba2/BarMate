import { GET_BAR, POST_BAR, EDIT_BAR} from './actionTypes'

const getBar = (data) => {
  return {
    type: GET_BAR,
    payload: data
  }
}

const postBar = (data) => {
  return {
    type: POST_BAR,
    payload: data
  }
}

const deleteBarIng = (data) => {
  return {
    type: EDIT_BAR,
    payload: data
  }
}

export const getBarThunk = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/bars/`)

    const data = await response.json()
    dispatch(getBar(data))
    return data
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

export const postBarThunk = (barIng) => async (dispatch) => {
  try {
    const response = await fetch(`/api/bars/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(barIng)
    })

    const data = await response.json()
    dispatch(postBar(data))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

export const deleteBarThunk = (ingId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/bars/${ingId}`, {
      method: "DELETE"
    })

    const data = await response.json()
    dispatch(deleteBarIng(ingId))
  } catch (error) {
    console.log('error: ', error)
    return error
  }
}

const initialState = {}

const barReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case GET_BAR:
      newState = {...state}
      const barArr = action.payload['Bar Ingredients']
      barArr.map((ingredientObj) => newState[ingredientObj.id] = ingredientObj)
      return newState
    case POST_BAR:
      newState = {...state}
      const newBarIng = action.payload
      newState[newBarIng.id] = newBarIng
      return newState
    case EDIT_BAR:
      newState = {...state}
      const ingId = action.payload
      delete newState[ingId]
      return newState
    default:
      return state
  }
}

export default barReducer
