import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import * as barActions from "../../redux/bars"
import './EditBarButton.css'

const EditBarButton = ({ ingredient, ingBool }) => {
  const dispatch = useDispatch()
  const { user } = useSelector(state => state.session)
  const ing = useSelector(state => state.bar[ingredient.id])
  const [ isSelected, setIsSelected ] = useState()
  const [ isLoaded, setIsLoaded ] = useState(false)
  const [ buttonClassName, setButtonClassName ] = useState(ingBool ? 'ing-in-bar' : 'ing-out-bar')


  useEffect(() => {
    if (ing) setButtonClassName('ing-in-bar')
    if (!ing) setButtonClassName('ing-out-bar')
    setIsLoaded(true)
  }, [ing])


  const handleAddIng = () => {
    setButtonClassName('ing-in-bar')
    let retIngObj = {
      ingredient_id: isSelected,
      user_id: user.id
    }
    dispatch(barActions.postBarThunk(retIngObj))
  }

  const handleRemoveIng = () => {
    setButtonClassName('ing-out-bar')
    dispatch(barActions.deleteBarThunk(isSelected))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    const ingInBar = ing

    if (!ingInBar) handleAddIng(isSelected)
    if (ingInBar) handleRemoveIng(isSelected)
  }

  if (!isLoaded) {
    return null
  }
  return (
    <div>
      <form action="" onSubmit={handleSubmit} key={ingredient.id}>
        <button className={buttonClassName} id={ingredient.name} onClick={() =>{
          setIsSelected(ingredient.id)
          }}>
          {ingredient.name}
        </button>
      </form>
    </div>
  )
}

export default EditBarButton
