import unittest
from app import create_app, db
from app.models import Author, Book

class BookTestCase(unittest.TestCase):

    def setUp(self):
        """Set up the test context and create the database tables."""
        self.app = create_app()
        self.app.config.from_object('config.TestingConfig')  # Use TestingConfig
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Create a sample author
        self.author = Author(name='George Orwell', bio='Author of 1984', birth_date='1903-06-25')
        db.session.add(self.author)
        db.session.commit()

    def tearDown(self):
        """Tear down the database and remove the app context."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_books(self):
        """Test GET /books - should return an empty list initially."""
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_book(self):
        """Test POST /books - create a new book."""
        response = self.client.post('/books/', json={
            'title': '1984', 'description': 'A dystopian novel', 'publish_date': '1949-06-08', 'author_id': self.author.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('1984', response.get_data(as_text=True))

    def test_get_book(self):
        """Test GET /books/{id} - get a specific book."""
        book = Book(title='Animal Farm', description='A novella', publish_date='1945-08-17', author_id=self.author.id)
        db.session.add(book)
        db.session.commit()

        response = self.client.get(f'/books/{book.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Animal Farm', response.get_data(as_text=True))

    def test_update_book(self):
        """Test PUT /books/{id} - update an existing book."""
        book = Book(title='The Fellowship of the Ring', description='Part of LOTR', publish_date='1954-07-29', author_id=self.author.id)
        db.session.add(book)
        db.session.commit()

        response = self.client.put(f'/books/{book.id}', json={
            'title': 'The Fellowship of the Ring', 'description': 'Updated Description', 'publish_date': '1954-07-29', 'author_id': self.author.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Description', response.get_data(as_text=True))

    def test_delete_book(self):
        """Test DELETE /books/{id} - delete an existing book."""
        book = Book(title='Foundation', description='Part of the Foundation series', publish_date='1951-01-01', author_id=self.author.id)
        db.session.add(book)
        db.session.commit()

        response = self.client.delete(f'/books/{book.id}')
        self.assertEqual(response.status_code, 204)

        # Verify deletion
        response = self.client.get(f'/books/{book.id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
