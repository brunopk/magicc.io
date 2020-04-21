from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_scss import Scss
from os import path, stat

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


# Injects context variables before rendering
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


@app.route('/')
def hello_world():
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
              (0, 255, 100), (0, 100, 100)]
    return render_template("index.html", title='Strip Controller', colors=colors)


if __name__ == '__main__':
    app.run()
