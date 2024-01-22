import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as ingredientActions from '../../redux/ingredients'

const AllIngredients = () => {
  const dispatch = useDispatch()
  const ingredients = useSelector((state) => state.ingredients)

  useEffect(() => {
    dispatch(ingredientActions.getIngredientsThunk())
  }, [dispatch])

  let ingredientsArr = Object.values(ingredients)


  if (!ingredients) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <>
      <div>
        {ingredientsArr.map((ingredient) => {
          return (
            <div key={ingredient.id}>
              <div>{ingredient.name}</div>
            </div>
          )
        })}
      </div>
      </>
    );
  }
}

export default AllIngredients;
