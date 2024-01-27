import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate, useParams } from "react-router-dom";
import * as barActions from "../../redux/bars"
import * as ingredientActions from "../../redux/ingredients"
import EditBar from "../EditBar/EditBar";

const MyBar = () => {
  const dispatch = useDispatch()
  const { user } = useSelector(state => state.session)
  const userBar = useSelector(state => state.bar)
  const ingredients = useSelector(state => state.ingredients)
  const [ isSelected, setIsSelected ] = useState()
  // const [ isInBar, setIsInBar ] = useState()

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
  console.log('userBarr: ', userBarr)

  let existingBar
  useEffect(() => {
    dispatch(ingredientActions.getIngredientsThunk())
    existingBar = dispatch(barActions.getBarThunk())
  }, [dispatch])

  const handleSubmit = async (e) => {
    e.preventDefault()

    console.log('isSelected: ', isSelected)
    let target = ingredientsArr.filter(ingObj => ingObj.name === isSelected)
    console.log('target[0]: ', target[0])

    let ingInBar = userBarr.find(ing => ing.name === isSelected)
    console.log('ingInBar: ', ingInBar)

    if (!ingInBar) {
      let retIngObj = {
        ingredient_id: target[0].id,
        user_id: user.id
      }

      console.log('retingobj: ', retIngObj)
      dispatch(barActions.postBarThunk(retIngObj))
    }
    if (ingInBar) {
      dispatch(barActions.deleteBarThunk(ingInBar.id))
    }

  }


  // const handleAddToBar = (ingName) => {
  //   setMyBarr([...myBarr, ingName])
  // }

  // const handleRemoveFromBar = (ing) => {
  //   setMyBarr(myBarr.filter(ingredient => ingredient !== ing))
  // }


  if (!true) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div>
        <div>My ingredients:</div>
        <ul>
          {userBarr.map((ingredient) => {
            return (
              <li key={ingredient.id}>{ingredient.name}</li>
            )
          })}
        </ul>
        <div><EditBar isSelected={isSelected} setIsSelected={setIsSelected} ingredientsArr={ingredientsArr} handleSubmit={handleSubmit}/></div>
      </div>
    );
  }
}

export default MyBar;
