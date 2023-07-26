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
    
class Post(db.Model):
    """Table of users' blog posts"""
    __tablename__ = 'jog_posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable = False, default="Untitled Post")
    content = db.Column(db.Text, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('joggers.id'))
    
    # Navigate one-to-many and many-to-many-relationships
    jogger = db.relationship('User', backref='jog_posts')
    # No need for assigned = db.relationship('PostTag', backref ='tag_post') and then extra step
    # Secondary relationship goes 'through' the middle table
    tags = db.relationship(
        'Tag', secondary = 'jog_tags', backref = 'user_posts'
    )

    def __repr__(self):
        """dunder method for easy representation of user-object records"""
        jog_post = self
        return f"<Post id = {jog_post.id} Title = {jog_post.title} Created at = {jog_post.created_at}  User = {jog_post.jogger.full_name}>"
    
class Tag(db.Model):
    """Table of tags for categorizing a blog post"""
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    def __repr__(self):
        """dunder method for easy representation of tags"""
        tag = self
        return f"<Tag id = {tag.id} Name of Tag = {tag.name}>"
    
    assignments = db.relationship('PostTag', backref = 'tagged')

class PostTag(db.Model):
    """Middle table for joining together a post and a tag"""
    __tablename__ = "jog_tags"

    post_id = db.Column(db.Integer, db.ForeignKey("jog_posts.id"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key=True)

    def __repr__(self):
        """dunder method for easy representation of posts and tags"""
        p_tag = self
        return f"<Post,Tag id = {p_tag.post_id,p_tag.tag_id}; Name of Tag = {p_tag.tagged.name}; Title of Post = {p_tag.post.title}>"
    
    def post_tag_join():
        # Show title of blog_post and name of tag
        tagged_jogs = (db.session.query(Post.title, Tag.name)
                  .join(Tag).all())

    post = db.relationship('Post', backref = 'post_tag')