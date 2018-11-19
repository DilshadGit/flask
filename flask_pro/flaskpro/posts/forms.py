from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    TextAreaField,
)
# this for validate the length of the field
from wtforms.validators import (
    DataRequired,
)


class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(), ])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Create Post')


class UpdatePostForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(), ])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Update Post')
