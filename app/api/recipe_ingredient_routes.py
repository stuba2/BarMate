from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, RecipeIngredient, Recipe, Ingredient
from ..forms.recipe_ingredient_form import RecipeIngredientForm

recipe_ingredient_routes = Blueprint('recipe_ingredients', __name__)

@recipe_ingredient_routes.route('/', methods=['POST'])
def add_recipe_ingredient():
  form = RecipeIngredientForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if form.validate_on_submit():
    new_recipe_ingredient = RecipeIngredient(
      amount = form.data['amount'],
      unit = form.data['unit'],
      ingredient_id = form.data['ingredient_id'],
      recipe_id = form.data['recipe_id']
    )
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

@recipe_ingredient_routes.route('/<int:recipe_ingredient_id>', methods=['PUT'])
def edit_recipe_ingredient(recipe_ingredient_id):
  form = RecipeIngredientForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  recipe_full = Recipe.query.get(form.data['recipe_id'])
  ingredient_full = Ingredient.query.get(form.data['ingredient_id'])


  existing_ri = RecipeIngredient.query.get(recipe_ingredient_id)

  if not existing_ri:
    new_recipe_ingredient = RecipeIngredient(
      amount = form.data['amount'],
      unit = form.data['unit'],
      ingredient_id = form.data['ingredient_id'],
      recipe_id = form.data['recipe_id']
    )
    db.session.add(new_recipe_ingredient)
    db.session.commit()

    ret = {
      'id': new_recipe_ingredient.id,
      'amount': new_recipe_ingredient.amount,
      'unit': new_recipe_ingredient.to_dict()['unit'].value,
      'ingredient_id': new_recipe_ingredient.ingredient_id,
      'recipe_id': new_recipe_ingredient.recipe_id
    }

    return ret

  if existing_ri:
    existing_ri.amount = form.data['amount']
    existing_ri.unit = form.data['unit']
    existing_ri.ingredient_id = form.data['ingredient_id']
    existing_ri.recipe_id = form.data['recipe_id']
    db.session.commit()

    ret = {
      'id': existing_ri.id,
      'amount': existing_ri.amount,
      'unit': existing_ri.to_dict()['unit'].value,
      'ingredient_id': existing_ri.ingredient_id,
      'recipe_id': existing_ri.recipe_id
    }

    return ret

  return {
    'message': 'Bad Request',
    'errors': form.errors
  }
