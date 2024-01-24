import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as ingredientActions from "../../redux/ingredients"
import * as recipeActions from "../../redux/recipes"
import RecipeIngredient from "../RecipeIngredient/RecipeIngredient";
import './CreateRecipe.css'

const CreateRecipe = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const { user } = useSelector((state) => state.session)
  const recipes = useSelector((state) => state.recipes)
  const ingredients = useSelector((state) => state.ingredients)
  const userId = user.id
  const [ name, setName ] = useState('')
  const [ description, setDescription ] = useState('')
  const [ instructions, setInstructions ] = useState('')
  const [ validationErrors, setValidationErrors ] = useState({})
  const [ recipeIngredients, setRecipeIngredients ] = useState([])
  const [ recipeAmounts, setRecipeAmounts ] = useState([])
  const [ recipeUnits, setRecipeUnits ] = useState([])
  const [ overallRecipeIngredients, setOverallRecipeIngredients ] = useState([])
  // const [ finalRI, setFinalRI ] = useState([])
  const [ count, setCount ] = useState(1)

  const ingredientsArr = Object.values(ingredients)
  const recipesArr = Object.values(recipes)



  // tracking the changes in the individual CreateIngredient components
  useEffect(() => {
    console.log('recipeIngredients: ', recipeIngredients)
    console.log('recipeAmounts: ', recipeAmounts)
    console.log('recipeUnits: ', recipeUnits)
    console.log('===', recipesArr)

    for (let i = 0; i < recipeIngredients.length; i++) {
      let matchedIng = ingredientsArr.filter(ing => ing.name === recipeIngredients[i])
      console.log('---', matchedIng[0].id)
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

      setValidationErrors(errors)
    },[name, instructions])

  const handleSubmit = async (e) => {
    e.preventDefault()

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
        // handleAddRI(createdRecipe.id)

        // handles the addition of RecipeIngredients to the store, called from the handleSubmit
        // const handleAddRI = (createdRecipe.id) => {
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
            console.log('finalIngredient: ', finalIngredient)

            finalRI.push(finalIngredient)

          }
          for (let i = 0; i < finalRI.length; i++) {
            let singleRI = finalRI[i]
            console.log('singleRI: ', singleRI)
            dispatch(recipeActions.addRecipeIngredientsThunk(singleRI))
          }
        // }

        navigate(`/recipes/${createdRecipe.id}`)
      }
    } else {console.log('validation error to be done!', validationErrors)}
  }

  const componentSingular = <RecipeIngredient recipeIngredients={recipeIngredients} setRecipeIngredients={setRecipeIngredients} recipeAmounts={recipeAmounts} setRecipeAmounts={setRecipeAmounts} recipeUnits={recipeUnits} setRecipeUnits={setRecipeUnits}/>

  const [componentArr, setComponentArr ] = useState([componentSingular])

  const counterFunc = (e) => {
    e.preventDefault()
    setCount(+count+1)
    setComponentArr([...componentArr, componentSingular])
  }

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

          <div>ingredients</div>
          <div>
            {componentArr.map((oneComponent) => {
              return (
                oneComponent
              )
            })}
          </div>

          <button onClick={counterFunc}>Add Ingredient</button>

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

export default CreateRecipe;
