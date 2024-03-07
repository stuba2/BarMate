import './EditBar.css'
import { useSelector } from 'react-redux';
import EditBarButton from '../EditBarButton/EditBarButton';

const EditBar = ({ ingredientsArr}) => {
  const userBar = useSelector(state => state.bar)

  return (
    <div className="edit-bar-button-container">
      {ingredientsArr.map((ingredient) => {
        const ingBool = userBar[ingredient.id] ? true : false
        return (
          <EditBarButton key={ingredient.id} ingredient={ingredient} ingBool={ingBool} />
        )
      })}
    </div>
  );
}

export default EditBar;
