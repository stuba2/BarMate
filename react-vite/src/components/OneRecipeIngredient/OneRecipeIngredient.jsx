import { useEffect, useState } from "react";
import unitTypes from "../../../public/unitTypes";
import './OneRecipeIngredient.css'
import { useSubmit } from "react-router-dom";

const OneRecipeIngredient = ({ rIObj, ingredientsArr, hasSubmitted, errors, setErrors, rIErrors, setRIErrors }) => {
  const [ ingredientIndividual, setIngredientIndividual ] = useState(rIObj.ingName ? rIObj.ingName : '')
  const [ amountIndividual, setAmountIndividual ] = useState(rIObj.ingAmt ? rIObj.ingAmt : '')
  const [ unitIndividual, setUnitIndividual ] = useState(rIObj.ingUnit ? rIObj.ingUnit : '')
  const [ individualErrors, setIndividualErrors ] = useState({})
  // const [ errorClassName, setErrorClassName ] = useState('')
  // let errorClassName

  useEffect(() => {
    const localValErrors = {}
    if (rIObj.ingName === 'none') localValErrors['ingredientName'] = 'Pick an ingredient'
    if (rIObj.ingAmt < 1) localValErrors['ingredientAmount'] = 'Amount must be greater than 0'
    if (rIObj.ingUnit === 'none') localValErrors['ingredientUnit'] = 'Pick a unit of measure'

    if (Object.values(localValErrors).length) setRIErrors([...rIErrors, localValErrors])
    else setRIErrors([])

    setIndividualErrors(localValErrors)
    setErrors({...individualErrors, ...errors})
  }, [rIObj.ingName, rIObj.ingAmt, rIObj.ingUnit])


  // Updates recipeIngredients component in CreateRecipe on field change
  const handleChangeIngName = (name) => {
    rIObj.ingName = name
  }
  const handleChangeIngAmt = (amt) => {
    rIObj.ingAmt = amt
  }
  const handleChangeIngUnit = (unit) => {
    rIObj.ingUnit = unit
  }

  if (!ingredientsArr) {
    return <div>...loading</div>
  } else {
    return (
      <div>
        <div className="rec-ing-ingredient-drop">
          <label>Ingredient Name</label>
          <select
            id="ingredient-options"
            value={ingredientIndividual}
            onChange={(e) => {
                setIngredientIndividual(e.target.value)
                handleChangeIngName(e.target.value)
              }}
            required
          >
            <option value='none' defaultValue='none' disabled>Ingredient...</option>
            {ingredientsArr.map((ingredientObj) => {
              return (
                <option value={ingredientObj.name} key={ingredientObj.id}>{ingredientObj.name}</option>
                )
              })}
          </select>
          <div className="validation-error">{hasSubmitted && individualErrors.ingredientName && `*${individualErrors.ingredientName}`}</div>
        </div>

        <div>
          <label>Amount</label>
          <input
            type="number"
            id="number-options"
            value={amountIndividual}
            onChange={(e) => {
              setAmountIndividual(e.target.value)
              handleChangeIngAmt(e.target.value)
            }}
            // value={1}
            required
            min='1'
            placeholder="Amount"
            />
        </div>
        <div className="validation-error">{hasSubmitted && individualErrors.ingredientAmount && `*${individualErrors.ingredientAmount}`}</div>

        <div className="rec-ing-unit-drop">
          <label>Unit</label>
          <select
          id="unit-options"
            value={unitIndividual}
            onChange={(e) => {
              setUnitIndividual(e.target.value)
              handleChangeIngUnit(e.target.value)
            }}
            required
          >
            <option value='none' defaultValue='none' disabled>Unit...</option>
            {unitTypes.map((unit) => {
              return (
                <option value={unit} key={unit}>{unit}</option>
                )
              })}
          </select>
          <div className="validation-error">{hasSubmitted && individualErrors.ingredientUnit && `*${individualErrors.ingredientUnit}`}</div>
        </div>
      </div>
    )
  }
}

export default OneRecipeIngredient
