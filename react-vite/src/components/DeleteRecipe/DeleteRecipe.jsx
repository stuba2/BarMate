import { useDispatch } from "react-redux"
import { useModal } from "../../context/Modal"
import { useNavigate } from "react-router-dom"
import * as recipeActions from '../../redux/recipes'
import './DeleteRecipe.css'

const DeleteRecipe = ({ recipeId }) => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const { closeModal } = useModal()

  const handleDelete = (e) => {
    e.preventDefault()

    dispatch(recipeActions.deleteRecipeThunk(recipeId))
    closeModal()
    navigate('/myCocktails')

  }

  const handleKeep = (e) => {
    closeModal()
  }


  return (
    <div className="delete-rec-container">

        <h4 className="delete-rec-header">Confirm Delete</h4>

      <div className="delete-rec-p-body-container">
        <p className="delete-rec-p-body">Are you sure you want to delete this recipe?</p>
      </div>

      <div className="delete-rec-buttons">
        <div className="delete-rec-delete-container"><button onClick={handleDelete} className="delete-rec-delete-button">Yes (Delete Recipe)</button></div>
        <div className="delete-rec-keep-container"><button onClick={handleKeep} className="delete-rec-keep-button">No (Keep Recipe)</button></div>
      </div>

    </div>
  )
}

export default DeleteRecipe
