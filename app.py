from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config["SECRET_KEY"] = "yeahyeah"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """Redirects to show list of users"""
    return redirect('/users')

@app.route('/users')
def index_users():
    """Shows page listing all users"""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users = users)

@app.route('/users/new')
def show_add_form():
    """Page with add-new-blogger form"""
    return render_template("users/new.html")

@app.route('/users/new', methods=["POST"])
def process_add_form():
    """Handle form to add a new user"""
    new_blogger = User(
        first_name = request.form["first_name"],
        last_name = request.form["last_name"],
        image_url = request.form["image_url"] or None
    )
    db.session.add(new_blogger)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def blogger_info(user_id):
    """Show information about the given user"""
    blog_user = User.query.get_or_404(user_id)
    user_posts = Post.query.filter_by(user_id=blog_user.id).all()
    
    return render_template("users/[user-id].html", blog_user = blog_user, blog_posts = user_posts)

@app.route('/users/<int:user_id>/edit')
def show_edit_user(user_id):
    """Show form for updating a blogger's deets"""
    blog_user = User.query.get_or_404(user_id)
    return render_template("users/[user-id]/edit.html", blog_user = blog_user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def process_edit_form(user_id):
    """Handle form to edit an existing user"""
    edit_blogger = User.query.get_or_404(user_id)

    if request.form["first_name"]:
        edit_blogger.first_name = request.form["first_name"]
 
    if request.form["last_name"]: 
        edit_blogger.last_name = request.form["last_name"]

    if request.form["image_url"]:
        edit_blogger.image_url = request.form["image_url"]
    
    db.session.add(edit_blogger)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete')
def del_page(user_id):
    """Shows button for deleting the given user"""
    blog_user = User.query.get_or_404(user_id)
    return render_template("users/[user-id]/delete.html", blog_user = blog_user)

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def del_blogger(user_id):
    """Delete the blogly user"""
    User.query.filter_by(id=user_id).delete()
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/posts/new')
def show_add_post(user_id):
    """Show page with post-new-blog form"""
    blog_user = User.query.get_or_404(user_id)
    return render_template("users/[user-id]/posts/new.html", blogger = blog_user)

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def process_add_post(user_id):
    """Handle form to add a new post"""
    blog_user = User.query.get_or_404(user_id)

    new_post = Post(
        title = request.form["blog_title"],
        content = request.form["blog_content"],
        user_id = user_id
    )
    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/users/{user_id}')

@app.route('/posts/<int:blog_id>')
def post_info(blog_id):
    """Shows detailed content of the given post"""
    blog_post = Post.query.get_or_404(blog_id)
    blogger = blog_post.jogger
    
    return render_template("posts/[post-id].html", post = blog_post, blogger = blogger)

@app.route('/posts/<int:blog_id>/edit')
def show_edit_post(blog_id):
    """Show form for updating a blogger's deets"""
    blog_post = Post.query.get_or_404(blog_id)
    return render_template("posts/[post-id]/edit.html", post = blog_post)

@app.route('/posts/<int:blog_id>/edit', methods=["POST"])
def post_edit_form(blog_id):
    """Handle form to edit an existing post"""
    edit_post = Post.query.get_or_404(blog_id)

    if request.form["blog_title"]:
        edit_post.title = request.form["blog_title"]
    if request.form["blog_content"]: 
        edit_post.content = request.form["blog_content"]
    
    db.session.add(edit_post)
    db.session.commit()

    return redirect(f'/posts/{blog_id}')

@app.route('/posts/<int:blog_id>/delete')
def del_post_page(blog_id):
    """Shows button for deleting the given post"""
    blog_post = Post.query.get_or_404(blog_id)
    return render_template("posts/[post-id]/delete.html", post = blog_post)

@app.route('/posts/<int:blog_id>/delete', methods=["POST"])
def del_post(blog_id):
    """Deletes the blog post"""
    Post.query.filter_by(id=blog_id).delete()
    db.session.commit()

    return redirect('/users')