from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Recipe

def recipe_name_exists(form, field):
    name = field.data
    recipe = Recipe.query.filter(Recipe.name == name).first()
    if recipe:
        raise ValidationError('Recipe already exists with that name')

class BarForm(FlaskForm):
    user_id = IntegerField('User Id', validators=[DataRequired()])
    ingredient_id = IntegerField('Ingredient Id', validators=[DataRequired()])
    submit = SubmitField('Submit')
