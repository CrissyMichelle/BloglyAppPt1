"""Seed file to make sample data for blogly database"""
from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add bloggers
isaac = User(first_name='Issac', last_name='Newton')
bowser = User(first_name='King', last_name='Koopa')
albert = User(first_name='Albert', last_name='Einstein')
cher = User(first_name="Cher", last_name="Sarkisian")

# Add new user objects to db and commit
db.session.add(isaac)
db.session.add(bowser)
db.session.add(albert)
db.session.add(cher)

db.session.commit()