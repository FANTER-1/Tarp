from django.db import models
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

# Конфигурация приложения
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # Секретный ключ для работы с формами , пока что вот так позже может доработаю
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Путь к БД SQLite
db = SQLAlchemy(app)


# Создание модели для хранения информации о пользователях
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    photo = db.Column(db.String(100))


# Создание формы регистрации
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Register')


# Страница регистрации
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():  # Если форма отправлена и данные прошли валидацию
        username = form.username.data
        email = form.email.data

        # Сохранение данных пользователя в БД
        new_user = User(username=username, email=email) # email и пользователя оставлю так , потом может добавлю
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('photos'))  # Перенаправление на страницу с фотографиями

    return render_template('registration.html', form=form)


# Страница с фотографиями
@app.route('/photos', methods=['GET', 'POST'])
def photos():
    # Обработка загрузки фотографий
    if request.method == 'POST':
        # Сохранение фотографий на сервере или в БД
        # Код обработки загрузки фотографий

        return redirect(url_for('photos'))

    return render_template('photos.html')


if __name__ == '__main__':
    app.run(debug=True)
