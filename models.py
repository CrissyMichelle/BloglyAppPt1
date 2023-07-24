from flask_sqlalchemy import SQLAlchemy

db =  SQLAlchemy()

def connect_db(app):
    """Wraps logic into a function connecting app to database"""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """Users of the blogly app"""
    __tablename__ = "joggers"

    @classmethod
    def get_by_image_url(cls, image_url):
        """Filter all users based on their profile pic"""
        return cls.query.filter_by(image_url=image_url).all()

    def __repr__(self):
        """dunder method for easy representation of user-object records"""
        jogger = self
        return f"<User id = {jogger.id} First Name = {jogger.first_name} Last Name = {jogger.last_name} Image URL = {jogger.image_url}>"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default='https://cdn-icons-png.flaticon.com/512/5073/5073810.png')

    def greet(self):
        """Welcome message greeting blogger"""
        return f"Greetings {self.first_name}!  Glad you're here."
    
    @property
    def full_name(self):
        """Returns concatenation of user's names"""
        return f"{self.first_name} {self.last_name}"