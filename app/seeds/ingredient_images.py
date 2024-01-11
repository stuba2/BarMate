from app.models import db, environment, SCHEMA
from app.models.ingredient_image import IngredientImage
from sqlalchemy.sql import text


# Adds a demo user, you can add other ingredient_images here if you want
def seed_ingredient_images():
    malort_pic = IngredientImage(
        recipe_id=1,
        url='https://live.staticflickr.com/96/260768879_7bb31839a0_c.jpg')
    red_bull_pic = IngredientImage(
        recipe_id=2,
        url='https://live.staticflickr.com/4073/4935622208_03f0dbaf3b.jpg')
    hamms_pic = IngredientImage(
        recipe_id=3,
        url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Can_of_Hamm%27s_beer.jpg/450px-Can_of_Hamm%27s_beer.jpg?20220620020535')
    mountain_dew_pic = IngredientImage(
        recipe_id=4,
        url='https://live.staticflickr.com/3241/2684540855_a4b6734fab_z.jpg')

    db.session.add(malort_pic)
    db.session.add(red_bull_pic)
    db.session.add(hamms_pic)
    db.session.add(mountain_dew_pic)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the ingredient_images table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_ingredient_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.ingredient_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM ingredient_images"))

    db.session.commit()
