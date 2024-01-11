from app.models import db, environment, SCHEMA
from app.models.review import Review
from sqlalchemy.sql import text


# Adds a demo user, you can add other reviews here if you want
def seed_reviews():
    review_1 = Review(
        review_text='I can\'t believe people drink this',
        rating=2,
        user_id=1,
        recipe_id=4)
    review_2 = Review(
        review_text='Love this for camping trips!',
        rating=5,
        user_id=2,
        recipe_id=3)
    review_3 = Review(
        review_text='Never heard of this before, very refreshing!',
        rating=4,
        user_id=3,
        recipe_id=2)
    review_4 = Review(
        review_text='Doesn\'t hit like it used to',
        rating=3,
        user_id=4,
        recipe_id=1)

    db.session.add(review_1)
    db.session.add(review_2)
    db.session.add(review_3)
    db.session.add(review_4)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the reviews table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
