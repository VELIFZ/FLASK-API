from app import app

from flask import render_template
from .services import get_poke_info
from .forms import Search

@app.route('/')
def pokemon():
    form = Search()
    if form.validate_on_submit():
        print(get_poke_info(form.pokename.data))
        print('hello world')
    return render_template('index.html', form = form)
