from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Ingredient, User, RecipeImage
from ..forms.recipe_form import RecipeForm
from ..forms.recipe_image_form import RecipeImageForm
from ..models.ingredient import bar_ingredients

bar_routes = Blueprint('bars', __name__)

@bar_routes.route('/')
def get_bar():
  ret = []
  # bar_ingredients_wrong = Ingredient.query.filter(Ingredient.bar_ingredients_users == current_user.id).all() ######### wrong

  bar_ingredients_correct = Ingredient.query.join(bar_ingredients).join(User).filter((bar_ingredients.c.ingredient_id == Ingredient.id) & (bar_ingredients.c.user_id == current_user.id)).all()
  bar_ingredients_list = []
  for ingredient in bar_ingredients_correct:
    bar_ingredients_list.append(ingredient.to_dict())

  # for ingredient in bar_ingredients_wrong:
  #   ret_ingredient = {
  #     'id': ingredient.id,
  #     'name': ingredient.name,
  #     'created_at': ingredient.created_at,
  #     'updated_at': ingredient.updated_at
  #   }

  #   ret.append(ret_ingredient)

  return {
    'Bar Ingredients': bar_ingredients_list
  }

######### needs work
@bar_routes.route('/', methods=['POST'])
def create_bar(ingredient_list):
  form = RecipeForm() # bar form? not sure this will work with how i'm going about it
  form['csrf_token'].data = request.cookies['csrf_token']
  user = User.query.filter(User.id == current_user.id).first()

  if form.validate_on_submit():
    ret = []
    for ingredient in ingredient_list:
      item = Ingredient.query.filter(Ingredient.id == ingredient.id)

      item.bar_ingredients_users.append(user)
      db.session.commit()

      ret.append(item)

    return {
      "Bar": ret
    }

  return {
    'message': 'Bad Request',
    'errors': form.errors
  }

@bar_routes.route('/', methods=['PUT'])
def edit_bar(ingredient_list):
  user = User.query.filter(User.id == current_user.id).first()
  existing_bar_ingredients = Ingredient.query.filter(Ingredient.bar_ingredients_users.id == current_user.id).all()

  # if form.validate_etc
  for ingredient in existing_bar_ingredients:
    db.session.delete(ingredient)
    db.session.commit()

  ret = []
  for ingredient in ingredient_list:
    item = Ingredient.query.filter(Ingredient.id == ingredient.id)

    item.bar_ingredients_users.append(user)
    db.session.commit()

    ret.append(item)

  return {
    'Bar': ret
  }
