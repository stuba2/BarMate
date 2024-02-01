import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as barActions from "../../redux/bars"
import * as ingredientActions from "../../redux/ingredients"
import EditBar from "../EditBar/EditBar";
import './MyBar.css'
import CreateIngredient from "../CreateIngredient/CreateIngredient";

const MyBar = () => {
  const dispatch = useDispatch()
  const { user } = useSelector(state => state.session)
  const userBar = useSelector(state => state.bar)
  const ingredients = useSelector(state => state.ingredients)
  const [ isSelected, setIsSelected ] = useState()

  let userBarr = Object.values(userBar).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })
  let ingredientsArr = Object.values(ingredients).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })

  let existingBar
  useEffect(() => {
    dispatch(ingredientActions.getIngredientsThunk())
    existingBar = dispatch(barActions.getBarThunk())
  }, [dispatch])

  const handleSubmit = async (e) => {
    e.preventDefault()

    let target = ingredientsArr.filter(ingObj => ingObj.name === isSelected)

    let ingInBar = userBarr.find(ing => ing.name === isSelected)

    if (!ingInBar) {
      let retIngObj = {
        ingredient_id: target[0].id,
        user_id: user.id
      }

      dispatch(barActions.postBarThunk(retIngObj))
    }
    if (ingInBar) {
      dispatch(barActions.deleteBarThunk(ingInBar.id))
    }

  }

  if (!true) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div className="my-bar-container">
        <div className="my-bar-lower">
          <div className="my-bar-current-ings">
            <div className="my-bar-ingredient-header">My Ingredients:</div>
            <ul className="my-bar-ingredient-ul">
              {userBarr.map((ingredient) => {
                return (
                  <li key={ingredient.id} className="my-bar-ingredient">{ingredient.name}</li>
                )
              })}
            </ul>
          </div>
          <div className="my-bar-possible-ings"><EditBar setIsSelected={setIsSelected} ingredientsArr={ingredientsArr} handleSubmit={handleSubmit}/></div>
        </div>
        <div className="my-bar-upper">
          <CreateIngredient />
        </div>
      </div>
    );
  }
}

export default MyBar;
