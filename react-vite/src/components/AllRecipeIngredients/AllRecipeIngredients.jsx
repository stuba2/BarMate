import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
// import { useNavigate } from "react-router-dom";
import * as ingredientActions from "../../redux/ingredients"
// import * as recipeActions from "../../redux/recipes"
// import RecipeIngredient from "../RecipeIngredient/RecipeIngredient";
import OneRecipeIngredient from "../OneRecipeIngredient/OneRecipeIngredient";

const AllRecipeIngredients = ({ what, setWhat, tryHandleChange, tryHandleDelete, recipeIngredients, setRecipeIngredients, recipeAmounts, setRecipeAmounts, recipeUnits, setRecipeUnits }) => {
  const dispatch = useDispatch()
  const ingredients = useSelector(state => state.ingredients)
  const [ ingredientIndividual, setIngredientIndividual ] = useState('')
  const [ amountIndividual, setAmountIndividual ] = useState('')
  const [ unitIndividual, setUnitIndividual ] = useState('')
  console.log('what: ', what)

  const ingredientsArr = Object.values(ingredients).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })

  const handleWhat = () => {
    const addedObj = {
      ingName: ingredientIndividual,
      amount: amountIndividual,
      unit: unitIndividual
    }
    setWhat([...what, addedObj])
  }

  useEffect(() => {
    dispatch(ingredientActions.getIngredientsThunk())
  }, [dispatch])

  if (!what) {
    return (
      <div>...</div>
    )
  } else {
    return (
      <div>
      {what.map((obj) => {
        return (
          <OneRecipeIngredient obj={obj} tryHandleChange={tryHandleChange} tryHandleDelete={tryHandleDelete} recipeIngredients={recipeIngredients} setRecipeIngredients={setRecipeIngredients} recipeAmounts={recipeAmounts} setRecipeAmounts={setRecipeAmounts} recipeUnits={recipeUnits} setRecipeUnits={setRecipeUnits} ingredientsABC={ingredientsArr} ingredientIndividual={ingredientIndividual} setIngredientIndividual={setIngredientIndividual} amountIndividual={amountIndividual} setAmountIndividual={setAmountIndividual} unitIndividual={unitIndividual} setUnitIndividual={setUnitIndividual}/>
          )
        })}

        <OneRecipeIngredient tryHandleChange={tryHandleChange} tryHandleDelete={tryHandleDelete} recipeIngredients={recipeIngredients} setRecipeIngredients={setRecipeIngredients} recipeAmounts={recipeAmounts} setRecipeAmounts={setRecipeAmounts} recipeUnits={recipeUnits} setRecipeUnits={setRecipeUnits} ingredientsABC={ingredientsArr}/>

      <button onClick={handleWhat}>Add Ingredient</button>
    </div>
  )
}
}

export default AllRecipeIngredients
