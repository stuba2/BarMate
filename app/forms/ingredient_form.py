from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class IngredientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Submit')
