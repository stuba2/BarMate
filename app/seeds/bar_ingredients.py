from app.models import db, environment, SCHEMA
from app.models.ingredient import bar_ingredients
from sqlalchemy.sql import text


# Adds a demo user, you can add other bar_ingredients here if you want
def seed_bar_ingredients():
    mountain_dew = bar_ingredients(
        user_id=1,
        ingredient_id=4
        )
    red_bull = bar_ingredients(
        user_id=1,
        ingredient_id=2
        )
    vodka = bar_ingredients(
        user_id=1,
        ingredient_id=5
        )
    hamms = bar_ingredients(
        user_id=1,
        ingredient_id=3
        )
    gin = bar_ingredients(
        user_id=2,
        ingredient_id=6
        )
    apple_cider = bar_ingredients(
        user_id=2,
        ingredient_id=7
        )
    lemon_juice = bar_ingredients(
        user_id=2,
        ingredient_id=8
        )
    maple_syrup = bar_ingredients(
        user_id=2,
        ingredient_id=9
        )
    bourbon = bar_ingredients(
        user_id=3,
        ingredient_id=10
        )
    lime_juice = bar_ingredients(
        user_id=3,
        ingredient_id=11
        )
    ginger_beer = bar_ingredients(
        user_id=3,
        ingredient_id=12
        )
    mint = bar_ingredients(
        user_id=3,
        ingredient_id=13
        )
    tequila = bar_ingredients(
        user_id=4,
        ingredient_id=14
        )
    lime_juice_2 = bar_ingredients(
        user_id=4,
        ingredient_id=11
        )
    orange_juice = bar_ingredients(
        user_id=4,
        ingredient_id=15
        )
    malort = bar_ingredients(
        user_id=4,
        ingredient_id=1
        )
    ginger_beer_2 = bar_ingredients(
        user_id=4,
        ingredient_id=12
        )

    db.session.add(mountain_dew)
    db.session.add(red_bull)
    db.session.add(vodka)
    db.session.add(hamms)
    db.session.add(gin)
    db.session.add(apple_cider)
    db.session.add(lemon_juice)
    db.session.add(maple_syrup)
    db.session.add(bourbon)
    db.session.add(lime_juice)
    db.session.add(ginger_beer)
    db.session.add(mint)
    db.session.add(tequila)
    db.session.add(lime_juice_2)
    db.session.add(orange_juice)
    db.session.add(malort)
    db.session.add(ginger_beer_2)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the bar_ingredients table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_bar_ingredients():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.bar_ingredients RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM bar_ingredients"))

    db.session.commit()
