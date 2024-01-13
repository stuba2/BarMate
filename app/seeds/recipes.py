from app.models import db, environment, SCHEMA
from app.models.recipe import Recipe
from sqlalchemy.sql import text


# Adds a demo user, you can add other recipes here if you want
def seed_recipes():
    vodka_red_bull = Recipe(
        name='Vodka Red Bull',
        description='Quick and easy energy burst',
        instructions='Mix 2oz vodka, and top off with Red Bull',
        user_id=1)
    gin_apple_cider = Recipe(
        name='Gin Apple Cider',
        description='Refreshing cocktail for the early fall',
        instructions='Mix 2oz gin, 1oz apple cider, 1oz lemon juice, and 3/4oz maple syrup in a shaker with ice. Strain into ice',
        user_id=2)
    kentucky_mule = Recipe(
        name='Kentucky Mule',
        description='An American twist on the Moscow Mule',
        instructions='Mix 2oz bourbon and 1/2oz lime juice into a copper mug with ice. Top off with ginger beer and a mint sprig to garnish.',
        user_id=3)
    malort_highball = Recipe(
        name='Malort Highball',
        description='Chicago\'s favorite upscale cocktail.',
        instructions='Mix 1 1/2oz tequila, 3/4oz lime juice, 3/4oz orange juice, 1/2oz Jeppson\'s Malort in a shaker, and strain into ice. Top off with 2oz ginger beer.',
        user_id=4)

    db.session.add(vodka_red_bull)
    db.session.add(gin_apple_cider)
    db.session.add(kentucky_mule)
    db.session.add(malort_highball)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the recipes table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_recipes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM recipes"))

    db.session.commit()
