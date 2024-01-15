from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class ToastForm(FlaskForm):
    user_id = IntegerField('User Id', validators=[DataRequired()])
    recipe_id = IntegerField('Recipe Id', validators=[DataRequired()])
    submit = SubmitField('Submit')
