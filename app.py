from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
api = Api(app)

# Definir modelos de la base de datos
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(250), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Funciones para autenticación JWT
def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()

jwt = JWT(app, authenticate, identity)

# Recurso para obtener la lista de libros
class BookListResource(Resource):
    @jwt_required()
    def get(self):
        books = Book.query.all()
        book_list = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
        return jsonify({'books': book_list})

# Agregar el recurso a la API
api.add_resource(BookListResource, '/books')

if __name__ == '__main__':
    # Crear las tablas en la base de datos antes de ejecutar la aplicación
    db.create_all()
    app.run(port=5000, debug=True)
