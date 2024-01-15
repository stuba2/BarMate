from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Review, Recipe, User, RecipeImage
from ..forms.recipe_form import RecipeForm
from ..forms.recipe_image_form import RecipeImageForm

review_routes = Blueprint('reviews', __name__)

@review_routes.route('/')
def get_all_recipes():
  ret = []
  all_recipes = Recipe.query.all()

  for recipe in all_recipes:
    owner_details = User.query.filter(User.id == recipe.user_id).first()
    ret_recipe = {
      'id': recipe.id,
      'name': recipe.name,
      'description': recipe.description,
      'instructions': recipe.instructions,
      'user_id': recipe.user_id,
      'owner_details': {
        'username': owner_details.username,
        'dob': owner_details.dob,
        'bar_id': owner_details.bar_id
      },
      'created_at': recipe.created_at,
      'updated_at': recipe.updated_at
    }

    ret.append(ret_recipe)

  return {
    'Recipes': ret
  }

@review_routes.route('/<int:recipe_id>', methods=['GET'])
def get_one_recipe(recipe_id):
  ret = []
  recipe = Recipe.query.filter(Recipe.id == recipe_id).first()

  owner_details = User.query.filter(User.id == recipe.user_id).first()
  ret_recipe = {
    'id': recipe.id,
    'name': recipe.name,
    'description': recipe.description,
    'instructions': recipe.instructions,
    'user_id': recipe.user_id,
    'owner_details': {
      'username': owner_details.username,
      'dob': owner_details.dob,
      'bar_id': owner_details.bar_id
    },
    'created_at': recipe.created_at,
    'updated_at': recipe.updated_at
  }

  ret.append(ret_recipe)

  return {
    'Recipe': ret
  }

@review_routes.route('/user', methods=['GET'])
def get_users_recipes():
  ret = []
  user_recipes = Recipe.query.filter(Recipe.user_id == current_user.id).all()

  for recipe in user_recipes:
    owner_details = User.query.filter(User.id == recipe.user_id).first()
    ret_recipe = {
      'id': recipe.id,
      'name': recipe.name,
      'description': recipe.description,
      'instructions': recipe.instructions,
      'user_id': recipe.user_id,
      'owner_details': {
        'username': owner_details.username,
        'dob': owner_details.dob,
        'bar_id': owner_details.bar_id
      },
      'created_at': recipe.created_at,
      'updated_at': recipe.updated_at
    }

    ret.append(ret_recipe)

  return {
    'Recipes': ret
  }

@review_routes.route('/', methods=['POST'])
def create_a_recipe():
  owner_details = User.query.filter(User.id == current_user.id).first()
  form = RecipeForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if form.validate_on_submit():
    new_recipe = Recipe(
      name = form.data['name'],
      description = form.data['description'],
      instructions = form.data['instructions'],
      user_id = current_user.get_id()
    )
    db.session.add(new_recipe)
    db.session.commit()

    ret = {
      'id': new_recipe.id,
      'name': new_recipe.name,
      'description': new_recipe.description,
      'instructions': new_recipe.instructions,
      'user_id': new_recipe.user_id,
      'owner_details': {
        'username': owner_details.username,
        'dob': owner_details.dob,
        'bar_id': owner_details.bar_id
      },
      'created_at': new_recipe.created_at,
      'updated_at': new_recipe.updated_at
    }

    return ret

  return {
    'message': 'Bad Request',
    'errors': form.errors
  }

@review_routes.route('/<int:recipe_id>/image', methods=['POST'])
def create_image_on_recipe(recipe_id):
  form = RecipeImageForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if form.validate_on_submit():
    new_recipe_image = RecipeImage(
      recipe_id = recipe_id,
      url = form.data['url']
    )
    db.session.add(new_recipe_image)
    db.session.commit()

    ret = {
      'id': new_recipe_image.id,
      'recipe_id': new_recipe_image.recipe_id,
      'url': new_recipe_image.url
    }

    return ret

  return {
    'message': 'Bad Request',
    'errors': form.errors
  }

@review_routes.route('/<int:recipe_id>', methods=['PUT'])
def edit_a_recipe(recipe_id):
  existing_recipe = Recipe.query.get(recipe_id)
  owner_details = User.query.filter(User.id == existing_recipe.user_id).first()
  form = RecipeForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if not existing_recipe:
    return {
      'message': 'Recipe does not exist'
    }

  if form.validate_on_submit():
    existing_recipe.url = form.data['url']
    db.session.commit()
    ret = {
      'id': existing_recipe.id,
      'recipe_id': existing_recipe.recipe_id,
      'url': existing_recipe.url
    }

    return ret

  return {
    'message': 'Bad Request',
    'errors': form.errors
  }

@review_routes.route('/<int:recipe_id>', methods=['DELETE'])
def delete_a_recipe(recipe_id):
  recipe_to_delete = Recipe.query.filter(Recipe.id == recipe_id).first()

  if not recipe_to_delete:
    return {
      "message": "Recipe does not exist"
    }

  db.session.delete(recipe_to_delete)
  db.session.commit()

  return {
    "message": "Successfully Deleted"
  }
