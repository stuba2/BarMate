from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from datetime import datetime
import enum

class UnitTypes(enum.Enum):
    BAR_SPOON = 'bar spoon'
    CUBE = 'cube'
    CUP = 'cup'
    DASH = 'dash'
    LEAF = 'leaf'
    OZ = 'oz'
    PEEL = 'peel'
    STICK = 'stick'
    TBSP = 'tbsp'
    TSP = 'tsp'
    WEDGE = 'wedge'


recipe_ingredients = db.Table(
    "recipeIngredients",
    db.Model.metadata,
    db.Column('amount', db.Float(precision=4, scale=2), nullable=False),
    db.Column('unit', db.Enum(UnitTypes, values_callable=lambda x: [str(member.value) for member in UnitTypes]), nullable=False),
    db.Column('recipeId', db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), primary_key=True),
    db.Column('ingredientId', db.Integer, db.ForeignKey(add_prefix_for_prod('ingredients.id')), primary_key=True)
)

if environment == 'production':
    recipe_ingredients.schema = SCHEMA

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

    # needs fixing
    recipes_users = db.relationship("User", secondary=usersboards, back_populates="users_recipes")

    # boards_owner = db.relationship("User", back_populates="owner_boards")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'instructions': self.instructions,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
