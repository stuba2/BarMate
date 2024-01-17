import { GET_BAR, POST_BAR, EDIT_BAR} from './actionTypes'

const getBar = (data) => {
  return {
    type: GET_BAR,
    payload: data
  }
}

export const getBarThunk = () => async (dispatch) => {
  try {
    const response = await fetch(`/api/bars`)

    const data = await response.json()
    dispatch(getBar(data))
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
    default:
      return state
  }
}

export default barReducer
