from locust import HttpUser, TaskSet, task, between

class AuthorTasks(TaskSet):
    @task(1)
    def get_authors(self):
        """Simulate getting all authors."""
        self.client.get("/authors/")

    @task(2)
    def create_author(self):
        """Simulate creating a new author."""
        self.client.post("/authors/", json={
            "name": "Test Author",
            "bio": "This is a test author",
            "birth_date": "1980-01-01"
        })

    @task(1)
    def get_books(self):
        """Simulate getting all books."""
        self.client.get("/books/")

    @task(2)
    def create_book(self):
        """Simulate creating a new book."""
        self.client.post("/books/", json={
            "title": "Test Book",
            "description": "This is a test book",
            "publish_date": "2000-01-01",
            "author_id": 1  # Assuming author ID 1 exists
        })

class WebsiteUser(HttpUser):
    tasks = [AuthorTasks]
    wait_time = between(1, 5)  # Simulate a wait time between tasks
