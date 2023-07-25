from unittest import TestCase

from app import app
from models import db, User, Post

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Tests for Users model"""

    def setUp(self):
        """Clean up any existing users"""
        Post.query.delete()
        User.query.delete()
        
    def tearDown(self):
        """Clean up any fouled transactions"""
        db.session.rollback()

    def test_greet(self):
        blogger = User(first_name="Test", last_name="User")
        self.assertEqual(blogger.greet(), "Greetings Test!  Glad you're here.")
    
    def test_full_name(self):
        blogger = User(id=29, first_name="Test", last_name="User")
        self.assertEqual(blogger.full_name, "Test User")


class PostModelTestCase(TestCase):
    """Tests for Users model"""

    def setUp(self):
        """Clean up any existing posts"""
        Post.query.delete()
        User.query.delete()
    
    def tearDown(self):
        """Clean up any fouled transactions"""
        db.session.rollback()
            
    def test_relationship(self):
        blogger = User(first_name="Test", last_name="User")       
        db.session.add(blogger)
        db.session.commit()

        post = Post(title="Example", content="Test post.", user_id=blogger.id)
        db.session.add(post)
        db.session.commit()

        self.assertEqual(blogger.id, post.jogger.id)