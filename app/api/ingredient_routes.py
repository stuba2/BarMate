from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Ingredient, User, IngredientImage
from ..forms.ingredient_form import IngredientForm
from ..forms.ingredient_image_form import IngredientImageForm

ingredient_routes = Blueprint('ingredients', __name__)

@ingredient_routes.route('/')
def get_all_ingredients():
  ret = []
  all_ingredients = Ingredient.query.order_by(Ingredient.name).all()

  for ingredient in all_ingredients:
    ret_ingredient = {
      'id': ingredient.id,
      'name': ingredient.name,
      'created_at': ingredient.created_at,
      'updated_at': ingredient.updated_at
    }

    ret.append(ret_ingredient)

  return {
    'Ingredients': ret
  }

@ingredient_routes.route('/<int:ingredient_id>', methods=['GET'])
def get_one_ingredient(ingredient_id):
  ret = []
  ingredient = Ingredient.query.filter(Ingredient.id == ingredient_id).first()

  ret_ingredient = {
    'id': ingredient.id,
    'name': ingredient.name,
    'created_at': ingredient.created_at,
    'updated_at': ingredient.updated_at
  }

  ret.append(ret_ingredient)

  return {
    'Ingredient': ret
  }

@ingredient_routes.route('/', methods=['POST'])
def create_an_ingredient():
  form = IngredientForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if form.validate_on_submit():
    new_ingredient = Ingredient(
      name = form.data['name']
    )
    db.session.add(new_ingredient)
    db.session.commit()

    ret = {
      'id': new_ingredient.id,
      'name': new_ingredient.name,
      'created_at': new_ingredient.created_at,
      'updated_at': new_ingredient.updated_at
    }

    return ret

  return {
    'message': 'Bad Request',
    'errors': form.errors
  }

@ingredient_routes.route('/<int:ingredient_id>/image', methods=['POST'])
def create_image_on_ingredient(ingredient_id):
  form = IngredientImageForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if form.validate_on_submit():
    new_ingredient_image = IngredientImage(
      ingredient_id = ingredient_id,
      url = form.data['url']
    )
    db.session.add(new_ingredient_image)
    db.session.commit()

    ret = {
      'id': new_ingredient_image.id,
      'ingredient_id': new_ingredient_image.ingredient_id,
      'url': new_ingredient_image.url
    }

    return ret

  return {
    'message': 'Bad Request',
    'errors': form.errors
  }
