from app import create_app, db
from app.models import Author, Book


def seed_data():
    app = create_app()
    with app.app_context():
        # Add some authors
        author_1 = Author(name="J.K. Rowling", bio="Author of Harry Potter", birth_date="1965-07-31")
        author_2 = Author(name="George Orwell", bio="Author of 1984", birth_date="1903-06-25")
        author_3 = Author(name="J.R.R. Tolkien", bio="Author of The Lord of the Rings", birth_date="1892-01-03")

        db.session.add_all([author_1, author_2, author_3])
        db.session.commit()

        # Add books
        book_1 = Book(title="Harry Potter and the Philosopher's Stone", description="First Harry Potter book",
                      publish_date="1997-06-26", author_id=author_1.id)
        book_2 = Book(title="1984", description="A dystopian novel", publish_date="1949-06-08", author_id=author_2.id)
        book_3 = Book(title="The Lord of the Rings: The Fellowship of the Ring", description="First book in LOTR",
                      publish_date="1954-07-29", author_id=author_3.id)

        db.session.add_all([book_1, book_2, book_3])
        db.session.commit()

        print("Database seeded successfully!")


if __name__ == '__main__':
    seed_data()
