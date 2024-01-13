from app.models import db, environment, SCHEMA
from app.models.ingredient import Ingredient
from sqlalchemy.sql import text


# Adds a demo user, you can add other ingredients here if you want
def seed_ingredients():
    malort = Ingredient(
        name='Jeppson\s Malort')
    red_bull = Ingredient(
        name='Red Bull')
    hamms = Ingredient(
        name='Hamm\'s Beer')
    mountain_dew = Ingredient(
        name='Mountain Dew')

    db.session.add(malort)
    db.session.add(red_bull)
    db.session.add(hamms)
    db.session.add(mountain_dew)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the ingredients table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_ingredients():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.ingredients RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM ingredients"))

    db.session.commit()
