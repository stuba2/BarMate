from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Review, Recipe, User, RecipeImage
from ..forms.recipe_form import RecipeForm
from ..forms.recipe_image_form import RecipeImageForm

review_routes = Blueprint('reviews', __name__)

@review_routes.route('/<int:recipe_id>/reviews', methods=['GET'])
def get_recipe_reviews(recipe_id):
  ret = []
  all_reviews = Review.query.filter(Review.recipe_id == recipe_id).all()

  for review in all_reviews:
    reviewer_details = User.query.filter(User.id == review.user_id)
    ret_review = {
      'id': review.id,
      'review_text': review.review_text,
      'rating': review.rating,
      'user_id': review.user_id,
      'recipe_id': review.recipe_id,
      'reviewer_details': {
        'username': reviewer_details.username
      },
      'created_at': review.created_at,
      'updated_at': review.updated_at
    }

    ret.append(ret_review)

  return {
    'Reviews': ret
  }
