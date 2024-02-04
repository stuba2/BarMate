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
          <select
            id="ingredient-options"
            value={ingredientIndividual}
            onChange={(e) => {
              setIngredientIndividual(e.target.value)
              handleChangeIngName(e.target.value)
            }}
            required
          >
            <option value={''}>Ingredient...</option>
            {ingredientsArr.map((ingredientObj) => {
              return (
                <option value={ingredientObj.name} key={ingredientObj.id}>{ingredientObj.name}</option>
                )
              })}
          </select>
          <div className={errorClassName}>Ingredient must be in dropdown list</div>
        </div>

        <div>
          <input
            type="number"
            id="number-options"
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
          <select
          id="unit-options"
            value={unitIndividual}
            onChange={(e) => {
              setUnitIndividual(e.target.value)
              handleChangeIngUnit(e.target.value)
            }}
            required
          >
            <option value={''}>Unit...</option>
            {unitTypes.map((unit) => {
              return (
                <option value={unit} key={unit}>{unit}</option>
                )
              })}
          </select>
        </div>
      </div>
    )
  }
}

export default OneRecipeIngredient
