from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime


class Review(db.Model, UserMixin):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("recipes.id")), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    reviews_user = db.relationship("User", back_populates="user_reviews")

    reviews_recipe = db.relationship("Recipe", back_populates="recipe_reviews")

    def to_dict(self):
        return {
            'id': self.id,
            'review_text': self.review_text,
            'rating': self.rating,
            'user_id': self.user_id,
            "recipe_id": self.recipe_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
