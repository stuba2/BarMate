import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import * as ingredientActions from "../../redux/ingredients"
import * as recipeActions from "../../redux/recipes"
import './CreateRecipe.css'
import AllRecipeIngredients from "../AllRecipeIngredients/AllRecipeIngredients";

const CreateRecipe = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const { user } = useSelector(state => state.session)
  const recipes = useSelector(state => state.recipes)
  const ingredients = useSelector(state => state.ingredients)
  const backendErr = useSelector(state => state.recipes.Errors)
  const userId = user.id
  const [ name, setName ] = useState('')
  const [ description, setDescription ] = useState('')
  const [ instructions, setInstructions ] = useState('')
  const [ recipeImageUrl, setRecipeImageUrl ] = useState('')
  const [ errors, setErrors ] = useState({})
  const [ hasSubmitted, setHasSubmitted ] = useState(false)
  const [ submitValidity, setSubmitValidity ] = useState(true)

  let num = 1
  const ingredientsArr = Object.values(ingredients).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })
  const recipesArr = Object.values(recipes)

  const [ recipeIngredients, setRecipeIngredients ] = useState([{ingNum: num, ingName: "Jeppson's Malort", ingAmt: 1, ingUnit: 'bottle'}])

  // keeping up with the up to date ing/rec
  useEffect(() => {
    dispatch(ingredientActions.getIngredientsThunk())
    dispatch(recipeActions.getRecipesThunkAll())
  },[dispatch])

  useEffect(() => {
    const errors = {}
    let existingRecipeName = recipesArr.filter((recipe) => (recipe.name) === name)[0]

    if (!name) errors['name'] = 'Cocktail name is required'
    if (name.length > 64) errors['name'] = 'Cocktail name must be 64 characters or less'
    if (existingRecipeName) errors['name'] = 'Recipe already exists with that name'
    if (backendErr && backendErr.name) errors['name'] = backendErr.name
    if (description.length > 1000) errors['description'] = 'Description must be 1000 characters or less'
    if (!instructions) errors['instructions'] = 'Instructions are required'
    if (instructions.length > 2000) errors['description'] = 'Instructions must be 2000 characters or less'
    // for (let ri of recipeIngredients) {
    //   let existingIngName = ingredientsArr.find(ing => ing.name = ri.ingName)
    //   if (!existingIngName) errors['ingredients'] = 'Ingredient names '
    // }
    if (recipeImageUrl.length > 255) errors['description'] = 'Instructions must be 255 characters or less'


    setErrors(errors)
  }, [name, description, instructions, recipeIngredients, backendErr])

  const handleNewRI = async (e) => {
    e.preventDefault()
    let newRI = {
      ingNum: num,
      ingName: "Jeppson's Malort",
      ingAmt: 1,
      ingUnit: 'bottle'
    }
    num += 1
    setRecipeIngredients([...recipeIngredients, newRI])
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setHasSubmitted(true)

    const recipeForm = {
      name: name,
      description: description,
      instructions: instructions,
      user_id: userId
    }

    let createdRecipe
    if (!Object.values(errors).length && submitValidity) {
      createdRecipe = await dispatch(recipeActions.createRecipeThunk(recipeForm))
      .catch(async (res) => {
        // const data = await res.json()
        console.log('create res: ', res)
        if (res && res.Errors) {
          console.log('res errors: ', res.Errors)
        }
      })

      if (createdRecipe && createdRecipe.Errors) setErrors(createdRecipe.Errors)

      if (createdRecipe && createdRecipe.id) {
        let rIForm
        for (let rIObj of recipeIngredients) {
          let matchedIng = ingredientsArr.find(ing => ing.name === rIObj.ingName)
          rIForm = {
            amount: +rIObj.ingAmt,
            unit: rIObj.ingUnit,
            ingredient_id: matchedIng.id,
            recipe_id: createdRecipe.id
          }
          dispatch(recipeActions.addRecipeIngredientsThunk(rIForm))
        }

        let imageForm = {
          recipe_id: createdRecipe.id,
          url: recipeImageUrl
        }

        dispatch(recipeActions.addRecipeImageThunk(createdRecipe.id, imageForm))
      }
      navigate(`/recipes/${createdRecipe.id}`)
    }
  }

  if (!ingredients) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div className="create-rec-container">
        <div>create a recipe</div>

        <form onSubmit={handleSubmit}>

          <label className="create-rec-name">
            <div className="create-rec-name-name-val">
              <div className="create-rec-name-name">Name</div>
              <div className="validation-error">
                {hasSubmitted && errors.name && `*${errors.name}`}
              </div>
            </div>

            <input
              type="text"
              className="create-rec-name-input"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
              maxLength='64'
              minLength='1'
              placeholder="Name"
            />
          </label>

          <label className="create-rec-description">
            <div className="create-rec-description-name-val">
              <div className="create-rec-description-name">description</div>
              <div className="validation-error">
                {hasSubmitted && errors.description && `*${errors.description}`}
              </div>
            </div>

            <textarea
              type="text"
              className="create-rec-description-input"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              maxLength='1000'
              placeholder="Write a description (optional)"
            />
          </label>

          <label className="create-rec-ingredients">
            <div className="create-rec-ingredients-name-val">
              <div className="create-rec-ingredients-name">ingredients</div>
              <div className="validation-error">
                {hasSubmitted && errors.recipeIngredient && `*${errors.recipeIngredient}`}
              </div>
              <div>
                <AllRecipeIngredients recipeIngredients={recipeIngredients} setRecipeIngredients={setRecipeIngredients} handleNewRI={handleNewRI} ingredientsArr={ingredientsArr} setSubmitValidity={setSubmitValidity} hasSubmitted={hasSubmitted}/>
              </div>
            </div>

          </label>

          <label className="create-rec-instructions">
            <div className="create-rec-instructions-name-val">
              <div className="create-rec-instructions-name">instructions</div>
              <div className="validation-error">
                {hasSubmitted && errors.instructions && `*${errors.instructions}`}
              </div>
            </div>

            <textarea
              type="text"
              className="create-rec-instructions-input"
              value={instructions}
              onChange={(e) => setInstructions(e.target.value)}
              maxLength='2000'
              required
              placeholder="Recipe instructions..."
            />
          </label>

          <label>
            <div>
              <div>Recipe Image</div>
              <input
                value={recipeImageUrl}
                onChange={(e) => setRecipeImageUrl(e.target.value)}
                maxLength={'255'}
                placeholder="Image URL"
              />
            </div>
          </label>

          <div className="create-rec-submit-container">
            <button className="create-rec-submit-button">Create new drink!</button>
          </div>

        </form>
      </div>
    );
  }
}

export default CreateRecipe;
