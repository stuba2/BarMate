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

  console.log('recipe: ', recipe)

  useEffect(() => {
    dispatch(recipeActions.getRecipesThunk())
  }, [dispatch])

  let recipeArr = Object.values(recipe)


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
                <li key={ingredient.name}>{ingredient.name}</li>
              )
            })}
          </ul>
        </div>
        <div>{recipe.instructions}</div>
        <div>update the route to include recipe image instead of making it's own request?</div>
      </div>
      </>
    );
  }
}

export default OneRecipe;
