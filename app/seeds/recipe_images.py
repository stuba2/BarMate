from app.models import db, environment, SCHEMA
from app.models.recipe_image import RecipeImage
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    vodka_red_bull_pic = RecipeImage(
        recipe_id=1,
        url='https://images.pexels.com/photos/16444383/pexels-photo-16444383/free-photo-of-glass-of-red-bull.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
    gin_apple_cider_pic = RecipeImage(
        recipe_id=2,
        url='https://images.rawpixel.com/image_600/cHJpdmF0ZS9zdGF0aWMvaW1hZ2Uvd2Vic2l0ZS8yMDIyLTA0L2xyL3NrODA0LWltYWdlLWt3dnVrMWZtLmpwZw.jpg')
    kentucky_mule_pic = RecipeImage(
        recipe_id=3,
        url='https://live.staticflickr.com/7255/7560780984_6e2a5f066e_c.jpg')
    malort_highball_pic = RecipeImage(
        recipe_id=4,
        url='https://negativespace.co/wp-content/uploads/2019/06/negative-space-red-summer-cocktail-473x708.jpg')

    db.session.add(vodka_red_bull_pic)
    db.session.add(gin_apple_cider_pic)
    db.session.add(kentucky_mule_pic)
    db.session.add(malort_highball_pic)
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
