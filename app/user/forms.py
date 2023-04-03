from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, IntegerField, SelectField, SubmitField, validators
from wtforms.validators import ValidationError, DataRequired, NumberRange
from flask_login import current_user
from ..model import User


class EditUserProfile(FlaskForm):
    username = StringField("Enter Username")
    email = EmailField("Email address")
    age = IntegerField("Age", validators=[NumberRange(min=0)])
    gender = SelectField("Gender", choices=[(-1, "Gender"), (1, "Female"), (2, "Male")])
    password = PasswordField("Password", validators=[DataRequired()])
    new_password = PasswordField("New Password")
    submit = SubmitField("Save")

    def validate_password(self, data):
        user = User.query.get(current_user.id)

        if user.verify_password(data.data):
            return

        raise ValidationError("Password did not match")

    def validate_username(self, data):
        if data.data.startswith("@"):
            raise ValidationError("Invalid username: username should not start with character '@' ")

    def validate_email(self, data):
        counsellor = User.query.filter_by(email=data.data).first()
        if counsellor:
            raise ValidationError("This email is linked with another account.")
