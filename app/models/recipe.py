from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime
import enum

class Recipe(db.Model, UserMixin):
    __tablename__ = 'recipes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    description = db.Column(db.String(1000))
    instructions = db.Column(db.String(2000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    recipes_user = db.relationship("User", back_populates="user_recipes")

    recipe_reviews = db.relationship("Review", back_populates="reviews_recipe")

    recipe_toasts = db.relationship("Toast", back_populates="toasts_recipe")

    recipes_recipe_ingredients = db.relationship("RecipeIngredient", back_populates="recipe_ingredients_recipe")

    recipe_recipe_image = db.relationship("RecipeImage", back_populates="recipe_image_recipe")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'instructions': self.instructions,
            "user_id": self.user_id,
            "recipes_user": self.recipes_user.to_dict(),
            "recipe_reviews": self.recipe_reviews,
            "recipe_toasts": self.recipe_toasts,
            "recipes_recipe_ingredients": self.recipes_recipe_ingredients,
            "recipe_recipe_image": self.recipe_recipe_image,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
