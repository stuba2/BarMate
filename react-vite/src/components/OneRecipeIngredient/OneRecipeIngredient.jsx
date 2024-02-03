import { useEffect, useState } from "react";
import unitTypes from "../../../public/unitTypes";
import './OneRecipeIngredient.css'
import { useSubmit } from "react-router-dom";

const OneRecipeIngredient = ({ rIObj, ingredientsArr, setSubmitValidity, hasSubmitted }) => {
  const [ ingredientIndividual, setIngredientIndividual ] = useState(rIObj.ingName ? rIObj.ingName : '')
  const [ amountIndividual, setAmountIndividual ] = useState(rIObj.ingAmt ? rIObj.ingAmt : '')
  const [ unitIndividual, setUnitIndividual ] = useState(rIObj.ingUnit ? rIObj.ingUnit : '')
  const [ individualErrors, setIndividualErrors ] = useState({})
  const [ errorClassName, setErrorClassName ] = useState('')
  // let errorClassName

  useEffect(() => {
    let existingIngName = ingredientsArr.find(ing => ing.name === ingredientIndividual)
    console.log('name:= ', ingredientIndividual)
    console.log('existing=: ', existingIngName)
    console.log('!existing=: ', !existingIngName)
    if (!existingIngName && hasSubmitted) {
      setErrorClassName('validation-error')
    } else {
      setErrorClassName('validation-error hidden')
    }

  }, [ingredientIndividual])


  const handleChangeIngName = (name) => {
    let existingIngName = ingredientsArr.find(ing => ing.name === name)
    if (!existingIngName) setSubmitValidity(false)
    else setSubmitValidity(true)

    rIObj.ingName = name
  }
  const handleChangeIngAmt = (amt) => {
    rIObj.ingAmt = amt
  }
  const handleChangeIngUnit = (unit) => {
    let existingUnitName = unitTypes.find(unitType => unitType === unit)
    if (!existingUnitName) setSubmitValidity(false)
    else setSubmitValidity(true)

    rIObj.ingUnit = unit
  }

  if (!ingredientsArr) {
    return <div>...loading</div>
  } else {
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
            required
            placeholder="Ingredient..."
          />
          <datalist id="ingredient-options">
            {ingredientsArr.map((ingredientObj) => {
              return (
                <option value={ingredientObj.name} key={ingredientObj.id}></option>
                )
              })}
          </datalist>
          <div className={errorClassName}>Ingredient must be in dropdown list</div>
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
            min='1'
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
            required
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
}

export default OneRecipeIngredient
