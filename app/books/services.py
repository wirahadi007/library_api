from app.models import Book, db

def get_all_books():
    books = Book.query.all()
    return [{'id': book.id, 'title': book.title} for book in books]

def create_book(data):
    book = Book(
        title=data['title'],
        description=data.get('description'),
        publish_date=data.get('publish_date'),
        author_id=data['author_id']
    )
    db.session.add(book)
    db.session.commit()
    return {'id': book.id, 'title': book.title}

def update_book(id, data):
    book = Book.query.get_or_404(id)
    book.title = data['title']
    book.description = data.get('description')
    book.publish_date = data.get('publish_date')
    db.session.commit()
    return book

def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()