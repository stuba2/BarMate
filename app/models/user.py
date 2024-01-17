from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from .ingredient import bar_ingredients

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    # bar_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('bar_ingredients.id')), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_recipes = db.relationship(
        "Recipe",
        back_populates='recipes_user')

    user_toasts = db.relationship(
        "Toast",
        back_populates='toasts_user')

    user_reviews = db.relationship(
        "Review",
        back_populates="reviews_user")

    users_bar_ingredients = db.relationship(
        "Ingredient",
        secondary=bar_ingredients,
        back_populates="bar_ingredients_users")

    # user_bar_ingredient = db.relationship(
    #     "bar_ingredients",
    #     back_populates='bar_ingredient_user',
    #     foreign_keys=[])

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'dob': self.dob
        }
