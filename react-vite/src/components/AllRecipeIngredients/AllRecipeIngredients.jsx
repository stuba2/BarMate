import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as ingredientActions from "../../redux/ingredients"
import OneRecipeIngredient from "../OneRecipeIngredient/OneRecipeIngredient";

const AllRecipeIngredients = ({ recipeIngredients, setRecipeIngredients, handleNewRI, ingredientsArr, hasSubmitted, errors, setErrors, rIErrors, setRIErrors }) => {
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
            <OneRecipeIngredient key={rIObj.ingNum} rIObj={rIObj} ingredientsArr={ingredientsArr} hasSubmitted={hasSubmitted} errors={errors} setErrors={setErrors} rIErrors={rIErrors} setRIErrors={setRIErrors}/>
          )
        })}

      <div><button onClick={handleNewRI}>Add Ingredient</button></div>
    </div>
  )
}
}

export default AllRecipeIngredients
