from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import User

class SignUpForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already taken.')


class LoginForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
    
    def validate_username(form, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError("No user with that username, please try again")
    
    def validate_password(form, password):
        user = User.query.filter_by(username=form.password.data).first()
        if user is None:
            return
        if not bcrypt.check_password_hash(user.password, PasswordField.data):
            raise ValidationError("Password didn't match. PLease try agian")