import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
// import { Navigate, useNavigate } from "react-router-dom";
import * as ingredientActions from "../../redux/ingredients"

const CreateIngredient = () => {
  const dispatch = useDispatch()
  const ingredients = useSelector((state) => state.ingredients)
  const [ name, setName ] = useState('')
  const [ url, setUrl ] = useState('')

  useEffect(() => {
    dispatch(ingredientActions.getIngredientsThunk())
  }, [dispatch])

  const handleSubmit = async (e) => {
    e.preventDefault()
    let createdIngredient

    const newIngredient = {
      name: name
    }


    createdIngredient = dispatch(ingredientActions.postIngredientThunk(newIngredient))

    const newIngredientImage = {
      ingredient_id: +createdIngredient.id,
      url
    }

    if (createdIngredient) dispatch(ingredientActions.po)
    // send new ing obj to thunk
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            placeholder="Name"
          />
        </div>
        <div>
          <label>Image URL</label>
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Image URL"
          />
        </div>
        <button>Submit</button>
      </form>
    </div>
  )

}

export default CreateIngredient
