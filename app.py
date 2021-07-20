from flask import Flask, render_template, Response, request

from models import User

app = Flask(__name__)

USERS = [
    User(0, 'akbar', 'asqar', 'akbar1', 'asd@gmail.com'),
    User(1, 'akbar2', 'asqari2', 'akbar2', 'asd2@gmail.com'),
    User(2, 'akbar3', 'asqari3', 'akbar3', 'asd3@gmail.com'),
    User(3, 'akbar4', 'asqari4', 'akbar4', 'asd4@gmail.com'),
]


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


@app.route('/user')
def users():
    resp = {
        'users': [
            {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name}
            for user in USERS
        ]
    }
    return resp


@app.route('/user/', defaults={'user_id': None})
@app.route('/user/<int:user_id>')
def user_detail(user_id):
    user = USERS[user_id]
    return vars(user)

@app.route('/contact', methods=['POST'])
def contact_us():
    print(request.form)
    return "Received!"


if __name__ == '__main__':
    app.run(use_reloader=True)
