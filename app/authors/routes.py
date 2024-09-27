from flask import jsonify, request
from . import authors_bp
from .services import get_all_authors, create_author, update_author, delete_author, get_authors_byid
from app.models import Author, db

@authors_bp.route('/', methods=['GET'])
def get_authors():
    """
    Retrieve a list of all authors
    ---
    responses:
      200:
        description: A list of authors
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              bio:
                type: string
              birth_date:
                type: string
                format: date
    """
    authors = Author.query.all()
    return jsonify([{'id': author.id, 'name': author.name, 'bio': author.bio, 'birth_date': author.birth_date} for author in authors])

# POST /authors - Create a new author
@authors_bp.route('/', methods=['POST'])
def add_author():
    """
    Create a new author
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: J.K. Rowling
            bio:
              type: string
              example: Author of Harry Potter series
            birth_date:
              type: string
              format: date
              example: 1965-07-31
    responses:
      201:
        description: The created author
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            bio:
              type: string
            birth_date:
              type: string
              format: date
    """
    data = request.json
    new_author = create_author(data)
    return jsonify({'id': new_author.id, 'name': new_author.name}), 201

# GET /authors/{id} - Retrieve details of a specific author
@authors_bp.route('/<int:id>', methods=['GET'])
def get_author(id):
    """
    Retrieve details of a specific author
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The ID of the author
    responses:
      200:
        description: Author found
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            bio:
              type: string
            birth_date:
              type: string
              format: date
      404:
        description: Author not found
    """
    author = get_authors_byid(id)
    return jsonify(author)

# PUT /authors/{id} - Update an existing author
@authors_bp.route('/authors/<int:id>', methods=['PUT'])
def edit_author(id):
    """
    Update an existing author
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The ID of the author
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: "Updated Author Name"
            bio:
              type: string
              example: "Updated author bio"
            birth_date:
              type: string
              format: date
              example: "1980-01-01"
    responses:
      200:
        description: Author updated successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
    """
    data = request.json
    author = update_author(id, data)
    return jsonify({'id': author.id, 'name': author.name})

# DELETE /authors/{id} - Delete an author
@authors_bp.route('/authors/<int:id>', methods=['DELETE'])
def remove_author(id):
    """
    Delete a specific author
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The ID of the author
    responses:
      204:
        description: Author deleted successfully
      404:
        description: Author not found
    """
    delete_author(id)
    return jsonify({'message': 'Author deleted successfully'}), 204

# GET /authors/{id}/books - Retrieve all books by a specific author
@authors_bp.route('/authors/<int:id>/books', methods=['GET'])
def get_books_by_author(id):
    """
    Retrieve all books by a specific author
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The ID of the author
    responses:
      200:
        description: List of books by the author
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
      404:
        description: Author not found
    """
    author = Author.query.get_or_404(id)
    books = [{'id': book.id, 'title': book.title} for book in author.books]
    return jsonify(books)