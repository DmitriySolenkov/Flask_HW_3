from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8)])
