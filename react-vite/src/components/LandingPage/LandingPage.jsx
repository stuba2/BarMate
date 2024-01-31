import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import * as recipeActions from '../../redux/recipes'
import './LandingPage.css'
import { NavLink } from "react-router-dom"
import OnceRecipeSmall from "../OneRecipeSmall/OneRecipeSmall"

const LandingPage = ({}) => {
  const dispatch = useDispatch()
  const recipes = useSelector(state => state.recipes)
  const displayRec = Object.values(recipes)[0]


  useEffect(() => {
    dispatch(recipeActions.getRandomRecipeThunk())
  }, [dispatch])


  if (!recipes || !displayRec) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <div className="land-main-contain">
        <div className="land-main-small-container">
          <h1 className="land-h1">Welcome!</h1>
          <div><NavLink to="/account/myBar" className="land-update-bar">Update your Bar</NavLink></div>
          <div className="land-rand-rec-container">
            <h2>Featured Cocktail</h2>
            <div className="land-rand-name">{displayRec.name}</div>
            <NavLink
              to={`/recipes/${displayRec.id}`}
              className="land-rand-rec-nav"
              key={displayRec.id}
              title={displayRec.name}>
                <OnceRecipeSmall recipeId={displayRec.id} />
              </NavLink>
          </div>
        </div>
      </div>
    )
  }
}

export default LandingPage
