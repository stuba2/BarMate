from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Recipe, User, RecipeImage, Review, Toast, Ingredient, RecipeIngredient
from ..forms.recipe_form import RecipeForm
from ..forms.recipe_image_form import RecipeImageForm
from ..forms.review_form import ReviewForm
from ..forms.toast_form import ToastForm
from ..forms.recipe_edit_form import RecipeEditForm
from ..models.ingredient import bar_ingredients
import random

recipe_routes = Blueprint('recipes', __name__)

@recipe_routes.route('/index/<int:page>')
def get_paginated_recipes(page):
  ret = []
  print('\n page:::::', page)
  per_page = 8
  all_recipes = Recipe.query.all()
  # paginated = db.paginate(all_recipes, page=1, per_page=per_page, error_out=False)
  paginated = Recipe.query.paginate(page=page, per_page=per_page)
  print('\n ::::::::::', paginated)
  print('\n ::::::::::', paginated.items)
  # print('\n ::::::::::', paginated.ret.allrecipes)

  for recipe in paginated.items:
    owner_details = User.query.filter(User.id == recipe.user_id).first()

    recipe_ingredients = RecipeIngredient.query.filter(RecipeIngredient.recipe_id == recipe.id).all()

    recipe_image = RecipeImage.query.filter(RecipeImage.recipe_id == recipe.id).first()
    recipe_ingredient_list = []
    for ingredient in recipe_ingredients:
      ingredient_name = Ingredient.query.get(ingredient.ingredient_id)
      unit = ingredient.to_dict()['unit'].value
      real_ingredient = {
        'name': ingredient_name.name,
        'amount': ingredient.amount,
        'unit': unit,
        'recipe_id': ingredient.recipe_id,
        'ingredient_id': ingredient.ingredient_id
      }
      recipe_ingredient_list.append(real_ingredient)

    ret_recipe = {
      'id': recipe.id,
      'name': recipe.name,
      'description': recipe.description,
      'instructions': recipe.instructions,
      'user_id': recipe.user_id,
      'owner_details': {
        'username': owner_details.username,
        'dob': owner_details.dob
      },
      'recipe_image_url': recipe_image.url,
      'recipe_ingredients': recipe_ingredient_list,
      'created_at': recipe.created_at,
      'updated_at': recipe.updated_at
    }

    ret.append(ret_recipe)

  return {
    'Recipes': ret
  }

@recipe_routes.route('/')
def get_all_recipes():
  ret = []
  all_recipes = Recipe.query.join('recipes_recipe_ingredients').join('recipe_recipe_image').join('recipes_user').join(Ingredient).all()

  for recipe in all_recipes:
    owner_details = recipe.recipes_user
    recipe_image = recipe.recipe_recipe_image[0]

    recipe_ingredients = recipe.recipes_recipe_ingredients
    recipe_ingredient_list = []

    for ingredient in recipe_ingredients:
      unit = ingredient.to_dict()['unit'].value
      real_ingredient = {
        'name': ingredient.recipe_ingredients_ingredients.name,
        'amount': ingredient.amount,
        'unit': unit,
        'recipe_id': ingredient.recipe_id,
        'ingredient_id': ingredient.ingredient_id
      }
      recipe_ingredient_list.append(real_ingredient)

    ret_recipe = {
      'id': recipe.id,
      'name': recipe.name,
      'description': recipe.description,
      'instructions': recipe.instructions,
      'user_id': recipe.user_id,
      'owner_details': {
        'username': owner_details.username,
        'dob': owner_details.dob
      },
      'recipe_image_url': recipe_image.url if recipe_image else None,
      'recipe_ingredients': recipe_ingredient_list,
      'created_at': recipe.created_at,
      'updated_at': recipe.updated_at
    }

    ret.append(ret_recipe)
    
  return {
    'Recipes': ret
  }

@recipe_routes.route('/<int:recipe_id>', methods=['GET'])
def get_one_recipe(recipe_id):
  ret = []
  recipe = Recipe.query.filter(Recipe.id == recipe_id).first()

  owner_details = User.query.filter(User.id == recipe.user_id).first()

  recipe_ingredients = RecipeIngredient.query.filter(RecipeIngredient.recipe_id == recipe.id).all()
  recipe_image = RecipeImage.query.filter(RecipeImage.recipe_id == recipe.id).first()

  recipe_ingredient_list = []
  for ingredient in recipe_ingredients:
    ingredient_name = Ingredient.query.get(ingredient.ingredient_id)
    unit = ingredient.to_dict()['unit'].value
    real_ingredient = {
      'id': ingredient.id,
      'name': ingredient_name.name,
      'amount': ingredient.amount,
      'unit': unit,
      'recipe_id': ingredient.recipe_id,
      'ingredient_id': ingredient.ingredient_id
    }
    recipe_ingredient_list.append(real_ingredient)

  ret_recipe = {
    'id': recipe.id,
    'name': recipe.name,
    'description': recipe.description,
    'instructions': recipe.instructions,
    'user_id': recipe.user_id,
    'owner_details': {
      'username': owner_details.username,
      'dob': owner_details.dob
    },
    'recipe_image_url': recipe_image.url if recipe_image else None,
    'recipe_ingredients': recipe_ingredient_list,
    'created_at': recipe.created_at,
    'updated_at': recipe.updated_at
  }

  ret.append(ret_recipe)

  return {
    'Recipe': ret
  }

@recipe_routes.route('/random', methods=['GET'])
def get_random_recipe():
  ret = []
  all_recipes = Recipe.query.all()
  total_recipes = Recipe.query.count()
  random_num = random.randrange(1,total_recipes)
  rand_recipe = all_recipes[random_num - 1]
  owner_details = User.query.filter(User.id == rand_recipe.user_id).first()
  recipe_image = RecipeImage.query.filter(RecipeImage.recipe_id == rand_recipe.id).first()
  recipe_ingredients = RecipeIngredient.query.filter(RecipeIngredient.recipe_id == rand_recipe.id).all()

  recipe_ingredient_list = []
  for ingredient in recipe_ingredients:
    ingredient_name = Ingredient.query.get(ingredient.ingredient_id)
    unit = ingredient.to_dict()['unit'].value
    real_ingredient = {
      'name': ingredient_name.name,
      'amount': ingredient.amount,
      'unit': unit,
      'recipe_id': ingredient.recipe_id,
      'ingredient_id': ingredient.ingredient_id
    }
    recipe_ingredient_list.append(real_ingredient)

  ret_recipe = {
      'id': rand_recipe.id,
      'name': rand_recipe.name,
      'description': rand_recipe.description,
      'instructions': rand_recipe.instructions,
      'user_id': rand_recipe.user_id,
      'owner_details': {
        'username': owner_details.username,
        'dob': owner_details.dob
      },
      'recipe_image_url': recipe_image.url if recipe_image else None,
      'recipe_ingredients': recipe_ingredient_list,
      'created_at': rand_recipe.created_at,
      'updated_at': rand_recipe.updated_at
    }

  ret.append(ret_recipe)

  return {
    'Recipe': ret
  }

@recipe_routes.route('/makable', methods=['GET'])
def get_makable_recipes():
  ret = []
  all_recipes = Recipe.query.join('recipes_recipe_ingredients').join('recipe_recipe_image').join('recipes_user').join(Ingredient).all()
  print('\n ********************: ', all_recipes[0].to_dict())

  my_bar = Ingredient.query.join(bar_ingredients).join(User).filter((bar_ingredients.c.ingredient_id == Ingredient.id) & (bar_ingredients.c.user_id == current_user.get_id())).order_by(Ingredient.name).all()
  ing_ids = []
  for ing in my_bar:
    ing_ids.append(ing.id)

  bar_ing_set = set(ing_ids)

  print('\n all_recs: ', all_recipes)
  for recipe in all_recipes:
    ris = recipe.recipes_recipe_ingredients
    ri_id = [ri.ingredient_id for ri in ris]
    found = set(ri_id).issubset(bar_ing_set)
    if found:
      owner_details = recipe.recipes_user
      recipe_image = recipe.recipe_recipe_image[0]



      recipe_ingredient_list = []
      for ingredient in ris:
        unit = ingredient.to_dict()['unit'].value
        real_ingredient = {
          'id': ingredient.id,
          'name': ingredient.recipe_ingredients_ingredients.name,
          'amount': ingredient.amount,
          'unit': unit,
          'recipe_id': ingredient.recipe_id,
          'ingredient_id': ingredient.ingredient_id
        }
        recipe_ingredient_list.append(real_ingredient)

      ret_recipe = {
        'id': recipe.id,
        'name': recipe.name,
        'description': recipe.description,
        'instructions': recipe.instructions,
        'user_id': recipe.user_id,
        'owner_details': {
          'username': owner_details.username,
          'dob': owner_details.dob
        },
        'recipe_image_url': recipe_image.url if recipe_image else None,
        'recipe_ingredients': recipe_ingredient_list,
        'created_at': recipe.created_at,
        'updated_at': recipe.updated_at
      }
      ret.append(ret_recipe)

  print('\n ==============', ret)

  return {
    "ret": ret
  }

@recipe_routes.route('/user', methods=['GET'])
def get_users_recipes():
  ret = []
  user_recipes = Recipe.query.filter(Recipe.user_id == current_user.id).all()

  for recipe in user_recipes:
    owner_details = User.query.filter(User.id == recipe.user_id).first()
    recipe_image = RecipeImage.query.filter(RecipeImage.recipe_id == recipe.id).first()
    recipe_ingredient_list = []

    ret_recipe = {
      'id': recipe.id,
      'name': recipe.name,
      'description': recipe.description,
      'instructions': recipe.instructions,
      'user_id': recipe.user_id,
      'owner_details': {
        'username': owner_details.username,
        'dob': owner_details.dob,
      },
      'recipe_image_url': recipe_image.url if recipe_image else None,
      'recipe_ingredients': recipe_ingredient_list,
      'created_at': recipe.created_at,
      'updated_at': recipe.updated_at
    }

    ret.append(ret_recipe)

  return {
    'Recipes': ret
  }

@recipe_routes.route('/', methods=['POST'])
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
      },
      'created_at': new_recipe.created_at,
      'updated_at': new_recipe.updated_at
    }

    return ret

  return {
      "Errors": form.errors
    }, 500

@recipe_routes.route('/<int:recipe_id>/image', methods=['POST'])
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

@recipe_routes.route('/<int:recipe_id>', methods=['PUT'])
def edit_a_recipe(recipe_id):
  existing_recipe = Recipe.query.get(recipe_id)
  owner_details = User.query.filter(User.id == existing_recipe.user_id).first()
  recipe_image = RecipeImage.query.filter(RecipeImage.recipe_id == existing_recipe.id).first()
  form = RecipeEditForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if not existing_recipe:
    return {
      'message': 'Recipe does not exist'
    }

  if form.validate_on_submit():
    existing_recipe.name = form.data['name']
    existing_recipe.description = form.data['description']
    existing_recipe.instructions = form.data['instructions']
    db.session.commit()

    ret = {
      'id': existing_recipe.id,
      'name': existing_recipe.name,
      'description': existing_recipe.description,
      'instructions': existing_recipe.instructions,
      'user_id': existing_recipe.user_id,
      'owner_details': {
        'username': owner_details.username,
        'dob': owner_details.dob,
      },
      'recipe_image_url': recipe_image.url if recipe_image else None,
      'created_at': existing_recipe.created_at,
      'updated_at': existing_recipe.updated_at
    }

    return ret

  return {
    'message': 'Bad Request',
    'errors': form.errors
  }

@recipe_routes.route('/<int:recipe_id>/image', methods=['PUT'])
def edit_image_on_recipe(recipe_id):
  form = RecipeImageForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  recipe = Recipe.query.get(recipe_id)
  existing_img = RecipeImage.query.filter(RecipeImage.recipe_id == recipe.id).first()

  if form.validate_on_submit():
    existing_img.url = form.data['url']
    db.session.commit()

    ret = {
      'id': existing_img.id,
      'recipe_id': existing_img.recipe_id,
      'url': existing_img.url
    }

    return ret

  return {
    'message': 'Bad Request',
    'errors': form.errors
  }

@recipe_routes.route('/<int:recipe_id>', methods=['DELETE'])
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

# reorder these
@recipe_routes.route('/<int:recipe_id>/reviews', methods=["POST"])
# @login_required
def post_review(recipe_id):
  recipe = Recipe.query.get(recipe_id)
  reviewer_details = User.query.filter(User.id == current_user.id).first()
  form = ReviewForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if not recipe:
    return {
      "message": "Recipe does not exist"
    }

  if form.validate_on_submit():
    new_review = Review(
      review_text = form.data['review_text'],
      rating = form.data['rating'],
      user_id = current_user.get_id(),
      recipe_id = recipe_id
    )
    db.session.add(new_review)
    db.session.commit()

    ret = {
      'id': new_review.id,
      'review_text': new_review.review_text,
      'rating': new_review.rating,
      'user_id': new_review.user_id,
      'recipe_id': new_review.recipe_id,
      'reviewer_details': {
        'username': reviewer_details.username
      },
      'created_at': new_review.created_at,
      'updated_at': new_review.updated_at
    }

    return ret

  return {
    "message": "Bad Request",
    "errors": form.errors
  }

@recipe_routes.route('/<int:recipe_id>/reviews/<int:review_id>', methods=["PUT"])
# @login_required
def edit_a_review(recipe_id, review_id):
  existing_review = Review.query.get(review_id)
  reviewer_details = User.query.filter(User.id == existing_review.user_id).first()
  form = ReviewForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if not existing_review:
    return {
      "message": "Review does not exist"
    }

  if form.validate_on_submit():
    existing_review.review_text = form.data['review_text']
    existing_review.rating = form.data['rating']
    db.session.commit()
    ret = {
      'id': existing_review.id,
      'review_text': existing_review.review_text,
      'rating': existing_review.rating,
      'user_id': existing_review.user_id,
      'recipe_id': existing_review.recipe_id,
      'reviewer_details': {
        'username': reviewer_details.username
      },
      'created_at': existing_review.created_at,
      'updated_at': existing_review.updated_at
    }

    return ret

  return {
    "message": "Bad Request",
    "errors": form.errors
  }

# @recipe_routes.route('/<int:recipe_id>/reviews/<int:review_id>', methods=['DELETE'])
# # @login_required
# def delete_a_review(review_id):
#   review_to_delete = Review.query.filter(Review.id == review_id).first()
#   print('\n -----------review_to_delete: ', review_to_delete)

#   if not review_to_delete:
#     print('\n ==========wrong')
#     return {
#       "message": "Review does not exist"
#     }

#   db.session.delete(review_to_delete)
#   db.session.commit()

#   return {
#     "message": "Successfully Deleted"
#   }

@recipe_routes.route('/<int:recipe_id>/toasts', methods=['GET'])
def get_recipe_toasts(recipe_id):
  ret = []
  all_toasts = Toast.query.filter(Toast.recipe_id == recipe_id).all()

  for toast in all_toasts:
    toaster_details = User.query.filter(User.id == toast.user_id).first()
    ret_toast = {
      'id': toast.id,
      'user_id': toast.user_id,
      'recipe_id': toast.recipe_id,
      'toaster_details': {
        'username': toaster_details.username
      },
      'created_at': toast.created_at,
      'updated_at': toast.updated_at
    }

    ret.append(ret_toast)

  return {
    'Toasts': ret
  }

@recipe_routes.route('/<int:recipe_id>/toasts', methods=["POST"])
# @login_required
def post_toast(recipe_id):
  recipe = Recipe.query.get(recipe_id)
  toaster_details = User.query.filter(User.id == current_user.id).first()
  form = ToastForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if not recipe:
    return {
      "message": "Recipe does not exist"
    }

  if form.validate_on_submit():
    new_toast = Toast(
      user_id = current_user.get_id(),
      recipe_id = recipe_id
    )
    db.session.add(new_toast)
    db.session.commit()

    ret = {
      'id': new_toast.id,
      'user_id': new_toast.user_id,
      'recipe_id': new_toast.recipe_id,
      'toaster_details': {
        'username': toaster_details.username
      },
      'created_at': new_toast.created_at,
      'updated_at': new_toast.updated_at
    }

    return ret

  return {
    "message": "Bad Request",
    "errors": form.errors
  }

@recipe_routes.route('/<int:recipe_id>/toasts', methods=['DELETE'])
# @login_required
def delete_a_toast(recipe_id):
  toast_to_delete = Toast.query.filter(Toast.recipe_id == recipe_id, Toast.user_id == current_user.id).first()

  if not toast_to_delete:
    return {
      "message": "Toast does not exist"
    }

  db.session.delete(toast_to_delete)
  db.session.commit()

  return {
    "message": "Successfully Deleted"
  }
