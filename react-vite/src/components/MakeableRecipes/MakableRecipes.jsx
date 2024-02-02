import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as recipeActions from "../../redux/recipes"
import * as barActions from "../../redux/bars"
import { NavLink } from "react-router-dom";
import OnceRecipeSmall from "../OneRecipeSmall/OneRecipeSmall";
import './MakableRecipes.css'

const MakableRecipes = () => {
  const dispatch = useDispatch()
  const recipes = useSelector(state => state.recipes)
  const myBar = useSelector(state => state.bar)

  let recipesArr = Object.values(recipes)
  const barIngredients = Object.values(myBar).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })

  useEffect(() => {
    dispatch(recipeActions.getMakableRecipesThunk())
    dispatch(barActions.getBarThunk())
  }, [])


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
        <ul className="makable-rec-ul">
          {recipesArr.map((recipe) => {
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

export default MakableRecipes
