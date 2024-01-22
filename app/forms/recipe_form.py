from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class RecipeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=64)])
    description = StringField('Description', validators=[ Length(max=1000)])
    instructions = StringField('Instructions', validators=[DataRequired(), Length(max=2000)])
    user_id = IntegerField('User Id', validators=[DataRequired()])
    submit = SubmitField('Submit')
