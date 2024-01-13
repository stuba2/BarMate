from app.models import db, environment, SCHEMA
from app.models.toast import Toast
from sqlalchemy.sql import text


# Adds a demo user, you can add other toasts here if you want
def seed_toasts():
    malort = Toast(
        user_id=1,
        recipe_id=2)
    red_bull = Toast(
        user_id=2,
        recipe_id=3)
    hamms = Toast(
        user_id=3,
        recipe_id=4)
    mountain_dew = Toast(
        user_id=4,
        recipe_id=1)

    db.session.add(malort)
    db.session.add(red_bull)
    db.session.add(hamms)
    db.session.add(mountain_dew)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the toasts table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_toasts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.toasts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM toasts"))

    db.session.commit()
