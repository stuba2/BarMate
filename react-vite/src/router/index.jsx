import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import AllRecipes from '../components/AllRecipes/AllRecipes';
import OneRecipe from '../components/OneRecipe/OneRecipe';
import MyBar from '../components/Bar/Bar';
import Layout from './Layout';

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
        path: "/recipes/:recipeId",
        element: <OneRecipe />
      },
      {
        path: "/myBar",
        element: <MyBar />
      },
    ],
  },
]);
