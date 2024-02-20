from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

bar_ingredients = db.Table(
    "bar_ingredients",
    db.Model.metadata,
    # db.Column('id', db.Integer, primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), primary_key=True),
    db.Column("ingredient_id", db.Integer, db.ForeignKey(add_prefix_for_prod("ingredients.id")), primary_key=True),

    # bar_ingredient_user = db.relationship('User', back_populates='user_bar_ingredient')
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

    ingredients_recipe_ingredients = db.relationship("RecipeIngredient", back_populates="recipe_ingredients_ingredients")

    ingredient_ingredient_image = db.relationship("IngredientImage", back_populates="ingredient_image_ingredient")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'bar_ingredients_users': [user.to_dict() for user in self.bar_ingredients_users],
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
