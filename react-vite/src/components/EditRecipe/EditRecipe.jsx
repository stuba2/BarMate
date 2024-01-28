import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import * as ingredientActions from "../../redux/ingredients"
import * as recipeActions from "../../redux/recipes"
import RecipeIngredient from "../RecipeIngredient/RecipeIngredient";
import './EditRecipe.css'

const EditRecipe = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const { recipeId } = useParams()
  const { user } = useSelector(state => state.session)
  const recipes = useSelector(state => state.recipes)
  const ingredients = useSelector(state => state.ingredients)
  const userId = user.id

  // keeping up with the up to date ing/rec
  useEffect(() => {
    dispatch(recipeActions.getOneRecipeThunk(recipeId))
    dispatch(ingredientActions.getIngredientsThunk())
  },[dispatch])

  const ingredientsArr = Object.values(ingredients)
  const recipesArr = Object.values(recipes)
  const recipe = recipesArr.find(recipe => recipe.id === +recipeId)

  const [ name, setName ] = useState(recipe ? recipe.name : '')
  const [ description, setDescription ] = useState(recipe ? recipe.description : '')
  const [ instructions, setInstructions ] = useState(recipe ? recipe.instructions : '')
  const [ validationErrors, setValidationErrors ] = useState({})
  const [ recipeIngredients, setRecipeIngredients ] = useState([])
  const [ recipeAmounts, setRecipeAmounts ] = useState([])
  const [ recipeUnits, setRecipeUnits ] = useState([])
  // const [ count, setCount ] = useState(recipe ? recipe.recipe_ingredients.length : 1)
  const [componentArr, setComponentArr ] = useState([])

  // tracking the changes in the individual CreateIngredient components
  useEffect(() => {
    for (let i = 0; i < recipeIngredients.length; i++) {
      let matchedIng = ingredientsArr.filter(ing => ing.name === recipeIngredients[i])
      // console.log('---', matchedIng[0].id)
      console.log('recipeIngredients up top: ', recipeIngredients)
      console.log('recipeAmounts up top: ', recipeAmounts)
      console.log('recipeUnits up top: ', recipeUnits)
    }
  }, [recipeIngredients, recipeAmounts, recipeUnits])

  // populates componentArr with existing RI
  let allIngFull = []
  let oneIngFull
      let rIName = []
      let rIAmt = []
      let rIUnit = []
  if (recipe && recipe.recipe_ingredients && componentArr.length < recipe.recipe_ingredients.length) {
    for (let i = 0; i < recipe.recipe_ingredients.length; i ++) {
      let rI = recipe.recipe_ingredients[i]
      console.log('ri: ', rI)
      console.log('ri.id: ', rI.id)
      console.log('hi before')

      rIName.push(rI.name)
      rIAmt.push(+rI.amount)
      rIUnit.push(rI.unit)

      console.log('hi after')

      oneIngFull = <RecipeIngredient  recipeIngredients={[...rIName]} setRecipeIngredients={setRecipeIngredients} recipeAmounts={[...rIAmt]} setRecipeAmounts={setRecipeAmounts} recipeUnits={[...rIUnit]} setRecipeUnits={setRecipeUnits} originalName={rI.name} originalAmount={rI.amount} originalUnit={rI.unit} originalId={rI.id}/>

      allIngFull.push(oneIngFull)
    }
    setComponentArr([...allIngFull])
    setRecipeIngredients([...rIName])
    setRecipeAmounts([...rIAmt])
    setRecipeUnits([...rIUnit])
  }

  // tracking front end validation errors
  // useEffect(() => {
  //     const errors = {}
  //     let existingRecipeName = recipesArr.filter((recipe) => (recipe.name) === name)[0]
  //     if (existingRecipeName) errors['name'] = 'Recipe already exists with that name'
  //     if (!name) errors['name'] = 'Cocktail name is required'
  //     if (!instructions) errors['instructions'] = 'Instructions are required'
  //     // add in length requirements
  //     setValidationErrors(errors)
  //   },[name, instructions])

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
      createdRecipe = await dispatch(recipeActions.editRecipeThunk(recipeId, recipeForm))
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
        console.log('ingredientsArr: ', ingredientsArr)
        console.log('recipeIngredients: ', recipeIngredients)
        for (let i = 0; i < recipeIngredients.length; i++) {
          console.log('hi')
          let matchedIng = ingredientsArr.filter(ing => ing.name === recipeIngredients[i])
          console.log('matchedIng: ', matchedIng)

          finalIngredient = {
            // id:
            amount: recipeAmounts[i],
            unit: recipeUnits[i],
            recipe_id: createdRecipe.id,
            ingredient_id: matchedIng[0].id
          }
          finalRI.push(finalIngredient)
        }

        for (let i = 0; i < finalRI.length; i++) {
          let singleRI = finalRI[i]
          console.log('singleRI to thunk: ', singleRI)
          dispatch(recipeActions.editRecipeIngredientsThunk(singleRI))
        }

        // navigate(`/recipes/${createdRecipe.id}`)
      }
    } else {console.log('validation error to be done!', validationErrors)}
  }

  const componentSingular = <RecipeIngredient recipeIngredients={recipeIngredients} setRecipeIngredients={setRecipeIngredients} recipeAmounts={recipeAmounts} setRecipeAmounts={setRecipeAmounts} recipeUnits={recipeUnits} setRecipeUnits={setRecipeUnits}/>


  const counterFunc = (e) => {
    e.preventDefault()
    // setCount(+(recipe.recipe_ingredients.length)+1)
    // populate recipeI,A,U with existing ings
    for (let rIComponent of componentArr) {
      // console.log('props name: ', rIComponent.props.originalName)
      // console.log('props amount: ', rIComponent.props.originalAmount)
      // console.log('props unit: ', rIComponent.props.originalUnit)
      // setRecipeIngredients([...recipeIngredients, rIComponent.props.originalName])
      // setRecipeAmounts([...recipeAmounts, rIComponent.props.originalAmount])
      // setRecipeUnits([...recipeUnits, rIComponent.props.originalUnit])
    }
                                            console.log('componentArr before: ', componentArr)
    // allIngFull = [...allIngFull, componentSingular]
    setComponentArr([...componentArr, componentSingular])
                                            console.log('componentArr after: ', componentArr)
                                            console.log('recipeIngredients: ', recipeIngredients)
                                            console.log('recipeAmounts: ', recipeAmounts)
                                            console.log('recipeUnits: ', recipeUnits)
  }

  if (!recipe) {
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
            <button>Save Cocktail!</button>
          </div>
        </form>
      </div>
    );
  }
}

export default EditRecipe;
