import sqlalchemy
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_jwt_extended import create_access_token
from datetime import timedelta


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    sex = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.id, expires_delta=expire_delta
        )
        return token

    def __repr__(self):
        return f"<User> {self.email}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
