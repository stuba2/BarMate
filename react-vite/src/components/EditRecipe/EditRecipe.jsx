import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate, useParams, useHistory } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as recipeActions from "../../redux/recipes"

const EditRecipe = () => {
  const dispatch = useDispatch()
  const { recipeId } = useParams()
  const history = useHistory()
  const { recipes } = useSelector((state) => state.recipes)
  const { user } = useSelector((state) => state.session)
  const [ name, setName ] = useState('')
  const [ description, setDescription ] = useState('')
  const [ instructions, setInstructions ] = useState('')
  const [ validationErrors, setValidationErrors ] = useState({})

  const recipe = recipes[+recipeId]

  useEffect(() => {
    dispatch(recipeActions.getRecipesThunk())
  }, [dispatch])

  


  const handleSubmit = async (e) => {
    e.preventDefault()

    const recipeForm = {
      name: name,
      description: description,
      instructions: instructions,
      user_id: user.id
    }
    if (!Object.values(validationErrors)) {
      dispatch(recipeActions)
    }
  }

  let recipesArr = Object.values(recipes)


  if (!recipes) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div>
        <div>create a recipe</div>
        <form onSubmit={handleSubmit}>
          <div>Name</div>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            maxLength='64'
            minLength='1'
            placeholder="Name"
          />
          <div>description</div>
          <textarea
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            maxLength='1000'
            placeholder="Write a description (optional)"
          />
          <div>instructions</div>
          <textarea
            type="text"
            value={instructions}
            onChange={(e) => setInstructions(e.target.value)}
            maxLength='2000'
            required
            placeholder="Recipe instructions..."
          />
          <div>
            <button>Create new drink!</button>
          </div>
        </form>
      </div>
    );
  }
}

export default EditRecipe;
