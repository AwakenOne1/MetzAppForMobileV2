from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/alexeydubovik/PycharmProjects/METZApplicationApp/instance/METZ.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class WUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tab_number = db.Column(db.String(20), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    department = db.Column(db.String(40), nullable=False)
    full_name = db.Column(db.String(40), nullable=False)
    password_hash = db.Column(db.String(1024), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


class WApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.NVARCHAR(None), nullable=False)
    inventory_number = db.Column(db.String(20), nullable=False)
    photo = db.Column(db.String(100))
    status = db.Column(db.Integer)
    latest_valubale_date = db.Column(db.DATETIME())
    user_id = db.Column(db.Integer, db.ForeignKey('w_user.id'), nullable=False)


# Создание базы данных
with app.app_context():
    db.create_all()

# Завершение работы приложения
app.app_context().push()
db.session.commit()
