from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, RecipeIngredient
from ..forms.recipe_ingredient_form import RecipeIngredientForm

recipe_ingredient_routes = Blueprint('recipe_ingredients', __name__)

@recipe_ingredient_routes.route('/', methods=['POST'])
def add_recipe_ingredient():
  print('\n ********* in the route')
  form = RecipeIngredientForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if form.validate_on_submit():
    print('\n ==== form is doing good')
    new_recipe_ingredient = RecipeIngredient(
      amount = form.data['amount'],
      unit = form.data['unit'],
      ingredient_id = form.data['ingredient_id'],
      recipe_id = form.data['recipe_id']
    )
    print('\n --- new RI: ', new_recipe_ingredient)
    db.session.add(new_recipe_ingredient)
    db.session.commit()

    ret = {
      'id': new_recipe_ingredient.id,
      'amount': new_recipe_ingredient.amount,
      'unit': new_recipe_ingredient.unit,
      'ingredient_id': new_recipe_ingredient.ingredient_id,
      'recipe_id': new_recipe_ingredient.recipe_id
    }

    return ret

  return {
    'message': 'Bad Request',
    'errors': form.errors
  }