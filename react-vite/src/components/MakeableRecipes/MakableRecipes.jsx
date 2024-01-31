import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import * as recipeActions from "../../redux/recipes"
import * as barActions from "../../redux/bars"
import OnceRecipeSmall from "../OneRecipeSmall/OneRecipeSmall";
import './MakableRecipes.css'

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
      <div className="makable-drinks-container">

        <div className="make-left">
          <div><NavLink to="/account/myBar" className="make-update-bar">Update your Bar</NavLink></div>

          <div className="makable-ings-container">
            <div className="makable-ings-header">My Ingredients:</div>
            <ul className="makable-ings-ul">
              {barIngredients.map((ingredient) => {
                return (
                  <li key={ingredient.id} className="makable-ing">{ingredient.name}</li>
                )
              })}
            </ul>
          </div>
        </div>

        <div className="makable-recs-container">
          {/* <div>Possible drinks:</div> */}
          <ul className="makable-rec-ul">
            {ret.map((recipe) => {
              return (
                <NavLink
                  to={`/recipes/${recipe.id}`}
                  className="makable-one-recipe-container"
                  key={recipe.id}
                  title={recipe.name}>
                    <OnceRecipeSmall recipeId={recipe.id}/>
                  </NavLink>
              )
            })}
          </ul>
        </div>
      </div>
    );
  }
}

export default MakableRecipes;
