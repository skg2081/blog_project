# forms 
from flask_wtf import FlaskForm 
from wtform import StringField, PasswordField, SubmitField, ValidationError 
from wtform.validators import DataRequired, Email, EqualTo 
from flask_wtf.file import FileField,  FileAllowed 

from flask_login import current_user 
from puppycompanyblog.model import User 

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired(), EqualTo('pass_confirm', message = 'Password must match')])
    pass_confirm = PasswordField('Confirm Password', validators = [DataRequired()]) 


    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been registered')

    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has been registered')
