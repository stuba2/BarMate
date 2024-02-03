from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
import enum

class UnitTypes(enum.Enum):
    BAR_SPOON = 'bar spoon'
    BLENDER = 'blender'
    BOTTLE = 'bottle'
    BOTTLES= 'bottles'
    CAN = 'can'
    CANS = 'cans'
    CL = 'cl'
    CUBE = 'cube'
    CUBES = 'cubes'
    CUP = 'cup'
    CUPS = 'cups'
    DASH = 'dash'
    DASHES = 'dashes'
    DL = 'dl'
    DROP = 'drop'
    DROPS = 'drops'
    FIFTH = 'fifth'
    FINGER = 'finger'
    FINGERS = 'fingers'
    GAL = 'gal'
    GARNISH = 'garnish'
    GLASS = 'glass'
    GR = 'gr'
    HANDFUL = 'handful'
    INCH = 'inch'
    JIGGER = 'jigger'
    JIGGERS = 'jiggers'
    JUICE = 'juice'
    KG = 'kg'
    L = 'l'
    LB = 'lb'
    LEAF = 'leaf'
    ML = 'ml'
    OZ = 'oz'
    PACKAGE = 'package'
    PACKAGES = 'packages'
    PART = 'part'
    PARTS = 'parts'
    PEEL = 'peel'
    PIECE = 'piece'
    PIECES = 'pieces'
    PINCH = 'pinch'
    PINCHES = 'pinches'
    PINT = 'pint'
    QT = 'qt'
    SCOOP = 'scoop'
    SCOOPS = 'scoops'
    SHOT = 'shot'
    SHOTS = 'shots'
    SLICE = 'slice'
    SPLASH = 'splash'
    SPLASHES = 'splashes'
    SPRIG = 'sprig'
    SPRIGS = 'sprigs'
    STICK = 'stick'
    STICKS = 'sticks'
    TBSP = 'tbsp'
    TOP_OFF = 'top off'
    TO_TASTE = 'to taste'
    TSP = 'tsp'
    TWIST = 'twist'
    UNIT = 'unit'
    UNITS = 'units'
    WEDGE = 'wedge'
    WEDGES = 'wedges'
    WHOLE = 'whole'

class RecipeIngredient(db.Model, UserMixin):
    __tablename__ = 'recipe_ingredients'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float(precision=4, decimal_return_scale=2), nullable=False, unique=False)
    unit = db.Column(db.Enum(UnitTypes, values_callable=lambda x: [str(member.value) for member in UnitTypes]), nullable=False, unique=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')))
    ingredient_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('ingredients.id')))

    recipe_ingredients_recipe = db.relationship("Recipe", back_populates="recipes_recipe_ingredients")

    recipe_ingredients_ingredients = db.relationship("Ingredient", back_populates="ingredients_recipe_ingredients")

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'unit': self.unit,
            "recipe_id": self.recipe_id,
            "ingredient_id": self.ingredient_id,
            "recipe_ingredients_recipe": self.recipe_ingredients_recipe,
            "recipe_ingredients_ingredients": self.recipe_ingredients_ingredients,
        }
