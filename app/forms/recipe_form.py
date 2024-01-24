from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Recipe

def recipe_name_exists(form, field):
    name = field.data
    recipe = Recipe.query.filter(Recipe.name == name).first()
    if recipe:
        raise ValidationError('Recipe already exists with that name')

class RecipeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=64), recipe_name_exists])
    description = StringField('Description', validators=[ Length(max=1000)])
    instructions = StringField('Instructions', validators=[DataRequired(), Length(max=2000)])
    user_id = IntegerField('User Id', validators=[DataRequired()])
    submit = SubmitField('Submit')
