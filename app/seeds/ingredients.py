from app.models import db, environment, SCHEMA
from app.models.ingredient import Ingredient
from sqlalchemy.sql import text
from app.seeds.users import ex
from app.models.ingredient import bar_ingredients

# Adds a demo user, you can add other ingredients here if you want
def seed_ingredients():
    malort = Ingredient( #1
        name='Jeppson\s Malort')
    red_bull = Ingredient( #2
        name='Red Bull')
    hamms = Ingredient( #3
        name='Hamm\'s Beer')
    mountain_dew = Ingredient( #4
        name='Mountain Dew')
    vodka = Ingredient( #5
        name='Vodka')
    gin = Ingredient( #6
        name='Gin')
    apple_cider = Ingredient( #7
        name='Apple Cider')
    lemon_juice = Ingredient( #8
        name='Lemon Juice')
    maple_syrup = Ingredient( #9
        name='Maple Syrup')
    bourbon = Ingredient( #10
        name='Bourbon')
    lime_juice = Ingredient( #11
        name='Lime Juice')
    ginger_beer = Ingredient( #12
        name='Ginger Beer')
    mint = Ingredient( #13
        name='Mint')
    tequila = Ingredient( #14
        name='Tequila')
    orange_juice = Ingredient( #15
        name='Orange Juice')

    mountain_dew.bar_ingredients_users.append(ex[0])
    red_bull.bar_ingredients_users.append(ex[0])
    vodka.bar_ingredients_users.append(ex[0])
    hamms.bar_ingredients_users.append(ex[0])

    gin.bar_ingredients_users.append(ex[1])
    apple_cider.bar_ingredients_users.append(ex[1])
    lemon_juice.bar_ingredients_users.append(ex[1])
    maple_syrup.bar_ingredients_users.append(ex[1])

    bourbon.bar_ingredients_users.append(ex[2])
    lime_juice.bar_ingredients_users.append(ex[2])
    ginger_beer.bar_ingredients_users.append(ex[2])
    mint.bar_ingredients_users.append(ex[2])

    tequila.bar_ingredients_users.append(ex[3])
    lime_juice.bar_ingredients_users.append(ex[3])
    orange_juice.bar_ingredients_users.append(ex[3])
    malort.bar_ingredients_users.append(ex[3])
    ginger_beer.bar_ingredients_users.append(ex[3])

    print('-------------', ex)
    print('~~~~~~~~~~~~~~~~~~~~~', malort.bar_ingredients_users)
    print('~~~~~~~~~~~~~~~~~~~~~2', malort.bar_ingredients_users[0].to_dict())

    db.session.add(malort)
    db.session.add(red_bull)
    db.session.add(hamms)
    db.session.add(mountain_dew)
    db.session.add(vodka)
    db.session.add(gin)
    db.session.add(apple_cider)
    db.session.add(lemon_juice)
    db.session.add(maple_syrup)
    db.session.add(bourbon)
    db.session.add(lime_juice)
    db.session.add(ginger_beer)
    db.session.add(mint)
    db.session.add(tequila)
    db.session.add(orange_juice)
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
