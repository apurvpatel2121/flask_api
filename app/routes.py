import os
from . import create_app
from .models import Book
from flask import jsonify,request
from . import db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.route('/book/create', methods=['POST'])
def create_book():
    obj = Book(
                author=request.json.get('author')
               ,title=request.json.get('title')
               ,price=request.json.get('price')
               )
    db.session.add(obj)
    db.session.commit()

    return jsonify({
        'success':'book added suceessfully'
    }),201

@app.route('/book/list', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_json() for book in books]),200

@app.route('/book/<int:isbn>', methods=['GET'])
def get_book(isbn):
    book = Book.query.get(isbn)
    if book is None:
        return {'error', "Book not found"},404
    return jsonify(book.to_json())

@app.route("/book/delete/<int:isbn>", methods=['GET','DELETE'])
def delete_book(isbn):
    book = Book.query.get(isbn)
    if book is None:
        return jsonify({'message':'object not found'})
    else:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'result': True})

