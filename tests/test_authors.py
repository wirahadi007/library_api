import unittest
from app import create_app, db
from app.models import Author

class AuthorTestCase(unittest.TestCase):

    def setUp(self):
        """Set up the test context and create the database tables."""
        self.app = create_app()
        self.app.config.from_object('config.TestingConfig')  # Use TestingConfig
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Tear down the database and remove the app context."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_authors(self):
        """Test GET /authors - should return an empty list initially."""
        response = self.client.get('/authors/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_author(self):
        """Test POST /authors - create a new author."""
        response = self.client.post('/authors/', json={
            'name': 'J.K. Rowling', 'bio': 'Author of Harry Potter', 'birth_date': '1965-07-31'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('J.K. Rowling', response.get_data(as_text=True))

    def test_get_author(self):
        """Test GET /authors/{id} - get a specific author."""
        author = Author(name='George Orwell', bio='Author of 1984', birth_date='1903-06-25')
        db.session.add(author)
        db.session.commit()

        response = self.client.get(f'/authors/{author.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('George Orwell', response.get_data(as_text=True))

    def test_update_author(self):
        """Test PUT /authors/{id} - update an existing author."""
        author = Author(name='J.R.R. Tolkien', bio='Author of Lord of the Rings', birth_date='1892-01-03')
        db.session.add(author)
        db.session.commit()

        response = self.client.put(f'/authors/{author.id}', json={
            'name': 'J.R.R. Tolkien', 'bio': 'Updated Bio', 'birth_date': '1892-01-03'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Bio', response.get_data(as_text=True))

    def test_delete_author(self):
        """Test DELETE /authors/{id} - delete an existing author."""
        author = Author(name='Isaac Asimov', bio='Author of Foundation', birth_date='1920-01-02')
        db.session.add(author)
        db.session.commit()

        response = self.client.delete(f'/authors/{author.id}')
        self.assertEqual(response.status_code, 204)

        # Verify deletion
        response = self.client.get(f'/authors/{author.id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
