import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import * as ingredientActions from "../../redux/ingredients"
import * as recipeActions from "../../redux/recipes"
import RecipeIngredient from "../RecipeIngredient/RecipeIngredient";
import './CreateRecipe.css'
import AllRecipeIngredients from "../AllRecipeIngredients/AllRecipeIngredients";

const CreateRecipe = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const { user } = useSelector(state => state.session)
  const recipes = useSelector(state => state.recipes)
  const ingredients = useSelector(state => state.ingredients)
  const userId = user.id
  const [ name, setName ] = useState('')
  const [ description, setDescription ] = useState('')
  const [ instructions, setInstructions ] = useState('')
  const [ validationErrors, setValidationErrors ] = useState({})
  const [ recipeIngredients, setRecipeIngredients ] = useState([])
  const [ recipeAmounts, setRecipeAmounts ] = useState([])
  const [ recipeUnits, setRecipeUnits ] = useState([])
  const [ count, setCount ] = useState(1)
  const [ hasSubmitted, setHasSubmitted ] = useState(false)

  useEffect(() => {
    const errors = {}
    let riLength = recipeIngredients.length
    let raLength = recipeAmounts.length
    let ruLength = recipeUnits.length
    let existingRecipeName = recipesArr.filter((recipe) => (recipe.name) === name)[0]

    if (!name) errors['name'] = 'Cocktail name is required'
    if (name.length > 64) errors['name'] = 'Cocktail name must be 64 characters or less'
    if (existingRecipeName) errors['name'] = 'Recipe already exists with that name'
    if (description && description.length > 1000) errors['description'] = 'Cocktail description must be 1000 characters or less'
    if (!instructions) errors['instructions'] = 'Instructions are required'
    if (instructions.length > 2000) errors['instructions'] = 'Cocktail instructions must be 2000 characters or less'
    if ((riLength + raLength + ruLength)%3 !== 0) errors['ingredient'] = 'All ingredient fields are needed'

    setValidationErrors(errors)
  },[name, description, instructions, recipeIngredients, recipeAmounts, recipeUnits])

  const initialWhat = [
    // {name: 'Wine', amount: 1, unit:'cl'},
    // {name: 'Tea', amount: 2, unit:'oz'},
    // {name: 'Port', amount: 3, unit:'tbs'}
  ]
  const [ what, setWhat ] = useState(initialWhat ? initialWhat : [])

  const ingredientsArr = Object.values(ingredients)
  const recipesArr = Object.values(recipes)

//************************************* need to include recipe image

  // tracking the changes in the individual CreateIngredient components
  useEffect(() => {
    for (let i = 0; i < recipeIngredients.length; i++) {
      let matchedIng = ingredientsArr.filter(ing => ing.name === recipeIngredients[i])
      console.log('---', matchedIng[0].id)
      console.log('recipeIngredients: ', recipeIngredients)
      console.log('recipeAmounts: ', recipeAmounts)
      console.log('recipeUnits: ', recipeUnits)
    }
  }, [recipeIngredients, recipeAmounts, recipeUnits])

  // keeping up with the up to date ing/rec
  useEffect(() => {
    dispatch(ingredientActions.getIngredientsThunk())
    dispatch(recipeActions.getRecipesThunkAll())
  },[dispatch])

  // tracking front end validation errors
  useEffect(() => {
      const errors = {}
      let existingRecipeName = recipesArr.filter((recipe) => (recipe.name) === name)[0]
      if (existingRecipeName) errors['name'] = 'Recipe already exists with that name'
      if (!name) errors['name'] = 'Cocktail name is required'
      if (!instructions) errors['instructions'] = 'Instructions are required'
      // add in length requirements
      setValidationErrors(errors)
    },[name, instructions])

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

    if (!Object.values(validationErrors).length) {
      createdRecipe = await dispatch(recipeActions.createRecipeThunk(recipeForm))
      .catch(async (res) => {
        const data = await res.json()
        console.log('create data: ', data)
        if (data && data.Errors) {
          console.log('data errors: ', data.Errors)
        }
      })
      if (createdRecipe && createdRecipe.Errors) {
        setValidationErrors(createdRecipe.Errors)
      }

      console.log('createdRecipe: ', createdRecipe)
      if (createdRecipe && createdRecipe.id) {
        console.log("i'm a real boy: ", createdRecipe)

        // handles the addition of RecipeIngredients to the store, called from the handleSubmit
        let finalIngredient
        let finalRI = []
        for (let i = 0; i < recipeIngredients.length; i++) {
          let matchedIng = ingredientsArr.filter(ing => ing.name === recipeIngredients[i])

          finalIngredient = {
            amount: recipeAmounts[i],
            unit: recipeUnits[i],
            recipe_id: createdRecipe.id,
            ingredient_id: matchedIng[0].id
          }
          finalRI.push(finalIngredient)
        }

        for (let i = 0; i < finalRI.length; i++) {
          let singleRI = finalRI[i]
          dispatch(recipeActions.addRecipeIngredientsThunk(singleRI))
        }

        navigate(`/recipes/${createdRecipe.id}`)
      }
    } else {console.log('validation error to be done!', validationErrors)}
  }

  const componentSingular = <RecipeIngredient recipeIngredients={recipeIngredients} setRecipeIngredients={setRecipeIngredients} recipeAmounts={recipeAmounts} setRecipeAmounts={setRecipeAmounts} recipeUnits={recipeUnits} setRecipeUnits={setRecipeUnits}/>

  const [componentArr, setComponentArr ] = useState([componentSingular])

  const counterFunc = (e) => {
    e.preventDefault()
    setCount(+count+1)
    console.log('componentArr: ', componentArr)
    setComponentArr([...componentArr, componentSingular])
  }

  const antiCounterFunc = (e) => {
    e.preventDefault()
    setCount(+count-1)
    setComponentArr([componentArr.filter(rI => rI.key !== keyCount)])
  }

  const tryHandleAdd = (name, amount, unit) => {
    setWhat([
      ...what,
      {
        name,
        amount,
        unit
      }
    ])
  }

  const tryHandleChange = () => {

  }

  const tryHandleDelete = () => {

  }



  if (!recipes) {
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
                {hasSubmitted && validationErrors.name && `*${validationErrors.name}`}
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
                {hasSubmitted && validationErrors.description && `*${validationErrors.description}`}
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
                {hasSubmitted && validationErrors.ingredient && `*${validationErrors.ingredient}`}
              </div>
            </div>

            <div>
              {componentArr.map((oneComponent) => {
                return (
                  oneComponent
                )
              })}
            </div>
            {/* <AllRecipeIngredients what={what} setWhat={setWhat} tryHandleChange={tryHandleChange} tryHandleDelete={tryHandleDelete} recipeIngredients={recipeIngredients} setRecipeIngredients={setRecipeIngredients} recipeAmounts={recipeAmounts} setRecipeAmounts={setRecipeAmounts} recipeUnits={recipeUnits} setRecipeUnits={setRecipeUnits}/> */}

          </label>

          <div className="create-rec-add-ri-container">
            <button onClick={counterFunc} className="create-rec-add-ri-button">Add Ingredient</button>
          </div>

          <label className="create-rec-instructions">
            <div className="create-rec-instructions-name-val">
              <div className="create-rec-instructions-name">instructions</div>
              <div className="validation-error">
                {hasSubmitted && validationErrors.instructions && `*${validationErrors.instructions}`}
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

          <div className="create-rec-submit-container">
            <button className="create-rec-submit-button">Create new drink!</button>
          </div>

        </form>
      </div>
    );
  }
}

export default CreateRecipe;
