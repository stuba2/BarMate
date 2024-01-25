import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate, useParams } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as recipeActions from "../../redux/recipes"
import Reviews from "../Reviews/Reviews";
import Toasts from "../Toasts/Toasts";

const OneRecipe = () => {
  const dispatch = useDispatch()
  const recipes = useSelector((state) => state.recipes)
  const reviews = useSelector((state) => state.reviews)
  const { recipeId } = useParams()
  const recipe = recipes[+recipeId]
  const reviewsArr = Object.values(reviews)

  let ratingAvg = reviewsArr.reduce((total, next) => total + next.rating, 0) / reviewsArr.length

  console.log(ratingAvg)


  useEffect(() => {
    dispatch(recipeActions.getOneRecipeThunk(+recipeId))

  }, [dispatch])

  if (!recipe || !recipe.recipe_ingredients) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <>
      <div>
        <div>{recipe.name}</div>
        <div>{recipe.description}</div>
        <div>
          Ingredients:
          <ul>
            {recipe.recipe_ingredients.map((ingredient) => {
              return (
                <li key={ingredient.name}>{ingredient.name}: {ingredient.amount} {ingredient.unit}</li>
              )
            })}
          </ul>
        </div>
        <div>{recipe.instructions}</div>
        <div>Average Rating: <i class="fa-solid fa-star"></i> {ratingAvg}</div>
        <div><img src={recipe.recipe_image_url} width="335" /></div>
        <div><Reviews /></div>
        <div><Toasts /></div>
      </div>
      </>
    );
  }
}

export default OneRecipe;
