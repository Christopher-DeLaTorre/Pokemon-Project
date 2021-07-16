from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import *
from app.main.forms import *
from app import bcrypt, app, db

main = Blueprint('main', __name__)

@main.route('/')
def homepage():

    return render_template('base.html', user_party=[])

@main.route('/home')
def titlepage():
    if current_user.is_authenticated:
        party = current_user.party                          
        return render_template('home.html', user_party=party)
    return render_template('home.html', user_party=[])

@main.route('/pokemon_detail/<pokemon_id>', methods=['Get', 'POST'])
def pokemon_detail(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)

    return render_template('pokemon_detail.html', pokemon=pokemon)

@main.route('/new_pokemon', methods=['GET', 'POST'])
def new_pokemon():
    form = PokemonForm()
    if form.validate_on_submit():
        new_pokemon = Pokemon(
            name=form.name.data,
            attack=form.attack.data,
            defense=form.defense.data,
            hp=form.hp.data,
            typing=form.typing.data,
            photo_url=form.photo_url.data
        )
        new_pokemon.user_id = current_user.id  
        db.session.add(new_pokemon)
        db.session.commit()
        
        flash('success')
        return redirect(url_for('main.pokemon_detail', pokemon_id=new_pokemon.id)) 
    print(form.errors)
    return render_template('new_pokemon.html', form=form)

@main.route('/new_move/<pokemon_id>', methods=['GET', 'POST'])
def new_move(pokemon_id):
    form = MoveForm()
    pokemon = Pokemon.query.get(pokemon_id)
    if form.validate_on_submit():
        new_move = Move(
            name=form.name.data,
            power=form.power.data,
            amount=form.amount.data,
            typing=form.typing.data
        )
        new_move.pokemon_id = pokemon.id
        db.session.add(new_move)
        db.session.commit()

        flash('success')
        return redirect(url_for('main.pokemon_detail', pokemon_id=new_move.pokemon_id)) 
    print(form.errors)
    return render_template('new_move.html', form=form, pokemon_id=pokemon.id)