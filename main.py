from flask import Flask, render_template, url_for, redirect, request, session, abort
from flask_bootstrap import Bootstrap
from flask_scss import Scss
from functools import wraps
from os import path, stat
from rpi_ws281x import PixelStrip, Color

title = "Strip Controller"
pages = ['/colors/1', '/effects/1']
app = Flask(__name__)
Bootstrap(app)
Scss(app, static_dir='static', asset_dir='static')

# ASCII expression of 16 bit secret-key used for cookie encryption (used for based-client sessions)
app.secret_key = b"Q]J\n\x18\x86P\x84\x1f/Z\x99kUQ'"


# Avoid browser file caching, extracted from https://stackoverflow.com/questions/21714653/flask-css-not-updating
def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = path.join(app.root_path, endpoint, filename)
            values['q'] = int(stat(file_path).st_mtime)
    return url_for(endpoint, **values)


def previous_page(page):
    return pages[pages.index(page) - 1]


def next_page(page):
    return pages[(pages.index(page) + 1) % pages.__len__()]


def render_template_wrapper(actual_page, template, **kwargs):
    return render_template(template, title=title, previous_page=previous_page(actual_page),
                           next_page=next_page(actual_page), **kwargs)


# TODO mostrar que usuario esta logueado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'name' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# Injects context variables before rendering
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


# -------------------------------------------------------------------------------------------------------------------- #
#                                                   ROUTES                                                             #
# -------------------------------------------------------------------------------------------------------------------- #


@app.route('/')
@login_required
def index():
    return redirect(url_for('colors', n=1))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method.__eq__('POST'):
        session['name'] = request.form['name']
        return redirect(url_for('colors', n=1))
    elif request.method.__eq__('GET'):
        if 'name' in session:
            print(session['name'])
        return render_template_wrapper(pages[0], 'login.html')
    else:
        abort(404)


@app.route('/colors/<int:n>')
@login_required
def colors(n):
    actual_page = '/colors/{n}'.format(n=n)
    return render_template_wrapper(actual_page, 'colors_{n}.html'.format(n=n))


@app.route('/effects/<int:n>')
@login_required
def effects(n):
    actual_page = '/effects/{n}'.format(n=n)
    return render_template_wrapper(actual_page, 'effects_{n}.html'.format(n=n))


if __name__ == '__main__':
    app.run()
