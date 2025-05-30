from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Optional

class PostForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(),
        Length(min=3, max=100)
    ])
    content = TextAreaField('Content', validators=[
        DataRequired()
    ])
    picture = FileField('Add Image', validators=[
        FileAllowed(['jpg', 'png', 'jpeg'])
    ])
    submit = SubmitField('Post')

class SearchForm(FlaskForm):
    search_query = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')

class AITextGeneratorForm(FlaskForm):
    prompt = TextAreaField('I dont know what to write...', validators=[Optional()])
    use_ai_help = BooleanField('Using AI assistance')
    generate = SubmitField('Text generation')

class ImageCaptioningForm(FlaskForm):
    image = FileField('Upload image', validators=[
        FileAllowed(['jpg', 'png', 'jpeg'], 'Image files only (.jpg, .png, .jpeg)')
    ])
    analyze = SubmitField('Image analysis')

class ChatForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')