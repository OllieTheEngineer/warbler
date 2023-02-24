from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])

class EditUserForm(FlaskForm):
    """ Form to edit user information"""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired()])
    bio = TextAreaField("Who are you? What do you do?")
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=15)])
    image_url = StringField('Add a picture of yourself')
    header_image_url = StringField("Background image")
