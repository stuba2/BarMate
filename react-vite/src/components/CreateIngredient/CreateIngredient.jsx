import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import * as ingredientActions from "../../redux/ingredients"

const CreateIngredient = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const ingredients = useSelector(state => state.ingredients)
  const [ name, setName ] = useState('')
  // const [ url, setUrl ] = useState('')
  const [errors, setErrors] = useState({});
  const [ hasSubmitted, setHasSubmitted ] = useState(false)

  useEffect(() => {
    const errors = {}

    if (!name) errors['name'] = 'Ingredient name is required'
    if (name.length > 64) errors['name'] = 'Ingredient name must be 64 characters or less'

    setErrors(errors)
  },[name])

  useEffect(() => {
    dispatch(ingredientActions.getIngredientsThunk())
  }, [dispatch])

  const handleSubmit = async (e) => {
    e.preventDefault()
    setHasSubmitted(true)
    let createdIngredient

    const newIngredient = {
      name: name
    }

    if (!(Object.values(errors).length)) {
      createdIngredient = await dispatch(ingredientActions.postIngredientThunk(newIngredient))
    }
    // navigate somewhere (may be dependent on where this is rendered)

    // const newIngredientImage = {
    //   ingredient_id: +createdIngredient.id,
    //   url
    // }
    // console.log(createdIngredient, createdIngredient.id)

    // if (createdIngredient) {
    //   dispatch(ingredientActions.postIngredientImageThunk(newIngredientImage, createdIngredient.id))
    //   navigate('/ingredients')
    // }
    // // send new ing obj to thunk
  }

  return (
    <div className="create-ing-container">
      <div>create an ingredient</div>

      <form onSubmit={handleSubmit}>
        <div className="create-ing-name">
          <div className="create-ing-name-val">
            <label className="create-ing-name-name">Name</label>
            <div className="validation-error">
              {hasSubmitted && errors.name && `*${errors.name}`}
            </div>
          </div>

          <input
            type="text"
            className="create-ing-name-input"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            placeholder="Name"
          />
        </div>
        {/* <div>
          <label>Image URL</label>
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Image URL"
          />
        </div> */}
        <button>Submit</button>
      </form>
    </div>
  )

}

export default CreateIngredient
