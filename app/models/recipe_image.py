from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class RecipeImage(db.Model, UserMixin):
    __tablename__ = 'recipeImages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("recipes.id")), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    recipe_image_recipe = db.relationship("Recipe", back_populates="recipe_recipe_image")

    def to_dict(self):
        return {
            'id': self.id,
            'recipe_id': self.recipe_id,
            'url': self.url,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
