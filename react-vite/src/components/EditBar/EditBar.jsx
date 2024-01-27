import { useDispatch, useSelector } from "react-redux";

const EditBar = ({ setIsSelected, ingredientsArr, handleSubmit }) => {

  return (
    <>
    <form onSubmit={handleSubmit}></form>
    {ingredientsArr.map((ingredient) => {
      return (
        <form action="" onSubmit={handleSubmit} key={ingredient.id}>
          <button onClick={() => setIsSelected(ingredient.name)}>
            {ingredient.name}
          </button>
        </form>
      )
    })}
    </>
  );
}

export default EditBar;
