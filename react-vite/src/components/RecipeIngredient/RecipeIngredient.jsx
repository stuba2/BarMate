import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as ingredientActions from "../../redux/ingredients"
import unitTypes from "../../../public/unitTypes";
import './RecipeIngredient.css'

const RecipeIngredient = ({ recipeIngredients, setRecipeIngredients, recipeAmounts, setRecipeAmounts, recipeUnits, setRecipeUnits, originalName, originalAmount, originalUnit, originalId }) => {
  const dispatch = useDispatch()
  const ingredients = useSelector(state => state.ingredients)
  const [ ingredientIndividual, setIngredientIndividual ] = useState(originalName ? originalName : '')
  const [ amountIndividual, setAmountIndividual ] = useState(originalAmount ? originalAmount : '')
  const [ unitIndividual, setUnitIndividual ] = useState(originalUnit ? originalUnit : '')

  const ingredientsArr = Object.values(ingredients)
  const ingredientsABC = ingredientsArr.sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })


  useEffect(() => {
    dispatch(ingredientActions.getIngredientsThunk())
  }, [dispatch])

  // need to add ingredientIndividual, etc to recipeIngredients arr


  return (
    // <div>
    //   <div>
    //     {}
    //   </div>
    // </div>
    <div className="create-rec-ing">
      Ingredient!
      <div>
        <div className="rec-ing-ingredient-drop">
          <input
            value={ingredientIndividual}
            onChange={(e) => {
              setIngredientIndividual(e.target.value)
              setRecipeIngredients([...recipeIngredients, e.target.value])
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
              // console.log('recipeAmounts in RI comp', recipeAmounts)
              setRecipeAmounts([...recipeAmounts, e.target.value])
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

export default RecipeIngredient
