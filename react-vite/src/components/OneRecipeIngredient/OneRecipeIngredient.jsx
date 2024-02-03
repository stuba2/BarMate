import { useState } from "react";
import unitTypes from "../../../public/unitTypes";

const OneRecipeIngredient = ({ rIObj, ingredientsArr }) => {
  const [ ingredientIndividual, setIngredientIndividual ] = useState(rIObj.ingName ? rIObj.ingName : '')
  const [ amountIndividual, setAmountIndividual ] = useState(rIObj.ingAmt ? rIObj.ingAmt : '')
  const [ unitIndividual, setUnitIndividual ] = useState(rIObj.ingUnit ? rIObj.ingUnit : '')

  const handleChangeIngName = (name) => {
    rIObj.ingName = name
  }
  const handleChangeIngAmt = (amt) => {
    rIObj.ingAmt = amt
  }
  const handleChangeIngUnit = (unit) => {
    rIObj.ingUnit = unit
  }

  return (
    <div>
        <div className="rec-ing-ingredient-drop">
           <input
            value={ingredientIndividual}
            onChange={(e) => {
              setIngredientIndividual(e.target.value)
              handleChangeIngName(e.target.value)
            }}
            list="ingredient-options"
            id="ingredient-option"
            name="ingredient-option"
            placeholder="Ingredient..."
          />
          <datalist id="ingredient-options">
            {ingredientsArr.map((ingredientObj) => {
              return (
                <option value={ingredientObj.name} key={ingredientObj.id}></option>
              )
            })}
          </datalist>
        </div>

        <div>
          <input
            type="number"
            value={amountIndividual}
            onChange={(e) => {
              setAmountIndividual(e.target.value)
              handleChangeIngAmt(e.target.value)
            }}
            required
            placeholder="Amount"
          />
        </div>

        <div>
          <input
            value={unitIndividual}
            onChange={(e) => {
              setUnitIndividual(e.target.value)
              handleChangeIngUnit(e.target.value)
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
          </datalist>
        </div>
    </div>
  )
}

export default OneRecipeIngredient
