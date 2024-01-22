import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate, useParams } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as recipeActions from "../../redux/recipes"

const OneRecipe = () => {
  const dispatch = useDispatch()
  const recipes = useSelector((state) => state.recipes)
  const { recipeId } = useParams()
  const recipe = recipes[+recipeId]


  useEffect(() => {
    dispatch(recipeActions.getOneRecipeThunk(+recipeId))

  }, [dispatch])

  if (!recipe) {
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
        <div><img src={recipe.recipe_image_url} width="335" /></div>
      </div>
      </>
    );
  }
}

export default OneRecipe;
