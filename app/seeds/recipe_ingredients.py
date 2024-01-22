from app.models import db, environment, SCHEMA, Recipe, Ingredient
from app.models.recipe_ingredient import RecipeIngredient
from sqlalchemy.sql import text


# Adds a demo user, you can add other recipe_ingredients here if you want
def seed_recipe_ingredients():
    vodkaa = RecipeIngredient(
        amount=2,
        unit='oz',
        recipe_id=1,
        ingredient_id=5
        )
    red_bulll = RecipeIngredient(
        amount=1,
        unit='can',
        recipe_id=1,
        ingredient_id=2
        )
    ginn = RecipeIngredient(
        amount=2,
        unit='oz',
        recipe_id=2,
        ingredient_id=6
        )
    apple_ciderr = RecipeIngredient(
        amount=1,
        unit='oz',
        recipe_id=2,
        ingredient_id=7
        )
    lemon_juicee = RecipeIngredient(
        amount=1,
        unit='oz',
        recipe_id=2,
        ingredient_id=8
        )
    maple_syrupp = RecipeIngredient(
        amount=0.75,
        unit='oz',
        recipe_id=2,
        ingredient_id=9
        )
    bourbonn = RecipeIngredient(
        amount=2,
        unit='oz',
        recipe_id=3,
        ingredient_id=10
        )
    lime_juicee_1 = RecipeIngredient(
        amount=0.5,
        unit='oz',
        recipe_id=3,
        ingredient_id=11
        )
    ginger_beerr_1 = RecipeIngredient(
        amount=3,
        unit='oz',
        recipe_id=3,
        ingredient_id=12
        )
    mintt = RecipeIngredient(
        amount=1,
        unit='sprig',
        recipe_id=3,
        ingredient_id=13
        )
    tequilaa = RecipeIngredient(
        amount=1.5,
        unit='oz',
        recipe_id=4,
        ingredient_id=14
        )
    lime_juicee_2 = RecipeIngredient(
        amount=0.75,
        unit='oz',
        recipe_id=4,
        ingredient_id=11
        )
    orange_juicee = RecipeIngredient(
        amount=0.75,
        unit='oz',
        recipe_id=4,
        ingredient_id=15
        )
    malortt = RecipeIngredient(
        amount=0.5,
        unit='oz',
        recipe_id=4,
        ingredient_id=1
        )
    ginger_beerr_2 = RecipeIngredient(
        amount=2,
        unit='oz',
        recipe_id=4,
        ingredient_id=12
        )

    db.session.add(vodkaa)
    db.session.add(red_bulll)
    db.session.add(ginn)
    db.session.add(apple_ciderr)
    db.session.add(lemon_juicee)
    db.session.add(maple_syrupp)
    db.session.add(bourbonn)
    db.session.add(lime_juicee_1)
    db.session.add(ginger_beerr_1)
    db.session.add(mintt)
    db.session.add(tequilaa)
    db.session.add(lime_juicee_2)
    db.session.add(orange_juicee)
    db.session.add(malortt)
    db.session.add(ginger_beerr_2)


    ir0 = RecipeIngredient(
            amount=1.75,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    ir2 = RecipeIngredient(
            amount=0.25,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir3 = RecipeIngredient(
            amount=0.125,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir4 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'ABC').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir5 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'ABC').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir6 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'ABC').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    ir7 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir8 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir9 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    ir10 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir11 = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg White').first().id
        )
    ir12 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'ACID').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    ir13 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'ACID').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wild Turkey').first().id
        )
    ir14 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir15 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir16 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir17 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'AT&T').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    ir18 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'AT&T').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir19 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'AT&T').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic water').first().id
        )
    ir20 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A. J.').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Applejack').first().id
        )
    ir21 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A. J.').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    ir22 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affair').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberry schnapps').first().id
        )
    ir23 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affair').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir24 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affair').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir25 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir26 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    ir27 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    ir28 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir29 = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir30 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pisang Ambon').first().id
        )
    ir31 = RecipeIngredient(
            amount=6,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    ir32 = RecipeIngredient(
            amount=1.5,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir33 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abilene').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir34 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abilene').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach nectar').first().id
        )
    ir35 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abilene').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir36 = RecipeIngredient(
            amount=1.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir37 = RecipeIngredient(
            amount=1.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vermouth').first().id
        )
    ir38 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almeria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir39 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almeria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir40 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almeria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ir41 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir42 = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir43 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir44 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir45 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ir46 = RecipeIngredient(
            amount=1,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir47 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir48 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir49 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir50 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir51 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Applejack').first().id
        )
    ir52 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir53 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir54 = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aviation').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir55 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aviation').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon juice').first().id
        )
    ir56 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aviation').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'maraschino liqueur').first().id
        )
    ir57 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir58 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir59 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir60 = RecipeIngredient(
            amount=0.5,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir61 = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    ir62 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addington').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir63 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addington').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir64 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addington').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir65 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'After sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir66 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'After sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Banane').first().id
        )
    ir67 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afterglow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir68 = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afterglow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir69 = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afterglow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir70 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir71 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir72 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Frangelico').first().id
        )
    ir73 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir74 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir75 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    ir76 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir77 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Algonquin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    ir78 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Algonquin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir79 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Algonquin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir80 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir81 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir82 = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberry brandy').first().id
        )
    ir83 = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir84 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir85 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ir86 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir87 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir88 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    ir89 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applejack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jack Daniels').first().id
        )
    ir90 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applejack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    ir91 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applejack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    ir92 = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir93 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir94 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir95 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autodafé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir96 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autodafé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir97 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalanche').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Crown Royal').first().id
        )
    ir98 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalanche').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir99 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalanche').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    ir100 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir101 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    ir102 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    ir103 = RecipeIngredient(
            amount=0.125,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lemon Juice').first().id
        )
    ir104 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Joy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir105 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Joy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    ir106 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Joy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir107 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angel Face').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    ir108 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angel Face').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple brandy').first().id
        )
    ir109 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angel Face').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir110 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aquamarine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hpnotiq').first().id
        )
    ir111 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aquamarine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    ir112 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aquamarine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana Liqueur').first().id
        )
    ir113 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir114 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    ir115 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    ir116 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir117 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir118 = RecipeIngredient(
            amount=50,
            unit='gr',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir119 = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anise').first().id
        )
    ir120 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Licorice root').first().id
        )
    ir121 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wormwood').first().id
        )
    ir122 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Kurant').first().id
        )
    ir123 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    ir124 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir125 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    ir126 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir127 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grape soda').first().id
        )
    ir128 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir129 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir130 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Candy').first().id
        )
    ir131 = RecipeIngredient(
            amount=1,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ir132 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir133 = RecipeIngredient(
            amount=7,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir134 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ir135 = RecipeIngredient(
            amount=0.5,
            unit='blender',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir136 = RecipeIngredient(
            amount=0.5,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ir137 = RecipeIngredient(
            amount=0.5,
            unit='blender',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir138 = RecipeIngredient(
            amount=10,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir139 = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    ir140 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir141 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped cream').first().id
        )
    ir142 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Grande').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir143 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Grande').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple cider').first().id
        )
    ir144 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Karate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    ir145 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Karate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Carrot').first().id
        )
    ir146 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir147 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    ir148 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir149 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir150 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ir151 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir152 = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir153 = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir154 = RecipeIngredient(
            amount=45,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice cordial').first().id
        )
    ir155 = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir156 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir157 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    ir158 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit syrup').first().id
        )
    ir159 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ir160 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    ir161 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir162 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir163 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir164 = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir165 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir166 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir167 = RecipeIngredient(
            amount=15,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Wine').first().id
        )
    ir168 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    ir169 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Mist').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir170 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Mist').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir171 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir172 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir173 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir174 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    ir175 = RecipeIngredient(
            amount=100,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aperol Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Aperol').first().id
        )
    ir176 = RecipeIngredient(
            amount=150,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aperol Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    ir177 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aperol Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir178 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '7-Up').first().id
        )
    ir179 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple schnapps').first().id
        )
    ir180 = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    ir181 = RecipeIngredient(
            amount=4,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir182 = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir183 = RecipeIngredient(
            amount=4,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '7-Up').first().id
        )
    ir184 = RecipeIngredient(
            amount=0.5,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir185 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arise My Love').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir186 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arise My Love').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Creme de Menthe').first().id
        )
    ir187 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ir188 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir189 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir190 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir191 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Piece of Ass').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir192 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Piece of Ass').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    ir193 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Piece of Ass').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir194 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir195 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir196 = RecipeIngredient(
            amount=0.25,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir197 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir198 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alfie Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon vodka').first().id
        )
    ir199 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alfie Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir200 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alfie Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir201 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir202 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir203 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir204 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    ir205 = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate ice-cream').first().id
        )
    ir206 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir207 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir208 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir209 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple Schnapps').first().id
        )
    ir210 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    ir211 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    ir212 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir213 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir214 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir215 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adonis Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir216 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adonis Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    ir217 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adonis Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir218 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    ir219 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir220 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    ir221 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir222 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir223 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir224 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yellow Chartreuse').first().id
        )
    ir225 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir226 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allies Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir227 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allies Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir228 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allies Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kummel').first().id
        )
    ir229 = RecipeIngredient(
            amount=0.5,
            unit='jigger',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir230 = RecipeIngredient(
            amount=3,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir231 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    ir232 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir233 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir234 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    ir235 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gold tequila').first().id
        )
    ir236 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir237 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir238 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream of coconut').first().id
        )
    ir239 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir240 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir241 = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    ir242 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir243 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    ir244 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir245 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir246 = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    ir247 = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rye whiskey').first().id
        )
    ir248 = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    ir249 = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir250 = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir251 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    ir252 = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir253 = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir254 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir255 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    ir256 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    ir257 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Banane').first().id
        )
    ir258 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir259 = RecipeIngredient(
            amount=0.75,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir260 = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot').first().id
        )
    ir261 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Almond flavoring').first().id
        )
    ir262 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grain alcohol').first().id
        )
    # ir263 = RecipeIngredient(
    #         amount=0.5,
    #         unit='cup',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
    #     )
    ir264 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir265 = RecipeIngredient(
            amount=3,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    # ir266 = RecipeIngredient(
    #         amount=6,
    #         unit='drops',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
    #     )
    # ir267 = RecipeIngredient(
    #         amount=2,
    #         unit='drops',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
    #     )
    ir268 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Glycerine').first().id
        )
    ir269 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir270 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    ir271 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir272 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir273 = RecipeIngredient(
            amount=0.25,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir274 = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angelica root').first().id
        )
    ir275 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Almond').first().id
        )
    ir276 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Allspice').first().id
        )
    ir277 = RecipeIngredient(
            amount=1,
            unit='stick',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ir278 = RecipeIngredient(
            amount=3,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anise').first().id
        )
    ir279 = RecipeIngredient(
            amount=0.125,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coriander').first().id
        )
    ir280 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Marjoram leaves').first().id
        )
    ir281 = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir282 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir283 = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir284 = RecipeIngredient(
            amount=1,
            unit='drop',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    # ir285 = RecipeIngredient(
    #         amount=1,
    #         unit='drop',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
    #     )
    ir286 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Mouthwash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maui').first().id
        )
    ir287 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Mouthwash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mountain Dew').first().id
        )
    ir288 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Mouthwash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir289 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Stingers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    ir290 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Stingers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Iced tea').first().id
        )
    ir291 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ir292 = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir293 = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger Beer').first().id
        )
    ir294 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    ir295 = RecipeIngredient(
            amount=0.67,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Evergreen').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    ir296 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Evergreen').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pisang Ambon').first().id
        )
    ir297 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Evergreen').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir298 = RecipeIngredient(
            amount=0.67,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    ir299 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir300 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir301 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic water').first().id
        )
    ir302 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    ir303 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    ir304 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut liqueur').first().id
        )
    ir305 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir306 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir307 = RecipeIngredient(
            amount=0.75,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir308 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    ir309 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guava juice').first().id
        )
    ir310 = RecipeIngredient(
            amount=1.5,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir311 = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    ir312 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir313 = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir314 = RecipeIngredient(
            amount=4,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple cider').first().id
        )
    ir315 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brown sugar').first().id
        )
    ir316 = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ir317 = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir318 = RecipeIngredient(
            amount=6,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    ir319 = RecipeIngredient(
            amount=6,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Allspice').first().id
        )
    ir320 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    ir321 = RecipeIngredient(
            amount=3,
            unit='sticks',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ir322 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Auburn Headbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    ir323 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Auburn Headbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    ir324 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut rum').first().id
        )
    ir325 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir326 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir327 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir328 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Furlong Too Late').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir329 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Furlong Too Late').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger beer').first().id
        )
    ir330 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Furlong Too Late').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir331 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    ir332 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ir333 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    ir334 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    ir335 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir336 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto And Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir337 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto And Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir338 = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Antifreeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir339 = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Antifreeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    ir340 = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Antifreeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ir341 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan\'s Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir342 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan\'s Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    ir343 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan\'s Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir344 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan\'s Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir345 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Fabulous').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir346 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Fabulous').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry Juice').first().id
        )
    ir347 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Fabulous').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir348 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice in Wonderland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir349 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice in Wonderland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    ir350 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice in Wonderland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    ir351 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir352 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    ir353 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir354 = RecipeIngredient(
            amount=1,
            unit='jigger',
            recipe_id=Recipe.query.filter(Recipe.name == 'A True Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir355 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'A True Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir356 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    ir357 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir358 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir359 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ir360 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Berry Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Berries').first().id
        )
    ir361 = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Berry Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple').first().id
        )
    ir362 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir363 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir364 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    ir365 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir366 = RecipeIngredient(
            amount=0.25,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lime Juice').first().id
        )
    ir367 = RecipeIngredient(
            amount=0.25,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir368 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir369 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    ir370 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir371 = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    # ir372 = RecipeIngredient(
    #         amount=1,
    #         unit='unit',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
    #     )
    ir373 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Supper Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir374 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Supper Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    ir375 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Supper Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir376 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir377 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kirschwasser').first().id
        )
    ir378 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberry liqueur').first().id
        )
    ir379 = RecipeIngredient(
            amount=5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir380 = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Pie with A Crust').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    ir381 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Pie with A Crust').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    ir382 = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Pie with A Crust').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ir383 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir384 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Añejo rum').first().id
        )
    ir385 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir386 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir387 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ir388 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir389 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Chocolate Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir390 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Chocolate Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Creme de Cacao').first().id
        )
    ir391 = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Chocolate Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir392 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    ir393 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    ir394 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir395 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot chocolate').first().id
        )
    ir396 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    ir397 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir398 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ir399 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir400 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    ir401 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir402 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir403 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir404 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-52').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir405 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-52').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    ir406 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-52').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir407 = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-53').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir408 = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-53').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    ir409 = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-53').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    ir410 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Bitters').first().id
        )
    ir411 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    ir412 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir413 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir414 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir415 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir416 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir417 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir418 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ir419 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Big Red').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish cream').first().id
        )
    ir420 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Big Red').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    ir421 = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir422 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    ir423 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir424 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon juice').first().id
        )
    ir425 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    ir426 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Mure').first().id
        )
    ir427 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir428 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir429 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir430 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir431 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir432 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir433 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir434 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir435 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir436 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir437 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rye Whiskey').first().id
        )
    ir438 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir439 = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Liqueur').first().id
        )
    ir440 = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir441 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Cherry').first().id
        )
    ir442 = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir443 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit juice').first().id
        )
    ir444 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir445 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir446 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir447 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir448 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir449 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    ir450 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir451 = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir452 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    ir453 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    ir454 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir455 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    ir456 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brigadier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot Chocolate').first().id
        )
    ir457 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brigadier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    ir458 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brigadier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry Heering').first().id
        )
    ir459 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    ir460 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir461 = RecipeIngredient(
            amount=3,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir462 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wormwood').first().id
        )
    ir463 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir464 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Buccaneer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Corona').first().id
        )
    ir465 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Buccaneer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bacardi Limon').first().id
        )
    ir466 = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Everclear').first().id
        )
    ir467 = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir468 = RecipeIngredient(
            amount=2,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mountain Dew').first().id
        )
    ir469 = RecipeIngredient(
            amount=2,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Surge').first().id
        )
    ir470 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir471 = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir472 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blackthorn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir473 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blackthorn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    ir474 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blackthorn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir475 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bob Marley').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    ir476 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bob Marley').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    ir477 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bob Marley').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    ir478 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    ir479 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir480 = RecipeIngredient(
            amount=2,
            unit='wedges',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir481 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    ir482 = RecipeIngredient(
            amount=0.25,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir483 = RecipeIngredient(
            amount=0.25,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana liqueur').first().id
        )
    ir484 = RecipeIngredient(
            amount=0.25,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir485 = RecipeIngredient(
            amount=0.25,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    ir486 = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bumble Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir487 = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bumble Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir488 = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bumble Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    ir489 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Eskimo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir490 = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Eskimo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir491 = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Eskimo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla ice-cream').first().id
        )
    ir492 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    ir493 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir494 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir495 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    # ir496 = RecipeIngredient(
    #         amount=1,
    #         unit='slice',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
    #     )
    ir497 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir498 = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir499 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    ir500 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana liqueur').first().id
        )
    ir501 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir502 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    ir503 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir504 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and Sour').first().id
        )
    ir505 = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brainteaser').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    ir506 = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brainteaser').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Erin Cream').first().id
        )
    ir507 = RecipeIngredient(
            amount=5,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brainteaser').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Advocaat').first().id
        )
    ir508 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir509 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato juice').first().id
        )
    ir510 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir511 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Worcestershire sauce').first().id
        )
    ir512 = RecipeIngredient(
            amount=2,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    ir513 = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir514 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black & Tan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ale').first().id
        )
    ir515 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black & Tan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guinness stout').first().id
        )
    ir516 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Lagoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir517 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Lagoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir518 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee\'s Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gold rum').first().id
        )
    ir519 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee\'s Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir520 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee\'s Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir521 = RecipeIngredient(
            amount=2,
            unit='jiggers',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee\'s Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    ir522 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir523 = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    ir524 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir525 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir526 = RecipeIngredient(
            amount=0.125,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    ir527 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir528 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir529 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    # ir530 = RecipeIngredient(
    #         amount=0.5,
    #         unit='slice',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
    #     )
    ir531 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir532 = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla Ice-Cream').first().id
        )
    ir533 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butterscotch schnapps').first().id
        )
    ir534 = RecipeIngredient(
            amount=1,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir535 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir536 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ir537 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir538 = RecipeIngredient(
            amount=1.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rye whiskey').first().id
        )
    ir539 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    ir540 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir541 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir542 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir543 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir544 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir545 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir546 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut liqueur').first().id
        )
    ir547 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir548 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    ir549 = RecipeIngredient(
            amount=10,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir550 = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir551 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir552 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    # ir553 = RecipeIngredient(
    #         amount=12,
    #         unit='oz',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
    #     )
    ir554 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raisins').first().id
        )
    ir555 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blueberries').first().id
        )
    ir556 = RecipeIngredient(
            amount=2,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Everclear').first().id
        )
    ir557 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    ir558 = RecipeIngredient(
            amount=0.5,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir559 = RecipeIngredient(
            amount=1,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kool-Aid').first().id
        )
    ir560 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir561 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato juice').first().id
        )
    ir562 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir563 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    ir564 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Celery salt').first().id
        )
    ir565 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir566 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir567 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Godiva liqueur').first().id
        )
    ir568 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir569 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butterscotch schnapps').first().id
        )
    ir570 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir571 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Añejo rum').first().id
        )
    ir572 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tia maria').first().id
        )
    ir573 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir574 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir575 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir576 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir577 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut Liqueur').first().id
        )
    ir578 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blueberries').first().id
        )
    ir579 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    ir580 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    ir581 = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir582 = RecipeIngredient(
            amount=20,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    ir583 = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lime Juice').first().id
        )
    ir584 = RecipeIngredient(
            amount=75,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger beer').first().id
        )
    ir585 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir586 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    ir587 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir588 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir589 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir590 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir591 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir592 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir593 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    ir594 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peachtree schnapps').first().id
        )
    ir595 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir596 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee liqueur').first().id
        )
    ir597 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir598 = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Guinness').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir599 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Guinness').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir600 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir601 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    ir602 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir603 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir604 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir605 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir606 = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir607 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    ir608 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passoa').first().id
        )
    ir609 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir610 = RecipeIngredient(
            amount=6,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and Sour').first().id
        )
    ir611 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir612 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir613 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir614 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir615 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir616 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir617 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir618 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir619 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    ir620 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cream Pi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu Rum').first().id
        )
    ir621 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cream Pi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana Liqueur').first().id
        )
    ir622 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cream Pi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    ir623 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir624 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir625 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    ir626 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir627 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir628 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir629 = RecipeIngredient(
            amount=8,
            unit='cubes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir630 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir631 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach nectar').first().id
        )
    ir632 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    ir633 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir634 = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black and Brown').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guinness stout').first().id
        )
    ir635 = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black and Brown').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Root beer').first().id
        )
    ir636 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir637 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    ir638 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir639 = RecipeIngredient(
            amount=1.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir640 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir641 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    ir642 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir643 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir644 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir645 = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Surge').first().id
        )
    ir646 = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir647 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    ir648 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir649 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir650 = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blueberries').first().id
        )
    ir651 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    ir652 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bermuda Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir653 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bermuda Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir654 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bermuda Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir655 = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry Vodka').first().id
        )
    ir656 = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry Juice').first().id
        )
    ir657 = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ir658 = RecipeIngredient(
            amount=10,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir659 = RecipeIngredient(
            amount=10,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir660 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir661 = RecipeIngredient(
            amount=1,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir662 = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir663 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir664 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    ir665 = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    ir666 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brave Bull Shooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir667 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brave Bull Shooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    ir668 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black Forest Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir669 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir670 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir671 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir672 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir673 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bailey\'s Dream Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir674 = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bailey\'s Dream Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla ice-cream').first().id
        )
    ir675 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir676 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir677 = RecipeIngredient(
            amount=1.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    ir678 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir679 = RecipeIngredient(
            amount=0.5,
            unit='lb',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir680 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    ir681 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    ir682 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir683 = RecipeIngredient(
            amount=0,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    ir684 = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla Ice-Cream').first().id
        )
    ir685 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir686 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Godiva liqueur').first().id
        )
    ir687 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped Cream').first().id
        )
    ir688 = RecipeIngredient(
            amount=4,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'caramel sauce').first().id
        )
    ir689 = RecipeIngredient(
            amount=4,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'chocolate sauce').first().id
        )
    ir690 = RecipeIngredient(
            amount=15,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mini-snickers bars').first().id
        )
    ir691 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cantaloupe Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cantaloupe').first().id
        )
    ir692 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cantaloupe Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    ir693 = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandon and Will\'s Coke Float').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla ice-cream').first().id
        )
    ir694 = RecipeIngredient(
            amount=1,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandon and Will\'s Coke Float').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    ir695 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandon and Will\'s Coke Float').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir696 = RecipeIngredient(
            amount=0.5,
            unit='lb',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir697 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    ir698 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    ir699 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir700 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    ir701 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir702 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir703 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir706 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir707 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir708 = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cachaca').first().id
        )
    ir709 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cream Soda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Spiced rum').first().id
        )
    ir710 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir711 = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir712 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    ir713 = RecipeIngredient(
            amount=1.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Rum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir714 = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Rum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    ir715 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Rum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir716 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libre').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir717 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libre').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir718 = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir719 = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Falernum').first().id
        )
    ir720 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir721 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Añejo rum').first().id
        )
    ir722 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'blackstrap rum').first().id
        )
    ir723 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Citrus Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bacardi Limon').first().id
        )
    ir724 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Citrus Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    ir725 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir726 = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir727 = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir728 = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    ir729 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir730 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir731 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir732 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ir733 = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir734 = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir735 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White rum').first().id
        )
    ir736 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir737 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'City Slicker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir738 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'City Slicker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir739 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'City Slicker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir740 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Campari Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    ir741 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Campari Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ir742 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir743 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Port').first().id
        )
    ir744 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir745 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir746 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ir747 = RecipeIngredient(
            amount=1.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir748 = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir749 = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    ir750 = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir751 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir752 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir753 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir754 = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla').first().id
        )
    ir755 = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir756 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir757 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir758 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    ir759 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir760 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg yolk').first().id
        )
    ir761 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir762 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    ir763 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lillet Blanc').first().id
        )
    ir764 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir765 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absinthe').first().id
        )
    ir766 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate liqueur').first().id
        )
    ir767 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir768 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir769 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clove Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir770 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clove Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    ir771 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clove Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    ir772 = RecipeIngredient(
            amount=10,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir773 = RecipeIngredient(
            amount=4,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    ir774 = RecipeIngredient(
            amount=2.5,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir775 = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir776 = RecipeIngredient(
            amount=2.5,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir777 = RecipeIngredient(
            amount=1,
            unit='dl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coke and Drops').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    ir778 = RecipeIngredient(
            amount=7,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coke and Drops').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir779 = RecipeIngredient(
            amount=125,
            unit='gr',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    ir780 = RecipeIngredient(
            amount=0.75,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir781 = RecipeIngredient(
            amount=4,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir782 = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir783 = RecipeIngredient(
            amount=4,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir784 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Almond flavoring').first().id
        )
    ir785 = RecipeIngredient(
            amount=2,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ir786 = RecipeIngredient(
            amount=8,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir787 = RecipeIngredient(
            amount=6,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir788 = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grain alcohol').first().id
        )
    ir789 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peppermint extract').first().id
        )
    ir790 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    ir791 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana liqueur').first().id
        )
    ir792 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    ir793 = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate ice-cream').first().id
        )
    ir794 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate syrup').first().id
        )
    ir795 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate milk').first().id
        )
    ir796 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped cream').first().id
        )
    ir797 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir798 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    ir799 = RecipeIngredient(
            amount=0.5,
            unit='kg',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Cordial').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberries').first().id
        )
    ir800 = RecipeIngredient(
            amount=0.75,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Cordial').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir801 = RecipeIngredient(
            amount=0.5,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Cordial').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir802 = RecipeIngredient(
            amount=6,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir803 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    ir804 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ir805 = RecipeIngredient(
            amount=3,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    ir806 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir807 = RecipeIngredient(
            amount=1,
            unit='piece',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir808 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir809 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir810 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    ir811 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    ir812 = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir813 = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir814 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir815 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir816 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Root Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir817 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Root Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    ir818 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Root Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    ir819 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir820 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir821 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg White').first().id
        )
    ir822 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir823 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir824 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    ir825 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    ir826 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir827 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir828 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir829 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Boilermaker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Corona').first().id
        )
    ir830 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Boilermaker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir831 = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir832 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir833 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir834 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir835 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir836 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir837 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir838 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir839 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate ice-cream').first().id
        )
    ir840 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cocktail Horse\'s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    ir841 = RecipeIngredient(
            amount=100,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cocktail Horse\'s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger Beer').first().id
        )
    ir842 = RecipeIngredient(
            amount=3,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cocktail Horse\'s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir843 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cocktail Horse\'s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Peel').first().id
        )
    ir844 = RecipeIngredient(
            amount=3,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Orange Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir845 = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Orange Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir846 = RecipeIngredient(
            amount=1.33,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Orange Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir847 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Castillian Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cocoa powder').first().id
        )
    ir848 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Castillian Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir849 = RecipeIngredient(
            amount=7,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Castillian Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cornstarch').first().id
        )
    ir850 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Castillian Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir851 = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Castillian Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir852 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir853 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir854 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir855 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White rum').first().id
        )
    ir856 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    ir857 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry Grenadine').first().id
        )
    ir858 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ir859 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    ir860 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Derby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'gin').first().id
        )
    ir861 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Derby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach Bitters').first().id
        )
    ir862 = RecipeIngredient(
            amount=2,
            unit='sprigs',
            recipe_id=Recipe.query.filter(Recipe.name == 'Derby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir863 = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Diesel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    ir864 = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Diesel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    ir865 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Diesel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackcurrant cordial').first().id
        )
    ir866 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir867 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir868 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir869 = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Danbooka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir870 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Danbooka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Everclear').first().id
        )
    ir871 = RecipeIngredient(
            amount=2,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Downshift').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fruit punch').first().id
        )
    ir872 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Downshift').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    ir873 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Downshift').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir874 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Downshift').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    ir875 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dragonfly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir876 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dragonfly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ir877 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dragonfly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir878 = RecipeIngredient(
            amount=1.67,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir879 = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir880 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive').first().id
        )
    ir881 = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Rob Roy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir882 = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Rob Roy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir883 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Rob Roy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir884 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dirty Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir885 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dirty Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir886 = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dirty Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive Brine').first().id
        )
    ir887 = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dirty Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir888 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dirty Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive').first().id
        )
    ir889 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Darkwood Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry Heering').first().id
        )
    ir890 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Darkwood Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    ir891 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Darkwood Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir892 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Darkwood Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir893 = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dark and Stormy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    ir894 = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dark and Stormy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger Beer').first().id
        )
    ir895 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dark Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'demerara Sugar').first().id
        )
    ir896 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dark Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir897 = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dark Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cachaca').first().id
        )
    ir898 = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pisco').first().id
        )
    ir899 = RecipeIngredient(
            amount=2.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir900 = RecipeIngredient(
            amount=2.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Syrup').first().id
        )
    ir901 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'St. Germain').first().id
        )
    ir902 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir903 = RecipeIngredient(
            amount=1,
            unit='pinch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepper').first().id
        )
    ir904 = RecipeIngredient(
            amount=2,
            unit='sprigs',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lavender').first().id
        )
    ir905 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Damned if you do').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whiskey').first().id
        )
    ir906 = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Damned if you do').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot Damn').first().id
        )
    ir907 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dubonnet Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dubonnet Rouge').first().id
        )
    ir908 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dubonnet Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir909 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dubonnet Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir910 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dubonnet Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir911 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    ir912 = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir913 = RecipeIngredient(
            amount=1,
            unit='stick',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ir914 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla').first().id
        )
    ir915 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    ir916 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped cream').first().id
        )
    ir917 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Death in the Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absinthe').first().id
        )
    ir918 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Death in the Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir919 = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate syrup').first().id
        )
    ir920 = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir921 = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    ir922 = RecipeIngredient(
            amount=6,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg yolk').first().id
        )
    ir923 = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir924 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir925 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir926 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir927 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    ir928 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    ir929 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipping cream').first().id
        )
    ir930 = RecipeIngredient(
            amount=6,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    # ir931 = RecipeIngredient(
    #         amount=0.25,
    #         unit='cup',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
    #     )
    ir932 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    ir933 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir934 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir935 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir936 = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir937 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir938 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    ir939 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Rumtini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir940 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Rumtini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla syrup').first().id
        )
    ir941 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Rumtini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Espresso').first().id
        )
    ir942 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Rumtini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir943 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    ir944 = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir945 = RecipeIngredient(
            amount=13,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Condensed milk').first().id
        )
    ir946 = RecipeIngredient(
            amount=0.75,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir947 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    ir948 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir949 = RecipeIngredient(
            amount=0,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    ir950 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    ir951 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir952 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir953 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir954 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir955 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir956 = RecipeIngredient(
            amount=60,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Elderflower Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cachaca').first().id
        )
    ir957 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Elderflower Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir958 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Elderflower Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Elderflower cordial').first().id
        )
    ir959 = RecipeIngredient(
            amount=6,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    ir960 = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir961 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    ir962 = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir963 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    ir964 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Empellón Cocina\'s Fat-Washed Mezcal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mezcal').first().id
        )
    ir965 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Empellón Cocina\'s Fat-Washed Mezcal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate liqueur').first().id
        )
    ir966 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Empellón Cocina\'s Fat-Washed Mezcal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee liqueur').first().id
        )
    ir967 = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frosé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rose').first().id
        )
    ir968 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frosé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir969 = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frosé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir970 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frosé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir971 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frappé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir972 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frappé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir973 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frappé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir974 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Foxy Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir975 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Foxy Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    ir976 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Foxy Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir977 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir978 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir979 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir980 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir981 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir982 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir983 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir984 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    ir985 = RecipeIngredient(
            amount=3,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Figs').first().id
        )
    ir986 = RecipeIngredient(
            amount=1,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Thyme').first().id
        )
    ir987 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir988 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic Water').first().id
        )
    ir989 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    ir990 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    ir991 = RecipeIngredient(
            amount=0.25,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir992 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    # ir993 = RecipeIngredient(
    #         amount=1,
    #         unit='slice',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
    #     )
    # ir994 = RecipeIngredient(
    #         amount=1,
    #         unit='slice',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
    #     )
    ir995 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    ir996 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    ir997 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir998 = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fruit').first().id
        )
    ir999 = RecipeIngredient(
            amount=6,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1000 = RecipeIngredient(
            amount=1,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    ir1001 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir1002 = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1003 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1004 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple').first().id
        )
    ir1005 = RecipeIngredient(
            amount=1,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    ir1006 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Freddy Kruger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    ir1007 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Freddy Kruger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    ir1008 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Freddy Kruger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1009 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir1010 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot Nectar').first().id
        )
    ir1011 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pomegranate juice').first().id
        )
    ir1012 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    ir1013 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir1014 = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fuzzy Asshole').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir1015 = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fuzzy Asshole').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    ir1016 = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1017 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry Liqueur').first().id
        )
    ir1018 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'pineapple juice').first().id
        )
    ir1019 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1020 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lillet').first().id
        )
    ir1021 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir1022 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    ir1023 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fahrenheit 5000').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Firewater').first().id
        )
    ir1024 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fahrenheit 5000').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Peppar').first().id
        )
    ir1025 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fahrenheit 5000').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    ir1026 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Dutchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1027 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Dutchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1028 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1029 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1030 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1031 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1032 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir1033 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1034 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Flip-Flop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    ir1035 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Flip-Flop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fruit juice').first().id
        )
    ir1036 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Scotchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir1037 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Scotchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir1038 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Scotchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir1039 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Scotchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    ir1040 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Connection').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    ir1041 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Connection').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1042 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1043 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1044 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    ir1045 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dr. Pepper').first().id
        )
    ir1046 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Beer').first().id
        )
    ir1047 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Lamborghini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir1048 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Lamborghini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    ir1049 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Lamborghini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir1050 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Lamborghini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir1051 = RecipeIngredient(
            amount=0.25,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flander\'s Flake-Out').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    ir1052 = RecipeIngredient(
            amount=0.75,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flander\'s Flake-Out').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sarsaparilla').first().id
        )
    ir1053 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Mint Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1054 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Mint Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1055 = RecipeIngredient(
            amount=6,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Mint Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir1056 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Mint Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1057 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Pineapple Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1058 = RecipeIngredient(
            amount=4,
            unit='cubes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Pineapple Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    ir1059 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Pineapple Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1060 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Pineapple Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1061 = RecipeIngredient(
            amount=2.5,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'GG').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    ir1062 = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1063 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1064 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir1065 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1066 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godchild').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1067 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godchild').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1068 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godchild').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    ir1069 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1070 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1071 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1072 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1073 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1074 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1075 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir1076 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir1077 = RecipeIngredient(
            amount=5,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gagliardo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach Vodka').first().id
        )
    ir1078 = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gagliardo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1079 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gagliardo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    ir1080 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gagliardo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sirup of roses').first().id
        )
    ir1081 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godmother').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1082 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godmother').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1083 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godfather').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir1084 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godfather').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1085 = RecipeIngredient(
            amount=1,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    ir1086 = RecipeIngredient(
            amount=125,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1087 = RecipeIngredient(
            amount=60,
            unit='gr',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1088 = RecipeIngredient(
            amount=1,
            unit='stick',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ir1089 = RecipeIngredient(
            amount=3,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    ir1090 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir1091 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1092 = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic Water').first().id
        )
    ir1093 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Peel').first().id
        )
    ir1094 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1095 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1096 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1097 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1098 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir1099 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1100 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Carbonated water').first().id
        )
    ir1101 = RecipeIngredient(
            amount=1,
            unit='cube',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1102 = RecipeIngredient(
            amount=4,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir1103 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir1104 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir1105 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1106 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1107 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1108 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1109 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir1110 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir1111 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1112 = RecipeIngredient(
            amount=8,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir1113 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Peel').first().id
        )
    ir1114 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1115 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1116 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1117 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1118 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1119 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    ir1120 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Greyhound').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1121 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Greyhound').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    ir1122 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1123 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1124 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    ir1125 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir1126 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1127 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Squirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1128 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Squirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1129 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Squirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1130 = RecipeIngredient(
            amount=3,
            unit='cubes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Squirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    ir1131 = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Squirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir1132 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grand Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    ir1133 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grand Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    ir1134 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grand Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir1135 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grand Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ir1136 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1137 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1138 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1139 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1140 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir1141 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    ir1142 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grass Skirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1143 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grass Skirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1144 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grass Skirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir1145 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grass Skirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1146 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grass Skirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    ir1147 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grasshopper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Creme de Menthe').first().id
        )
    ir1148 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grasshopper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    ir1149 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grasshopper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir1150 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grim Reaper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir1151 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grim Reaper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    ir1152 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grim Reaper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1153 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin and Soda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1154 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin and Soda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir1155 = RecipeIngredient(
            amount=0.25,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin and Soda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1156 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Golden dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    ir1157 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Golden dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    ir1158 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Golden dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1159 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Golden dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    ir1160 = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Green Goblin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    ir1161 = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Green Goblin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    ir1162 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Green Goblin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir1163 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grizzly Bear').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1164 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grizzly Bear').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    ir1165 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grizzly Bear').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir1166 = RecipeIngredient(
            amount=2.5,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grizzly Bear').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir1167 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin And Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1168 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin And Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic water').first().id
        )
    ir1169 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin And Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1170 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Basil Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1171 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Basil Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir1172 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Basil Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir1173 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Basil Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Basil').first().id
        )
    ir1174 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman\'s Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1175 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman\'s Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1176 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman\'s Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir1177 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman\'s Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    ir1178 = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Girl From Ipanema').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cachaca').first().id
        )
    ir1179 = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Girl From Ipanema').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir1180 = RecipeIngredient(
            amount=10,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Girl From Ipanema').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Agave Syrup').first().id
        )
    ir1181 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Girl From Ipanema').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir1182 = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Garibaldi Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1183 = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Garibaldi Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ir1184 = RecipeIngredient(
            amount=90,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Garibaldi Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1185 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Garibaldi Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    ir1186 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir1187 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1188 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1189 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir1190 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Melon liqueur').first().id
        )
    ir1191 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mountain Dew').first().id
        )
    ir1192 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grape lemon pineapple Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapes').first().id
        )
    ir1193 = RecipeIngredient(
            amount=0.25,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grape lemon pineapple Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1194 = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grape lemon pineapple Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    ir1195 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'H.D.').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whisky').first().id
        )
    ir1196 = RecipeIngredient(
            amount=8,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'H.D.').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir1197 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Honey Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Rum').first().id
        )
    ir1198 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Honey Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    ir1199 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Honey Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir1200 = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whiskey').first().id
        )
    ir1201 = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    ir1202 = RecipeIngredient(
            amount=1,
            unit='stick',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ir1203 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    ir1204 = RecipeIngredient(
            amount=2,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    ir1205 = RecipeIngredient(
            amount=5,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Herbal flame').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot Damn').first().id
        )
    ir1206 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Herbal flame').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    ir1207 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse\'s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir1208 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse\'s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1209 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse\'s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ir1210 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse\'s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir1211 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Happy Skipper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Spiced rum').first().id
        )
    ir1212 = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter\'s Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vermouth').first().id
        )
    ir1213 = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter\'s Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Cherry').first().id
        )
    ir1214 = RecipeIngredient(
            amount=10,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter\'s Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir1215 = RecipeIngredient(
            amount=100,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter\'s Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ir1216 = RecipeIngredient(
            amount=2,
            unit='units',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter\'s Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberries').first().id
        )
    ir1217 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry Juice').first().id
        )
    ir1218 = RecipeIngredient(
            amount=3,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    ir1219 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red Chili Flakes').first().id
        )
    ir1220 = RecipeIngredient(
            amount=10,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    ir1221 = RecipeIngredient(
            amount=6,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    ir1222 = RecipeIngredient(
            amount=20,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1223 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Havana Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1224 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Havana Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir1225 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Havana Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1227 = RecipeIngredient(
            amount=2.5,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1228 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Corn syrup').first().id
        )
    ir1229 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir1230 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    ir1231 = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1232 = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1233 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Creamy Bush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish whiskey').first().id
        )
    ir1234 = RecipeIngredient(
            amount=0.75,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Creamy Bush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir1235 = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Creamy Bush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir1236 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Harvey Wallbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1237 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Harvey Wallbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    ir1238 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Harvey Wallbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1239 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hawaiian Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1240 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hawaiian Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1241 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hawaiian Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir1242 = RecipeIngredient(
            amount=12,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hemingway Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir1243 = RecipeIngredient(
            amount=8,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hemingway Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    ir1244 = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hemingway Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Liqueur').first().id
        )
    ir1245 = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hemingway Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1246 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Highland Fling Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir1247 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Highland Fling Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir1248 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Highland Fling Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir1249 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Highland Fling Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive').first().id
        )
    ir1250 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    ir1251 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butter').first().id
        )
    ir1252 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    ir1253 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Half-and-half').first().id
        )
    ir1254 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Marshmallows').first().id
        )
    ir1255 = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1256 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brown sugar').first().id
        )
    ir1257 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit juice').first().id
        )
    ir1258 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ir1259 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1260 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ice Pick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1261 = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ice Pick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Iced tea').first().id
        )
    ir1262 = RecipeIngredient(
            amount=1,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ice Pick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1263 = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir1264 = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1265 = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1266 = RecipeIngredient(
            amount=4,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir1267 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir1268 = RecipeIngredient(
            amount=1.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Half-and-half').first().id
        )
    ir1269 = RecipeIngredient(
            amount=1,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Condensed milk').first().id
        )
    ir1270 = RecipeIngredient(
            amount=3,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut syrup').first().id
        )
    ir1271 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate syrup').first().id
        )
    ir1272 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish whiskey').first().id
        )
    ir1273 = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir1274 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1275 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped cream').first().id
        )
    ir1276 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish whiskey').first().id
        )
    ir1277 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach brandy').first().id
        )
    ir1278 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1279 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ir1280 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir1281 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir1282 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1283 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    ir1284 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1285 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1286 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1287 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir1288 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    ir1289 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guinness stout').first().id
        )
    ir1290 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1291 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1292 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Aperol').first().id
        )
    ir1293 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee Fillip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir1294 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee Fillip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir1295 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir1296 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir1297 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1298 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1299 = RecipeIngredient(
            amount=0.67,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jam Donut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir1300 = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jam Donut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    ir1301 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jam Donut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    ir1302 = RecipeIngredient(
            amount=2,
            unit='pinches',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jam Donut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1303 = RecipeIngredient(
            amount=2,
            unit='jiggers',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1304 = RecipeIngredient(
            amount=1,
            unit='jigger',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1305 = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1306 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1307 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1308 = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    ir1309 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    ir1310 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jackhammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jack Daniels').first().id
        )
    ir1311 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jackhammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1312 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jelly Bean').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberry brandy').first().id
        )
    ir1313 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jelly Bean').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anis').first().id
        )
    ir1314 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jello shots').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1315 = RecipeIngredient(
            amount=3,
            unit='packages',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jello shots').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jello').first().id
        )
    ir1316 = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jello shots').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1317 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaica Kiss').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee liqueur').first().id
        )
    ir1318 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaica Kiss').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1319 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaica Kiss').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1320 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir1321 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1322 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1323 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    ir1324 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir1325 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir1326 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    ir1327 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1328 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1329 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Port').first().id
        )
    ir1330 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ir1331 = RecipeIngredient(
            amount=0.167,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaican Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir1332 = RecipeIngredient(
            amount=0.167,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaican Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir1333 = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaican Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1334 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Just a Moonmint').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir1335 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jewel Of The Nile').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1336 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jewel Of The Nile').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    ir1337 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jewel Of The Nile').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yellow Chartreuse').first().id
        )
    ir1338 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple brandy').first().id
        )
    ir1339 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1340 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1341 = RecipeIngredient(
            amount=4,
            unit='cubes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack\'s Vanilla Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1342 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack\'s Vanilla Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tennessee whiskey').first().id
        )
    ir1343 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack\'s Vanilla Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    ir1344 = RecipeIngredient(
            amount=10,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack\'s Vanilla Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    ir1345 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kir').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    ir1346 = RecipeIngredient(
            amount=5,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kir').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir1347 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Karsk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir1348 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Karsk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grain alcohol').first().id
        )
    ir1349 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kamikaze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1350 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kamikaze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1351 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kamikaze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1352 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kir Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    ir1353 = RecipeIngredient(
            amount=5,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kir Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir1354 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kiwi liqueur').first().id
        )
    ir1355 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitter lemon').first().id
        )
    ir1356 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1357 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kurant Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Kurant').first().id
        )
    ir1358 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kurant Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    ir1359 = RecipeIngredient(
            amount=1,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kurant Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1360 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kioki Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir1361 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kioki Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1362 = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kiwi').first().id
        )
    ir1363 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir1364 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    # ir1365 = RecipeIngredient(
    #         amount=1,
    #         unit='top off',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Martini').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kiwi').first().id
    #     )
    ir1366 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiss me Quick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry vodka').first().id
        )
    ir1367 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiss me Quick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apfelkorn').first().id
        )
    ir1368 = RecipeIngredient(
            amount=7,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiss me Quick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Schweppes Russchian').first().id
        )
    ir1369 = RecipeIngredient(
            amount=8,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiss me Quick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    ir1370 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiss me Quick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1371 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1372 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1373 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    ir1374 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1375 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool First Aid').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    ir1376 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool First Aid').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kool-Aid').first().id
        )
    ir1377 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky B And B').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir1378 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky B And B').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    ir1379 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky Colonel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir1380 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky Colonel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    ir1381 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky Colonel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir1382 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kool-Aid').first().id
        )
    ir1383 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1384 = RecipeIngredient(
            amount=3,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Papaya Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kiwi').first().id
        )
    ir1385 = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Papaya Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Papaya').first().id
        )
    ir1386 = RecipeIngredient(
            amount=1,
            unit='inch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kill the cold Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    ir1387 = RecipeIngredient(
            amount=0.25,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kill the cold Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1388 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kill the cold Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1389 = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Limeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1390 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Limeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1391 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Limeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    ir1392 = RecipeIngredient(
            amount=0.75,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lunch Box').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Beer').first().id
        )
    ir1393 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lunch Box').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1394 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lunch Box').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1395 = RecipeIngredient(
            amount=1.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Drop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1396 = RecipeIngredient(
            amount=1.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Drop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    ir1397 = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Drop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1398 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    ir1399 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    ir1400 = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1401 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1402 = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1403 = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1404 = RecipeIngredient(
            amount=4,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura bitters').first().id
        )
    ir1405 = RecipeIngredient(
            amount=1,
            unit='dl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic water').first().id
        )
    ir1406 = RecipeIngredient(
            amount=4,
            unit='cubes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1407 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Khara').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    ir1408 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Khara').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1409 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Khara').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    ir1410 = RecipeIngredient(
            amount=1,
            unit='pinch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Khara').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Asafoetida').first().id
        )
    ir1411 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Raita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    ir1412 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Raita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1413 = RecipeIngredient(
            amount=2,
            unit='pieces',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemouroudji').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    ir1414 = RecipeIngredient(
            amount=1,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemouroudji').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1415 = RecipeIngredient(
            amount=1,
            unit='lb',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemouroudji').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1416 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemouroudji').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1417 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemouroudji').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cayenne pepper').first().id
        )
    ir1418 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir1419 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Drambuie').first().id
        )
    ir1420 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir1421 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir1422 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'London Town').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1423 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'London Town').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    ir1424 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'London Town').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir1425 = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Mango').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mango').first().id
        )
    ir1426 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Mango').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    ir1427 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Mango').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1428 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Mango').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1429 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    ir1430 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1431 = RecipeIngredient(
            amount=4,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1432 = RecipeIngredient(
            amount=1,
            unit='pinch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    ir1433 = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1434 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Limona Corona').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Corona').first().id
        )
    ir1435 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Limona Corona').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bacardi Limon').first().id
        )
    ir1436 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lord And Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir1437 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lord And Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tia maria').first().id
        )
    ir1438 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lady Love Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1439 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lady Love Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir1440 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lady Love Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1441 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lady Love Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1442 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lady Love Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ir1443 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1444 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1445 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1446 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir1447 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1448 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    ir1449 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lone Tree Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir1450 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lone Tree Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1451 = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lazy Coconut Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut Liqueur').first().id
        )
    ir1452 = RecipeIngredient(
            amount=75,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lazy Coconut Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    ir1453 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lazy Coconut Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir1454 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1455 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir1456 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1457 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1458 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    ir1459 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir1460 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Elderflower Spritzer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Elderflower cordial').first().id
        )
    ir1461 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Elderflower Spritzer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1462 = RecipeIngredient(
            amount=0.33,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Elderflower Spritzer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir1463 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Elderflower Spritzer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lemon Juice').first().id
        )
    ir1464 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    ir1465 = RecipeIngredient(
            amount=1.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1466 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cumin seed').first().id
        )
    ir1467 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    ir1468 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir1470 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1471 = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1472 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1473 = RecipeIngredient(
            amount=2,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir1474 = RecipeIngredient(
            amount=1,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mimosa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir1475 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mimosa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1476 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1477 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orgeat syrup').first().id
        )
    ir1478 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1479 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ir1480 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir1481 = RecipeIngredient(
            amount=1.67,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1482 = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir1483 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive').first().id
        )
    ir1484 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Beer').first().id
        )
    ir1485 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato Juice').first().id
        )
    ir1486 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1487 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot Sauce').first().id
        )
    ir1488 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Worcestershire Sauce').first().id
        )
    ir1489 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soy Sauce').first().id
        )
    ir1490 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir1491 = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir1492 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura bitters').first().id
        )
    ir1493 = RecipeIngredient(
            amount=2,
            unit='cubes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1494 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir1495 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    ir1496 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir1497 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1498 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1499 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mauresque').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ricard').first().id
        )
    ir1500 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mauresque').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orgeat Syrup').first().id
        )
    ir1501 = RecipeIngredient(
            amount=1,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mauresque').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1502 = RecipeIngredient(
            amount=4,
            unit='sprigs',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mint Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir1503 = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mint Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir1504 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mint Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1505 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mint Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1506 = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mudslinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    ir1507 = RecipeIngredient(
            amount=1,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mudslinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1508 = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mudslinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepsi Cola').first().id
        )
    ir1509 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez 2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1510 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez 2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir1511 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez 2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Liqueur').first().id
        )
    ir1512 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez 2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir1513 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moranguito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absinthe').first().id
        )
    ir1514 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moranguito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir1515 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moranguito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1516 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Miami Vice').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    ir1517 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Miami Vice').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pina colada mix').first().id
        )
    ir1518 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Miami Vice').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Daiquiri mix').first().id
        )
    ir1519 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moscow Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1520 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moscow Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1521 = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moscow Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ir1522 = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1523 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1524 = RecipeIngredient(
            amount=12,
            unit='units',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    ir1525 = RecipeIngredient(
            amount=2,
            unit='sticks',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ir1526 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir1527 = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    ir1528 = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1529 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1530 = RecipeIngredient(
            amount=3,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    ir1531 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    ir1532 = RecipeIngredient(
            amount=3,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cardamom').first().id
        )
    ir1533 = RecipeIngredient(
            amount=3,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    ir1534 = RecipeIngredient(
            amount=1,
            unit='piece',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ir1535 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Black pepper').first().id
        )
    ir1536 = RecipeIngredient(
            amount=0,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1537 = RecipeIngredient(
            amount=1,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir1538 = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1539 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1540 = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger Beer').first().id
        )
    ir1541 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cucumber').first().id
        )
    ir1542 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    ir1543 = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mocha-Berry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir1544 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mocha-Berry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    ir1545 = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mocha-Berry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cocoa powder').first().id
        )
    ir1546 = RecipeIngredient(
            amount=3,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1547 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mango').first().id
        )
    ir1548 = RecipeIngredient(
            amount=1,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir1549 = RecipeIngredient(
            amount=200,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Rum').first().id
        )
    ir1550 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1551 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    # ir1552 = RecipeIngredient(
    #         amount=1,
    #         unit='garnish',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mango').first().id
    #     )
    ir1553 = RecipeIngredient(
            amount=0.5,
            unit='handful',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir1554 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1555 = RecipeIngredient(
            amount=0.125,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir1556 = RecipeIngredient(
            amount=0.125,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    ir1557 = RecipeIngredient(
            amount=8,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura bitters').first().id
        )
    ir1558 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Gland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1559 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Gland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    ir1560 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Gland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1561 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Gland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1562 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Mint').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir1563 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Mint').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    ir1564 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Mint').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    ir1565 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1566 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir1567 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    ir1568 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1569 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir1570 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Wrench').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1571 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Wrench').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    ir1572 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Wrench').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir1573 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mother\'s Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    ir1574 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mother\'s Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butterscotch schnapps').first().id
        )
    ir1575 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mother\'s Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir1576 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Manx').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir1577 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Manx').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir1578 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Manx').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    ir1579 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Manx').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    ir1580 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Manx').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir1581 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Malibu Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    ir1582 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Malibu Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tropicana').first().id
        )
    ir1583 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Malibu Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir1584 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Cowboy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir1585 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Cowboy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir1586 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Cowboy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    ir1587 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1588 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir1589 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir1590 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberries').first().id
        )
    ir1591 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir1592 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir1593 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1594 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir1595 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1596 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir1597 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir1598 = RecipeIngredient(
            amount=5,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1599 = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cocoa powder').first().id
        )
    ir1600 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    ir1601 = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1602 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir1603 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    ir1604 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Orange Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mango').first().id
        )
    ir1605 = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Orange Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir1606 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1607 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1608 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir1609 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1610 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1611 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1612 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ir1613 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir1614 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    ir1615 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1616 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1617 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    ir1618 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nutty Irishman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir1619 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nutty Irishman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Frangelico').first().id
        )
    ir1620 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nutty Irishman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir1621 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir1622 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1623 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1624 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir1625 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    ir1626 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    ir1627 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    ir1628 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    ir1629 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1630 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    ir1631 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nuked Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cocoa powder').first().id
        )
    ir1632 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nuked Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1633 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nuked Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    ir1634 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nuked Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir1635 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    ir1636 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1637 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1638 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1639 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir1640 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Pal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rye whiskey').first().id
        )
    ir1641 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Pal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ir1642 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Pal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir1643 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Cuban').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Rum').first().id
        )
    ir1644 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Cuban').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir1645 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Cuban').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1646 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Cuban').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir1647 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Cuban').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    ir1648 = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orangeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1649 = RecipeIngredient(
            amount=15,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orangeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1650 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orangeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    ir1651 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Whip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1652 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Whip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir1653 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Whip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1654 = RecipeIngredient(
            amount=1,
            unit='package',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Whip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    ir1655 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Whip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1656 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Crush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1657 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Crush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1658 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Crush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1659 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Oasis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    ir1660 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Oasis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1661 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Oasis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1662 = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir1663 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura bitters').first().id
        )
    ir1664 = RecipeIngredient(
            amount=1,
            unit='cube',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1665 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1666 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oreo Mudslide').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1667 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oreo Mudslide').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir1668 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oreo Mudslide').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir1669 = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oreo Mudslide').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla ice-cream').first().id
        )
    ir1670 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oreo Mudslide').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Oreo cookie').first().id
        )
    ir1671 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oatmeal Cookie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir1672 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oatmeal Cookie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir1673 = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oatmeal Cookie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butterscotch schnapps').first().id
        )
    ir1674 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oatmeal Cookie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jagermeister').first().id
        )
    ir1675 = RecipeIngredient(
            amount=0.5,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oatmeal Cookie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    ir1676 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Push-up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Spiced rum').first().id
        )
    ir1677 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Push-up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1678 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Push-up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1679 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Push-up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    ir1680 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1681 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1682 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir1683 = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosemary Syrup').first().id
        )
    ir1684 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir1685 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosemary').first().id
        )
    ir1686 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    ir1687 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir1688 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    ir1689 = RecipeIngredient(
            amount=3,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    ir1690 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Espresso').first().id
        )
    ir1691 = RecipeIngredient(
            amount=0.125,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    ir1692 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen\'s Grandmother\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whiskey').first().id
        )
    ir1693 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen\'s Grandmother\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Beer').first().id
        )
    ir1694 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen\'s Grandmother\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ir1695 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen\'s Grandmother\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1696 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grape Soda').first().id
        )
    ir1697 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir1698 = RecipeIngredient(
            amount=7,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Paradise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1699 = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Paradise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot Brandy').first().id
        )
    ir1700 = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Paradise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1701 = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Gin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir1702 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Gin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1703 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1704 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Curacao').first().id
        )
    ir1705 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1706 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir1707 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Bitters').first().id
        )
    ir1708 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1709 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1710 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir1711 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ir1712 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1713 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut Liqueur').first().id
        )
    ir1714 = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Elderflower cordial').first().id
        )
    ir1715 = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1716 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberries').first().id
        )
    ir1717 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended Scotch').first().id
        )
    ir1718 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir1719 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey syrup').first().id
        )
    ir1720 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger Syrup').first().id
        )
    ir1721 = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Islay single malt Scotch').first().id
        )
    ir1722 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pisco').first().id
        )
    ir1723 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1724 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1725 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1726 = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Porto flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1727 = RecipeIngredient(
            amount=9,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Porto flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Port').first().id
        )
    ir1728 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Porto flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg Yolk').first().id
        )
    ir1729 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pina Colada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1730 = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pina Colada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut milk').first().id
        )
    ir1731 = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pina Colada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    ir1732 = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Penocha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Everclear').first().id
        )
    ir1733 = RecipeIngredient(
            amount=1750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Penocha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1734 = RecipeIngredient(
            amount=1750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Penocha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    ir1735 = RecipeIngredient(
            amount=1,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Penocha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1736 = RecipeIngredient(
            amount=1,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Penocha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir1737 = RecipeIngredient(
            amount=40,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir1738 = RecipeIngredient(
            amount=20,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passoa').first().id
        )
    ir1739 = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1740 = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit syrup').first().id
        )
    ir1741 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach Bitters').first().id
        )
    ir1742 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir1743 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Popped cherry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1744 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Popped cherry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry liqueur').first().id
        )
    ir1745 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Popped cherry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir1746 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Popped cherry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1747 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Poppy Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1748 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Poppy Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    ir1749 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Port').first().id
        )
    ir1750 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir1751 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1752 = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    ir1753 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir1754 = RecipeIngredient(
            amount=0.5,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orgeat syrup').first().id
        )
    ir1755 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1756 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir1757 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir1758 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    ir1759 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lime Juice').first().id
        )
    ir1760 = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    ir1761 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1762 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepper').first().id
        )
    ir1763 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pornstar Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1764 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pornstar Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passoa').first().id
        )
    ir1765 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pornstar Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit juice').first().id
        )
    ir1766 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pornstar Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1767 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pornstar Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    ir1768 = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    # ir1769 = RecipeIngredient(
    #         amount=3,
    #         unit='cl',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
    #     )
    ir1770 = RecipeIngredient(
            amount=3.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    ir1771 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1772 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir1773 = RecipeIngredient(
            amount=4,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir1774 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port And Starboard').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1775 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port And Starboard').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Creme de Menthe').first().id
        )
    ir1776 = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Port').first().id
        )
    ir1777 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1778 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pysch Vitamin Light').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1779 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pysch Vitamin Light').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    ir1780 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pysch Vitamin Light').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir1781 = RecipeIngredient(
            amount=1,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Panty Pulldowns').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    ir1782 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Panty Pulldowns').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pink lemonade').first().id
        )
    ir1783 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Panty Pulldowns').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1784 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Passion Fruit Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1785 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Passion Fruit Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir1786 = RecipeIngredient(
            amount=1,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Passion Fruit Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit juice').first().id
        )
    ir1787 = RecipeIngredient(
            amount=0.25,
            unit='inch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Gingerale Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    ir1788 = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Gingerale Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    ir1789 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quentin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir1790 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quentin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir1791 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quentin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir1792 = RecipeIngredient(
            amount=0.125,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quentin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    ir1793 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee brandy').first().id
        )
    ir1794 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime vodka').first().id
        )
    ir1795 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    ir1796 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quick F**K').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir1797 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quick F**K').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    ir1798 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quick F**K').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir1799 = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quick-sand').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Black Sambuca').first().id
        )
    ir1800 = RecipeIngredient(
            amount=250,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quick-sand').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1801 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Charlotte').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    ir1802 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Charlotte').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1803 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Elizabeth').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir1804 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Elizabeth').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1805 = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Elizabeth').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    ir1806 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker\'s Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1807 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker\'s Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1808 = RecipeIngredient(
            amount=0.25,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker\'s Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1809 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker\'s Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry syrup').first().id
        )
    ir1810 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quarter Deck Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1811 = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quarter Deck Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    ir1812 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quarter Deck Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1813 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir1814 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1815 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    ir1816 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1817 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1818 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Beer').first().id
        )
    ir1819 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '7-Up').first().id
        )
    ir1820 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1821 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1822 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1823 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir1824 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir1825 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir1826 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ir1827 = RecipeIngredient(
            amount=355,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fruit punch').first().id
        )
    ir1828 = RecipeIngredient(
            amount=355,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1829 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1830 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir1831 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1832 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir1833 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1834 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1835 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ir1836 = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    ir1837 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir1838 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    ir1839 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1840 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    ir1841 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberry brandy').first().id
        )
    ir1842 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1843 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir1844 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir1845 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rusty Nail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir1846 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rusty Nail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Drambuie').first().id
        )
    ir1847 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rusty Nail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir1848 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Red Snapper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Crown Royal').first().id
        )
    ir1849 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Red Snapper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1850 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Red Snapper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir1851 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Bitch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Frangelico').first().id
        )
    ir1852 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Bitch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Crown Royal').first().id
        )
    ir1853 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Flush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Crown Royal').first().id
        )
    ir1854 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Flush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    ir1855 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Flush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    ir1856 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Flush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir1857 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1858 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    ir1859 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1860 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir1861 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir1862 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir1863 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ruby Tuesday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1864 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ruby Tuesday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir1865 = RecipeIngredient(
            amount=2,
            unit='splashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ruby Tuesday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir1866 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rail Splitter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    ir1867 = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rosemary Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1868 = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rosemary Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir1869 = RecipeIngredient(
            amount=100,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rosemary Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic Water').first().id
        )
    ir1870 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rosemary Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosemary').first().id
        )
    ir1871 = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1872 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir1873 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir1874 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    ir1875 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg White').first().id
        )
    ir1876 = RecipeIngredient(
            amount=2,
            unit='drop',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    ir1877 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir1878 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1879 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1880 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1881 = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    ir1882 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Milk Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1883 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Milk Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir1884 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Milk Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1885 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir1886 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry syrup').first().id
        )
    ir1887 = RecipeIngredient(
            amount=8,
            unit='sprigs',
            recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir1888 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Screwdriver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1889 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Screwdriver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1890 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry vodka').first().id
        )
    ir1891 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    ir1892 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir1893 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    ir1894 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1895 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir1896 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1897 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime peel').first().id
        )
    ir1898 = RecipeIngredient(
            amount=2.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Russian Spring Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1899 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Russian Spring Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    ir1900 = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Russian Spring Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir1901 = RecipeIngredient(
            amount=2.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Russian Spring Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir1902 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir1903 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1904 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir1905 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1906 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir1907 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    ir1908 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    ir1909 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    ir1910 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    ir1911 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    ir1912 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepsi Cola').first().id
        )
    ir1913 = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1914 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    ir1915 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ir1916 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir1917 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1918 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir1919 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir1920 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    ir1921 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1922 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1923 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1924 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Stinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1925 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Stinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    ir1926 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ricard').first().id
        )
    ir1927 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1928 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peychaud bitters').first().id
        )
    ir1929 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1930 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ir1931 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir1932 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    ir1933 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    ir1934 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir1935 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1936 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaro Montenegro').first().id
        )
    ir1937 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ruby Port').first().id
        )
    ir1938 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blood Orange').first().id
        )
    ir1939 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir1940 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    ir1941 = RecipeIngredient(
            amount=60,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1942 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Allspice').first().id
        )
    ir1943 = RecipeIngredient(
            amount=20,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir1944 = RecipeIngredient(
            amount=90,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir1945 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir1946 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange spiral').first().id
        )
    ir1947 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Advocaat').first().id
        )
    ir1948 = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ir1949 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1950 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir1951 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shot-gun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jim Beam').first().id
        )
    ir1952 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shot-gun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jack Daniels').first().id
        )
    ir1953 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shot-gun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wild Turkey').first().id
        )
    ir1954 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salty Dog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    ir1955 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salty Dog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir1956 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salty Dog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    ir1957 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    ir1958 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir1959 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ir1960 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sea breeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1961 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sea breeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ir1962 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sea breeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    ir1963 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir1964 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1965 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1966 = RecipeIngredient(
            amount=0.5,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir1967 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir1968 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Tooth').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Godiva liqueur').first().id
        )
    ir1969 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Screwdriver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1970 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    ir1971 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ir1972 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1973 = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    ir1974 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sol Y Sombra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1975 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sol Y Sombra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anisette').first().id
        )
    ir1976 = RecipeIngredient(
            amount=1,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shark Attack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ir1977 = RecipeIngredient(
            amount=3,
            unit='cans',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shark Attack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1978 = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shark Attack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1979 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'San Francisco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir1980 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'San Francisco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Banane').first().id
        )
    ir1981 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Space Odyssey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    ir1982 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Space Odyssey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    ir1983 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Space Odyssey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir1984 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Eggnog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    ir1985 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Eggnog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir1986 = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Eggnog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    ir1987 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Bananas').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir1988 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Bananas').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    ir1989 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Bananas').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    ir1990 = RecipeIngredient(
            amount=2,
            unit='bottles',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    ir1991 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir1992 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir1993 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple').first().id
        )
    ir1994 = RecipeIngredient(
            amount=0,
            unit='wedges',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir1995 = RecipeIngredient(
            amount=0,
            unit='wedges',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir1996 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir1997 = RecipeIngredient(
            amount=4,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir1998 = RecipeIngredient(
            amount=4,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Curacao').first().id
        )
    ir1999 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir2000 = RecipeIngredient(
            amount=1,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir2001 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Swedish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir2002 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Swedish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Aquavit').first().id
        )
    ir2003 = RecipeIngredient(
            amount=1,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Swedish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir2004 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Singapore Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    ir2005 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Singapore Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir2006 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Singapore Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2007 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Singapore Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ir2008 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Slippery Nipple').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    ir2009 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Slippery Nipple').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish cream').first().id
        )
    ir2010 = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snake Bite (UK)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    ir2011 = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snake Bite (UK)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    ir2012 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Screaming Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2013 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Screaming Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir2014 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Screaming Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir2015 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sex on the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2016 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sex on the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    ir2017 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir2018 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir2019 = RecipeIngredient(
            amount=0.25,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir2020 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz Veneziano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    ir2021 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz Veneziano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Aperol').first().id
        )
    ir2022 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz Veneziano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir2023 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sloe Gin Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    ir2024 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sloe Gin Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir2025 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sloe Gin Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir2026 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spanish chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    ir2027 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spanish chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    ir2028 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spanish chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ir2029 = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spanish chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg yolk').first().id
        )
    ir2030 = RecipeIngredient(
            amount=1.5,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    ir2031 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir2032 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir2033 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir2034 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple').first().id
        )
    ir2035 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir2036 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shanghai Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir2037 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shanghai Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anisette').first().id
        )
    ir2038 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shanghai Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir2039 = RecipeIngredient(
            amount=0.25,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shanghai Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir2040 = RecipeIngredient(
            amount=46,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach nectar').first().id
        )
    ir2041 = RecipeIngredient(
            amount=20,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir2042 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brown sugar').first().id
        )
    ir2043 = RecipeIngredient(
            amount=9,
            unit='inch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ir2044 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    ir2045 = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2046 = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Shivers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir2047 = RecipeIngredient(
            amount=4,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Shivers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    ir2048 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Shivers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir2049 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberry schnapps').first().id
        )
    ir2050 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir2051 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2052 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir2053 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir2054 = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir2055 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir2056 = RecipeIngredient(
            amount=8,
            unit='units',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir2057 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir2058 = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snakebite and Black').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    ir2059 = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snakebite and Black').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    ir2060 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snakebite and Black').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackcurrant squash').first().id
        )
    ir2061 = RecipeIngredient(
            amount=46,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir2062 = RecipeIngredient(
            amount=28,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    ir2063 = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir2064 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir2065 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Berries').first().id
        )
    ir2066 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ir2067 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Surf City Lifesaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ouzo').first().id
        )
    ir2068 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Surf City Lifesaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir2069 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Surf City Lifesaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2070 = RecipeIngredient(
            amount=0.5,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Surf City Lifesaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    ir2071 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberry schnapps').first().id
        )
    ir2072 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir2073 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir2074 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir2075 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir2076 = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2077 = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate liqueur').first().id
        )
    ir2078 = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir2079 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate Sauce').first().id
        )
    ir2080 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salted Chocolate').first().id
        )
    ir2081 = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Johnnie Walker').first().id
        )
    ir2082 = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    ir2083 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angelica root').first().id
        )
    ir2084 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fennel seeds').first().id
        )
    ir2085 = RecipeIngredient(
            amount=2,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ir2086 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Watermelon').first().id
        )
    ir2087 = RecipeIngredient(
            amount=5,
            unit='sprigs',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir2088 = RecipeIngredient(
            amount=0.33,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    ir2089 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir2090 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    # ir2091 = RecipeIngredient(
    #         amount=1,
    #         unit='top off',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Watermelon').first().id
    #     )
    # ir2092 = RecipeIngredient(
    #         amount=1,
    #         unit='top off',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
    #     )
    ir2093 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thriller').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir2094 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thriller').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    ir2095 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thriller').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir2096 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    ir2097 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ir2098 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme De Banane').first().id
        )
    ir2099 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    ir2100 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2101 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tia-Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir2102 = RecipeIngredient(
            amount=0.75,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tia-Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brown sugar').first().id
        )
    ir2103 = RecipeIngredient(
            amount=4,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tia-Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir2104 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tia-Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir2105 = RecipeIngredient(
            amount=4,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tia-Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    ir2106 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tipperary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish Whiskey').first().id
        )
    ir2107 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tipperary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir2108 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tipperary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    ir2109 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turkeyball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wild Turkey').first().id
        )
    ir2110 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turkeyball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir2111 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turkeyball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir2112 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ir2113 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish cream').first().id
        )
    ir2114 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir2115 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    ir2116 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    ir2117 = RecipeIngredient(
            amount=6,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir2118 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coriander').first().id
        )
    ir2119 = RecipeIngredient(
            amount=4,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cardamom').first().id
        )
    ir2120 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2121 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir2122 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ir2123 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    ir2124 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ir2125 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir2126 = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tomato Tang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato juice').first().id
        )
    ir2127 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tomato Tang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir2128 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tomato Tang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Celery salt').first().id
        )
    ir2129 = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Talos Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    ir2130 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Talos Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir2131 = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tennesee Mud').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir2132 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tennesee Mud').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jack Daniels').first().id
        )
    ir2133 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tennesee Mud').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir2134 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir2135 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir2136 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir2137 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ir2138 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir2139 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir2140 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    # ir2141 = RecipeIngredient(
    #         amount=0.5,
    #         unit='slice',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sour').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
    #     )
    ir2142 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir2143 = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    ir2144 = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ir2145 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Condensed milk').first().id
        )
    ir2146 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir2147 = RecipeIngredient(
            amount=1,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir2148 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Last Word').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    ir2149 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Last Word').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Liqueur').first().id
        )
    ir2150 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Last Word').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2151 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Last Word').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2152 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir2153 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2154 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anis').first().id
        )
    ir2155 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ir2156 = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    ir2157 = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2158 = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Elderflower cordial').first().id
        )
    ir2159 = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosso Vermouth').first().id
        )
    ir2160 = RecipeIngredient(
            amount=75,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic Water').first().id
        )
    ir2161 = RecipeIngredient(
            amount=2,
            unit='wedges',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir2162 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    ir2163 = RecipeIngredient(
            amount=1,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    ir2164 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir2165 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '7-up').first().id
        )
    ir2166 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir2167 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2168 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Melon Liqueur').first().id
        )
    ir2169 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Bitters').first().id
        )
    ir2170 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir2171 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    ir2172 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir2173 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2174 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    ir2175 = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anis').first().id
        )
    ir2176 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir2177 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ir2178 = RecipeIngredient(
            amount=1,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Surprise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir2179 = RecipeIngredient(
            amount=8,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Surprise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    ir2180 = RecipeIngredient(
            amount=1,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    ir2181 = RecipeIngredient(
            amount=2,
            unit='units',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    ir2182 = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Jimmy Conway').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish Whiskey').first().id
        )
    ir2183 = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Jimmy Conway').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir2184 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Jimmy Conway').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry Juice').first().id
        )
    ir2185 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Rattlesnake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yukon Jack').first().id
        )
    ir2186 = RecipeIngredient(
            amount=0.5,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Rattlesnake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    ir2187 = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Rattlesnake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    ir2188 = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Rattlesnake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ir2189 = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tommy\'s Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir2190 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tommy\'s Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2191 = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tommy\'s Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Agave syrup').first().id
        )
    ir2192 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light Rum').first().id
        )
    ir2193 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2194 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir2195 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ir2196 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir2197 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orgeat Syrup').first().id
        )
    ir2198 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    ir2199 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Evil Blue Thing').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    ir2200 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Evil Blue Thing').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    ir2201 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Evil Blue Thing').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir2202 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2203 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2204 = RecipeIngredient(
            amount=0.75,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lillet Blanc').first().id
        )
    ir2205 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victor').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2206 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victor').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir2207 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victor').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ir2208 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir2209 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato Juice').first().id
        )
    ir2210 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir2211 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2212 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    ir2213 = RecipeIngredient(
            amount=1,
            unit='pinch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    ir2214 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir2215 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ir2216 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir2217 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir2218 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ir2219 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Veteran').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ir2220 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Veteran').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    ir2221 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Van Vleet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ir2222 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Van Vleet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maple syrup').first().id
        )
    ir2223 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Van Vleet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir2224 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2225 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Half-and-half').first().id
        )
    ir2226 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Limeade').first().id
        )
    ir2227 = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2228 = RecipeIngredient(
            amount=7,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir2229 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Peel').first().id
        )
    ir2230 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir2231 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Slime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    ir2232 = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Slime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2233 = RecipeIngredient(
            amount=1.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Slime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2234 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2235 = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic Water').first().id
        )
    ir2236 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Peel').first().id
        )
    ir2237 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2238 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir2239 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive').first().id
        )
    ir2240 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2241 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vermouth Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ir2242 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vermouth Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    ir2243 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victory Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2244 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victory Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir2245 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victory Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grape juice').first().id
        )
    ir2246 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victory Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir2247 = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victory Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir2248 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka And Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2249 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Valencia Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    ir2250 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Valencia Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir2251 = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Valencia Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    ir2252 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whisky Mac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ir2253 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whisky Mac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    ir2254 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2255 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    ir2256 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    ir2257 = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    ir2258 = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir2259 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir2260 = RecipeIngredient(
            amount=3,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ir2261 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir2262 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    ir2263 = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    ir2264 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir2265 = RecipeIngredient(
            amount=1.67,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir2266 = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ir2267 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2268 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    ir2269 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosemary Syrup').first().id
        )
    ir2270 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    ir2271 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    ir2272 = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir2273 = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    ir2274 = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    # ir2275 = RecipeIngredient(
    #         amount=0.5,
    #         unit='slice',
    #         recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
    #         ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
    #     )
    ir2276 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2277 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee liqueur').first().id
        )
    ir2278 = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir2279 = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    ir2280 = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2281 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Agave Syrup').first().id
        )
    ir2282 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepper').first().id
        )
    ir2283 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ir2284 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    ir2285 = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Wine').first().id
        )
    ir2286 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    ir2287 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple').first().id
        )
    ir2288 = RecipeIngredient(
            amount=3,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple Brandy').first().id
        )
    ir2289 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ir2290 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whitecap Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir2291 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whitecap Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ir2292 = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whitecap Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream of coconut').first().id
        )
    ir2293 = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whitecap Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2294 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Waikiki Beachcomber').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ir2295 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Waikiki Beachcomber').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ir2296 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Waikiki Beachcomber').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ir2297 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yellow Bird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Rum').first().id
        )
    ir2298 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yellow Bird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    ir2299 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yellow Bird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    ir2300 = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yellow Bird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2301 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yoghurt Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    ir2302 = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yoghurt Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fruit').first().id
        )
    ir2303 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    ir2304 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ir2305 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    ir2306 = RecipeIngredient(
            amount=4,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peachtree schnapps').first().id
        )
    ir2307 = RecipeIngredient(
            amount=4,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Surge').first().id
        )
    ir2309 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir2310 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gold rum').first().id
        )
    ir2311 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    ir2312 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pernod').first().id
        )
    ir2313 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ir2314 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ir2315 = RecipeIngredient(
            amount=1,
            unit='drop',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    ir2316 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zambeer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    ir2317 = RecipeIngredient(
            amount=10,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zambeer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Root beer').first().id
        )
    ir2318 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zambeer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir2319 = RecipeIngredient(
            amount=1.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorbatini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2320 = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorbatini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ouzo').first().id
        )
    ir2321 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zenmeister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    ir2322 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zenmeister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Root beer').first().id
        )
    ir2323 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zipperhead').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    ir2324 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zipperhead').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ir2325 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zipperhead').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    ir2326 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zima Blaster').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Zima').first().id
        )
    ir2327 = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zima Blaster').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    ir2328 = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zizi Coin-coin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    ir2329 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zizi Coin-coin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ir2330 = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zizi Coin-coin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ir2331 = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zizi Coin-coin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ir2332 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zimadori Zinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    ir2333 = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zimadori Zinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Zima').first().id
        )
    ir2334 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zippy\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ir2335 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zippy\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ir2336 = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zippy\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kool-Aid').first().id
        )
    ir2337 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ziemes Martini Apfelsaft').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vermouth').first().id
        )
    ir2338 = RecipeIngredient(
            amount=16,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ziemes Martini Apfelsaft').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )


    db.session.add(ir0)
    db.session.add(ir1)
    db.session.add(ir2)
    db.session.add(ir3)
    db.session.add(ir4)
    db.session.add(ir5)
    db.session.add(ir6)
    db.session.add(ir7)
    db.session.add(ir8)
    db.session.add(ir9)
    db.session.add(ir10)
    db.session.add(ir11)
    db.session.add(ir12)
    db.session.add(ir13)
    db.session.add(ir14)
    db.session.add(ir15)
    db.session.add(ir16)
    db.session.add(ir17)
    db.session.add(ir18)
    db.session.add(ir19)
    db.session.add(ir20)
    db.session.add(ir21)
    db.session.add(ir22)
    db.session.add(ir23)
    db.session.add(ir24)
    db.session.add(ir25)
    db.session.add(ir26)
    db.session.add(ir27)
    db.session.add(ir28)
    db.session.add(ir29)
    db.session.add(ir30)
    db.session.add(ir31)
    db.session.add(ir32)
    db.session.add(ir33)
    db.session.add(ir34)
    db.session.add(ir35)
    db.session.add(ir36)
    db.session.add(ir37)
    db.session.add(ir38)
    db.session.add(ir39)
    db.session.add(ir40)
    db.session.add(ir41)
    db.session.add(ir42)
    db.session.add(ir43)
    db.session.add(ir44)
    db.session.add(ir45)
    db.session.add(ir46)
    db.session.add(ir47)
    db.session.add(ir48)
    db.session.add(ir49)
    db.session.add(ir50)
    db.session.add(ir51)
    db.session.add(ir52)
    db.session.add(ir53)
    db.session.add(ir54)
    db.session.add(ir55)
    db.session.add(ir56)
    db.session.add(ir57)
    db.session.add(ir58)
    db.session.add(ir59)
    db.session.add(ir60)
    db.session.add(ir61)
    db.session.add(ir62)
    db.session.add(ir63)
    db.session.add(ir64)
    db.session.add(ir65)
    db.session.add(ir66)
    db.session.add(ir67)
    db.session.add(ir68)
    db.session.add(ir69)
    db.session.add(ir70)
    db.session.add(ir71)
    db.session.add(ir72)
    db.session.add(ir73)
    db.session.add(ir74)
    db.session.add(ir75)
    db.session.add(ir76)
    db.session.add(ir77)
    db.session.add(ir78)
    db.session.add(ir79)
    db.session.add(ir80)
    db.session.add(ir81)
    db.session.add(ir82)
    db.session.add(ir83)
    db.session.add(ir84)
    db.session.add(ir85)
    db.session.add(ir86)
    db.session.add(ir87)
    db.session.add(ir88)
    db.session.add(ir89)
    db.session.add(ir90)
    db.session.add(ir91)
    db.session.add(ir92)
    db.session.add(ir93)
    db.session.add(ir94)
    db.session.add(ir95)
    db.session.add(ir96)
    db.session.add(ir97)
    db.session.add(ir98)
    db.session.add(ir99)
    db.session.add(ir100)
    db.session.add(ir101)
    db.session.add(ir102)
    db.session.add(ir103)
    db.session.add(ir104)
    db.session.add(ir105)
    db.session.add(ir106)
    db.session.add(ir107)
    db.session.add(ir108)
    db.session.add(ir109)
    db.session.add(ir110)
    db.session.add(ir111)
    db.session.add(ir112)
    db.session.add(ir113)
    db.session.add(ir114)
    db.session.add(ir115)
    db.session.add(ir116)
    db.session.add(ir117)
    db.session.add(ir118)
    db.session.add(ir119)
    db.session.add(ir120)
    db.session.add(ir121)
    db.session.add(ir122)
    db.session.add(ir123)
    db.session.add(ir124)
    db.session.add(ir125)
    db.session.add(ir126)
    db.session.add(ir127)
    db.session.add(ir128)
    db.session.add(ir129)
    db.session.add(ir130)
    db.session.add(ir131)
    db.session.add(ir132)
    db.session.add(ir133)
    db.session.add(ir134)
    db.session.add(ir135)
    db.session.add(ir136)
    db.session.add(ir137)
    db.session.add(ir138)
    db.session.add(ir139)
    db.session.add(ir140)
    db.session.add(ir141)
    db.session.add(ir142)
    db.session.add(ir143)
    db.session.add(ir144)
    db.session.add(ir145)
    db.session.add(ir146)
    db.session.add(ir147)
    db.session.add(ir148)
    db.session.add(ir149)
    db.session.add(ir150)
    db.session.add(ir151)
    db.session.add(ir152)
    db.session.add(ir153)
    db.session.add(ir154)
    db.session.add(ir155)
    db.session.add(ir156)
    db.session.add(ir157)
    db.session.add(ir158)
    db.session.add(ir159)
    db.session.add(ir160)
    db.session.add(ir161)
    db.session.add(ir162)
    db.session.add(ir163)
    db.session.add(ir164)
    db.session.add(ir165)
    db.session.add(ir166)
    db.session.add(ir167)
    db.session.add(ir168)
    db.session.add(ir169)
    db.session.add(ir170)
    db.session.add(ir171)
    db.session.add(ir172)
    db.session.add(ir173)
    db.session.add(ir174)
    db.session.add(ir175)
    db.session.add(ir176)
    db.session.add(ir177)
    db.session.add(ir178)
    db.session.add(ir179)
    db.session.add(ir180)
    db.session.add(ir181)
    db.session.add(ir182)
    db.session.add(ir183)
    db.session.add(ir184)
    db.session.add(ir185)
    db.session.add(ir186)
    db.session.add(ir187)
    db.session.add(ir188)
    db.session.add(ir189)
    db.session.add(ir190)
    db.session.add(ir191)
    db.session.add(ir192)
    db.session.add(ir193)
    db.session.add(ir194)
    db.session.add(ir195)
    db.session.add(ir196)
    db.session.add(ir197)
    db.session.add(ir198)
    db.session.add(ir199)
    db.session.add(ir200)
    db.session.add(ir201)
    db.session.add(ir202)
    db.session.add(ir203)
    db.session.add(ir204)
    db.session.add(ir205)
    db.session.add(ir206)
    db.session.add(ir207)
    db.session.add(ir208)
    db.session.add(ir209)
    db.session.add(ir210)
    db.session.add(ir211)
    db.session.add(ir212)
    db.session.add(ir213)
    db.session.add(ir214)
    db.session.add(ir215)
    db.session.add(ir216)
    db.session.add(ir217)
    db.session.add(ir218)
    db.session.add(ir219)
    db.session.add(ir220)
    db.session.add(ir221)
    db.session.add(ir222)
    db.session.add(ir223)
    db.session.add(ir224)
    db.session.add(ir225)
    db.session.add(ir226)
    db.session.add(ir227)
    db.session.add(ir228)
    db.session.add(ir229)
    db.session.add(ir230)
    db.session.add(ir231)
    db.session.add(ir232)
    db.session.add(ir233)
    db.session.add(ir234)
    db.session.add(ir235)
    db.session.add(ir236)
    db.session.add(ir237)
    db.session.add(ir238)
    db.session.add(ir239)
    db.session.add(ir240)
    db.session.add(ir241)
    db.session.add(ir242)
    db.session.add(ir243)
    db.session.add(ir244)
    db.session.add(ir245)
    db.session.add(ir246)
    db.session.add(ir247)
    db.session.add(ir248)
    db.session.add(ir249)
    db.session.add(ir250)
    db.session.add(ir251)
    db.session.add(ir252)
    db.session.add(ir253)
    db.session.add(ir254)
    db.session.add(ir255)
    db.session.add(ir256)
    db.session.add(ir257)
    db.session.add(ir258)
    db.session.add(ir259)
    db.session.add(ir260)
    db.session.add(ir261)
    db.session.add(ir262)
    # db.session.add(ir263)
    db.session.add(ir264)
    db.session.add(ir265)
    # db.session.add(ir266)
    # db.session.add(ir267)
    db.session.add(ir268)
    db.session.add(ir269)
    db.session.add(ir270)
    db.session.add(ir271)
    db.session.add(ir272)
    db.session.add(ir273)
    db.session.add(ir274)
    db.session.add(ir275)
    db.session.add(ir276)
    db.session.add(ir277)
    db.session.add(ir278)
    db.session.add(ir279)
    db.session.add(ir280)
    db.session.add(ir281)
    db.session.add(ir282)
    db.session.add(ir283)
    db.session.add(ir284)
    # db.session.add(ir285)
    db.session.add(ir286)
    db.session.add(ir287)
    db.session.add(ir288)
    db.session.add(ir289)
    db.session.add(ir290)
    db.session.add(ir291)
    db.session.add(ir292)
    db.session.add(ir293)
    db.session.add(ir294)
    db.session.add(ir295)
    db.session.add(ir296)
    db.session.add(ir297)
    db.session.add(ir298)
    db.session.add(ir299)
    db.session.add(ir300)
    db.session.add(ir301)
    db.session.add(ir302)
    db.session.add(ir303)
    db.session.add(ir304)
    db.session.add(ir305)
    db.session.add(ir306)
    db.session.add(ir307)
    db.session.add(ir308)
    db.session.add(ir309)
    db.session.add(ir310)
    db.session.add(ir311)
    db.session.add(ir312)
    db.session.add(ir313)
    db.session.add(ir314)
    db.session.add(ir315)
    db.session.add(ir316)
    db.session.add(ir317)
    db.session.add(ir318)
    db.session.add(ir319)
    db.session.add(ir320)
    db.session.add(ir321)
    db.session.add(ir322)
    db.session.add(ir323)
    db.session.add(ir324)
    db.session.add(ir325)
    db.session.add(ir326)
    db.session.add(ir327)
    db.session.add(ir328)
    db.session.add(ir329)
    db.session.add(ir330)
    db.session.add(ir331)
    db.session.add(ir332)
    db.session.add(ir333)
    db.session.add(ir334)
    db.session.add(ir335)
    db.session.add(ir336)
    db.session.add(ir337)
    db.session.add(ir338)
    db.session.add(ir339)
    db.session.add(ir340)
    db.session.add(ir341)
    db.session.add(ir342)
    db.session.add(ir343)
    db.session.add(ir344)
    db.session.add(ir345)
    db.session.add(ir346)
    db.session.add(ir347)
    db.session.add(ir348)
    db.session.add(ir349)
    db.session.add(ir350)
    db.session.add(ir351)
    db.session.add(ir352)
    db.session.add(ir353)
    db.session.add(ir354)
    db.session.add(ir355)
    db.session.add(ir356)
    db.session.add(ir357)
    db.session.add(ir358)
    db.session.add(ir359)
    db.session.add(ir360)
    db.session.add(ir361)
    db.session.add(ir362)
    db.session.add(ir363)
    db.session.add(ir364)
    db.session.add(ir365)
    db.session.add(ir366)
    db.session.add(ir367)
    db.session.add(ir368)
    db.session.add(ir369)
    db.session.add(ir370)
    db.session.add(ir371)
    # db.session.add(ir372)
    db.session.add(ir373)
    db.session.add(ir374)
    db.session.add(ir375)
    db.session.add(ir376)
    db.session.add(ir377)
    db.session.add(ir378)
    db.session.add(ir379)
    db.session.add(ir380)
    db.session.add(ir381)
    db.session.add(ir382)
    db.session.add(ir383)
    db.session.add(ir384)
    db.session.add(ir385)
    db.session.add(ir386)
    db.session.add(ir387)
    db.session.add(ir388)
    db.session.add(ir389)
    db.session.add(ir390)
    db.session.add(ir391)
    db.session.add(ir392)
    db.session.add(ir393)
    db.session.add(ir394)
    db.session.add(ir395)
    db.session.add(ir396)
    db.session.add(ir397)
    db.session.add(ir398)
    db.session.add(ir399)
    db.session.add(ir400)
    db.session.add(ir401)
    db.session.add(ir402)
    db.session.add(ir403)
    db.session.add(ir404)
    db.session.add(ir405)
    db.session.add(ir406)
    db.session.add(ir407)
    db.session.add(ir408)
    db.session.add(ir409)
    db.session.add(ir410)
    db.session.add(ir411)
    db.session.add(ir412)
    db.session.add(ir413)
    db.session.add(ir414)
    db.session.add(ir415)
    db.session.add(ir416)
    db.session.add(ir417)
    db.session.add(ir418)
    db.session.add(ir419)
    db.session.add(ir420)
    db.session.add(ir421)
    db.session.add(ir422)
    db.session.add(ir423)
    db.session.add(ir424)
    db.session.add(ir425)
    db.session.add(ir426)
    db.session.add(ir427)
    db.session.add(ir428)
    db.session.add(ir429)
    db.session.add(ir430)
    db.session.add(ir431)
    db.session.add(ir432)
    db.session.add(ir433)
    db.session.add(ir434)
    db.session.add(ir435)
    db.session.add(ir436)
    db.session.add(ir437)
    db.session.add(ir438)
    db.session.add(ir439)
    db.session.add(ir440)
    db.session.add(ir441)
    db.session.add(ir442)
    db.session.add(ir443)
    db.session.add(ir444)
    db.session.add(ir445)
    db.session.add(ir446)
    db.session.add(ir447)
    db.session.add(ir448)
    db.session.add(ir449)
    db.session.add(ir450)
    db.session.add(ir451)
    db.session.add(ir452)
    db.session.add(ir453)
    db.session.add(ir454)
    db.session.add(ir455)
    db.session.add(ir456)
    db.session.add(ir457)
    db.session.add(ir458)
    db.session.add(ir459)
    db.session.add(ir460)
    db.session.add(ir461)
    db.session.add(ir462)
    db.session.add(ir463)
    db.session.add(ir464)
    db.session.add(ir465)
    db.session.add(ir466)
    db.session.add(ir467)
    db.session.add(ir468)
    db.session.add(ir469)
    db.session.add(ir470)
    db.session.add(ir471)
    db.session.add(ir472)
    db.session.add(ir473)
    db.session.add(ir474)
    db.session.add(ir475)
    db.session.add(ir476)
    db.session.add(ir477)
    db.session.add(ir478)
    db.session.add(ir479)
    db.session.add(ir480)
    db.session.add(ir481)
    db.session.add(ir482)
    db.session.add(ir483)
    db.session.add(ir484)
    db.session.add(ir485)
    db.session.add(ir486)
    db.session.add(ir487)
    db.session.add(ir488)
    db.session.add(ir489)
    db.session.add(ir490)
    db.session.add(ir491)
    db.session.add(ir492)
    db.session.add(ir493)
    db.session.add(ir494)
    db.session.add(ir495)
    # db.session.add(ir496)
    db.session.add(ir497)
    db.session.add(ir498)
    db.session.add(ir499)
    db.session.add(ir500)
    db.session.add(ir501)
    db.session.add(ir502)
    db.session.add(ir503)
    db.session.add(ir504)
    db.session.add(ir505)
    db.session.add(ir506)
    db.session.add(ir507)
    db.session.add(ir508)
    db.session.add(ir509)
    db.session.add(ir510)
    db.session.add(ir511)
    db.session.add(ir512)
    db.session.add(ir513)
    db.session.add(ir514)
    db.session.add(ir515)
    db.session.add(ir516)
    db.session.add(ir517)
    db.session.add(ir518)
    db.session.add(ir519)
    db.session.add(ir520)
    db.session.add(ir521)
    db.session.add(ir522)
    db.session.add(ir523)
    db.session.add(ir524)
    db.session.add(ir525)
    db.session.add(ir526)
    db.session.add(ir527)
    db.session.add(ir528)
    db.session.add(ir529)
    # db.session.add(ir530)
    db.session.add(ir531)
    db.session.add(ir532)
    db.session.add(ir533)
    db.session.add(ir534)
    db.session.add(ir535)
    db.session.add(ir536)
    db.session.add(ir537)
    db.session.add(ir538)
    db.session.add(ir539)
    db.session.add(ir540)
    db.session.add(ir541)
    db.session.add(ir542)
    db.session.add(ir543)
    db.session.add(ir544)
    db.session.add(ir545)
    db.session.add(ir546)
    db.session.add(ir547)
    db.session.add(ir548)
    db.session.add(ir549)
    db.session.add(ir550)
    db.session.add(ir551)
    db.session.add(ir552)
    # db.session.add(ir553)
    db.session.add(ir554)
    db.session.add(ir555)
    db.session.add(ir556)
    db.session.add(ir557)
    db.session.add(ir558)
    db.session.add(ir559)
    db.session.add(ir560)
    db.session.add(ir561)
    db.session.add(ir562)
    db.session.add(ir563)
    db.session.add(ir564)
    db.session.add(ir565)
    db.session.add(ir566)
    db.session.add(ir567)
    db.session.add(ir568)
    db.session.add(ir569)
    db.session.add(ir570)
    db.session.add(ir571)
    db.session.add(ir572)
    db.session.add(ir573)
    db.session.add(ir574)
    db.session.add(ir575)
    db.session.add(ir576)
    db.session.add(ir577)
    db.session.add(ir578)
    db.session.add(ir579)
    db.session.add(ir580)
    db.session.add(ir581)
    db.session.add(ir582)
    db.session.add(ir583)
    db.session.add(ir584)
    db.session.add(ir585)
    db.session.add(ir586)
    db.session.add(ir587)
    db.session.add(ir588)
    db.session.add(ir589)
    db.session.add(ir590)
    db.session.add(ir591)
    db.session.add(ir592)
    db.session.add(ir593)
    db.session.add(ir594)
    db.session.add(ir595)
    db.session.add(ir596)
    db.session.add(ir597)
    db.session.add(ir598)
    db.session.add(ir599)
    db.session.add(ir600)
    db.session.add(ir601)
    db.session.add(ir602)
    db.session.add(ir603)
    db.session.add(ir604)
    db.session.add(ir605)
    db.session.add(ir606)
    db.session.add(ir607)
    db.session.add(ir608)
    db.session.add(ir609)
    db.session.add(ir610)
    db.session.add(ir611)
    db.session.add(ir612)
    db.session.add(ir613)
    db.session.add(ir614)
    db.session.add(ir615)
    db.session.add(ir616)
    db.session.add(ir617)
    db.session.add(ir618)
    db.session.add(ir619)
    db.session.add(ir620)
    db.session.add(ir621)
    db.session.add(ir622)
    db.session.add(ir623)
    db.session.add(ir624)
    db.session.add(ir625)
    db.session.add(ir626)
    db.session.add(ir627)
    db.session.add(ir628)
    db.session.add(ir629)
    db.session.add(ir630)
    db.session.add(ir631)
    db.session.add(ir632)
    db.session.add(ir633)
    db.session.add(ir634)
    db.session.add(ir635)
    db.session.add(ir636)
    db.session.add(ir637)
    db.session.add(ir638)
    db.session.add(ir639)
    db.session.add(ir640)
    db.session.add(ir641)
    db.session.add(ir642)
    db.session.add(ir643)
    db.session.add(ir644)
    db.session.add(ir645)
    db.session.add(ir646)
    db.session.add(ir647)
    db.session.add(ir648)
    db.session.add(ir649)
    db.session.add(ir650)
    db.session.add(ir651)
    db.session.add(ir652)
    db.session.add(ir653)
    db.session.add(ir654)
    db.session.add(ir655)
    db.session.add(ir656)
    db.session.add(ir657)
    db.session.add(ir658)
    db.session.add(ir659)
    db.session.add(ir660)
    db.session.add(ir661)
    db.session.add(ir662)
    db.session.add(ir663)
    db.session.add(ir664)
    db.session.add(ir665)
    db.session.add(ir666)
    db.session.add(ir667)
    db.session.add(ir668)
    db.session.add(ir669)
    db.session.add(ir670)
    db.session.add(ir671)
    db.session.add(ir672)
    db.session.add(ir673)
    db.session.add(ir674)
    db.session.add(ir675)
    db.session.add(ir676)
    db.session.add(ir677)
    db.session.add(ir678)
    db.session.add(ir679)
    db.session.add(ir680)
    db.session.add(ir681)
    db.session.add(ir682)
    db.session.add(ir683)
    db.session.add(ir684)
    db.session.add(ir685)
    db.session.add(ir686)
    db.session.add(ir687)
    db.session.add(ir688)
    db.session.add(ir689)
    db.session.add(ir690)
    db.session.add(ir691)
    db.session.add(ir692)
    db.session.add(ir693)
    db.session.add(ir694)
    db.session.add(ir695)
    db.session.add(ir696)
    db.session.add(ir697)
    db.session.add(ir698)
    db.session.add(ir699)
    db.session.add(ir700)
    db.session.add(ir701)
    db.session.add(ir702)
    db.session.add(ir703)
    db.session.add(ir706)
    db.session.add(ir707)
    db.session.add(ir708)
    db.session.add(ir709)
    db.session.add(ir710)
    db.session.add(ir711)
    db.session.add(ir712)
    db.session.add(ir713)
    db.session.add(ir714)
    db.session.add(ir715)
    db.session.add(ir716)
    db.session.add(ir717)
    db.session.add(ir718)
    db.session.add(ir719)
    db.session.add(ir720)
    db.session.add(ir721)
    db.session.add(ir722)
    db.session.add(ir723)
    db.session.add(ir724)
    db.session.add(ir725)
    db.session.add(ir726)
    db.session.add(ir727)
    db.session.add(ir728)
    db.session.add(ir729)
    db.session.add(ir730)
    db.session.add(ir731)
    db.session.add(ir732)
    db.session.add(ir733)
    db.session.add(ir734)
    db.session.add(ir735)
    db.session.add(ir736)
    db.session.add(ir737)
    db.session.add(ir738)
    db.session.add(ir739)
    db.session.add(ir740)
    db.session.add(ir741)
    db.session.add(ir742)
    db.session.add(ir743)
    db.session.add(ir744)
    db.session.add(ir745)
    db.session.add(ir746)
    db.session.add(ir747)
    db.session.add(ir748)
    db.session.add(ir749)
    db.session.add(ir750)
    db.session.add(ir751)
    db.session.add(ir752)
    db.session.add(ir753)
    db.session.add(ir754)
    db.session.add(ir755)
    db.session.add(ir756)
    db.session.add(ir757)
    db.session.add(ir758)
    db.session.add(ir759)
    db.session.add(ir760)
    db.session.add(ir761)
    db.session.add(ir762)
    db.session.add(ir763)
    db.session.add(ir764)
    db.session.add(ir765)
    db.session.add(ir766)
    db.session.add(ir767)
    db.session.add(ir768)
    db.session.add(ir769)
    db.session.add(ir770)
    db.session.add(ir771)
    db.session.add(ir772)
    db.session.add(ir773)
    db.session.add(ir774)
    db.session.add(ir775)
    db.session.add(ir776)
    db.session.add(ir777)
    db.session.add(ir778)
    db.session.add(ir779)
    db.session.add(ir780)
    db.session.add(ir781)
    db.session.add(ir782)
    db.session.add(ir783)
    db.session.add(ir784)
    db.session.add(ir785)
    db.session.add(ir786)
    db.session.add(ir787)
    db.session.add(ir788)
    db.session.add(ir789)
    db.session.add(ir790)
    db.session.add(ir791)
    db.session.add(ir792)
    db.session.add(ir793)
    db.session.add(ir794)
    db.session.add(ir795)
    db.session.add(ir796)
    db.session.add(ir797)
    db.session.add(ir798)
    db.session.add(ir799)
    db.session.add(ir800)
    db.session.add(ir801)
    db.session.add(ir802)
    db.session.add(ir803)
    db.session.add(ir804)
    db.session.add(ir805)
    db.session.add(ir806)
    db.session.add(ir807)
    db.session.add(ir808)
    db.session.add(ir809)
    db.session.add(ir810)
    db.session.add(ir811)
    db.session.add(ir812)
    db.session.add(ir813)
    db.session.add(ir814)
    db.session.add(ir815)
    db.session.add(ir816)
    db.session.add(ir817)
    db.session.add(ir818)
    db.session.add(ir819)
    db.session.add(ir820)
    db.session.add(ir821)
    db.session.add(ir822)
    db.session.add(ir823)
    db.session.add(ir824)
    db.session.add(ir825)
    db.session.add(ir826)
    db.session.add(ir827)
    db.session.add(ir828)
    db.session.add(ir829)
    db.session.add(ir830)
    db.session.add(ir831)
    db.session.add(ir832)
    db.session.add(ir833)
    db.session.add(ir834)
    db.session.add(ir835)
    db.session.add(ir836)
    db.session.add(ir837)
    db.session.add(ir838)
    db.session.add(ir839)
    db.session.add(ir840)
    db.session.add(ir841)
    db.session.add(ir842)
    db.session.add(ir843)
    db.session.add(ir844)
    db.session.add(ir845)
    db.session.add(ir846)
    db.session.add(ir847)
    db.session.add(ir848)
    db.session.add(ir849)
    db.session.add(ir850)
    db.session.add(ir851)
    db.session.add(ir852)
    db.session.add(ir853)
    db.session.add(ir854)
    db.session.add(ir855)
    db.session.add(ir856)
    db.session.add(ir857)
    db.session.add(ir858)
    db.session.add(ir859)
    db.session.add(ir860)
    db.session.add(ir861)
    db.session.add(ir862)
    db.session.add(ir863)
    db.session.add(ir864)
    db.session.add(ir865)
    db.session.add(ir866)
    db.session.add(ir867)
    db.session.add(ir868)
    db.session.add(ir869)
    db.session.add(ir870)
    db.session.add(ir871)
    db.session.add(ir872)
    db.session.add(ir873)
    db.session.add(ir874)
    db.session.add(ir875)
    db.session.add(ir876)
    db.session.add(ir877)
    db.session.add(ir878)
    db.session.add(ir879)
    db.session.add(ir880)
    db.session.add(ir881)
    db.session.add(ir882)
    db.session.add(ir883)
    db.session.add(ir884)
    db.session.add(ir885)
    db.session.add(ir886)
    db.session.add(ir887)
    db.session.add(ir888)
    db.session.add(ir889)
    db.session.add(ir890)
    db.session.add(ir891)
    db.session.add(ir892)
    db.session.add(ir893)
    db.session.add(ir894)
    db.session.add(ir895)
    db.session.add(ir896)
    db.session.add(ir897)
    db.session.add(ir898)
    db.session.add(ir899)
    db.session.add(ir900)
    db.session.add(ir901)
    db.session.add(ir902)
    db.session.add(ir903)
    db.session.add(ir904)
    db.session.add(ir905)
    db.session.add(ir906)
    db.session.add(ir907)
    db.session.add(ir908)
    db.session.add(ir909)
    db.session.add(ir910)
    db.session.add(ir911)
    db.session.add(ir912)
    db.session.add(ir913)
    db.session.add(ir914)
    db.session.add(ir915)
    db.session.add(ir916)
    db.session.add(ir917)
    db.session.add(ir918)
    db.session.add(ir919)
    db.session.add(ir920)
    db.session.add(ir921)
    db.session.add(ir922)
    db.session.add(ir923)
    db.session.add(ir924)
    db.session.add(ir925)
    db.session.add(ir926)
    db.session.add(ir927)
    db.session.add(ir928)
    db.session.add(ir929)
    db.session.add(ir930)
    # db.session.add(ir931)
    db.session.add(ir932)
    db.session.add(ir933)
    db.session.add(ir934)
    db.session.add(ir935)
    db.session.add(ir936)
    db.session.add(ir937)
    db.session.add(ir938)
    db.session.add(ir939)
    db.session.add(ir940)
    db.session.add(ir941)
    db.session.add(ir942)
    db.session.add(ir943)
    db.session.add(ir944)
    db.session.add(ir945)
    db.session.add(ir946)
    db.session.add(ir947)
    db.session.add(ir948)
    db.session.add(ir949)
    db.session.add(ir950)
    db.session.add(ir951)
    db.session.add(ir952)
    db.session.add(ir953)
    db.session.add(ir954)
    db.session.add(ir955)
    db.session.add(ir956)
    db.session.add(ir957)
    db.session.add(ir958)
    db.session.add(ir959)
    db.session.add(ir960)
    db.session.add(ir961)
    db.session.add(ir962)
    db.session.add(ir963)
    db.session.add(ir964)
    db.session.add(ir965)
    db.session.add(ir966)
    db.session.add(ir967)
    db.session.add(ir968)
    db.session.add(ir969)
    db.session.add(ir970)
    db.session.add(ir971)
    db.session.add(ir972)
    db.session.add(ir973)
    db.session.add(ir974)
    db.session.add(ir975)
    db.session.add(ir976)
    db.session.add(ir977)
    db.session.add(ir978)
    db.session.add(ir979)
    db.session.add(ir980)
    db.session.add(ir981)
    db.session.add(ir982)
    db.session.add(ir983)
    db.session.add(ir984)
    db.session.add(ir985)
    db.session.add(ir986)
    db.session.add(ir987)
    db.session.add(ir988)
    db.session.add(ir989)
    db.session.add(ir990)
    db.session.add(ir991)
    db.session.add(ir992)
    # db.session.add(ir993)
    # db.session.add(ir994)
    db.session.add(ir995)
    db.session.add(ir996)
    db.session.add(ir997)
    db.session.add(ir998)
    db.session.add(ir999)
    db.session.add(ir1000)
    db.session.add(ir1001)
    db.session.add(ir1002)
    db.session.add(ir1003)
    db.session.add(ir1004)
    db.session.add(ir1005)
    db.session.add(ir1006)
    db.session.add(ir1007)
    db.session.add(ir1008)
    db.session.add(ir1009)
    db.session.add(ir1010)
    db.session.add(ir1011)
    db.session.add(ir1012)
    db.session.add(ir1013)
    db.session.add(ir1014)
    db.session.add(ir1015)
    db.session.add(ir1016)
    db.session.add(ir1017)
    db.session.add(ir1018)
    db.session.add(ir1019)
    db.session.add(ir1020)
    db.session.add(ir1021)
    db.session.add(ir1022)
    db.session.add(ir1023)
    db.session.add(ir1024)
    db.session.add(ir1025)
    db.session.add(ir1026)
    db.session.add(ir1027)
    db.session.add(ir1028)
    db.session.add(ir1029)
    db.session.add(ir1030)
    db.session.add(ir1031)
    db.session.add(ir1032)
    db.session.add(ir1033)
    db.session.add(ir1034)
    db.session.add(ir1035)
    db.session.add(ir1036)
    db.session.add(ir1037)
    db.session.add(ir1038)
    db.session.add(ir1039)
    db.session.add(ir1040)
    db.session.add(ir1041)
    db.session.add(ir1042)
    db.session.add(ir1043)
    db.session.add(ir1044)
    db.session.add(ir1045)
    db.session.add(ir1046)
    db.session.add(ir1047)
    db.session.add(ir1048)
    db.session.add(ir1049)
    db.session.add(ir1050)
    db.session.add(ir1051)
    db.session.add(ir1052)
    db.session.add(ir1053)
    db.session.add(ir1054)
    db.session.add(ir1055)
    db.session.add(ir1056)
    db.session.add(ir1057)
    db.session.add(ir1058)
    db.session.add(ir1059)
    db.session.add(ir1060)
    db.session.add(ir1061)
    db.session.add(ir1062)
    db.session.add(ir1063)
    db.session.add(ir1064)
    db.session.add(ir1065)
    db.session.add(ir1066)
    db.session.add(ir1067)
    db.session.add(ir1068)
    db.session.add(ir1069)
    db.session.add(ir1070)
    db.session.add(ir1071)
    db.session.add(ir1072)
    db.session.add(ir1073)
    db.session.add(ir1074)
    db.session.add(ir1075)
    db.session.add(ir1076)
    db.session.add(ir1077)
    db.session.add(ir1078)
    db.session.add(ir1079)
    db.session.add(ir1080)
    db.session.add(ir1081)
    db.session.add(ir1082)
    db.session.add(ir1083)
    db.session.add(ir1084)
    db.session.add(ir1085)
    db.session.add(ir1086)
    db.session.add(ir1087)
    db.session.add(ir1088)
    db.session.add(ir1089)
    db.session.add(ir1090)
    db.session.add(ir1091)
    db.session.add(ir1092)
    db.session.add(ir1093)
    db.session.add(ir1094)
    db.session.add(ir1095)
    db.session.add(ir1096)
    db.session.add(ir1097)
    db.session.add(ir1098)
    db.session.add(ir1099)
    db.session.add(ir1100)
    db.session.add(ir1101)
    db.session.add(ir1102)
    db.session.add(ir1103)
    db.session.add(ir1104)
    db.session.add(ir1105)
    db.session.add(ir1106)
    db.session.add(ir1107)
    db.session.add(ir1108)
    db.session.add(ir1109)
    db.session.add(ir1110)
    db.session.add(ir1111)
    db.session.add(ir1112)
    db.session.add(ir1113)
    db.session.add(ir1114)
    db.session.add(ir1115)
    db.session.add(ir1116)
    db.session.add(ir1117)
    db.session.add(ir1118)
    db.session.add(ir1119)
    db.session.add(ir1120)
    db.session.add(ir1121)
    db.session.add(ir1122)
    db.session.add(ir1123)
    db.session.add(ir1124)
    db.session.add(ir1125)
    db.session.add(ir1126)
    db.session.add(ir1127)
    db.session.add(ir1128)
    db.session.add(ir1129)
    db.session.add(ir1130)
    db.session.add(ir1131)
    db.session.add(ir1132)
    db.session.add(ir1133)
    db.session.add(ir1134)
    db.session.add(ir1135)
    db.session.add(ir1136)
    db.session.add(ir1137)
    db.session.add(ir1138)
    db.session.add(ir1139)
    db.session.add(ir1140)
    db.session.add(ir1141)
    db.session.add(ir1142)
    db.session.add(ir1143)
    db.session.add(ir1144)
    db.session.add(ir1145)
    db.session.add(ir1146)
    db.session.add(ir1147)
    db.session.add(ir1148)
    db.session.add(ir1149)
    db.session.add(ir1150)
    db.session.add(ir1151)
    db.session.add(ir1152)
    db.session.add(ir1153)
    db.session.add(ir1154)
    db.session.add(ir1155)
    db.session.add(ir1156)
    db.session.add(ir1157)
    db.session.add(ir1158)
    db.session.add(ir1159)
    db.session.add(ir1160)
    db.session.add(ir1161)
    db.session.add(ir1162)
    db.session.add(ir1163)
    db.session.add(ir1164)
    db.session.add(ir1165)
    db.session.add(ir1166)
    db.session.add(ir1167)
    db.session.add(ir1168)
    db.session.add(ir1169)
    db.session.add(ir1170)
    db.session.add(ir1171)
    db.session.add(ir1172)
    db.session.add(ir1173)
    db.session.add(ir1174)
    db.session.add(ir1175)
    db.session.add(ir1176)
    db.session.add(ir1177)
    db.session.add(ir1178)
    db.session.add(ir1179)
    db.session.add(ir1180)
    db.session.add(ir1181)
    db.session.add(ir1182)
    db.session.add(ir1183)
    db.session.add(ir1184)
    db.session.add(ir1185)
    db.session.add(ir1186)
    db.session.add(ir1187)
    db.session.add(ir1188)
    db.session.add(ir1189)
    db.session.add(ir1190)
    db.session.add(ir1191)
    db.session.add(ir1192)
    db.session.add(ir1193)
    db.session.add(ir1194)
    db.session.add(ir1195)
    db.session.add(ir1196)
    db.session.add(ir1197)
    db.session.add(ir1198)
    db.session.add(ir1199)
    db.session.add(ir1200)
    db.session.add(ir1201)
    db.session.add(ir1202)
    db.session.add(ir1203)
    db.session.add(ir1204)
    db.session.add(ir1205)
    db.session.add(ir1206)
    db.session.add(ir1207)
    db.session.add(ir1208)
    db.session.add(ir1209)
    db.session.add(ir1210)
    db.session.add(ir1211)
    db.session.add(ir1212)
    db.session.add(ir1213)
    db.session.add(ir1214)
    db.session.add(ir1215)
    db.session.add(ir1216)
    db.session.add(ir1217)
    db.session.add(ir1218)
    db.session.add(ir1219)
    db.session.add(ir1220)
    db.session.add(ir1221)
    db.session.add(ir1222)
    db.session.add(ir1223)
    db.session.add(ir1224)
    db.session.add(ir1225)
    db.session.add(ir1227)
    db.session.add(ir1228)
    db.session.add(ir1229)
    db.session.add(ir1230)
    db.session.add(ir1231)
    db.session.add(ir1232)
    db.session.add(ir1233)
    db.session.add(ir1234)
    db.session.add(ir1235)
    db.session.add(ir1236)
    db.session.add(ir1237)
    db.session.add(ir1238)
    db.session.add(ir1239)
    db.session.add(ir1240)
    db.session.add(ir1241)
    db.session.add(ir1242)
    db.session.add(ir1243)
    db.session.add(ir1244)
    db.session.add(ir1245)
    db.session.add(ir1246)
    db.session.add(ir1247)
    db.session.add(ir1248)
    db.session.add(ir1249)
    db.session.add(ir1250)
    db.session.add(ir1251)
    db.session.add(ir1252)
    db.session.add(ir1253)
    db.session.add(ir1254)
    db.session.add(ir1255)
    db.session.add(ir1256)
    db.session.add(ir1257)
    db.session.add(ir1258)
    db.session.add(ir1259)
    db.session.add(ir1260)
    db.session.add(ir1261)
    db.session.add(ir1262)
    db.session.add(ir1263)
    db.session.add(ir1264)
    db.session.add(ir1265)
    db.session.add(ir1266)
    db.session.add(ir1267)
    db.session.add(ir1268)
    db.session.add(ir1269)
    db.session.add(ir1270)
    db.session.add(ir1271)
    db.session.add(ir1272)
    db.session.add(ir1273)
    db.session.add(ir1274)
    db.session.add(ir1275)
    db.session.add(ir1276)
    db.session.add(ir1277)
    db.session.add(ir1278)
    db.session.add(ir1279)
    db.session.add(ir1280)
    db.session.add(ir1281)
    db.session.add(ir1282)
    db.session.add(ir1283)
    db.session.add(ir1284)
    db.session.add(ir1285)
    db.session.add(ir1286)
    db.session.add(ir1287)
    db.session.add(ir1288)
    db.session.add(ir1289)
    db.session.add(ir1290)
    db.session.add(ir1291)
    db.session.add(ir1292)
    db.session.add(ir1293)
    db.session.add(ir1294)
    db.session.add(ir1295)
    db.session.add(ir1296)
    db.session.add(ir1297)
    db.session.add(ir1298)
    db.session.add(ir1299)
    db.session.add(ir1300)
    db.session.add(ir1301)
    db.session.add(ir1302)
    db.session.add(ir1303)
    db.session.add(ir1304)
    db.session.add(ir1305)
    db.session.add(ir1306)
    db.session.add(ir1307)
    db.session.add(ir1308)
    db.session.add(ir1309)
    db.session.add(ir1310)
    db.session.add(ir1311)
    db.session.add(ir1312)
    db.session.add(ir1313)
    db.session.add(ir1314)
    db.session.add(ir1315)
    db.session.add(ir1316)
    db.session.add(ir1317)
    db.session.add(ir1318)
    db.session.add(ir1319)
    db.session.add(ir1320)
    db.session.add(ir1321)
    db.session.add(ir1322)
    db.session.add(ir1323)
    db.session.add(ir1324)
    db.session.add(ir1325)
    db.session.add(ir1326)
    db.session.add(ir1327)
    db.session.add(ir1328)
    db.session.add(ir1329)
    db.session.add(ir1330)
    db.session.add(ir1331)
    db.session.add(ir1332)
    db.session.add(ir1333)
    db.session.add(ir1334)
    db.session.add(ir1335)
    db.session.add(ir1336)
    db.session.add(ir1337)
    db.session.add(ir1338)
    db.session.add(ir1339)
    db.session.add(ir1340)
    db.session.add(ir1341)
    db.session.add(ir1342)
    db.session.add(ir1343)
    db.session.add(ir1344)
    db.session.add(ir1345)
    db.session.add(ir1346)
    db.session.add(ir1347)
    db.session.add(ir1348)
    db.session.add(ir1349)
    db.session.add(ir1350)
    db.session.add(ir1351)
    db.session.add(ir1352)
    db.session.add(ir1353)
    db.session.add(ir1354)
    db.session.add(ir1355)
    db.session.add(ir1356)
    db.session.add(ir1357)
    db.session.add(ir1358)
    db.session.add(ir1359)
    db.session.add(ir1360)
    db.session.add(ir1361)
    db.session.add(ir1362)
    db.session.add(ir1363)
    db.session.add(ir1364)
    # db.session.add(ir1365)
    db.session.add(ir1366)
    db.session.add(ir1367)
    db.session.add(ir1368)
    db.session.add(ir1369)
    db.session.add(ir1370)
    db.session.add(ir1371)
    db.session.add(ir1372)
    db.session.add(ir1373)
    db.session.add(ir1374)
    db.session.add(ir1375)
    db.session.add(ir1376)
    db.session.add(ir1377)
    db.session.add(ir1378)
    db.session.add(ir1379)
    db.session.add(ir1380)
    db.session.add(ir1381)
    db.session.add(ir1382)
    db.session.add(ir1383)
    db.session.add(ir1384)
    db.session.add(ir1385)
    db.session.add(ir1386)
    db.session.add(ir1387)
    db.session.add(ir1388)
    db.session.add(ir1389)
    db.session.add(ir1390)
    db.session.add(ir1391)
    db.session.add(ir1392)
    db.session.add(ir1393)
    db.session.add(ir1394)
    db.session.add(ir1395)
    db.session.add(ir1396)
    db.session.add(ir1397)
    db.session.add(ir1398)
    db.session.add(ir1399)
    db.session.add(ir1400)
    db.session.add(ir1401)
    db.session.add(ir1402)
    db.session.add(ir1403)
    db.session.add(ir1404)
    db.session.add(ir1405)
    db.session.add(ir1406)
    db.session.add(ir1407)
    db.session.add(ir1408)
    db.session.add(ir1409)
    db.session.add(ir1410)
    db.session.add(ir1411)
    db.session.add(ir1412)
    db.session.add(ir1413)
    db.session.add(ir1414)
    db.session.add(ir1415)
    db.session.add(ir1416)
    db.session.add(ir1417)
    db.session.add(ir1418)
    db.session.add(ir1419)
    db.session.add(ir1420)
    db.session.add(ir1421)
    db.session.add(ir1422)
    db.session.add(ir1423)
    db.session.add(ir1424)
    db.session.add(ir1425)
    db.session.add(ir1426)
    db.session.add(ir1427)
    db.session.add(ir1428)
    db.session.add(ir1429)
    db.session.add(ir1430)
    db.session.add(ir1431)
    db.session.add(ir1432)
    db.session.add(ir1433)
    db.session.add(ir1434)
    db.session.add(ir1435)
    db.session.add(ir1436)
    db.session.add(ir1437)
    db.session.add(ir1438)
    db.session.add(ir1439)
    db.session.add(ir1440)
    db.session.add(ir1441)
    db.session.add(ir1442)
    db.session.add(ir1443)
    db.session.add(ir1444)
    db.session.add(ir1445)
    db.session.add(ir1446)
    db.session.add(ir1447)
    db.session.add(ir1448)
    db.session.add(ir1449)
    db.session.add(ir1450)
    db.session.add(ir1451)
    db.session.add(ir1452)
    db.session.add(ir1453)
    db.session.add(ir1454)
    db.session.add(ir1455)
    db.session.add(ir1456)
    db.session.add(ir1457)
    db.session.add(ir1458)
    db.session.add(ir1459)
    db.session.add(ir1460)
    db.session.add(ir1461)
    db.session.add(ir1462)
    db.session.add(ir1463)
    db.session.add(ir1464)
    db.session.add(ir1465)
    db.session.add(ir1466)
    db.session.add(ir1467)
    db.session.add(ir1468)
    db.session.add(ir1470)
    db.session.add(ir1471)
    db.session.add(ir1472)
    db.session.add(ir1473)
    db.session.add(ir1474)
    db.session.add(ir1475)
    db.session.add(ir1476)
    db.session.add(ir1477)
    db.session.add(ir1478)
    db.session.add(ir1479)
    db.session.add(ir1480)
    db.session.add(ir1481)
    db.session.add(ir1482)
    db.session.add(ir1483)
    db.session.add(ir1484)
    db.session.add(ir1485)
    db.session.add(ir1486)
    db.session.add(ir1487)
    db.session.add(ir1488)
    db.session.add(ir1489)
    db.session.add(ir1490)
    db.session.add(ir1491)
    db.session.add(ir1492)
    db.session.add(ir1493)
    db.session.add(ir1494)
    db.session.add(ir1495)
    db.session.add(ir1496)
    db.session.add(ir1497)
    db.session.add(ir1498)
    db.session.add(ir1499)
    db.session.add(ir1500)
    db.session.add(ir1501)
    db.session.add(ir1502)
    db.session.add(ir1503)
    db.session.add(ir1504)
    db.session.add(ir1505)
    db.session.add(ir1506)
    db.session.add(ir1507)
    db.session.add(ir1508)
    db.session.add(ir1509)
    db.session.add(ir1510)
    db.session.add(ir1511)
    db.session.add(ir1512)
    db.session.add(ir1513)
    db.session.add(ir1514)
    db.session.add(ir1515)
    db.session.add(ir1516)
    db.session.add(ir1517)
    db.session.add(ir1518)
    db.session.add(ir1519)
    db.session.add(ir1520)
    db.session.add(ir1521)
    db.session.add(ir1522)
    db.session.add(ir1523)
    db.session.add(ir1524)
    db.session.add(ir1525)
    db.session.add(ir1526)
    db.session.add(ir1527)
    db.session.add(ir1528)
    db.session.add(ir1529)
    db.session.add(ir1530)
    db.session.add(ir1531)
    db.session.add(ir1532)
    db.session.add(ir1533)
    db.session.add(ir1534)
    db.session.add(ir1535)
    db.session.add(ir1536)
    db.session.add(ir1537)
    db.session.add(ir1538)
    db.session.add(ir1539)
    db.session.add(ir1540)
    db.session.add(ir1541)
    db.session.add(ir1542)
    db.session.add(ir1543)
    db.session.add(ir1544)
    db.session.add(ir1545)
    db.session.add(ir1546)
    db.session.add(ir1547)
    db.session.add(ir1548)
    db.session.add(ir1549)
    db.session.add(ir1550)
    db.session.add(ir1551)
    # db.session.add(ir1552)
    db.session.add(ir1553)
    db.session.add(ir1554)
    db.session.add(ir1555)
    db.session.add(ir1556)
    db.session.add(ir1557)
    db.session.add(ir1558)
    db.session.add(ir1559)
    db.session.add(ir1560)
    db.session.add(ir1561)
    db.session.add(ir1562)
    db.session.add(ir1563)
    db.session.add(ir1564)
    db.session.add(ir1565)
    db.session.add(ir1566)
    db.session.add(ir1567)
    db.session.add(ir1568)
    db.session.add(ir1569)
    db.session.add(ir1570)
    db.session.add(ir1571)
    db.session.add(ir1572)
    db.session.add(ir1573)
    db.session.add(ir1574)
    db.session.add(ir1575)
    db.session.add(ir1576)
    db.session.add(ir1577)
    db.session.add(ir1578)
    db.session.add(ir1579)
    db.session.add(ir1580)
    db.session.add(ir1581)
    db.session.add(ir1582)
    db.session.add(ir1583)
    db.session.add(ir1584)
    db.session.add(ir1585)
    db.session.add(ir1586)
    db.session.add(ir1587)
    db.session.add(ir1588)
    db.session.add(ir1589)
    db.session.add(ir1590)
    db.session.add(ir1591)
    db.session.add(ir1592)
    db.session.add(ir1593)
    db.session.add(ir1594)
    db.session.add(ir1595)
    db.session.add(ir1596)
    db.session.add(ir1597)
    db.session.add(ir1598)
    db.session.add(ir1599)
    db.session.add(ir1600)
    db.session.add(ir1601)
    db.session.add(ir1602)
    db.session.add(ir1603)
    db.session.add(ir1604)
    db.session.add(ir1605)
    db.session.add(ir1606)
    db.session.add(ir1607)
    db.session.add(ir1608)
    db.session.add(ir1609)
    db.session.add(ir1610)
    db.session.add(ir1611)
    db.session.add(ir1612)
    db.session.add(ir1613)
    db.session.add(ir1614)
    db.session.add(ir1615)
    db.session.add(ir1616)
    db.session.add(ir1617)
    db.session.add(ir1618)
    db.session.add(ir1619)
    db.session.add(ir1620)
    db.session.add(ir1621)
    db.session.add(ir1622)
    db.session.add(ir1623)
    db.session.add(ir1624)
    db.session.add(ir1625)
    db.session.add(ir1626)
    db.session.add(ir1627)
    db.session.add(ir1628)
    db.session.add(ir1629)
    db.session.add(ir1630)
    db.session.add(ir1631)
    db.session.add(ir1632)
    db.session.add(ir1633)
    db.session.add(ir1634)
    db.session.add(ir1635)
    db.session.add(ir1636)
    db.session.add(ir1637)
    db.session.add(ir1638)
    db.session.add(ir1639)
    db.session.add(ir1640)
    db.session.add(ir1641)
    db.session.add(ir1642)
    db.session.add(ir1643)
    db.session.add(ir1644)
    db.session.add(ir1645)
    db.session.add(ir1646)
    db.session.add(ir1647)
    db.session.add(ir1648)
    db.session.add(ir1649)
    db.session.add(ir1650)
    db.session.add(ir1651)
    db.session.add(ir1652)
    db.session.add(ir1653)
    db.session.add(ir1654)
    db.session.add(ir1655)
    db.session.add(ir1656)
    db.session.add(ir1657)
    db.session.add(ir1658)
    db.session.add(ir1659)
    db.session.add(ir1660)
    db.session.add(ir1661)
    db.session.add(ir1662)
    db.session.add(ir1663)
    db.session.add(ir1664)
    db.session.add(ir1665)
    db.session.add(ir1666)
    db.session.add(ir1667)
    db.session.add(ir1668)
    db.session.add(ir1669)
    db.session.add(ir1670)
    db.session.add(ir1671)
    db.session.add(ir1672)
    db.session.add(ir1673)
    db.session.add(ir1674)
    db.session.add(ir1675)
    db.session.add(ir1676)
    db.session.add(ir1677)
    db.session.add(ir1678)
    db.session.add(ir1679)
    db.session.add(ir1680)
    db.session.add(ir1681)
    db.session.add(ir1682)
    db.session.add(ir1683)
    db.session.add(ir1684)
    db.session.add(ir1685)
    db.session.add(ir1686)
    db.session.add(ir1687)
    db.session.add(ir1688)
    db.session.add(ir1689)
    db.session.add(ir1690)
    db.session.add(ir1691)
    db.session.add(ir1692)
    db.session.add(ir1693)
    db.session.add(ir1694)
    db.session.add(ir1695)
    db.session.add(ir1696)
    db.session.add(ir1697)
    db.session.add(ir1698)
    db.session.add(ir1699)
    db.session.add(ir1700)
    db.session.add(ir1701)
    db.session.add(ir1702)
    db.session.add(ir1703)
    db.session.add(ir1704)
    db.session.add(ir1705)
    db.session.add(ir1706)
    db.session.add(ir1707)
    db.session.add(ir1708)
    db.session.add(ir1709)
    db.session.add(ir1710)
    db.session.add(ir1711)
    db.session.add(ir1712)
    db.session.add(ir1713)
    db.session.add(ir1714)
    db.session.add(ir1715)
    db.session.add(ir1716)
    db.session.add(ir1717)
    db.session.add(ir1718)
    db.session.add(ir1719)
    db.session.add(ir1720)
    db.session.add(ir1721)
    db.session.add(ir1722)
    db.session.add(ir1723)
    db.session.add(ir1724)
    db.session.add(ir1725)
    db.session.add(ir1726)
    db.session.add(ir1727)
    db.session.add(ir1728)
    db.session.add(ir1729)
    db.session.add(ir1730)
    db.session.add(ir1731)
    db.session.add(ir1732)
    db.session.add(ir1733)
    db.session.add(ir1734)
    db.session.add(ir1735)
    db.session.add(ir1736)
    db.session.add(ir1737)
    db.session.add(ir1738)
    db.session.add(ir1739)
    db.session.add(ir1740)
    db.session.add(ir1741)
    db.session.add(ir1742)
    db.session.add(ir1743)
    db.session.add(ir1744)
    db.session.add(ir1745)
    db.session.add(ir1746)
    db.session.add(ir1747)
    db.session.add(ir1748)
    db.session.add(ir1749)
    db.session.add(ir1750)
    db.session.add(ir1751)
    db.session.add(ir1752)
    db.session.add(ir1753)
    db.session.add(ir1754)
    db.session.add(ir1755)
    db.session.add(ir1756)
    db.session.add(ir1757)
    db.session.add(ir1758)
    db.session.add(ir1759)
    db.session.add(ir1760)
    db.session.add(ir1761)
    db.session.add(ir1762)
    db.session.add(ir1763)
    db.session.add(ir1764)
    db.session.add(ir1765)
    db.session.add(ir1766)
    db.session.add(ir1767)
    db.session.add(ir1768)
    # db.session.add(ir1769)
    db.session.add(ir1770)
    db.session.add(ir1771)
    db.session.add(ir1772)
    db.session.add(ir1773)
    db.session.add(ir1774)
    db.session.add(ir1775)
    db.session.add(ir1776)
    db.session.add(ir1777)
    db.session.add(ir1778)
    db.session.add(ir1779)
    db.session.add(ir1780)
    db.session.add(ir1781)
    db.session.add(ir1782)
    db.session.add(ir1783)
    db.session.add(ir1784)
    db.session.add(ir1785)
    db.session.add(ir1786)
    db.session.add(ir1787)
    db.session.add(ir1788)
    db.session.add(ir1789)
    db.session.add(ir1790)
    db.session.add(ir1791)
    db.session.add(ir1792)
    db.session.add(ir1793)
    db.session.add(ir1794)
    db.session.add(ir1795)
    db.session.add(ir1796)
    db.session.add(ir1797)
    db.session.add(ir1798)
    db.session.add(ir1799)
    db.session.add(ir1800)
    db.session.add(ir1801)
    db.session.add(ir1802)
    db.session.add(ir1803)
    db.session.add(ir1804)
    db.session.add(ir1805)
    db.session.add(ir1806)
    db.session.add(ir1807)
    db.session.add(ir1808)
    db.session.add(ir1809)
    db.session.add(ir1810)
    db.session.add(ir1811)
    db.session.add(ir1812)
    db.session.add(ir1813)
    db.session.add(ir1814)
    db.session.add(ir1815)
    db.session.add(ir1816)
    db.session.add(ir1817)
    db.session.add(ir1818)
    db.session.add(ir1819)
    db.session.add(ir1820)
    db.session.add(ir1821)
    db.session.add(ir1822)
    db.session.add(ir1823)
    db.session.add(ir1824)
    db.session.add(ir1825)
    db.session.add(ir1826)
    db.session.add(ir1827)
    db.session.add(ir1828)
    db.session.add(ir1829)
    db.session.add(ir1830)
    db.session.add(ir1831)
    db.session.add(ir1832)
    db.session.add(ir1833)
    db.session.add(ir1834)
    db.session.add(ir1835)
    db.session.add(ir1836)
    db.session.add(ir1837)
    db.session.add(ir1838)
    db.session.add(ir1839)
    db.session.add(ir1840)
    db.session.add(ir1841)
    db.session.add(ir1842)
    db.session.add(ir1843)
    db.session.add(ir1844)
    db.session.add(ir1845)
    db.session.add(ir1846)
    db.session.add(ir1847)
    db.session.add(ir1848)
    db.session.add(ir1849)
    db.session.add(ir1850)
    db.session.add(ir1851)
    db.session.add(ir1852)
    db.session.add(ir1853)
    db.session.add(ir1854)
    db.session.add(ir1855)
    db.session.add(ir1856)
    db.session.add(ir1857)
    db.session.add(ir1858)
    db.session.add(ir1859)
    db.session.add(ir1860)
    db.session.add(ir1861)
    db.session.add(ir1862)
    db.session.add(ir1863)
    db.session.add(ir1864)
    db.session.add(ir1865)
    db.session.add(ir1866)
    db.session.add(ir1867)
    db.session.add(ir1868)
    db.session.add(ir1869)
    db.session.add(ir1870)
    db.session.add(ir1871)
    db.session.add(ir1872)
    db.session.add(ir1873)
    db.session.add(ir1874)
    db.session.add(ir1875)
    db.session.add(ir1876)
    db.session.add(ir1877)
    db.session.add(ir1878)
    db.session.add(ir1879)
    db.session.add(ir1880)
    db.session.add(ir1881)
    db.session.add(ir1882)
    db.session.add(ir1883)
    db.session.add(ir1884)
    db.session.add(ir1885)
    db.session.add(ir1886)
    db.session.add(ir1887)
    db.session.add(ir1888)
    db.session.add(ir1889)
    db.session.add(ir1890)
    db.session.add(ir1891)
    db.session.add(ir1892)
    db.session.add(ir1893)
    db.session.add(ir1894)
    db.session.add(ir1895)
    db.session.add(ir1896)
    db.session.add(ir1897)
    db.session.add(ir1898)
    db.session.add(ir1899)
    db.session.add(ir1900)
    db.session.add(ir1901)
    db.session.add(ir1902)
    db.session.add(ir1903)
    db.session.add(ir1904)
    db.session.add(ir1905)
    db.session.add(ir1906)
    db.session.add(ir1907)
    db.session.add(ir1908)
    db.session.add(ir1909)
    db.session.add(ir1910)
    db.session.add(ir1911)
    db.session.add(ir1912)
    db.session.add(ir1913)
    db.session.add(ir1914)
    db.session.add(ir1915)
    db.session.add(ir1916)
    db.session.add(ir1917)
    db.session.add(ir1918)
    db.session.add(ir1919)
    db.session.add(ir1920)
    db.session.add(ir1921)
    db.session.add(ir1922)
    db.session.add(ir1923)
    db.session.add(ir1924)
    db.session.add(ir1925)
    db.session.add(ir1926)
    db.session.add(ir1927)
    db.session.add(ir1928)
    db.session.add(ir1929)
    db.session.add(ir1930)
    db.session.add(ir1931)
    db.session.add(ir1932)
    db.session.add(ir1933)
    db.session.add(ir1934)
    db.session.add(ir1935)
    db.session.add(ir1936)
    db.session.add(ir1937)
    db.session.add(ir1938)
    db.session.add(ir1939)
    db.session.add(ir1940)
    db.session.add(ir1941)
    db.session.add(ir1942)
    db.session.add(ir1943)
    db.session.add(ir1944)
    db.session.add(ir1945)
    db.session.add(ir1946)
    db.session.add(ir1947)
    db.session.add(ir1948)
    db.session.add(ir1949)
    db.session.add(ir1950)
    db.session.add(ir1951)
    db.session.add(ir1952)
    db.session.add(ir1953)
    db.session.add(ir1954)
    db.session.add(ir1955)
    db.session.add(ir1956)
    db.session.add(ir1957)
    db.session.add(ir1958)
    db.session.add(ir1959)
    db.session.add(ir1960)
    db.session.add(ir1961)
    db.session.add(ir1962)
    db.session.add(ir1963)
    db.session.add(ir1964)
    db.session.add(ir1965)
    db.session.add(ir1966)
    db.session.add(ir1967)
    db.session.add(ir1968)
    db.session.add(ir1969)
    db.session.add(ir1970)
    db.session.add(ir1971)
    db.session.add(ir1972)
    db.session.add(ir1973)
    db.session.add(ir1974)
    db.session.add(ir1975)
    db.session.add(ir1976)
    db.session.add(ir1977)
    db.session.add(ir1978)
    db.session.add(ir1979)
    db.session.add(ir1980)
    db.session.add(ir1981)
    db.session.add(ir1982)
    db.session.add(ir1983)
    db.session.add(ir1984)
    db.session.add(ir1985)
    db.session.add(ir1986)
    db.session.add(ir1987)
    db.session.add(ir1988)
    db.session.add(ir1989)
    db.session.add(ir1990)
    db.session.add(ir1991)
    db.session.add(ir1992)
    db.session.add(ir1993)
    db.session.add(ir1994)
    db.session.add(ir1995)
    db.session.add(ir1996)
    db.session.add(ir1997)
    db.session.add(ir1998)
    db.session.add(ir1999)
    db.session.add(ir2000)
    db.session.add(ir2001)
    db.session.add(ir2002)
    db.session.add(ir2003)
    db.session.add(ir2004)
    db.session.add(ir2005)
    db.session.add(ir2006)
    db.session.add(ir2007)
    db.session.add(ir2008)
    db.session.add(ir2009)
    db.session.add(ir2010)
    db.session.add(ir2011)
    db.session.add(ir2012)
    db.session.add(ir2013)
    db.session.add(ir2014)
    db.session.add(ir2015)
    db.session.add(ir2016)
    db.session.add(ir2017)
    db.session.add(ir2018)
    db.session.add(ir2019)
    db.session.add(ir2020)
    db.session.add(ir2021)
    db.session.add(ir2022)
    db.session.add(ir2023)
    db.session.add(ir2024)
    db.session.add(ir2025)
    db.session.add(ir2026)
    db.session.add(ir2027)
    db.session.add(ir2028)
    db.session.add(ir2029)
    db.session.add(ir2030)
    db.session.add(ir2031)
    db.session.add(ir2032)
    db.session.add(ir2033)
    db.session.add(ir2034)
    db.session.add(ir2035)
    db.session.add(ir2036)
    db.session.add(ir2037)
    db.session.add(ir2038)
    db.session.add(ir2039)
    db.session.add(ir2040)
    db.session.add(ir2041)
    db.session.add(ir2042)
    db.session.add(ir2043)
    db.session.add(ir2044)
    db.session.add(ir2045)
    db.session.add(ir2046)
    db.session.add(ir2047)
    db.session.add(ir2048)
    db.session.add(ir2049)
    db.session.add(ir2050)
    db.session.add(ir2051)
    db.session.add(ir2052)
    db.session.add(ir2053)
    db.session.add(ir2054)
    db.session.add(ir2055)
    db.session.add(ir2056)
    db.session.add(ir2057)
    db.session.add(ir2058)
    db.session.add(ir2059)
    db.session.add(ir2060)
    db.session.add(ir2061)
    db.session.add(ir2062)
    db.session.add(ir2063)
    db.session.add(ir2064)
    db.session.add(ir2065)
    db.session.add(ir2066)
    db.session.add(ir2067)
    db.session.add(ir2068)
    db.session.add(ir2069)
    db.session.add(ir2070)
    db.session.add(ir2071)
    db.session.add(ir2072)
    db.session.add(ir2073)
    db.session.add(ir2074)
    db.session.add(ir2075)
    db.session.add(ir2076)
    db.session.add(ir2077)
    db.session.add(ir2078)
    db.session.add(ir2079)
    db.session.add(ir2080)
    db.session.add(ir2081)
    db.session.add(ir2082)
    db.session.add(ir2083)
    db.session.add(ir2084)
    db.session.add(ir2085)
    db.session.add(ir2086)
    db.session.add(ir2087)
    db.session.add(ir2088)
    db.session.add(ir2089)
    db.session.add(ir2090)
    # db.session.add(ir2091)
    # db.session.add(ir2092)
    db.session.add(ir2093)
    db.session.add(ir2094)
    db.session.add(ir2095)
    db.session.add(ir2096)
    db.session.add(ir2097)
    db.session.add(ir2098)
    db.session.add(ir2099)
    db.session.add(ir2100)
    db.session.add(ir2101)
    db.session.add(ir2102)
    db.session.add(ir2103)
    db.session.add(ir2104)
    db.session.add(ir2105)
    db.session.add(ir2106)
    db.session.add(ir2107)
    db.session.add(ir2108)
    db.session.add(ir2109)
    db.session.add(ir2110)
    db.session.add(ir2111)
    db.session.add(ir2112)
    db.session.add(ir2113)
    db.session.add(ir2114)
    db.session.add(ir2115)
    db.session.add(ir2116)
    db.session.add(ir2117)
    db.session.add(ir2118)
    db.session.add(ir2119)
    db.session.add(ir2120)
    db.session.add(ir2121)
    db.session.add(ir2122)
    db.session.add(ir2123)
    db.session.add(ir2124)
    db.session.add(ir2125)
    db.session.add(ir2126)
    db.session.add(ir2127)
    db.session.add(ir2128)
    db.session.add(ir2129)
    db.session.add(ir2130)
    db.session.add(ir2131)
    db.session.add(ir2132)
    db.session.add(ir2133)
    db.session.add(ir2134)
    db.session.add(ir2135)
    db.session.add(ir2136)
    db.session.add(ir2137)
    db.session.add(ir2138)
    db.session.add(ir2139)
    db.session.add(ir2140)
    # db.session.add(ir2141)
    db.session.add(ir2142)
    db.session.add(ir2143)
    db.session.add(ir2144)
    db.session.add(ir2145)
    db.session.add(ir2146)
    db.session.add(ir2147)
    db.session.add(ir2148)
    db.session.add(ir2149)
    db.session.add(ir2150)
    db.session.add(ir2151)
    db.session.add(ir2152)
    db.session.add(ir2153)
    db.session.add(ir2154)
    db.session.add(ir2155)
    db.session.add(ir2156)
    db.session.add(ir2157)
    db.session.add(ir2158)
    db.session.add(ir2159)
    db.session.add(ir2160)
    db.session.add(ir2161)
    db.session.add(ir2162)
    db.session.add(ir2163)
    db.session.add(ir2164)
    db.session.add(ir2165)
    db.session.add(ir2166)
    db.session.add(ir2167)
    db.session.add(ir2168)
    db.session.add(ir2169)
    db.session.add(ir2170)
    db.session.add(ir2171)
    db.session.add(ir2172)
    db.session.add(ir2173)
    db.session.add(ir2174)
    db.session.add(ir2175)
    db.session.add(ir2176)
    db.session.add(ir2177)
    db.session.add(ir2178)
    db.session.add(ir2179)
    db.session.add(ir2180)
    db.session.add(ir2181)
    db.session.add(ir2182)
    db.session.add(ir2183)
    db.session.add(ir2184)
    db.session.add(ir2185)
    db.session.add(ir2186)
    db.session.add(ir2187)
    db.session.add(ir2188)
    db.session.add(ir2189)
    db.session.add(ir2190)
    db.session.add(ir2191)
    db.session.add(ir2192)
    db.session.add(ir2193)
    db.session.add(ir2194)
    db.session.add(ir2195)
    db.session.add(ir2196)
    db.session.add(ir2197)
    db.session.add(ir2198)
    db.session.add(ir2199)
    db.session.add(ir2200)
    db.session.add(ir2201)
    db.session.add(ir2202)
    db.session.add(ir2203)
    db.session.add(ir2204)
    db.session.add(ir2205)
    db.session.add(ir2206)
    db.session.add(ir2207)
    db.session.add(ir2208)
    db.session.add(ir2209)
    db.session.add(ir2210)
    db.session.add(ir2211)
    db.session.add(ir2212)
    db.session.add(ir2213)
    db.session.add(ir2214)
    db.session.add(ir2215)
    db.session.add(ir2216)
    db.session.add(ir2217)
    db.session.add(ir2218)
    db.session.add(ir2219)
    db.session.add(ir2220)
    db.session.add(ir2221)
    db.session.add(ir2222)
    db.session.add(ir2223)
    db.session.add(ir2224)
    db.session.add(ir2225)
    db.session.add(ir2226)
    db.session.add(ir2227)
    db.session.add(ir2228)
    db.session.add(ir2229)
    db.session.add(ir2230)
    db.session.add(ir2231)
    db.session.add(ir2232)
    db.session.add(ir2233)
    db.session.add(ir2234)
    db.session.add(ir2235)
    db.session.add(ir2236)
    db.session.add(ir2237)
    db.session.add(ir2238)
    db.session.add(ir2239)
    db.session.add(ir2240)
    db.session.add(ir2241)
    db.session.add(ir2242)
    db.session.add(ir2243)
    db.session.add(ir2244)
    db.session.add(ir2245)
    db.session.add(ir2246)
    db.session.add(ir2247)
    db.session.add(ir2248)
    db.session.add(ir2249)
    db.session.add(ir2250)
    db.session.add(ir2251)
    db.session.add(ir2252)
    db.session.add(ir2253)
    db.session.add(ir2254)
    db.session.add(ir2255)
    db.session.add(ir2256)
    db.session.add(ir2257)
    db.session.add(ir2258)
    db.session.add(ir2259)
    db.session.add(ir2260)
    db.session.add(ir2261)
    db.session.add(ir2262)
    db.session.add(ir2263)
    db.session.add(ir2264)
    db.session.add(ir2265)
    db.session.add(ir2266)
    db.session.add(ir2267)
    db.session.add(ir2268)
    db.session.add(ir2269)
    db.session.add(ir2270)
    db.session.add(ir2271)
    db.session.add(ir2272)
    db.session.add(ir2273)
    db.session.add(ir2274)
    # db.session.add(ir2275)
    db.session.add(ir2276)
    db.session.add(ir2277)
    db.session.add(ir2278)
    db.session.add(ir2279)
    db.session.add(ir2280)
    db.session.add(ir2281)
    db.session.add(ir2282)
    db.session.add(ir2283)
    db.session.add(ir2284)
    db.session.add(ir2285)
    db.session.add(ir2286)
    db.session.add(ir2287)
    db.session.add(ir2288)
    db.session.add(ir2289)
    db.session.add(ir2290)
    db.session.add(ir2291)
    db.session.add(ir2292)
    db.session.add(ir2293)
    db.session.add(ir2294)
    db.session.add(ir2295)
    db.session.add(ir2296)
    db.session.add(ir2297)
    db.session.add(ir2298)
    db.session.add(ir2299)
    db.session.add(ir2300)
    db.session.add(ir2301)
    db.session.add(ir2302)
    db.session.add(ir2303)
    db.session.add(ir2304)
    db.session.add(ir2305)
    db.session.add(ir2306)
    db.session.add(ir2307)
    db.session.add(ir2309)
    db.session.add(ir2310)
    db.session.add(ir2311)
    db.session.add(ir2312)
    db.session.add(ir2313)
    db.session.add(ir2314)
    db.session.add(ir2315)
    db.session.add(ir2316)
    db.session.add(ir2317)
    db.session.add(ir2318)
    db.session.add(ir2319)
    db.session.add(ir2320)
    db.session.add(ir2321)
    db.session.add(ir2322)
    db.session.add(ir2323)
    db.session.add(ir2324)
    db.session.add(ir2325)
    db.session.add(ir2326)
    db.session.add(ir2327)
    db.session.add(ir2328)
    db.session.add(ir2329)
    db.session.add(ir2330)
    db.session.add(ir2331)
    db.session.add(ir2332)
    db.session.add(ir2333)
    db.session.add(ir2334)
    db.session.add(ir2335)
    db.session.add(ir2336)
    db.session.add(ir2337)
    db.session.add(ir2338)


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
