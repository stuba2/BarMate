import { useState } from 'react';
import './EditBar.css'
import { useSelector } from 'react-redux';
import EditBarButton from '../EditBarButton/EditBarButton';

const EditBar = ({ setIsSelected, ingredientsArr, handleSubmit }) => {
  const [ ingName, setIngName ] = useState()
  const userBar = useSelector(state => state.bar)
  let userBarr = Object.values(userBar).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })

  return (
    <div className="edit-bar-button-container">
      <form onSubmit={handleSubmit}></form>
      {ingredientsArr.map((ingredient) => {
        return (
          <EditBarButton key={ingredient.id} ingredient={ingredient} handleSubmit={handleSubmit} setIsSelected={setIsSelected}/>
        )
      })}
    </div>
  );
}

export default EditBar;
