import { useState, useEffect } from "react";
import unitTypes from "../../../unitTypes";
// import { useDispatch, useSelector } from "react-redux";
// import { Navigate, useNavigate } from "react-router-dom";
// import { thunkSignup } from "../../redux/session";
// import * as ingredientActions from "../../redux/ingredients"
// import unitTypes from "../../../dist/assets/unitTypes";

const OneRecipeIngredient = ({ obj, tryHandleChange, tryHandleDelete, recipeIngredients, setRecipeIngredients, recipeAmounts, setRecipeAmounts, recipeUnits, setRecipeUnits, ingredientsABC, ingredientIndividual, setIngredientIndividual, amountIndividual, setAmountIndividual, unitIndividual, setUnitIndividual }) => {
  // const [ isEditing, setIsEditing ] = useState(false)
  // const [ ingredientIndividual, setIngredientIndividual ] = useState('')
  // const [ amountIndividual, setAmountIndividual ] = useState('')
  // const [ unitIndividual, setUnitIndividual ] = useState('')

  return (
    <div>
      <div>
         <div className="rec-ing-ingredient-drop">
           <input
            value={ingredientIndividual}
            onChange={(e) => {
              setIngredientIndividual(e.target.value)
              setRecipeIngredients([...recipeIngredients, ...e.target.value])
            }}
            list="ingredient-options"
            id="ingredient-option"
            name="ingredient-option"
            placeholder="Ingredient..."
          />
          <datalist id="ingredient-options">
            {ingredientsABC.map((ingredientObj) => {
              return (
                <option value={ingredientObj.name} key={ingredientObj.id}></option>
              )
            })}
          </datalist>
        </div>
        <div>
          <input
            type="text"
            value={amountIndividual}
            onChange={(e) => {
              setAmountIndividual(e.target.value)
              setRecipeAmounts([...recipeAmounts, ...e.target.value])
            }}
            required
            placeholder="Amount"
          />
        </div>
        <div><input
            value={unitIndividual}
            onChange={(e) => {
              setUnitIndividual(e.target.value)
              setRecipeUnits([...recipeUnits, e.target.value])
            }}
            list="unit-options"
            id="unit-option"
            name="unit-option"
            placeholder="Unit..."
          />
          <datalist id="unit-options">
            {unitTypes.map((unit) => {
              return (
                <option value={unit} key={unit}></option>
              )
            })}
          </datalist></div>
          <div>
            <button>X</button>
          </div>
      </div>
    </div>
  )
}

export default OneRecipeIngredient
