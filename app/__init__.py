from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_login import UserMixin, LoginManager, logout_user
from flask_admin.contrib.sqla import ModelView
from config import Config
from flask_migrate import Migrate



# БД - Таблицы - Записи
# Таблица :

#       id    title   price   isActive

#       1     Some    100     True

#       2     Some2   200     False

#       3     Some3   40      True


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.config.from_pyfile('../config-extended.py')

    return app

app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Ставим редирект, если пользователь не авторизован, для страниц где обязательна авторизация

login_manager = LoginManager(app)
login_manager.login_view = 'admin_blueprint.login'

from app.admin.routes import admin_bp
app.register_blueprint(admin_bp, url_prefix="/admin")