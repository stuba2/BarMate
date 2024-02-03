import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as ingredientActions from "../../redux/ingredients"
import OneRecipeIngredient from "../OneRecipeIngredient/OneRecipeIngredient";

const AllRecipeIngredients = ({ recipeIngredients, setRecipeIngredients, handleNewRI, ingredientsArr, setSubmitValidity, hasSubmitted }) => {
  const dispatch = useDispatch()
  const ingredients = useSelector(state => state.ingredients)

  if (!true) {
    return (
      <div>...</div>
    )
  } else {
    return (
      <div>
        {recipeIngredients.map(rIObj => {
          return (
            <OneRecipeIngredient rIObj={rIObj} ingredientsArr={ingredientsArr} setSubmitValidity={setSubmitValidity} hasSubmitted={hasSubmitted}/>
          )
        })}

      <div><button onClick={handleNewRI}>Add Ingredient</button></div>
    </div>
  )
}
}

export default AllRecipeIngredients
