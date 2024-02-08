from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime

class Toast(db.Model, UserMixin):
    __tablename__ = 'toasts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("recipes.id")), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    toasts_user = db.relationship("User", back_populates="user_toasts")

    toasts_recipe = db.relationship("Recipe", back_populates="recipe_toasts")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id,
            'toasts_user': self.toasts_user,
            'toasts_recipe': self.toasts_recipe,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
