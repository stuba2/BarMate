import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as barActions from "../../redux/bars"
import * as ingredientActions from "../../redux/ingredients"
import EditBar from "../EditBar/EditBar";
import './MyBar.css'
import CreateIngredient from "../CreateIngredient/CreateIngredient";

const MyBar = () => {
  const dispatch = useDispatch()
  const userBar = useSelector(state => state.bar)
  const ingredients = useSelector(state => state.ingredients)
  const [ isLoading, setIsLoading ] = useState(false)
  const [ barChangeIsLoading, setBarChangeIsLoading ] = useState(false)

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

  useEffect(() => {
    if (!Object.values(ingredients).length && !Object.values(userBar).length) setIsLoading(true)
    else setIsLoading(false)
  }, [ingredients, userBar])

  let possibleIngClass
  if (!barChangeIsLoading) possibleIngClass = 'my-bar-possible-ings'
  if (barChangeIsLoading) possibleIngClass = 'ing-loading'

  if (isLoading) {
    return (
      <div className="center">
        <div className="wave"></div>
        <div className="wave"></div>
        <div className="wave"></div>
        <div className="wave"></div>
        <div className="wave"></div>
        <div className="wave"></div>
        <div className="wave"></div>
        <div className="wave"></div>
        <div className="wave"></div>
        <div className="wave"></div>
      </div>
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
          <div className="my-bar-possible-ings"><EditBar ingredientsArr={ingredientsArr} /></div>
        </div>
        <div className="my-bar-upper">
          <CreateIngredient />
        </div>
      </div>
    );
  }
}

export default MyBar;
