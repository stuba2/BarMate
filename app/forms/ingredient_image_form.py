from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class IngredientImageForm(FlaskForm):
    ingredient_id = IntegerField('Ingredient Id', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Submit')
