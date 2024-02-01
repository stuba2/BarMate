import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import * as ingredientActions from "../../redux/ingredients"
import * as recipeActions from "../../redux/recipes"
import './EditRecipe.css'
import AllRecipeIngredients from "../AllRecipeIngredients/AllRecipeIngredients";

const EditRecipe = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const { recipeId } = useParams()
  const { user } = useSelector(state => state.session)
  const recipes = useSelector(state => state.recipes)
  const ingredients = useSelector(state => state.ingredients)
  const userId = user.id

  const ingredientsArr = Object.values(ingredients)
  const recipesArr = Object.values(recipes)
  const recipe = recipesArr.find(recipe => recipe.id === +recipeId)

  const [ name, setName ] = useState(recipe ? recipe.name : '')
  const [ description, setDescription ] = useState(recipe ? recipe.description : '')
  const [ instructions, setInstructions ] = useState(recipe ? recipe.instructions : '')
  const [ recipeIngredients, setRecipeIngredients ] = useState([])
  const [ recipeImageUrl, setRecipeImageUrl ] = useState(recipe ? recipe.recipe_image_url : '')
  const [ errors, setErrors ] = useState({})

  // keeping up with the up to date ing/rec
  useEffect(() => {
    dispatch(recipeActions.getOneRecipeThunk(recipeId))
    dispatch(ingredientActions.getIngredientsThunk())
  },[dispatch])

  useEffect(() => {
    console.log('recipeIngredients: ', recipeIngredients)
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

  let newNum = recipeIngredients.length +1
  const handleNewRI = async (e) => {
    e.preventDefault()
    let newRI = {
      ingNum: newNum,
      ingName: '',
      ingAmt: '',
      ingUnit: ''
    }
    newNum += 1
    setRecipeIngredients([...recipeIngredients, newRI])
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    console.log('recipeIngredients: ', recipeIngredients)

    const recipeForm = {
      name: name,
      description: description,
      instructions: instructions,
      user_id: userId
    }

    let updatedRecipe

    if (!Object.values(errors).length) {
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
              ingredient_id: matchedIng.id
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

  if (!recipe) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div className="edit-rec-container">
        <div>edit a recipe</div>

        <form onSubmit={handleSubmit}>

          <div>
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
          </div>

          <div>
            <div>description</div>
            <textarea
              type="text"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              maxLength='1000'
              placeholder="Write a description (optional)"
            />
          </div>

          <div>
            <AllRecipeIngredients recipeIngredients={recipeIngredients} setRecipeIngredients={setRecipeIngredients} handleNewRI={handleNewRI}/>
          </div>

          <div>
            <div>instructions</div>
            <textarea
              type="text"
              value={instructions}
              onChange={(e) => setInstructions(e.target.value)}
              maxLength='2000'
              required
              placeholder="Recipe instructions..."
            />
          </div>

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

          <div>
            <button onClick={handleSubmit}>Save Cocktail!</button>
          </div>

        </form>
      </div>
    );
  }
}

export default EditRecipe;
