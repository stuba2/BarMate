import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import AllRecipes from '../components/AllRecipes/AllRecipes';
import OneRecipe from '../components/OneRecipe/OneRecipe';
import MyBar from '../components/MyBar/MyBar';
import Layout from './Layout';
import AllIngredients from '../components/AllIngredients/AllIngredients';
import CreateRecipe from '../components/CreateRecipe/CreateRecipe';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <h1>Welcome!</h1>,
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
        path: "/recipes/new",
        element: <CreateRecipe />
      },
      {
        path: "/recipes/:recipeId",
        element: <OneRecipe />
      },
      {
        path: "/myBar",
        element: <MyBar />
      },
      {
        path: "/ingredients",
        element: <AllIngredients />
      },
    ],
  },
]);
