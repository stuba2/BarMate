from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='demo',
        email='demo@aa.io',
        password='password',
        dob=datetime(1985,1,1))
    tobey = User(
        username='tobey',
        email='tobey@tobey.io',
        password='password',
        dob=datetime(1990,1,1))
    andrew = User(
        username='andrew',
        email='andrew@andrew.io',
        password='password',
        dob=datetime(1995,1,1))
    tom = User(
        username='tom',
        email='tom@tom.io',
        password='password',
        dob=datetime(2000,1,1))

    db.session.add(demo)
    db.session.add(tobey)
    db.session.add(andrew)
    db.session.add(tom)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
