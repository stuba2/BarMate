import { useSelector } from "react-redux"
import './OneRecipeSmall.css'

const OnceRecipeSmall = ({recipeId}) => {
  const randRecipes = useSelector(state => state.randomRec)
  const makableRecipes = useSelector(state => state.makableRec)
  const recipes = useSelector(state => state.recipes)
  const randRecipe = randRecipes[+recipeId]
  const makableRecipe = makableRecipes[+recipeId]
  const recipe = recipes[+recipeId]

  let chosenRecipe
  if (recipe) chosenRecipe = recipe
  else if (randRecipe) chosenRecipe = randRecipe
  else if (makableRecipe) chosenRecipe = makableRecipe

  const recPic = chosenRecipe ? <img className="small-recipe-image" src={chosenRecipe.recipe_image_url} /> : <img src='https://source.unsplash.com/random/700x700/?house' style={{ width: '100px'}}/>


  if (!chosenRecipe) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div className="whole-thing-small-recipe">
        <div className="small-recipe-image-container">
          {recPic}
        </div>
        <div className="under-pic">
          <div className="small-recipe-name-link">{chosenRecipe.name}</div>
        </div>
      </div>
    )
  }
}

  export default OnceRecipeSmall
