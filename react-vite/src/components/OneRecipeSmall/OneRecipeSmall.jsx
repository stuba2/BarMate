import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
// import * as spotActions from '../../store/spot'
import { useParams, NavLink } from "react-router-dom"
// import './ASmallSpotMain.css'

const OnceRecipeSmall = ({recipeId}) => {
  const dispatch = useDispatch()
  const recipes = useSelector(state => state.recipes)
  const recipe = recipes[+recipeId]
  // console.log('recipe: ', recipe)

  const recPic = recipe ? <img src={recipe.recipe_image_url} style={{width: '100px'}} /> : <img src='https://source.unsplash.com/random/700x700/?house' style={{ width: '100px'}}/>


  if (!recipe) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div className="whole-thing-small-spot">
        <div className="spot-image">
          {recPic}
        </div>
        <div className="under-pic">
          <div>{recipe.name}</div>
        </div>
      </div>
    )
  }
}

  export default OnceRecipeSmall
