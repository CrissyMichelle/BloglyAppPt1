"""Seed file to make sample data for blogly database"""
from models import User, Post, Tag, PostTag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()
Tag.query.delete()
PostTag.query.delete()

# Add bloggers
isaac = User(first_name='Issac', last_name='Newton')
charbli = User(first_name='Charbli', last_name='Dean', image_url='https://republicasiamedia.com/wp-content/uploads/2023/02/download.jpeg')
al = User(first_name='Al', last_name='Franken')
jeroen = User(first_name='Jeroen', last_name='Bosch', image_url='https://ia601008.us.archive.org/BookReader/BookReaderImages.php?zip=/27/items/secretsofopeningsurprises_vol7/Bosch%20-%20SOS%20-%20Secrets%20of%20Opening%20Surprises%20Vol.7_jp2.zip&file=Bosch%20-%20SOS%20-%20Secrets%20of%20Opening%20Surprises%20Vol.7_jp2/Bosch%20-%20SOS%20-%20Secrets%20of%20Opening%20Surprises%20Vol.7_0000.jp2&id=secretsofopeningsurprises_vol7&scale=2&rotate=0')
ol_blue = User(first_name='Ol', last_name='Blue')
tammy = User(first_name='Tammy', last_name='TamTam', image_url='https://parade.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTkwNTc5MDEyNDEwNjE1Njc2/nia-vardalos.jpg')
stan = User(first_name='Stanley', last_name='Statistician', image_url='https://jameshoward.us/assets/images/mathematician-different-kind-mathematician-statistician.jpg')
tonya = User(first_name='Tonya', last_name='Harding', image_url='https://www.the-sun.com/wp-content/uploads/sites/6/2023/01/1994-hamar-near-lillehammer-xviith-1068580.jpg?w=1240')
nancy = User(first_name='Nancy', last_name='Kerrigan', image_url='https://www.the-sun.com/wp-content/uploads/sites/6/2023/01/lm_tonyanancy_comp-copy.jpg?w=1280&quality=44')
barry = User(first_name='Barrigold', last_name='Bionic', image_url='https://uproxx.com/wp-content/uploads/2015/01/barry-main.jpg?w=650')
cher = User(first_name='Cher', last_name='Sarkisian', image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Cher_in_2019_cropped.jpg/440px-Cher_in_2019_cropped.jpg')
bowser = User(first_name='King', last_name='Koopa', image_url='https://i.ytimg.com/vi/yY7bRl5Kz3Q/mqdefault.jpg')
albert = User(first_name='Albert', last_name='Einstein')

# Add blog posts
first = Post(title="First Post!", content="Oh hai there", user_id=7)
code_rules = Post(title="I love Flask", content="Flask frameworks fly freely from flowing fountains.", user_id=11)
third = Post(title="Doctor says", content="Sweden this time of year might be good for my health?", user_id=11)
vacay = Post(title="Pet Hair", content="I may be covered in cat hair and bunny fluff but I still smell good.", user_id=11)
moonlight = Post(title="This Moonlight", content="Until we fall asleep the rolling thunder rattles the ice cream machine", user_id=11)
nine_toe = Post(title="Rock All Night", content="We says no funny stuff.  His girlfriend gave up her toe!", user_id=11)
putput = Post(title="The Ring of Fire", content="Bilbo liked listening to Johnny the Bard Cash, and that means comfort.", user_id=9)     
# Add and commit new user objects first
db.session.add(isaac)
db.session.add(charbli)
db.session.add(jeroen)
db.session.add(al)
db.session.add(ol_blue)
db.session.add(tammy)
db.session.add(stan)
db.session.add(tonya)
db.session.add(nancy)
db.session.add(barry)
db.session.add(bowser)
db.session.add(albert)
db.session.add(cher)

db.session.commit()

# Now we know the post objects will meet the Foreign Key constraint
db.session.add(first)
db.session.add(code_rules)
db.session.add(third)
db.session.add(vacay)
db.session.add(moonlight)
db.session.add(nine_toe)
db.session.add(putput)

db.session.commit()

# Add tags and tagged posts
fun = Tag(name='Fun')
health = Tag(name='Feels')
bloop = Tag(name='on Fleek')
boats = Tag(name="Boating") 

db.session.add(fun)
db.session.add(health)
db.session.add(bloop)
db.session.add(boats)

db.session.commit()

tag_jog = PostTag(post_id=1, tag_id=1)
put_tag = PostTag(post_id=7, tag_id=4)

db.session.add(tag_jog)
db.session.add(put_tag)

db.session.commit()