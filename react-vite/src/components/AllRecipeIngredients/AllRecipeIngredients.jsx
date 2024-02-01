import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as ingredientActions from "../../redux/ingredients"
import OneRecipeIngredient from "../OneRecipeIngredient/OneRecipeIngredient";

const AllRecipeIngredients = ({ recipeIngredients, setRecipeIngredients, handleNewRI }) => {
  const dispatch = useDispatch()
  const ingredients = useSelector(state => state.ingredients)

  const ingredientsArr = Object.values(ingredients).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })
  const ingredientsABC = ingredientsArr.sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })

  useEffect(() => {
    dispatch(ingredientActions.getIngredientsThunk())
  }, [dispatch])

  if (!true) {
    return (
      <div>...</div>
    )
  } else {
    return (
      <div>
        {recipeIngredients.map(rIObj => {
          return (
            <OneRecipeIngredient rIObj={rIObj} ingredientsABC={ingredientsABC}/>
          )
        })}

      <div><button onClick={handleNewRI}>Add Ingredient</button></div>
    </div>
  )
}
}

export default AllRecipeIngredients
