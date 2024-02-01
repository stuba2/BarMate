import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import * as recipeActions from "../../redux/recipes"
import Reviews from "../Reviews/Reviews";
import Toasts from "../Toasts/Toasts";
import CreateReview from "../CreateReview/CreateReview";
import './OneRecipe.css'

const OneRecipe = () => {
  const dispatch = useDispatch()
  const recipes = useSelector(state => state.recipes)
  const reviews = useSelector(state => state.reviews)
  const { recipeId } = useParams()
  const recipe = recipes[+recipeId]
  const reviewsArr = Object.values(reviews)

  let ratingAvg = (Math.round((reviewsArr.reduce((total, next) => total + next.rating, 0) / reviewsArr.length) * 100) / 100)
  if (Number.isNaN(ratingAvg)) ratingAvg = 'Be the first to rate!'


  useEffect(() => {
    dispatch(recipeActions.getOneRecipeThunk(+recipeId))

  }, [dispatch])

  if (!recipe || !recipe.recipe_ingredients) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div className="one-rec-whole-container">

        <div className="one-rec-name-description-img">

          <div className="one-rec-name-description-rating-toast">
            <h1 className="one-rec-name">{recipe.name}</h1>
            <div className="one-rec-description">{recipe.description}</div>

            <div className="one-rec-rating-toast">
              <div className="one-rec-rating">Average Rating: <i className="fa-solid fa-star"></i> {ratingAvg}</div>
              <div className="one-rec-toast-container"><Toasts recipeId={recipeId}/></div>
            </div>
          </div>

          <div><img src={recipe.recipe_image_url} width="335" className="one-rec-img"/></div>
        </div>

        <div className="one-rec-ing-instructions">
          <div className="one-rec-ing-container">
            Ingredients:
            <ul>
              {recipe.recipe_ingredients.map((ingredient) => {
                return (
                  <li key={ingredient.name}>{ingredient.name}: {ingredient.amount} {ingredient.unit}</li>
                )
              })}
            </ul>
          </div>
          <div className="one-rec-instructions">{recipe.instructions}</div>
        </div>

        <div className="one-rec-rev-super-container">
          <div className="one-rec-create-rev"><CreateReview recipeId={recipeId}/></div>
          <div className="one-rec-revs"><Reviews /></div>
        </div>
      </div>
    );
  }
}

export default OneRecipe;
