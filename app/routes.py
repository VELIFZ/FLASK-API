from app import app

from flask import redirect, render_template, request, url_for, redirect
from .forms import Search


import requests as r

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pokemon', methods = ['GET', 'POST'])
def pokemon():
    form = Search()
    if request.method == "POST":
        res = r.get(f'https://pokeapi.co/api/v2/pokemon/{form.pokename.data}').json()
        if res:
            po_name = res['name']
            weight = res['weight']
            height = res['height']
            abilities = [i['ability']['name'] for i in res['abilities']]
            types = [i['type']['name'] for i in res['types']]
            images_url = res['sprites']['other']['official-artwork']['front_default']
            return render_template('pokemon.html', form=form, po_name=po_name, weight=weight, height=height, abilities=abilities, types=types, images_url=images_url )
        else:
            return redirect(url_for('pokemon'))

    

    # if form.validate_on_submit():
    #     print(get_poke_info(form.pokename.data))
    #     print('hello world')
    

# what if isim is pokemon name and isim will go in get_poke_info function and on page show only one pokemon info?
# @app.route('/<isim>')
# def get_poke_name(isim):
#     return isim # burada function'a mi donecem