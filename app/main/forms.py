# Create your forms here.from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from app.models import User, Pokemon, PokemonTypes, Move

class PokemonForm(FlaskForm):
    """Form for adding a Pokemon."""

    name = StringField('Name of Pokemon', validators=[DataRequired(), Length(min=3, max=80)])
    attack = FloatField('Attack Value', validators=[DataRequired()])
    defense = FloatField('Defence Value', validators=[DataRequired()])
    hp = FloatField('HP Value', validators=[DataRequired()])
    typing = SelectField('Pokemon Typing',  choices=PokemonTypes.choices())
    photo_url = StringField('Photo_url')
    submit = SubmitField('Submit')

class MoveForm(FlaskForm):
    """Form for adding a Pokemon Move."""

    name = StringField('Name of Pokemon Move', validators=[DataRequired(), Length(min=3, max=80)])
    power = FloatField('Power Value', validators=[DataRequired()])
    amount = FloatField('PP Value', validators=[DataRequired()])
    typing = SelectField('Pokemon Move Typing',  choices=PokemonTypes.choices())
    submit = SubmitField('Submit')
