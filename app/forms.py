from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,validators
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    username = StringField('username', [validators.DataRequired(),validators.Length(min=4, max=15)])
    email = StringField('email',[validators.DataRequired(),validators.Length(min=4, max=15)])

    password = PasswordField('Password', [validators.DataRequired(),validators.Length(min=8, max=20)])
    submit = SubmitField('SignUp')

class LoginForm(FlaskForm):
    username  = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('SignIn')

