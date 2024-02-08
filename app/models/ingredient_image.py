from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class IngredientImage(db.Model, UserMixin):
    __tablename__ = 'ingredient_images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("ingredients.id")), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    ingredient_image_ingredient = db.relationship("Ingredient", back_populates="ingredient_ingredient_image")

    def to_dict(self):
        return {
            'id': self.id,
            'ingredient_id': self.ingredient_id,
            'url': self.url,
            'ingredient_image_ingredient': self.ingredient_image_ingredient,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
