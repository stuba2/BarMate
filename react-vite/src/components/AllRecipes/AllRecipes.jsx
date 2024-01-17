import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as recipeActions from "../../redux/recipes"

const AllRecipes = () => {
  const dispatch = useDispatch()
  const recipes = useSelector((state) => state.recipes)

  useEffect(() => {
    dispatch(recipeActions.getRecipesThunk())
  }, [dispatch])

  let recipesArr = Object.values(recipes)


  if (!recipes) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <>
      <div>
        {recipesArr.map((recipe) => {
          return (
            <div key={recipe.id}>
              <div>{recipe.name}</div>
              <ul>
                {recipe.recipe_ingredients.map((ingredient) => {
                  return (
                    <li key={ingredient.name}>{ingredient.amount} {ingredient.unit} {ingredient.name}</li>
                  )
                })}
              </ul>
            </div>
          )
        })}
      </div>
      </>
    );
  }
}

export default AllRecipes;
