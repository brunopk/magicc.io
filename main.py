import sqlite3
import uuid

from flask import Flask, render_template, url_for, redirect, request, session, abort
from flask_bootstrap import Bootstrap
from flask_scss import Scss
from functools import wraps
from os import path, stat
from rpi_ws281x import PixelStrip, Color

title = "Strip Controller"
db_name = 'sqlite3.db'
app_key = uuid.uuid1()
pages = ['/colors/1', '/effects/1']
app = Flask(__name__)
# ASCII expression of 16 bit secret-key used for cookie encryption (used for based-client sessions)
app.secret_key = b"Q]J\n\x18\x86P\x84\x1f/Z\x99kUQ'"


def init_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS user')
    c.execute('CREATE TABLE user(name VARCHAR)')
    conn.commit()
    conn.close()


def try_save_user_to_db(name):
    """
    Tries saving username into sqlite DB.
    If saved successfully, returns the value of the param 'username'.
    On the other hand, returns current username stored on DB.
    """

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('SELECT * FROM user')
    users = c.fetchone()
    if users is not None and users.__len__() > 0:
        res = users[0]
    else:
        c.execute('INSERT INTO user VALUES (?)', [name])
        res = name
        conn.commit()
    conn.close()
    return res

def remove_user_from_db(name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('DELETE FROM user WHERE name = "{name}"'.format(name=name))
    conn.commit()
    conn.close()


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


def render_template_wrapper(template, actual_page='', **kwargs):
    if not actual_page.__eq__(''):
        return render_template(template, title=title, previous_page=previous_page(actual_page),
                               next_page=next_page(actual_page), **kwargs)
    else:
        return render_template(template, **kwargs)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.keys().__contains__('key'):
            user_key = session.get('key')
            if not type(app_key.bytes).__name__.__eq__(type(user_key).__name__) or not user_key.__eq__(app_key.bytes):
                return redirect(url_for('login'))
        else:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# Injects context variables before rendering
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


Bootstrap(app)
Scss(app, static_dir='static', asset_dir='static')
init_db()


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
        new_user = request.form['name']
        if new_user is None or new_user.__eq__(''):
            error = 'You must provide username'
            return render_template_wrapper('login.html', error=error)
        else:
            current_user = try_save_user_to_db(new_user)
            if current_user.__eq__(new_user):
                session['key'] = app_key.bytes
                session['username'] = current_user
                return redirect(url_for('colors', n=1))
            else:
                error = '{s} is controlling the strip now. Try again later ;)'.format(s=current_user)
                return render_template_wrapper('login.html', error=error)
    elif request.method.__eq__('GET'):
        return render_template_wrapper('login.html')
    else:
        abort(404)


@app.route('/logout', methods=['POST'])
def logout():
    if session.keys().__contains__('key'):
        user_key = session.get('key')
        if not type(app_key.bytes).__name__.__eq__(type(user_key).__name__) or not user_key.__eq__(app_key.bytes):
            abort(400)
        else:
            current_user = session['username']
            session.pop('key')
            session.pop('username')
            remove_user_from_db(current_user)
            return redirect(url_for('login'))
    else:
        abort(400)


@app.route('/colors/<int:n>')
@login_required
def colors(n):
    return render_template_wrapper('colors_{n}.html'.format(n=n), actual_page='/colors/{n}'.format(n=n))


@app.route('/effects/<int:n>')
@login_required
def effects(n):
    return render_template_wrapper('effects_{n}.html'.format(n=n), '/effects/{n}'.format(n=n))


if __name__ == '__main__':
    app.run()
