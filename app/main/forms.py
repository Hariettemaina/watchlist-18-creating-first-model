from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[InputRequired()])
    review = TextAreaField('Movie review', validators=[InputRequired()])
    submit = SubmitField('Submit')

#from .models.reviews import Review
#from .forms import ReviewForm
#from wtforms.validators import InputRequired