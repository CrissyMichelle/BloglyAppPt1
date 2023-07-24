from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """Tests for Users model"""

    def setUp(self):
        """Clean up any existing users"""
        User.query.delete()
    
    def tearDown(self):
        """Clean up any fouled transactions"""
        db.session.rollback()
    
    def test_greet(self):
        blogger = User(first_name="Test", last_name="User")
        self.assertEquals(blogger.greet(), "Greetings Test!  Glad you're here.")
    
    def test_full_name(self):
        blogger = User(first_name="Test", last_name="User")
        self.assertEquals(blogger.full_name, "Test User")