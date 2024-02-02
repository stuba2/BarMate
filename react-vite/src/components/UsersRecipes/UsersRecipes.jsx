import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, Navigate, useNavigate, useParams } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import * as recipeActions from "../../redux/recipes"
import OnceRecipeSmall from "../OneRecipeSmall/OneRecipeSmall";
import './UsersRecipes.css'
import OpenModalButton from "../OpenModalButton/OpenModalButton";
import DeleteRecipe from "../DeleteRecipe/DeleteRecipe";

const UsersRecipes = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  let { page } = useParams()
  const recipes = useSelector(state => state.recipes)
  if (!page) page = 1

  useEffect(() => {
    dispatch(recipeActions.getUsersRecipesThunk())
  }, [dispatch, page])

  let recipesArr = Object.values(recipes)
  // console.log('recipesArr: ', recipesArr)
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
      <div>
        <div className="recipes-container">
          {recipesArr.map((recipe) => {
            return (
              <div key={recipe.id}>
                <NavLink
                  to={`/recipes/${recipe.id}`}
                  className="one-recipe-container"
                  key={recipe.id}
                  title={recipe.name}>
                    <OnceRecipeSmall recipeId={recipe.id}/>
                </NavLink>
                <div className="edit-delete-rec-button-container">
                  <NavLink to={`/recipes/${recipe.id}/edit`}>
                    <button className="edit-rec-button">
                      Edit Recipe
                    </button>
                  </NavLink>
                  <OpenModalButton
                    buttonText="Delete Recipe"
                    modalComponent={<DeleteRecipe recipeId={recipe.id} />}
                  />
                </div>
              </div>
            )
          })}
        </div>
      {/* <div><NavLink to={previousPage}>Previous page (Under Construction, please change the url to navigate to previous page)</NavLink></div>
      <div><NavLink to={nextPage}>Next page (Under Construction, please change the url to navigate to next page)</NavLink></div> */}
      </div>
    );
  }
}

export default UsersRecipes;
