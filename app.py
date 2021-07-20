from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', defaults={'page': None})
@app.route('/<page>')
def index(page):
    if page is None:
        return render_template('index.html')
    else:
        if page not in ('about', 'home', 'contact'):
            return ("Page not Found!", 404)
        content_html = f"{page}_content.html"
        return render_template(content_html)


if __name__ == '__main__':
    app.run(use_reloader=True)
