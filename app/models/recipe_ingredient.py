from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
import enum

class UnitTypes(enum.Enum):
    BAR_SPOON = 'bar spoon'
    CAN = 'can'
    CUBE = 'cube'
    CUP = 'cup'
    DASH = 'dash'
    LEAF = 'leaf'
    OZ = 'oz'
    PEEL = 'peel'
    SPRIG = 'sprig'
    STICK = 'stick'
    TBSP = 'tbsp'
    TSP = 'tsp'
    WEDGE = 'wedge'

class RecipeIngredient(db.Model, UserMixin):
    __tablename__ = 'recipe_ingredients'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float(precision=4, decimal_return_scale=2), nullable=False),
    unit = db.Column(db.Enum(UnitTypes, values_callable=lambda x: [str(member.value) for member in UnitTypes]), nullable=False),
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), primary_key=True),
    ingredient_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('ingredients.id')), primary_key=True)

    recipe_ingredients_recipe = db.relationship("Recipe", back_populates="recipes_recipe_ingredients")

    recipe_ingredients_ingredients = db.relationship("Ingredient", back_populates="ingredients_recipe_ingredients")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
