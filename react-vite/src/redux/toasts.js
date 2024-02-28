import { GET_TOASTS, POST_TOASTS, DELETE_TOASTS } from './actionTypes'

const getToasts = (data) => {
  return {
    type: GET_TOASTS,
    payload: data
  }
}

const postToast = (data) => {
  return {
    type: POST_TOASTS,
    payload: data
  }
}

const deleteToast = (data) => {
  return {
    type: DELETE_TOASTS,
    payload: data
  }
}


export const getToastsThunk = (recipeId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/${+recipeId}/toasts`)

    const data = await response.json()
    dispatch(getToasts(data))
  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

export const postToastThunk = (recipeId, toastObj) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/${recipeId}/toasts`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(toastObj)
    })

    const data = await response.json()
    dispatch(postToast(data))
  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

export const deleteToastThunk = (recipeId, toastId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/recipes/${+recipeId}/toasts`, {
      method: "DELETE"
    })

    const data = await response.json()
    dispatch(deleteToast(+toastId))
  } catch (error) {
    // console.log('error: ', error)
    return error
  }
}

const initialState = {}

const toastReducer = (state = initialState, action) => {
  let newState
  switch (action.type) {
    case GET_TOASTS:
      newState = {...state}
      const toastsArr = action.payload.Toasts
      toastsArr.map((toastObj) => newState[toastObj.id] = toastObj)
      return newState
    case POST_TOASTS:
      newState = {...state}
      const newToast = action.payload
      newState[newToast.id] = newToast
      return newState
    case DELETE_TOASTS:
      newState = {...state}
      const toastId = action.payload
      delete newState[+toastId]
      return newState
    default:
      return state
  }
}

export default toastReducer
