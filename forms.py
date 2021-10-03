from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = StringField('Password', validators=[DataRequired()])
	confirm_password = StringField('Comfirm Password', validators=[DataRequired(), EqualTo("password")])
	submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
	email = EmailField('Email', validators=[DataRequired(),Email()])
	password = StringField('Password', validators=[DataRequired()])
	
	#Remember the Password

	remember = BooleanField("Remember Me")
	submit = SubmitField("Sign Up")