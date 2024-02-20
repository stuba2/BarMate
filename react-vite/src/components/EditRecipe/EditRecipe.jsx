import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import * as ingredientActions from "../../redux/ingredients"
import * as recipeActions from "../../redux/recipes"
import './EditRecipe.css'
import AllRecipeIngredients from "../AllRecipeIngredients/AllRecipeIngredients";
import CreateIngredient from "../CreateIngredient/CreateIngredient";

const EditRecipe = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const { recipeId } = useParams()
  const { user } = useSelector(state => state.session)
  const recipes = useSelector(state => state.recipes)
  // const recipe = useSelector(state => state.recipes[recipeId])
  const ingredients = useSelector(state => state.ingredients)
  const backendErr = useSelector(state => state.recipes.Errors)
  const userId = user.id

  // keeping up with the up to date ing/rec
  useEffect(() => {
    dispatch(recipeActions.getOneRecipeThunk(recipeId))
    dispatch(ingredientActions.getIngredientsThunk())
  },[dispatch])

  const ingredientsArr = Object.values(ingredients).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })
  const recipesArr = Object.values(recipes)
  const recipe = recipesArr.find(recipe => recipe.id === +recipeId)

  const [ name, setName ] = useState(recipe ? recipe.name : '')
  const [ description, setDescription ] = useState(recipe ? recipe.description : '')
  const [ instructions, setInstructions ] = useState(recipe ? recipe.instructions : '')
  const [ recipeIngredients, setRecipeIngredients ] = useState([])
  const [ recipeImageUrl, setRecipeImageUrl ] = useState(recipe ? recipe.recipe_image_url : '')
  const [ errors, setErrors ] = useState({})
  const [ hasSubmitted, setHasSubmitted ] = useState(false)
  const [ submitValidity, setSubmitValidity ] = useState(true)
  const [ rIErrors, setRIErrors ] = useState([])


  useEffect(() => {
    if (recipe) setName(recipe.name)
    if (recipe && recipe.description) setDescription(recipe.description)
    if (recipe) setInstructions(recipe.instructions)
    if (recipe && recipe.recipe_image_url) setRecipeImageUrl(recipe.recipe_image_url)
  }, [recipeIngredients])


  let allIngredientsArr = []
  let num = 1
  if (recipe && recipe.recipe_ingredients && recipeIngredients.length < recipe.recipe_ingredients.length) {
    for (let rI of recipe.recipe_ingredients) {
      let existingRI = {
        ingNum: rI.id,
        ingName: rI.name,
        ingAmt: rI.amount,
        ingUnit: rI.unit
      }
      num += 1
      allIngredientsArr.push(existingRI)
    }
    setRecipeIngredients([...allIngredientsArr])
  }

  useEffect(() => {
    const errors = {}
    let existingRecipeName = recipesArr.find((recipe) => (recipe.name) === name)

    if (!name) errors['name'] = 'Cocktail name is required'
    if (name && name.length > 64) errors['name'] = 'Cocktail name must be 64 characters or less'
    if (existingRecipeName && existingRecipeName.id !== recipe.id) errors['name'] = 'Recipe already exists with that name'
    if (description && description.length > 1000) errors['description'] = 'Description must be 1000 characters or less'
    if (!instructions) errors['instructions'] = 'Instructions are required'
    if (instructions && instructions.length > 2000) errors['instructions'] = 'Instructions must be 2000 characters or less'
    if (recipeImageUrl && recipeImageUrl.length > 255) errors['instructions'] = 'Instructions must be 255 characters or less'
    if (rIErrors.length) errors['recipeIngredient'] = 'Please fill out all fields'
    if (recipeImageUrl && recipeImageUrl.length > 255) errors['recipeImage'] = 'Image URL must be 255 characters or less'

    if (!Object.values(errors).length) setSubmitValidity(true)
    setErrors(errors)
  }, [name, description, instructions, recipeIngredients, backendErr, rIErrors])

  let newNum = recipeIngredients.length +1
  const handleNewRI = async (e) => {
    e.preventDefault()
    let newRI = {
      ingNum: num,
      ingName: 'none',
      ingAmt: 1,
      ingUnit: 'none'
    }
    newNum += 1
    setRecipeIngredients([...recipeIngredients, newRI])
  }

  const handleSubmit = async (e) => {
    console.log('hi')
    e.preventDefault()

    const recipeForm = {
      name: name,
      description: description,
      instructions: instructions,
      user_id: userId
    }

    let updatedRecipe

    if (!Object.values(errors).length && submitValidity) {
      updatedRecipe = await dispatch(recipeActions.editRecipeThunk(recipeId, recipeForm))
      .catch(async (res) => {
        const data = await res.json()
        console.log('create data: ', data)
        if (data && data.Errors) {
          console.log('data errors: ', data.Errors)
        }
      })

      if (updatedRecipe && updatedRecipe.Errors) {
        setErrors(updatedRecipe.Errors)
      }

      if (updatedRecipe && updatedRecipe.id) {
        let rIForm
        for (let rIObj of recipeIngredients) {
          let matchedIng = ingredientsArr.find(ing => ing.name === rIObj.ingName)
          if (rIObj.ingNum > 15) {
            rIForm = {
              id: rIObj.ingNum,
              amount: +rIObj.ingAmt,
              unit: rIObj.ingUnit,
              recipe_id: updatedRecipe.id,
              ingredient_id: matchedIng? matchedIng.id : undefined,
            }
            dispatch(recipeActions.editRecipeIngredientsThunk(rIObj.ingNum, rIForm))
          } else {
            rIForm = {
              amount: +rIObj.ingAmt,
              unit: rIObj.ingUnit,
              ingredient_id: matchedIng.id,
              recipe_id: updatedRecipe.id
            }
            dispatch(recipeActions.addRecipeIngredientsThunk(rIForm))
          }
        }

        if (updatedRecipe && updatedRecipe.recipe_image_url) {
          let imageForm = {
            recipe_id: updatedRecipe.id,
            url: recipeImageUrl
          }

          dispatch(recipeActions.editRecipeImageThunk(updatedRecipe.id, imageForm))
        } else if (updatedRecipe && !updatedRecipe.recipe_image_url) {
          let imageForm = {
            recipe_id: updatedRecipe.id,
            url: recipeImageUrl
          }

          dispatch(recipeActions.addRecipeImageThunk(updatedRecipe.id, imageForm))
        }
      }
      navigate(`/recipes/${recipeId}`)
    }
  }

  const submitButtonClass = submitValidity ? 'edit-rec-submit-button' : 'edit-rec-submit-button-disabled'


  if (!recipe) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div className="edit-rec-super-container">
        <div className="edit-rec-lesser-container">

          <div className="edit-rec-header">Edit a Recipe</div>

          <form className="edit-rec-form" onSubmit={handleSubmit}>

            <label className="edit-rec-name">
              <div className="edit-rec-name-name">Name</div>

              <div className="edit-rec-name-input-val">
                <input
                  type="text"
                  className="edit-rec-name-input"
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

            <label className="edit-rec-description">
              <div className="edit-rec-description-name">Description</div>

              <div className="edit-rec-description-input-val">
                <textarea
                  type="text"
                  className="edit-rec-description-input"
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

            <label className="edit-rec-ingredients">
              <div className="edit-rec-ingredients-name-val">
                <div className="edit-rec-ingredients-name">Ingredients</div>
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

            <label className="edit-rec-instructions">
              <div className="edit-rec-instructions-name">Instructions</div>

              <div className="edit-rec-instructions-input-val">
                <textarea
                  type="text"
                  className="edit-rec-instructions-input"
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

            <label className="edit-rec-rec-image">
              <div className="edit-rec-rec-image-name">Recipe Image</div>

              <div className="edit-rec-rec-image-input-val">
                <input
                  className="edit-rec-rec-image-input"
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

            <div className="edit-rec-submit-container">
              <button className={submitButtonClass} onClick={handleSubmit} disabled={submitValidity ? false : true}>Save Cocktail!</button>
            </div>

          </form>
        </div>

        <CreateIngredient />
      </div>
    );
  }
}

export default EditRecipe;
