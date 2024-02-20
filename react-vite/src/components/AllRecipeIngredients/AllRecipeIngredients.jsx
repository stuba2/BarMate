import { useDispatch, useSelector } from "react-redux";
import OneRecipeIngredient from "../OneRecipeIngredient/OneRecipeIngredient";
import './AllRecipeIngredients.css'

const AllRecipeIngredients = ({ recipeIngredients, handleNewRI, ingredientsArr, hasSubmitted, errors, setErrors, rIErrors, setRIErrors }) => {
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

      <div className="add-ri-container"><button className="add-ri-button" onClick={handleNewRI}>Add Ingredient</button></div>
    </div>
  )
}
}

export default AllRecipeIngredients
