import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, Navigate, useNavigate, useParams } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as recipeActions from "../../redux/recipes"

const UsersRecipes = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  let { page } = useParams()
  const recipes = useSelector(state => state.recipes)
  if (!page) page = 1

  useEffect(() => {
    dispatch(recipeActions.getUsersRecipesTHunk())
  }, [dispatch, page])

  let recipesArr = Object.values(recipes)
  console.log('recipesArr: ', recipesArr)
  // let paginatedRecipes = recipes? do it from the store?
    // probably should do it from the api side. only send the first 10/20 recipes?


  // let previousPage = `/recipes/index/${+page - 1}`
  // let nextPage = `/recipes/index/${+page + 1}`


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
            <div key={recipe.id} className="one-recipe-container">
              <img src={recipe.recipe_image_url} width="100"></img>
              <div>{recipe.name}</div>
            </div>
          )
        })}
      </div>
      {/* <div><NavLink to={previousPage}>Previous page (Under Construction, please change the url to navigate to previous page)</NavLink></div>
      <div><NavLink to={nextPage}>Next page (Under Construction, please change the url to navigate to next page)</NavLink></div> */}
      </>
    );
  }
}

export default UsersRecipes;
