import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, Navigate, useNavigate, useParams } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as recipeActions from "../../redux/recipes"
import * as barActions from "../../redux/bars"
import OnceRecipeSmall from "../OneRecipeSmall/OneRecipeSmall";

const MakableRecipes = () => {
  const dispatch = useDispatch()
  const recipes = useSelector(state => state.recipes)
  const myBar = useSelector(state => state.bar)

  const barIngredients = Object.values(myBar).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })
  const recipesArr = Object.values(recipes)
  let ret = []

  for (let recipe of recipesArr) {
    let found
    for (let rI of recipe.recipe_ingredients) {
      found = barIngredients.find(ing => ing.name === rI.name)
      if (!found) break
    }
    if (found) {
      ret.push(recipe)
    }

  }

  useEffect(() => {
    dispatch(recipeActions.getRecipesThunkAll())
    dispatch(barActions.getBarThunk())
  }, [dispatch])


  if (!recipes) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <>
      <div>My ingredients:</div>
      <ul>
        {barIngredients.map((ingredient) => {
          return (
            <li key={ingredient.id}>{ingredient.name}</li>
          )
        })}
      </ul>
      <div>Possible drinks:</div>
      <ul>
        {ret.map((recipe) => {
          return (
            <NavLink
              to={`/recipes/${recipe.id}`}
              className="one-recipe-container"
              key={recipe.id}
              title={recipe.name}>
                <OnceRecipeSmall recipeId={recipe.id}/>
              </NavLink>
            // <div>
            //   <li style={{backgroundColor:"lightsalmon"}}>{recipe.name} {recipe.id}</li>
            //  { recipe.recipe_ingredients.map((ing) => {
            //   return (
            //     <>
            //       <li>{ing.name}</li>
            //     </>
            //   )
            //  })}
            // </div>
          )
        })}
      </ul>
      </>
    );
  }
}

export default MakableRecipes;
