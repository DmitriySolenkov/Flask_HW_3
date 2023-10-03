from flask import Flask, request, make_response, render_template, session, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from model import db, User


from register import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        add_user(form)
        return render_template('main.html')
    return render_template('login.html', form=form)


def add_user(form):
    user = User(name=form.name.data, surname=form.surname.data,
                email=form.email.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()


@app.cli.command("init-db")
def init_db():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
