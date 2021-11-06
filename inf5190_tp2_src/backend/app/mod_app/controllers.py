from re import search
from flask import Blueprint, json, request, render_template, flash, \
                                    redirect, url_for
from datetime import datetime


# Define the blueprint : 'article', set its url prefix : app.url/''
mod_home = Blueprint('home', __name__, url_prefix='')


@mod_home.route('/')
def documentation():
    time = datetime.now().time()
    return render_template('index.html', time=time)






