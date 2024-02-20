import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import * as ingredientActions from "../../redux/ingredients"
import * as recipeActions from "../../redux/recipes"
import './CreateRecipe.css'
import AllRecipeIngredients from "../AllRecipeIngredients/AllRecipeIngredients";
import CreateIngredient from "../CreateIngredient/CreateIngredient";

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
  const [ submitValidity, setSubmitValidity ] = useState(false)
  const [ rIErrors, setRIErrors ] = useState([])

  let num = 1
  const ingredientsArr = Object.values(ingredients).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })
  const recipesArr = Object.values(recipes)

  const [ recipeIngredients, setRecipeIngredients ] = useState([{ingNum: num, ingName: 'none', ingAmt: 1, ingUnit: 'none'}])

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
    if (instructions.length > 2000) errors['instructions'] = 'Instructions must be 2000 characters or less'
    if (recipeImageUrl.length > 255) errors['instructions'] = 'Instructions must be 255 characters or less'
    if (rIErrors.length) errors['recipeIngredient'] = 'Please fill out all fields'
    if (recipeImageUrl.length > 255) errors['recipeImage'] = 'Image URL must be 255 characters or less'

    if (!Object.values(errors).length) setSubmitValidity(true)
    setErrors(errors)
  }, [name, description, instructions, recipeIngredients, backendErr, rIErrors])

  const handleNewRI = async (e) => {
    e.preventDefault()
    let newRI = {
      ingNum: num,
      ingName: 'none',
      ingAmt: 1,
      ingUnit: 'none'
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
            ingredient_id: matchedIng? matchedIng.id : undefined,
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

  const submitButtonClass = submitValidity ? 'create-rec-submit-button' : 'create-rec-submit-button-disabled'


  if (!ingredients) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div className="create-rec-super-container">
        <div className="create-rec-lesser-container">

          <div className="create-rec-header">Create a Recipe</div>

          <form className="create-rec-form" onSubmit={handleSubmit}>

            <label className="create-rec-name">
              <div className="create-rec-name-name">Name</div>

              <div className="create-rec-name-input-val">
                <input
                  type="text"
                  className="create-rec-name-input"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  // required
                  maxLength='64'
                  minLength='1'
                  placeholder="Name"
                />

                <div className="validation-error">
                  {hasSubmitted && errors.name && `*${errors.name}`}
                </div>

              </div>
            </label>

            <label className="create-rec-description">
              <div className="create-rec-description-name">Description</div>

              <div className="create-rec-description-input-val">
                <textarea
                  type="text"
                  className="create-rec-description-input"
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  maxLength='1000'
                  placeholder="Write a description (optional)"
                />

                <div className="validation-error">
                  {hasSubmitted && errors.description && `*${errors.description}`}
                </div>

              </div>
            </label>

            <label className="create-rec-ingredients">
              <div className="create-rec-ingredients-name-val">
                <div className="create-rec-ingredients-name">Ingredients</div>
                <div>
                  <AllRecipeIngredients
                    recipeIngredients={recipeIngredients}
                    handleNewRI={handleNewRI}
                    ingredientsArr={ingredientsArr}
                    hasSubmitted={hasSubmitted}
                    errors={errors}
                    setErrors={setErrors}
                    rIErrors={rIErrors}
                    setRIErrors={setRIErrors}
                  />
                </div>
              </div>
            </label>

            <label className="create-rec-instructions">
              <div className="create-rec-instructions-name">Instructions</div>

              <div className="create-rec-instructions-input-val">
                <textarea
                  type="text"
                  className="create-rec-instructions-input"
                  value={instructions}
                  onChange={(e) => setInstructions(e.target.value)}
                  maxLength='2000'
                  // required
                  placeholder="Recipe instructions..."
                />

                <div className="validation-error">
                  {hasSubmitted && errors.instructions && `*${errors.instructions}`}
                </div>

              </div>
            </label>

            <label className="create-rec-rec-image">
              <div className="create-rec-rec-image-name">Recipe Image</div>

              <div className="create-rec-rec-image-input-val">
                <input
                  className="create-rec-rec-image-input"
                  value={recipeImageUrl}
                  onChange={(e) => setRecipeImageUrl(e.target.value)}
                  maxLength={'255'}
                  placeholder="Image URL"
                />

                <div className="validation-error">
                  {hasSubmitted && errors.recipeImage && `*${errors.recipeImage}`}
                </div>

              </div>
            </label>

            <div className="create-rec-submit-container">
              <button className={submitButtonClass} disabled={submitValidity ? false : true}>Create new drink!</button>
            </div>

          </form>
        </div>

        <CreateIngredient />
      </div>
    );
  }
}

export default CreateRecipe;
