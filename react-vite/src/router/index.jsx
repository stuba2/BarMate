import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import AllRecipes from '../components/AllRecipes/AllRecipes';
import OneRecipe from '../components/OneRecipe/OneRecipe';
import MyBar from '../components/MyBar/MyBar';
import Layout from './Layout';
import AllIngredients from '../components/AllIngredients/AllIngredients';
import CreateRecipe from '../components/CreateRecipe/CreateRecipe';
import EditRecipe from '../components/EditRecipe/EditRecipe';
import CreateIngredient from '../components/CreateIngredient/CreateIngredient';
import CreateReview from '../components/CreateReview/CreateReview';
import UsersRecipes from '../components/UsersRecipes/UsersRecipes';
import EditBar from '../components/EditBar/EditBar';
import MakableRecipes from '../components/MakeableRecipes/MakableRecipes';
import LandingPage from '../components/LandingPage/LandingPage';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <LandingPage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "/recipes",
        element: <AllRecipes />
      },
      {
        path: "/recipes/index/:page",
        element: <AllRecipes />
      },
      {
        path: "/recipes/new",
        element: <CreateRecipe />
      },
      {
        path: "/recipes/makable",
        element: <MakableRecipes />
      },
      {
        path: "/recipes/:recipeId/edit",
        element: <EditRecipe />
      },
      {
        path: "/recipes/:recipeId",
        element: <OneRecipe />
      },
      {
        path: "/account/myBar",
        element: <MyBar />
      },
      {
        path: "/account/myBar/edit",
        element: <EditBar />
      },
      {
        path: "/account/myCocktails",
        element: <UsersRecipes />
      },
      {
        path: "/ingredients",
        element: <AllIngredients />
      },
      {
        path: "/ingredients/new",
        element: <CreateIngredient />
      },
      {
        path: "/reviews/new",
        element: <CreateReview />
      },
    ],
  },
]);
