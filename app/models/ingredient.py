from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime
from .recipe import recipe_ingredients

bar_ingredients = db.Table(
    "barIngredients",
    db.Model.metadata,
    db.Column("userId", db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), primary_key=True),
    db.Column("ingredientId", db.Integer, db.ForeignKey(add_prefix_for_prod("ingredients.id")), primary_key=True)
)

if environment == "production":
    bar_ingredients.schema = SCHEMA

class Ingredient(db.Model, UserMixin):
    __tablename__ = 'ingredients'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    bar_ingredients_users = db.relationship("User", secondary=bar_ingredients, back_populates="users_bar_ingredients")

    ingredients_recipes = db.relationship("Recipe", secondary=recipe_ingredients, back_populates="recipes_ingredients")

    ingredient_ingredient_image = db.relationship("IngredientImage", back_populates="ingredient_image_ingredient")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
