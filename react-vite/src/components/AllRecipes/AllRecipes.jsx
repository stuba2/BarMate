import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, Navigate, useNavigate, useParams } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as recipeActions from "../../redux/recipes"
import OnceRecipeSmall from "../OneRecipeSmall/OneRecipeSmall";
import './AllRecipes.css'

const AllRecipes = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  let { page } = useParams()
  const recipes = useSelector(state => state.recipes)
  if (!page) page = 1

  useEffect(() => {
    dispatch(recipeActions.getRecipesThunk(page))
  }, [dispatch, page])

  let recipesArr = Object.values(recipes)
  // let paginatedRecipes = recipes? do it from the store?
    // probably should do it from the api side. only send the first 10/20 recipes?


  let previousPage = `/recipes/index/${+page - 1}`
  let nextPage = `/recipes/index/${+page + 1}`


  if (!recipes) {
    return (
      <div>...loading</div>
    )
  } else {
    return (
      <>
      <div className="recipes-container">
        {recipesArr.map((recipe) => {
          return (
            <NavLink
              to={`/recipes/${recipe.id}`}
              className="one-recipe-container"
              key={recipe.id}
              title={recipe.name}>
                <OnceRecipeSmall recipeId={recipe.id}/>
              </NavLink>
          )
        })}
      </div>
      {/* <div><NavLink to={previousPage}>Previous page (Under Construction, please change the url to navigate to previous page)</NavLink></div> */}
      <div className="more-cocktails-container"><NavLink className="more-cocktails" to={nextPage}>More cocktails...</NavLink></div>
      </>
    );
  }
}

export default AllRecipes;
