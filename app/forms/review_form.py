from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class ReviewForm(FlaskForm):
    review_text = StringField('Description', validators=[ Length(max=1000)])
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    user_id = IntegerField('User Id', validators=[DataRequired()])
    recipe_id = IntegerField('Recipe Id', validators=[DataRequired()])
    submit = SubmitField('Submit')
