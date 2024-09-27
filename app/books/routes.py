from flask import Blueprint, jsonify, request, abort
from . import books_bp
from app.books.services import create_book, update_book, delete_book
from app.models import Book, db

# GET /books - Retrieve a list of all books
@books_bp.route('/', methods=['GET'])
def get_books():
    """
    Retrieve a list of all books
    ---
    responses:
      200:
        description: A list of books
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
              description:
                type: string
              publish_date:
                type: string
                format: date
              author_id:
                type: integer
    """
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'description': book.description, 'publish_date': book.publish_date, 'author_id': book.author_id} for book in books])

# POST /books - Create a new book
@books_bp.route('/', methods=['POST'])
def add_book():
    """
    Create a new book
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: Harry Potter and the Philosopher's Stone
            description:
              type: string
              example: The first book of the Harry Potter series
            publish_date:
              type: string
              format: date
              example: 1997-06-26
            author_id:
              type: integer
              example: 1
    responses:
      201:
        description: The created book
        schema:
          type: object
          properties:
            id:
              type: integer
            title:
              type: string
            description:
              type: string
            publish_date:
              type: string
              format: date
            author_id:
              type: integer
    """
    data = request.json
    new_book = create_book(data)
    return jsonify({'id': new_book.id, 'title': new_book.title}), 201

# GET /books/{id} - Retrieve details of a specific book
@books_bp.route('/<int:id>', methods=['GET'])
def get_book(id):
    """
    Retrieve details of a specific book
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The ID of the book
    responses:
      200:
        description: Book found
        schema:
          type: object
          properties:
            id:
              type: integer
            title:
              type: string
            description:
              type: string
      404:
        description: Book not found
    """
    book = Book.query.get_or_404(id)
    return jsonify({'id': book.id, 'title': book.title, 'description': book.description})

# PUT /books/{id} - Update an existing book
@books_bp.route('/<int:id>', methods=['PUT'])
def edit_book(id):
    """
    Update an existing book
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The ID of the book
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: "Updated Book Title"
            description:
              type: string
              example: "Updated book description"
    responses:
      200:
        description: Book updated successfully
        schema:
          type: object
          properties:
            status:
              type: string
              example: "success"
            status_code:
              type: integer
              example: 200
            data:
              type: object
              properties:
                id:
                  type: integer
                title:
                  type: string
    """
    data = request.json
    book = update_book(id, data)
    return jsonify({'status': 'success', 'status_code': 200, 'data': {'id': book.id, 'title': book.title}})

# DELETE /books/{id} - Delete a book
@books_bp.route('/<int:id>', methods=['DELETE'])
def remove_book(id):
    """
    Delete a specific book
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The ID of the book
    responses:
      204:
        description: Book deleted successfully
      404:
        description: Book not found
    """
    delete_book(id)
    return jsonify({'message': 'Book deleted successfully'}), 204