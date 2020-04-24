from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_scss import Scss
from os import path, stat

title = "Strip Controller"
pages = ['/colors/1', '/effects/1']
app = Flask(__name__)
Bootstrap(app)
Scss(app, static_dir='static', asset_dir='static')


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


# Injects context variables before rendering
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


@app.route('/')
def index():
    return render_template_wrapper(pages[0], 'colors_1.html')


@app.route('/colors/<int:n>')
def colors(n):
    actual_page = '/colors/{n}'.format(n=n)
    return render_template_wrapper(actual_page, 'colors_{n}.html'.format(n=n))


@app.route('/effects/<int:n>')
def effects(n):
    actual_page = '/effects/{n}'.format(n=n)
    return render_template_wrapper(actual_page, 'effects_{n}.html'.format(n=n))


if __name__ == '__main__':
    app.run()
