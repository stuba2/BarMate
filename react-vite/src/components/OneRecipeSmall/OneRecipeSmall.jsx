import { useSelector } from "react-redux"
import './OneRecipeSmall.css'

const OnceRecipeSmall = ({recipeId}) => {
  const recipes = useSelector(state => state.recipes)
  const recipe = recipes[+recipeId]

  const recPic = recipe ? <img className="small-recipe-image" src={recipe.recipe_image_url} /> : <img src='https://source.unsplash.com/random/700x700/?house' style={{ width: '100px'}}/>


  if (!recipe) {
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
          <div className="small-recipe-name-link">{recipe.name}</div>
        </div>
      </div>
    )
  }
}

  export default OnceRecipeSmall
