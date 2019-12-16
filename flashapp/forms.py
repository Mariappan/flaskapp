from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class MemberForm(FlaskForm):
    member_name = StringField('Name', validators=[DataRequired()])
    member_age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField('Add')