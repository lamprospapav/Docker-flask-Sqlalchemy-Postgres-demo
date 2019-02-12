from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FloatField,SelectField
from wtforms.validators import DataRequired,NumberRange


class BookForm(FlaskForm):
    """
    Form  to add or edit a objectDemo
    
    """

    name = StringField("Name",validators=[DataRequired()])
    rating = FloatField("Rating",validators=[NumberRange(min=0, max=10, message='Rating 0-10')])
    submit = SubmitField('Submit')

