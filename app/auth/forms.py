from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, BooleanField, StringField, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NumberRange
from ..model import User


class LoginForm(FlaskForm):
    email = EmailField("email", validators=[DataRequired(), Length(2, 60)])
    password = PasswordField("password", validators=[DataRequired(), Length(2, 60)])
    remember = BooleanField("remember me")
    submit = SubmitField("Submit")


class SignInForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired(), Length(2, 20)])
    email = EmailField("Email: ", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(16, 100)])
    gender = SelectField(choices=[(-1, "Gender"), (1, "Female"), (2, "Male")], validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password: ", validators=[DataRequired(), EqualTo("password")])
    remember = BooleanField("remember me")
    submit = SubmitField("Create Account")

    def validate_username(self, data):
        if User.query.filter_by(username=data.data).first():
            raise ValidationError("Username already exists")

    def validate_email(self, data):
        if User.query.filter_by(email=data.data).first():
            raise ValidationError("Email already exists")

    def validate_gender(self, data):
        if int(data.data) < 0:
            raise ValidationError("Choose gender")








