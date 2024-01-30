import { useState } from "react"
import { useSelector } from "react-redux"

const EditBarButton = ({ ingredient, handleSubmit, setIsSelected}) => {
  const userBar = useSelector(state => state.bar)
  const [ ingName, setIngName ] = useState()
  let userBarr = Object.values(userBar).sort((a,b) => {
    if (a.name < b.name) return -1
    if (a.name > b.name) return 1
    return 0
  })

  let buttonClassName
  let target = userBarr.find(ingObj => ingObj.name === ingredient.name)

  if (target) buttonClassName = 'edit-bar-button-button ing-in-bar'
  if (!target) buttonClassName = 'edit-bar-button-button'

  return (
    <div>
      <form action="" onSubmit={handleSubmit} key={ingredient.id}>
        <button className={buttonClassName} id={ingredient.name} onClick={() =>{
          setIsSelected(ingredient.name)
          setIngName(ingredient.name)
          }}>
          {ingredient.name}
        </button>
      </form>
    </div>
  )
}

export default EditBarButton
