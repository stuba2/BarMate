import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as recipeActions from "../../redux/recipes"

const CreateRecipe = () => {
  const dispatch = useDispatch()
  const recipes = useSelector((state) => state.recipes)
  const { user } = useSelector((state) => state.session)
  const userId = user.id
  const [ name, setName ] = useState('')
  const [ description, setDescription ] = useState('')
  const [ instructions, setInstructions ] = useState('')
  const [ validationErrors, setValidationErrors ] = useState({})


  const handleSubmit = async (e) => {
    e.preventDefault()

    const recipeForm = {
      name: name,
      description: description,
      instructions: instructions,
      user_id: userId
    }
    // if (!Object.values(validationErrors))
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
        <form onSubmit={handleSubmit}></form>
      </div>
    );
  }
}

export default CreateRecipe;
