import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import * as ingredientActions from "../../redux/ingredients"
import * as recipeActions from "../../redux/recipes"
import RecipeIngredient from "../RecipeIngredient/RecipeIngredient";
import './EditRecipe2.css'
import AllRecipeIngredients from "../AllRecipeIngredients/AllRecipeIngredients";

const EditRecipe2 = () => {
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
        ingNum: num,
        ingName: rI.name,
        ingAmt: rI.amount,
        ingUnit: rI.unit
      }
      num += 1
      allIngredientsArr.push(existingRI)
    }
    setRecipeIngredients([...allIngredientsArr])
  }

  const handleNewRI = async (e) => {
    e.preventDefault()
    let newRI = {
      ingNum: num,
      ingName: '',
      ingAmt: '',
      ingUnit: ''
    }
    setRecipeIngredients([...recipeIngredients, newRI])
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
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
            {/* <button>Add Ingredient</button> */}
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

          <div>
            <button>Save Cocktail!</button>
          </div>

        </form>
      </div>
    );
  }
}

export default EditRecipe2;
