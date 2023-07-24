from unittest import TestCase
from models import db, User
from app import app

# Use test database and don't clutter tests with the SQL echo
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'

# Make Flask errors real errors rather than HTML pages with jinja error info
app.config['TESTING'] = True

# Hide Flask DebugToolbar for ease of testing
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """Tests four view routes for blogly app"""

    def setUp(self):
        """Add sample blogger"""
        User.query.delete()

        blogger = User(first_name="Test1", last_name="User", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Cher_in_2019_cropped.jpg/440px-Cher_in_2019_cropped.jpg")
        blogger2 = User(first_name="Test", last_name="--User2")

        db.session.add(blogger)
        db.session.add(blogger2)
        db.session.commit()

        self.blogger_id = blogger.id

    def tearDown(self):
        """Clean up any fouled transactions"""
        db.session.rollback()

    def test_show_user_index(self):
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)      
            self.assertIn('Test1 User', html)
            self.assertIn('--User2', html)

    def test_show_user(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.blogger_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h2>Test1 User</h2>', html)

    def test_add_user(self):
        with app.test_client() as client:
            new_data = {"first_name": "Rich", "last_name": "Router", "image_url": "https://www.google.com/"}
            resp = client.post("/users/new", data=new_data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Rich Router', html)
    
    def test_del_user(self):
        with app.test_client() as client:
            resp = client.post(f"/users/{self.blogger_id}/delete", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn('Test1', html)