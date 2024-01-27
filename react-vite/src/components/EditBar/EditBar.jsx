import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";
import * as ingredientActions from '../../redux/ingredients'
import * as barActions from '../../redux/bars'

const EditBar = ({ isSelected, setIsSelected, ingredientsArr, handleSubmit }) => {
  const dispatch = useDispatch()
  const { user } = useSelector(state => state.session)
  const ingredients = useSelector(state => state.ingredients)
  const userBar = useSelector(state => state.bar)

  return (
    <>
    I'm the Edit Bar!
    <form onSubmit={handleSubmit}></form>
    {ingredientsArr.map((ingredient) => {
      return (
        <form action="" onSubmit={handleSubmit} key={ingredient.id}>
          <button onClick={() => setIsSelected(ingredient.name)}>
            {ingredient.name}
          </button>
        </form>
      )
    })}
    </>
  );
}

export default EditBar;
