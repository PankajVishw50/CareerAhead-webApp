from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import ValidationError


class EditCounsellorProfile(FlaskForm):
    submit = SubmitField("UPLOAD")

    def validate_submit(self, data):
        raise ValidationError("This feature is not available right now")