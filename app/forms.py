from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    post = StringField('Post', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    submit = SubmitField('Delete')

class UpdateForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    post = StringField('Post', validators=[DataRequired()])
    submit = SubmitField('Update')
