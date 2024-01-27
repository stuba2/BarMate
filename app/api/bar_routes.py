from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Ingredient, User, RecipeImage
from ..forms.bar_form import BarForm
from ..models.ingredient import bar_ingredients

bar_routes = Blueprint('bars', __name__)

@bar_routes.route('/')
# @login_required
def get_bar():
  bar_ings = Ingredient.query.join(bar_ingredients).join(User).filter((bar_ingredients.c.ingredient_id == Ingredient.id) & (bar_ingredients.c.user_id == current_user.get_id())).all()

  bar_ingredients_list = []
  for ingredient in bar_ings:
    bar_ingredients_list.append(ingredient.to_dict())

  return {
    'Bar Ingredients': bar_ingredients_list
  }

@bar_routes.route('/', methods=['POST'])
def create_bar():
  form = BarForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  user = User.query.filter(User.id == current_user.id).first()

  if form.validate_on_submit():
    ret = []
    # for ingredient in ingredient_list:
    ing = Ingredient.query.filter(Ingredient.id == form.data['ingredient_id']).first()

    ing.bar_ingredients_users.append(user)
    db.session.commit()

    ret_ing = {
      'id': ing.id,
      'name': ing.name,
      'created_at': ing.created_at,
      'updated_at': ing.updated_at
    }

    return ret_ing

  return {
    'message': 'Bad Request',
    'errors': form.errors
  }

@bar_routes.route('/<int:ingredient_id>', methods=['DELETE'])
def delete_bar(ingredient_id):
  user = User.query.filter(User.id == current_user.id).first()
  # existing_bar_ingredients = Ingredient.query.filter(Ingredient.bar_ingredients_users.id == current_user.id).all()
  existing_ing = Ingredient.query.filter(Ingredient.id == ingredient_id).first()
  print('\n ---', existing_ing)
  print('\n ---', existing_ing.name)
  print('\n ---', existing_ing.bar_ingredients_users) # this is a list of users that have this ingredient in their bar

  print('\n +++', existing_ing.bar_ingredients_users) # this is a list of users that have this ingredient in their bar

  if not user:
    return {
      "message": "User does not exist"
    }

  if not existing_ing:
    return {
      "message": "Ingredient does not exist"
    }


  existing_ing.bar_ingredients_users.remove(user)

  return {
    "message": "Successfully Deleted"
  }
