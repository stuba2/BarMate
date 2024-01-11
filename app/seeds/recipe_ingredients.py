from app.models import db, environment, SCHEMA
from app.models.recipe_ingredient import RecipeIngredient
from sqlalchemy.sql import text


# Adds a demo user, you can add other recipe_ingredients here if you want
def seed_recipe_ingredients():
    vodka = RecipeIngredient(
        amount=2,
        unit='oz',
        recipe_id=1,
        ingredient_id=5
        )
    red_bull = RecipeIngredient(
        amount=1,
        unit='can',
        recipe_id=1,
        ingredient_id=2
        )
    gin = RecipeIngredient(
        amount=2,
        unit='oz',
        recipe_id=2,
        ingredient_id=6
        )
    apple_cider = RecipeIngredient(
        amount=1,
        unit='oz',
        recipe_id=2,
        ingredient_id=7
        )
    lemon_juice = RecipeIngredient(
        amount=1,
        unit='oz',
        recipe_id=2,
        ingredient_id=8
        )
    maple_syrup = RecipeIngredient(
        amount=0.75,
        unit='oz',
        recipe_id=2,
        ingredient_id=9
        )
    bourbon = RecipeIngredient(
        amount=2,
        unit='oz',
        recipe_id=3,
        ingredient_id=10
        )
    lime_juice_1 = RecipeIngredient(
        amount=0.5,
        unit='oz',
        recipe_id=3,
        ingredient_id=11
        )
    ginger_beer_1 = RecipeIngredient(
        amount=3,
        unit='oz',
        recipe_id=3,
        ingredient_id=12
        )
    mint = RecipeIngredient(
        amount=1,
        unit='sprig',
        recipe_id=3,
        ingredient_id=13
        )
    tequila = RecipeIngredient(
        amount=1.5,
        unit='oz',
        recipe_id=4,
        ingredient_id=14
        )
    lime_juice_2 = RecipeIngredient(
        amount=0.75,
        unit='oz',
        recipe_id=4,
        ingredient_id=11
        )
    orange_juice = RecipeIngredient(
        amount=0.75,
        unit='oz',
        recipe_id=4,
        ingredient_id=15
        )
    malort = RecipeIngredient(
        amount=0.5,
        unit='oz',
        recipe_id=4,
        ingredient_id=1
        )
    ginger_beer_2 = RecipeIngredient(
        amount=2,
        unit='oz',
        recipe_id=4,
        ingredient_id=12
        )

    db.session.add(vodka)
    db.session.add(red_bull)
    db.session.add(gin)
    db.session.add(apple_cider)
    db.session.add(lemon_juice)
    db.session.add(maple_syrup)
    db.session.add(bourbon)
    db.session.add(lime_juice_1)
    db.session.add(ginger_beer_1)
    db.session.add(mint)
    db.session.add(tequila)
    db.session.add(lime_juice_2)
    db.session.add(orange_juice)
    db.session.add(malort)
    db.session.add(ginger_beer_2)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the recipe_ingredients table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_recipe_ingredients():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipe_ingredients RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM recipe_ingredients"))

    db.session.commit()
