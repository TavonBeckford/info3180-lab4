from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    photo = FileField('Image', validators=[FileRequired(), 
    FileAllowed(['jpg','png','jpeg'], 'Images Only!')])
