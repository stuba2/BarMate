import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import * as ingredientActions from "../../redux/ingredients"
import './CreateIngredient.css'

const CreateIngredient = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const ingredients = useSelector(state => state.ingredients)
  const [ name, setName ] = useState('')
  // const [ url, setUrl ] = useState('')
  const [errors, setErrors] = useState({});
  const [ hasSubmitted, setHasSubmitted ] = useState(false)

  const ingredientsArr = Object.values(ingredients).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })

  useEffect(() => {
    const errors = {}
    let existingIngName = ingredientsArr.find(ing => ing.name === name)

    if (!name) errors['name'] = 'Ingredient name is required'
    if (name.length > 64) errors['name'] = 'Ingredient name must be 64 characters or less'
    if (existingIngName) errors['name'] = 'Ingredient already exists'

    setErrors(errors)
  },[name])

  useEffect(() => {
    dispatch(ingredientActions.getIngredientsThunk())
  }, [dispatch])

  const handleSubmit = async (e) => {
    e.preventDefault()
    setHasSubmitted(true)
    let createdIngredient

    const capitalizeFirst = (ing) => {
      let ret = []
      const words = ing.split(' ')
      for (let word of words) {
        if (word === 'de' || word === 'of') ret.push(word)
        else ret.push(word.charAt(0).toUpperCase() + word.slice(1))
      }
      return ret.join(' ')
    }

    const newIngredient = {
      name: capitalizeFirst(name)
    }

    if (!(Object.values(errors).length)) {
      createdIngredient = await dispatch(ingredientActions.postIngredientThunk(newIngredient))

      setName('')
      setErrors({})
      setHasSubmitted(false)
    }
  }

  return (
    <div className="create-ing-container">
      <div className="create-ing-header">Don't see an ingredient? Add it!</div>

      <form onSubmit={handleSubmit}>
        <div className="create-ing-name">
          <div className="create-ing-name-val">
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
            minLength='0'
            maxLength='64'
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
        <div className="create-ing-submit-container"><button className="create-ing-submit-button">Create New Ingredient</button></div>
      </form>
    </div>
  )

}

export default CreateIngredient
