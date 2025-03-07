from flask import Flask, render_template, request, redirect, jsonify, url_for
from utils.db import db
from models.resume import *
#from static.images import  *
#from static.videos import *

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resume.db'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True

db.init_app(flask_app)
with flask_app.app_context():
    db.create_all()

@flask_app.route('/')
def index():
    return render_template('index.html')

@flask_app.route('/login')
def login():
    login = Login.query.all()
    return render_template('login.html', content=login)

@flask_app.route('/logout')
def logout():
    return render_template('logout.html')

@flask_app.route('/resume')
def resume():
    return render_template('resume.html')

@flask_app.route('/sub', methods=['POST'])
def sub():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    email = form_data.get('email')
    password = form_data.get('password')
    login = Login(email=email, password=password)
    db.session.add(login)
    db.session.commit()
    print("submitted successfully")
    return redirect('/resume')



if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=8005,
        debug=True
    )