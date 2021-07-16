
from sqlalchemy_utils import URLType
from flask_login import UserMixin
from app import db
from app.utils import FormEnum

class PokemonTypes(FormEnum):
    """Pokemon Typings List (basic)"""
    NORMAL = 'Normal'
    FIGHTING = 'Fighting'
    FLYING = 'Flying'
    POISON = 'Poison'
    GROUND = 'Ground'
    ROCK = 'Rock'
    BUG = 'Bug'
    GHOST = "Ghost"
    STEEL = 'Steel'
    FIRE = 'Fire'
    WATER = 'Water'
    GRASS = 'Grass'
    ELECTRIC = 'Electric'
    PSYCHIC = 'Psychic'
    ICE = 'Ice'
    DRAGON = 'Dragon'
    DARK = 'Dark'

class User(UserMixin, db.Model):
    """Grocery Store model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    party = db.relationship('Pokemon', back_populates='user_party')

class Pokemon(db.Model):
    """Grocery Item model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    attack = db.Column(db.Float(precision=2), nullable=False)
    defense = db.Column(db.Float(precision=2), nullable=False)
    hp = db.Column(db.Float(precision=2), nullable=False)
    typing = db.Column(db.Enum(PokemonTypes), nullable=False)
    photo_url = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_party = db.relationship('User', back_populates='party')

    moves = db.relationship('Move', back_populates='pokemon_moves')

class Move(db.Model):
    """Grocery Item model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    power = db.Column(db.Float(precision=2), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    typing = db.Column(db.Enum(PokemonTypes), nullable=False)
    
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'), nullable=False)
    pokemon_moves = db.relationship('Pokemon', back_populates='moves')