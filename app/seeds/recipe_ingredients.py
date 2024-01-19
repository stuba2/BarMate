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


    gin = RecipeIngredient(
            amount=0.75,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    grandmarnier = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    amaretto = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'ABC').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'ABC').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    cognac = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'ABC').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    heavycream = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    milk = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='fresh',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg White').first().id
        )
    proofrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'ACID').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    wildturkey = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'ACID').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wild Turkey').first().id
        )
    darkrum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    absolutvodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'AT&T').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'AT&T').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    tonicwater = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'AT&T').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic water').first().id
        )
    applejack = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A. J.').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Applejack').first().id
        )
    grapefruitjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A. J.').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    strawberryschnapps = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affair').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberry schnapps').first().id
        )
    orangejuice = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affair').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affair').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    orangejuice = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    grapefruitjuice = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    applejuice = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    vodka = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    pisangambon = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pisang Ambon').first().id
        )
    applejuice = RecipeIngredient(
            amount=6,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=0.5,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    darkrum = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abilene').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    peachnectar = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abilene').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach nectar').first().id
        )
    orangejuice = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abilene').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    gin = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    vermouth = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vermouth').first().id
        )
    darkrum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almeria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almeria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almeria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    lightrum = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    triplesec = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    mint = RecipeIngredient(
            amount=1,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    scotch = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    orangebitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    applejack = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Applejack').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    gin = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aviation').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aviation').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon juice').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aviation').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'maraschino liqueur').first().id
        )
    rum = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    tequila = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    salt = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addington').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addington').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    sodawater = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addington').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'After sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    cremedebanane = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'After sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Banane').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afterglow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    orangejuice = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afterglow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afterglow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    frangelico = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Frangelico').first().id
        )
    coffee = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    gin = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    lightcream = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    blendedwhiskey = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Algonquin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Algonquin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Algonquin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    bourbon = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    blackberrybrandy = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberry brandy').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    campari = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    orangepeel = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    jackdaniels = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applejack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jack Daniels').first().id
        )
    midorimelonliqueur = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applejack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    sourmix = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applejack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    bitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    vodka = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autodafé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autodafé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    crownroyal = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalanche').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Crown Royal').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalanche').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    cream = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalanche').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    cognac = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    cremedecassis = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    freshlemonjuice = RecipeIngredient(
            amount=0.125,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lemon Juice').first().id
        )
    amaretto = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Joy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Joy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    lightcream = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Joy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    apricotbrandy = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angel Face').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    applebrandy = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angel Face').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple brandy').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angel Face').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    hpnotiq = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aquamarine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hpnotiq').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aquamarine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    bananaliqueur = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aquamarine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana Liqueur').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    wine = RecipeIngredient(
            amount=1,
            unit='oz green ginger',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    benedictine = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    sugar = RecipeIngredient(
            amount=50,
            unit='gr',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    anise = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anise').first().id
        )
    licoriceroot = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Licorice root').first().id
        )
    wormwood = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wormwood').first().id
        )
    absolutkurant = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Kurant').first().id
        )
    midorimelonliqueur = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    sprite = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    vodka = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    grapesoda = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grape soda').first().id
        )
    orangejuice = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    candy = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Candy').first().id
        )
    lemonade = RecipeIngredient(
            amount=1,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    vodka = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    rum = RecipeIngredient(
            amount=7,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    gingerale = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    vodka = RecipeIngredient(
            amount=0.5,
            unit='blender',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    lemonade = RecipeIngredient(
            amount=0.5,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    water = RecipeIngredient(
            amount=0.5,
            unit='blender',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    sugar = RecipeIngredient(
            amount=10,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    tea = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    amaretto = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    whippedcream = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped cream').first().id
        )
    tequila = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Grande').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    applecider = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Grande').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple cider').first().id
        )
    applejuice = RecipeIngredient(
            amount=2,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Karate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    carrot = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Karate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Carrot').first().id
        )
    lightrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    apricotbrandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    vodka = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    gin = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    limejuicecordial = RecipeIngredient(
            amount=45,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice cordial').first().id
        )
    ice = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    southerncomfort = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    passionfruitsyrup = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit syrup').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    clubsoda = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    amaretto = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    orangejuice = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    whitewine = RecipeIngredient(
            amount=15,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Wine').first().id
        )
    orangepeel = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    amaretto = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Mist').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Mist').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    amaretto = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    limejuice = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    amaretto = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    sourmix = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    aperol = RecipeIngredient(
            amount=100,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aperol Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Aperol').first().id
        )
    prosecco = RecipeIngredient(
            amount=150,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aperol Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    sodawater = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aperol Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    up = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '7-Up').first().id
        )
    appleschnapps = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple schnapps').first().id
        )
    apricotbrandy = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    champagne = RecipeIngredient(
            amount=4,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    up = RecipeIngredient(
            amount=4,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '7-Up').first().id
        )
    orangejuice = RecipeIngredient(
            amount=0.5,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    champagne = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arise My Love').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    greencremedementhe = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arise My Love').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Creme de Menthe').first().id
        )
    lemonade = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    triplesec = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Piece of Ass').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    southerncomfort = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Piece of Ass').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Piece of Ass').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    orangebitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    orange = RecipeIngredient(
            amount=0.25,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    lemonvodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alfie Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon vodka').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alfie Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alfie Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    cream = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    chocolateicecream = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate ice-cream').first().id
        )
    brandy = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    amaretto = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    appleschnapps = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple Schnapps').first().id
        )
    cognac = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    ginger = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adonis Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    sherry = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adonis Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    orangebitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adonis Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    southerncomfort = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    sloegin = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    orangebitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    yellowchartreuse = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yellow Chartreuse').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allies Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allies Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    kummel = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allies Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kummel').first().id
        )
    triplesec = RecipeIngredient(
            amount=0.5,
            unit='jigger',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    amaretto = RecipeIngredient(
            amount=3,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    cider = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    ice = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    maliburum = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    goldtequila = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gold tequila').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    creamofcoconut = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream of coconut').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    pineapple = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    grandmarnier = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    tea = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    ryewhiskey = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rye whiskey').first().id
        )
    redwine = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    rum = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    brandy = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    benedictine = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    sodawater = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    midorimelonliqueur = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    cremedebanane = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Banane').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    water = RecipeIngredient(
            amount=0.75,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    apricot = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot').first().id
        )
    almondflavoring = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Almond flavoring').first().id
        )
    grainalcohol = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grain alcohol').first().id
        )
    water = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    brandy = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    foodcoloring = RecipeIngredient(
            amount=3,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    foodcoloring = RecipeIngredient(
            amount=6,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    foodcoloring = RecipeIngredient(
            amount=2,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    glycerine = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Glycerine').first().id
        )
    amaretto = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    whitecremedementhe = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    orangejuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=0.25,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    angelicaroot = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angelica root').first().id
        )
    almond = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Almond').first().id
        )
    allspice = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Allspice').first().id
        )
    cinnamon = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    anise = RecipeIngredient(
            amount=3,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anise').first().id
        )
    coriander = RecipeIngredient(
            amount=0.125,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coriander').first().id
        )
    marjoramleaves = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Marjoram leaves').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    sugar = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    water = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    foodcoloring = RecipeIngredient(
            amount=1,
            unit='drop',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    foodcoloring = RecipeIngredient(
            amount=1,
            unit='drop',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    maui = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Mouthwash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maui').first().id
        )
    mountaindew = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Mouthwash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mountain Dew').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Mouthwash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    absolutvodka = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Stingers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    icedtea = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Stingers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Iced tea').first().id
        )
    campari = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    orangejuice = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    gingerbeer = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger Beer').first().id
        )
    orangepeel = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    absolutcitron = RecipeIngredient(
            amount=0.67,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Evergreen').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    pisangambon = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Evergreen').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pisang Ambon').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Evergreen').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    absolutcitron = RecipeIngredient(
            amount=0.67,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    limejuice = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    tonicwater = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic water').first().id
        )
    absolutvodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    coconutliqueur = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut liqueur').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    water = RecipeIngredient(
            amount=0.75,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ginger = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    guavajuice = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guava juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1.5,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    pineapple = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    applecider = RecipeIngredient(
            amount=4,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple cider').first().id
        )
    brownsugar = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brown sugar').first().id
        )
    lemonade = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    orangejuice = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    cloves = RecipeIngredient(
            amount=6,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    allspice = RecipeIngredient(
            amount=6,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Allspice').first().id
        )
    nutmeg = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    cinnamon = RecipeIngredient(
            amount=3,
            unit='sticks',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    jägermeister = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Auburn Headbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    goldschlager = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Auburn Headbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    coconutrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut rum').first().id
        )
    amaretto = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    orangejuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    lightrum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Furlong Too Late').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    gingerbeer = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Furlong Too Late').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger beer').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Furlong Too Late').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    absolutcitron = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    sprite = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    sodawater = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    amaretto = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto And Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    lightcream = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto And Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    vodka = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Antifreeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    midorimelonliqueur = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Antifreeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Antifreeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan's Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan's Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    orangejuice = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan's Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan's Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Fabulous').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Fabulous').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry Juice').first().id
        )
    champagne = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Fabulous').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice in Wonderland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    grandmarnier = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice in Wonderland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    southerncomfort = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice in Wonderland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    sourmix = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='jigger',
            recipe_id=Recipe.query.filter(Recipe.name == 'A True Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    lemon = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'A True Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    absolutcitron = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    gingerale = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    berries = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Berry Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Berries').first().id
        )
    apple = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Berry Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple').first().id
        )
    rum = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    cognac = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    gin = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    freshlimejuice = RecipeIngredient(
            amount=0.25,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lime Juice').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=0.25,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    water = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    apricotbrandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Supper Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    apricotbrandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Supper Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Supper Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    kirschwasser = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kirschwasser').first().id
        )
    strawberryliqueur = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberry liqueur').first().id
        )
    strawberries = RecipeIngredient(
            amount=5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    applejuice = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Pie with A Crust').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    maliburum = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Pie with A Crust').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    cinnamon = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Pie with A Crust').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    añejorum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Añejo rum').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    gingerale = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    amaretto = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Chocolate Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    darkcremedecacao = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Chocolate Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Creme de Cacao').first().id
        )
    coffee = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Chocolate Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    whitecremedementhe = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    southerncomfort = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    vodka = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    hotchocolate = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot chocolate').first().id
        )
    absolutvodka = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    gingerale = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    sourmix = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    amaretto = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    tequila = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-52').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    grandmarnier = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-52').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    kahlua = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-52').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    kahlua = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-53').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    sambuca = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-53').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    grandmarnier = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-53').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    orangebitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Bitters').first().id
        )
    greenchartreuse = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    irishcream = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Big Red').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish cream').first().id
        )
    goldschlager = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Big Red').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    champagne = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    gin = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon juice').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    cremedemure = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Mure').first().id
        )
    scotch = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    bitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    bitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ryewhiskey = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rye Whiskey').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Liqueur').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Cherry').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    passionfruitjuice = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    bitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    rum = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    galliano = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    limejuice = RecipeIngredient(
            amount=0,
            unit='1 dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    prosecco = RecipeIngredient(
            amount=NaN,
            unit='up',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    hotchocolate = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brigadier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot Chocolate').first().id
        )
    greenchartreuse = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brigadier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    cherryheering = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brigadier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry Heering').first().id
        )
    151proofrum = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    scotch = RecipeIngredient(
            amount=NaN,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    bitters = RecipeIngredient(
            amount=3,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    wormwood = RecipeIngredient(
            amount=1,
            unit='fresh',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wormwood').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    corona = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Buccaneer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Corona').first().id
        )
    bacardilimon = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Buccaneer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bacardi Limon').first().id
        )
    everclear = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Everclear').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='fifth smirnoff red label',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    mountaindew = RecipeIngredient(
            amount=2,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mountain Dew').first().id
        )
    surge = RecipeIngredient(
            amount=2,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Surge').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='small bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    rum = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blackthorn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    sloegin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blackthorn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blackthorn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    midorimelonliqueur = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bob Marley').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    jägermeister = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bob Marley').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    goldschlager = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bob Marley').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    southerncomfort = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lime = RecipeIngredient(
            amount=2,
            unit='wedges',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    sourmix = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    bananaliqueur = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana liqueur').first().id
        )
    orangejuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bumble Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    kahlua = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bumble Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    sambuca = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bumble Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    kahlua = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Eskimo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    milk = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Eskimo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    vanillaicecream = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Eskimo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla ice-cream').first().id
        )
    blendedwhiskey = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    rum = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    darkrum = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    bananaliqueur = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana liqueur').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    orangejuice = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and Sour').first().id
        )
    sambuca = RecipeIngredient(
            amount=30,
            unit='ml white',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brainteaser').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    erincream = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brainteaser').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Erin Cream').first().id
        )
    advocaat = RecipeIngredient(
            amount=5,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brainteaser').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Advocaat').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    tomatojuice = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    worcestershiresauce = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Worcestershire sauce').first().id
        )
    tabascosauce = RecipeIngredient(
            amount=NaN,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ale = RecipeIngredient(
            amount=1,
            unit='part bass pale',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black & Tan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ale').first().id
        )
    guinnessstout = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black & Tan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guinness stout').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Lagoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Lagoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    goldrum = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee's Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gold rum').first().id
        )
    orangejuice = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee's Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    limejuice = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee's Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    triplesec = RecipeIngredient(
            amount=2,
            unit='jiggers',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee's Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    brandy = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    egg = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    lightcream = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    nutmeg = RecipeIngredient(
            amount=NaN,
            unit='tsp grated',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    brandy = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    vanillaicecream = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla Ice-Cream').first().id
        )
    butterscotchschnapps = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butterscotch schnapps').first().id
        )
    milk = RecipeIngredient(
            amount=NaN,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    campari = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ryewhiskey = RecipeIngredient(
            amount=1,
            unit='1/4 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rye whiskey').first().id
        )
    orangepeel = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    bourbon = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    coconutliqueur = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut liqueur').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    sprite = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    vodka = RecipeIngredient(
            amount=10,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    strawberries = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    limejuice = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    lemonlimesoda = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    lemonlimesoda = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    raisins = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raisins').first().id
        )
    blueberries = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blueberries').first().id
        )
    everclear = RecipeIngredient(
            amount=2,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Everclear').first().id
        )
    wine = RecipeIngredient(
            amount=1,
            unit='bottle boone strawberry hill',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    orangejuice = RecipeIngredient(
            amount=NaN,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    koolaid = RecipeIngredient(
            amount=1,
            unit='gal tropical berry',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kool-Aid').first().id
        )
    tequila = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    tomatojuice = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    tabascosauce = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    celerysalt = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Celery salt').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    godivaliqueur = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Godiva liqueur').first().id
        )
    kahlua = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    butterscotchschnapps = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butterscotch schnapps').first().id
        )
    milk = RecipeIngredient(
            amount=0,
            unit='to fill
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    añejorum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Añejo rum').first().id
        )
    tiamaria = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tia maria').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    rum = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    coconutliqueur = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut Liqueur').first().id
        )
    blueberries = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blueberries').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    prosecco = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    gin = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    cremedecassis = RecipeIngredient(
            amount=20,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    freshlimejuice = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lime Juice').first().id
        )
    gingerbeer = RecipeIngredient(
            amount=75,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger beer').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ginger = RecipeIngredient(
            amount=1,
            unit='long strip',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    water = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    bourbon = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    chambordraspberryliqueur = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    peachtreeschnapps = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peachtree schnapps').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    coffeeliqueur = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee liqueur').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    kahlua = RecipeIngredient(
            amount=2,
            unit='1/2 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Guinness').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Guinness').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    clubsoda = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    brandy = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    rum = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    darkrum = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    passoa = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passoa').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=6,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and Sour').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    lightrum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    brandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    tequila = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    salt = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    maliburum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cream Pi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu Rum').first().id
        )
    bananaliqueur = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cream Pi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana Liqueur').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cream Pi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    lightrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    banana = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    limejuice = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ice = RecipeIngredient(
            amount=8,
            unit='cubes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    vodka = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    peachnectar = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach nectar').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    guinnessstout = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black and Brown').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guinness stout').first().id
        )
    rootbeer = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black and Brown').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Root beer').first().id
        )
    brandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=1,
            unit='oz white',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    lightcream = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='3/4 oz bacardi',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    darkrum = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    surge = RecipeIngredient(
            amount=NaN,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Surge').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=NaN,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    darkrum = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    blueberries = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blueberries').first().id
        )
    lemonlimesoda = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    brandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bermuda Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    gin = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bermuda Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bermuda Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    raspberryvodka = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry Vodka').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry Juice').first().id
        )
    lemonade = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=10,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=10,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    limejuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    mint = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    milk = RecipeIngredient(
            amount=10,
            unit='cl cold',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    orangejuice = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    banana = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    tequila = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brave Bull Shooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    tabascosauce = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brave Bull Shooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black Forest Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    brandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bailey's Dream Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    vanillaicecream = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bailey's Dream Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla ice-cream').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    scotch = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    benedictine = RecipeIngredient(
            amount=1,
            unit='1/4 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    strawberries = RecipeIngredient(
            amount=NaN,
            unit='lb frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    banana = RecipeIngredient(
            amount=1,
            unit='frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    yoghurt = RecipeIngredient(
            amount=1,
            unit='cup plain',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    milk = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    honey = RecipeIngredient(
            amount=0,
            unit='to taste
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    vanillaicecream = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla Ice-Cream').first().id
        )
    milk = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    godivaliqueur = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Godiva liqueur').first().id
        )
    whippedcream = RecipeIngredient(
            amount=NaN,
            unit='topping',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped Cream').first().id
        )
    caramelsauce = RecipeIngredient(
            amount=4,
            unit='tablespoons
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'caramel sauce').first().id
        )
    chocolatesauce = RecipeIngredient(
            amount=4,
            unit='tablespoons
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'chocolate sauce').first().id
        )
    minisnickersbars = RecipeIngredient(
            amount=15,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mini-snickers bars').first().id
        )
    cantaloupe = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cantaloupe Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cantaloupe').first().id
        )
    banana = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cantaloupe Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    vanillaicecream = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandon and Will's Coke Float').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla ice-cream').first().id
        )
    cocacola = RecipeIngredient(
            amount=1,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandon and Will's Coke Float').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    bourbon = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandon and Will's Coke Float').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    strawberries = RecipeIngredient(
            amount=NaN,
            unit='lb frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    banana = RecipeIngredient(
            amount=1,
            unit='frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    applejuice = RecipeIngredient(
            amount=2,
            unit='cups fresh',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    orangebitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    milk = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cafe Savoy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cafe Savoy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    sugar = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    cachaca = RecipeIngredient(
            amount=2,
            unit='1/2 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cachaca').first().id
        )
    spicedrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cream Soda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Spiced rum').first().id
        )
    darkrum = RecipeIngredient(
            amount=NaN,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    cocacola = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='1/4 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Rum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    cherrybrandy = RecipeIngredient(
            amount=1,
            unit='1/2 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Rum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    lightcream = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Rum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    lightrum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libre').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libre').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    falernum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Falernum').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    añejorum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Añejo rum').first().id
        )
    blackstraprum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'blackstrap rum').first().id
        )
    bacardilimon = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Citrus Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bacardi Limon').first().id
        )
    cocacola = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Citrus Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    lightrum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='1/2 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='1/2 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=1,
            unit='1/2 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    grenadine = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    lime = RecipeIngredient(
            amount=2,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    sugar = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    whiterum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White rum').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    brandy = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'City Slicker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'City Slicker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'City Slicker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    lager = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Campari Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    campari = RecipeIngredient(
            amount=1,
            unit='1/2 cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Campari Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    port = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Port').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='1/4 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    limejuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    cointreau = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    water = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    sugar = RecipeIngredient(
            amount=2,
            unit='cups white',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    coffee = RecipeIngredient(
            amount=NaN,
            unit='cup instant',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    vanilla = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    orangebitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    eggyolk = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg yolk').first().id
        )
    gin = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    lilletblanc = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lillet Blanc').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    absinthe = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absinthe').first().id
        )
    chocolateliqueur = RecipeIngredient(
            amount=NaN,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate liqueur').first().id
        )
    milk = RecipeIngredient(
            amount=NaN,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clove Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    sloegin = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clove Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    wine = RecipeIngredient(
            amount=NaN,
            unit='oz muscatel',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clove Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    coffee = RecipeIngredient(
            amount=10,
            unit='tbsp instant',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=4,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    sugar = RecipeIngredient(
            amount=2,
            unit='1/2 cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    water = RecipeIngredient(
            amount=2,
            unit='1/2 cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    cocacola = RecipeIngredient(
            amount=1,
            unit='dl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coke and Drops').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=7,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coke and Drops').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    chocolate = RecipeIngredient(
            amount=125,
            unit='gr',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    milk = RecipeIngredient(
            amount=NaN,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=4,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    sugar = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=4,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    almondflavoring = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Almond flavoring').first().id
        )
    gingerale = RecipeIngredient(
            amount=2,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    sugar = RecipeIngredient(
            amount=8,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    water = RecipeIngredient(
            amount=6,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    grainalcohol = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grain alcohol').first().id
        )
    peppermintextract = RecipeIngredient(
            amount=1,
            unit='oz pure',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peppermint extract').first().id
        )
    foodcoloring = RecipeIngredient(
            amount=1,
            unit='tbsp green',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    bananaliqueur = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana liqueur').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    chocolateicecream = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate ice-cream').first().id
        )
    chocolatesyrup = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate syrup').first().id
        )
    chocolatemilk = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate milk').first().id
        )
    whippedcream = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped cream').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    banana = RecipeIngredient(
            amount=1,
            unit='piece',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    cranberries = RecipeIngredient(
            amount=NaN,
            unit='kg chopped',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Cordial').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberries').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Cordial').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    lightrum = RecipeIngredient(
            amount=NaN,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Cordial').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    milk = RecipeIngredient(
            amount=6,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    chocolate = RecipeIngredient(
            amount=3,
            unit='oz mexican',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    cinnamon = RecipeIngredient(
            amount=1,
            unit='tsp powdered',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    egg = RecipeIngredient(
            amount=3,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    champagne = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='piece',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    bitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    cognac = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    blendedwhiskey = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    grenadine = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    kahlua = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Root Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    galliano = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Root Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Root Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    rum = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg White').first().id
        )
    bitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    nutmeg = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    cointreau = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    corona = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Boilermaker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Corona').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Boilermaker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    bitters = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    water = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    bourbon = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    chocolateicecream = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate ice-cream').first().id
        )
    cognac = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cocktail Horse’s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    gingerbeer = RecipeIngredient(
            amount=100,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cocktail Horse’s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger Beer').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=3,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cocktail Horse’s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cocktail Horse’s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Peel').first().id
        )
    orange = RecipeIngredient(
            amount=3,
            unit='large',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Orange Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    vodka = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Orange Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='1/3 cup superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Orange Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cocoapowder = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Castillian Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cocoa powder').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Castillian Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cornstarch = RecipeIngredient(
            amount=7,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Castillian Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cornstarch').first().id
        )
    water = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Castillian Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    milk = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Castillian Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    tequila = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    whiterum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White rum').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    cherrygrenadine = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry Grenadine').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    clubsoda = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    gin = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Derby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'gin').first().id
        )
    peachbitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Derby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach Bitters').first().id
        )
    mint = RecipeIngredient(
            amount=2,
            unit='fresh leaves',
            recipe_id=Recipe.query.filter(Recipe.name == 'Derby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    lager = RecipeIngredient(
            amount=NaN,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Diesel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    cider = RecipeIngredient(
            amount=NaN,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Diesel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    blackcurrantcordial = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Diesel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackcurrant cordial').first().id
        )
    lightrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    coffee = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Danbooka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    everclear = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Danbooka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Everclear').first().id
        )
    fruitpunch = RecipeIngredient(
            amount=2,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Downshift').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fruit punch').first().id
        )
    sprite = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Downshift').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    tequila = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Downshift').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    151proofrum = RecipeIngredient(
            amount=NaN,
            unit='bacardi',
            recipe_id=Recipe.query.filter(Recipe.name == 'Downshift').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dragonfly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    gingerale = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dragonfly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dragonfly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='2/3 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    olive = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive').first().id
        )
    scotch = RecipeIngredient(
            amount=2,
            unit='1/2 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Rob Roy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1,
            unit='1/2 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Rob Roy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Rob Roy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dirty Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dirty Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    olivebrine = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dirty Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive Brine').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dirty Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    olive = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dirty Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive').first().id
        )
    cherryheering = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Darkwood Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry Heering').first().id
        )
    sodawater = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Darkwood Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Darkwood Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Darkwood Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    darkrum = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dark and Stormy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    gingerbeer = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dark and Stormy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger Beer').first().id
        )
    demerarasugar = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dark Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'demerara Sugar').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dark Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    cachaca = RecipeIngredient(
            amount=2,
            unit='1/2 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dark Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cachaca').first().id
        )
    pisco = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pisco').first().id
        )
    limejuice = RecipeIngredient(
            amount=2.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    pineapplesyrup = RecipeIngredient(
            amount=2.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Syrup').first().id
        )
    st.germain = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'St. Germain').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    pepper = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepper').first().id
        )
    lavender = RecipeIngredient(
            amount=2,
            unit='sprigs',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lavender').first().id
        )
    whiskey = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Damned if you do').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whiskey').first().id
        )
    hotdamn = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Damned if you do').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot Damn').first().id
        )
    dubonnetrouge = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dubonnet Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dubonnet Rouge').first().id
        )
    gin = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dubonnet Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    bitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dubonnet Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dubonnet Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    heavycream = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    milk = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    cinnamon = RecipeIngredient(
            amount=1,
            unit='stick',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    vanilla = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla').first().id
        )
    chocolate = RecipeIngredient(
            amount=2,
            unit='oz finely chopped dark',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    whippedcream = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped cream').first().id
        )
    absinthe = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Death in the Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absinthe').first().id
        )
    champagne = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Death in the Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    chocolatesyrup = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate syrup').first().id
        )
    milk = RecipeIngredient(
            amount=6,
            unit='oz whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    sodawater = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    eggyolk = RecipeIngredient(
            amount=6,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg yolk').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    milk = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    lightrum = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    bourbon = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    salt = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    whippingcream = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipping cream').first().id
        )
    eggwhite = RecipeIngredient(
            amount=6,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    nutmeg = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    brandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    gin = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    vodka = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    rum = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Rumtini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    vanillasyrup = RecipeIngredient(
            amount=NaN,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Rumtini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla syrup').first().id
        )
    espresso = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Rumtini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Espresso').first().id
        )
    coffee = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Rumtini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    egg = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    sugar = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    condensedmilk = RecipeIngredient(
            amount=13,
            unit='oz skimmed',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Condensed milk').first().id
        )
    milk = RecipeIngredient(
            amount=NaN,
            unit='cup skimmed',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    rum = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    nutmeg = RecipeIngredient(
            amount=0,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    apricotbrandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    cachaca = RecipeIngredient(
            amount=60,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Elderflower Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cachaca').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Elderflower Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    elderflowercordial = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Elderflower Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Elderflower cordial').first().id
        )
    egg = RecipeIngredient(
            amount=6,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    salt = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    milk = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    mezcal = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Empellón Cocina's Fat-Washed Mezcal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mezcal').first().id
        )
    chocolateliqueur = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Empellón Cocina's Fat-Washed Mezcal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate liqueur').first().id
        )
    coffeeliqueur = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Empellón Cocina's Fat-Washed Mezcal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee liqueur').first().id
        )
    rose = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frosé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rose').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frosé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    strawberries = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frosé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frosé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    coffee = RecipeIngredient(
            amount=NaN,
            unit='cup black',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frappé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    milk = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frappé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frappé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    amaretto = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Foxy Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Foxy Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    lightcream = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Foxy Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sugar = RecipeIngredient(
            amount=2,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    champagne = RecipeIngredient(
            amount=4,
            unit='oz chilled',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    honey = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    figs = RecipeIngredient(
            amount=3,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Figs').first().id
        )
    thyme = RecipeIngredient(
            amount=1,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Thyme').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    tonicwater = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic Water').first().id
        )
    blendedwhiskey = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    benedictine = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/4',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    yoghurt = RecipeIngredient(
            amount=1,
            unit='cup fruit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    banana = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    orangejuice = RecipeIngredient(
            amount=4,
            unit='oz frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    fruit = RecipeIngredient(
            amount=NaN,
            unit='piece textural',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fruit').first().id
        )
    ice = RecipeIngredient(
            amount=6,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    applejuice = RecipeIngredient(
            amount=1,
            unit='can frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    strawberries = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    sugar = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    apple = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple').first().id
        )
    sodawater = RecipeIngredient(
            amount=1,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    jägermeister = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Freddy Kruger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    sambuca = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Freddy Kruger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Freddy Kruger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    rum = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    apricotnectar = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot Nectar').first().id
        )
    pomegranatejuice = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pomegranate juice').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    coffee = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fuzzy Asshole').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fuzzy Asshole').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    vodka = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    raspberryliqueur = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry Liqueur').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'pineapple juice').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lillet = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lillet').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    orangepeel = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    firewater = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fahrenheit 5000').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Firewater').first().id
        )
    absolutpeppar = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fahrenheit 5000').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Peppar').first().id
        )
    tabascosauce = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fahrenheit 5000').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Dutchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Dutchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lightrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    limejuice = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='cup crushed',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    yoghurt = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Flip-Flop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    fruitjuice = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Flip-Flop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fruit juice').first().id
        )
    scotch = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Scotchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Scotchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    bitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Scotchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Scotchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    cognac = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Connection').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    amaretto = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French Connection').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    151proofrum = RecipeIngredient(
            amount=1,
            unit='oz bacardi',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    dr.pepper = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dr. Pepper').first().id
        )
    beer = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Beer').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Lamborghini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    sambuca = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Lamborghini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Lamborghini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Lamborghini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    sambuca = RecipeIngredient(
            amount=NaN,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flander's Flake-Out').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    sarsaparilla = RecipeIngredient(
            amount=NaN,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flander's Flake-Out').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sarsaparilla').first().id
        )
    lightrum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Mint Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Mint Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    mint = RecipeIngredient(
            amount=6,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Mint Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Mint Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    lightrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Pineapple Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    pineapple = RecipeIngredient(
            amount=4,
            unit='chunks',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Pineapple Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Pineapple Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Pineapple Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    galliano = RecipeIngredient(
            amount=2,
            unit='1/2 shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'GG').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='1/2 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    limejuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godchild').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godchild').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    heavycream = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godchild').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    peachvodka = RecipeIngredient(
            amount=5,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gagliardo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach Vodka').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gagliardo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    galliano = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gagliardo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    sirupofroses = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gagliardo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sirup of roses').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godmother').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    amaretto = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godmother').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    scotch = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godfather').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    amaretto = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Godfather').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    redwine = RecipeIngredient(
            amount=1,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    water = RecipeIngredient(
            amount=125,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    sugar = RecipeIngredient(
            amount=60,
            unit='gr',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cinnamon = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    cloves = RecipeIngredient(
            amount=3,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    gin = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    tonicwater = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic Water').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Peel').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    water = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    carbonatedwater = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Carbonated water').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='cube',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    mint = RecipeIngredient(
            amount=4,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    grenadine = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    gin = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=8,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Peel').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    water = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    orangepeel = RecipeIngredient(
            amount=NaN,
            unit='of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Greyhound').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    grapefruitjuice = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Greyhound').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='up with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Squirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Squirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Squirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    pineapple = RecipeIngredient(
            amount=3,
            unit='chunks',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Squirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    strawberries = RecipeIngredient(
            amount=2,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Squirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    maliburum = RecipeIngredient(
            amount=1,
            unit='1/2 cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grand Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=1,
            unit='1/2 cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grand Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=1,
            unit='1/2 cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grand Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grand Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    limejuice = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    bitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    clubsoda = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grass Skirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grass Skirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grass Skirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grass Skirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    pineapple = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grass Skirt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    greencremedementhe = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grasshopper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Creme de Menthe').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=NaN,
            unit='oz white',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grasshopper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    lightcream = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grasshopper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grim Reaper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    151proofrum = RecipeIngredient(
            amount=1,
            unit='oz bacardi',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grim Reaper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grim Reaper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin and Soda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sodawater = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin and Soda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin and Soda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    galliano = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Golden dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    triplesec = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Golden dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    orangejuice = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Golden dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'orange juice').first().id
        )
    cream = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Golden dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    cider = RecipeIngredient(
            amount=NaN,
            unit='pint hard',
            recipe_id=Recipe.query.filter(Recipe.name == 'Green Goblin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    lager = RecipeIngredient(
            amount=NaN,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Green Goblin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Green Goblin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grizzly Bear').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    jägermeister = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grizzly Bear').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grizzly Bear').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    milk = RecipeIngredient(
            amount=2,
            unit='1/2 parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grizzly Bear').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin And Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    tonicwater = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin And Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic water').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin And Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    gin = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Basil Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Basil Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Basil Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    basil = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Basil Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Basil').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman's Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    brandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman's Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman's Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    clubsoda = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman's Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    cachaca = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Girl From Ipanema').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cachaca').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Girl From Ipanema').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    agavesyrup = RecipeIngredient(
            amount=10,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Girl From Ipanema').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Agave Syrup').first().id
        )
    champagne = RecipeIngredient(
            amount=NaN,
            unit='up with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Girl From Ipanema').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    gin = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Garibaldi Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    campari = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Garibaldi Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    orangejuice = RecipeIngredient(
            amount=90,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Garibaldi Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    orangepeel = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Garibaldi Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    darkrum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon's Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon's Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon's Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    tequila = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon's Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    melonliqueur = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon's Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Melon liqueur').first().id
        )
    mountaindew = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon's Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mountain Dew').first().id
        )
    grapes = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grape lemon pineapple Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapes').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grape lemon pineapple Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    pineapple = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grape lemon pineapple Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    whisky = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'H.D.').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whisky').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=8,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'H.D.').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    whiterum = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Honey Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Rum').first().id
        )
    honey = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Honey Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Honey Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    whiskey = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whiskey').first().id
        )
    honey = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    cinnamon = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    cloves = RecipeIngredient(
            amount=2,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    hotdamn = RecipeIngredient(
            amount=5,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Herbal flame').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot Damn').first().id
        )
    tea = RecipeIngredient(
            amount=NaN,
            unit='sweet',
            recipe_id=Recipe.query.filter(Recipe.name == 'Herbal flame').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='long strip',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse's Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    brandy = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse's Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    gingerale = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse's Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    bitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse's Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    spicedrum = RecipeIngredient(
            amount=1,
            unit='1/2 cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Happy Skipper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Spiced rum').first().id
        )
    vermouth = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter's Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vermouth').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter's Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Cherry').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=10,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter's Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    lemonade = RecipeIngredient(
            amount=100,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter's Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    blackberries = RecipeIngredient(
            amount=2,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter's Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberries').first().id
        )
    cherryjuice = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry Juice').first().id
        )
    orangepeel = RecipeIngredient(
            amount=3,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    redchiliflakes = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red Chili Flakes').first().id
        )
    cloves = RecipeIngredient(
            amount=10,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    ginger = RecipeIngredient(
            amount=6,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    vodka = RecipeIngredient(
            amount=20,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Havana Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Havana Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Havana Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    carbonatedsoftdrink = RecipeIngredient(
            amount=NaN,
            unit='orange
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Holloween Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Carbonated soft drink').first().id
        )
    sugar = RecipeIngredient(
            amount=2,
            unit='1/2 cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cornsyrup = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Corn syrup').first().id
        )
    coffee = RecipeIngredient(
            amount=1,
            unit='1/2 oz instant',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    water = RecipeIngredient(
            amount=3,
            unit='cups boiling',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    irishwhiskey = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Creamy Bush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish whiskey').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=NaN,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Creamy Bush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    coffee = RecipeIngredient(
            amount=6,
            unit='oz hot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Creamy Bush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Harvey Wallbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    galliano = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Harvey Wallbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    orangejuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Harvey Wallbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hawaiian Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hawaiian Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hawaiian Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    rum = RecipeIngredient(
            amount=12,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hemingway Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    grapefruitjuice = RecipeIngredient(
            amount=8,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hemingway Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hemingway Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Liqueur').first().id
        )
    limejuice = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hemingway Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    scotch = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Highland Fling Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Highland Fling Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    orangebitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Highland Fling Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    olive = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Highland Fling Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive').first().id
        )
    chocolate = RecipeIngredient(
            amount=12,
            unit='oz fine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    butter = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butter').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    halfandhalf = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Half-and-half').first().id
        )
    marshmallows = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Marshmallows').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    brownsugar = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brown sugar').first().id
        )
    passionfruitjuice = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit juice').first().id
        )
    gingerale = RecipeIngredient(
            amount=NaN,
            unit='up with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ice Pick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    icedtea = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ice Pick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Iced tea').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=0,
            unit='to taste
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ice Pick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    coffee = RecipeIngredient(
            amount=NaN,
            unit='cup instant',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    water = RecipeIngredient(
            amount=NaN,
            unit='cup hot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    milk = RecipeIngredient(
            amount=4,
            unit='cups cold',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    scotch = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    halfandhalf = RecipeIngredient(
            amount=1,
            unit='1/4 cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Half-and-half').first().id
        )
    condensedmilk = RecipeIngredient(
            amount=1,
            unit='can sweetened',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Condensed milk').first().id
        )
    coconutsyrup = RecipeIngredient(
            amount=3,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut syrup').first().id
        )
    chocolatesyrup = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate syrup').first().id
        )
    irishwhiskey = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish whiskey').first().id
        )
    coffee = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    whippedcream = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped cream').first().id
        )
    irishwhiskey = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish whiskey').first().id
        )
    peachbrandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach brandy').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    lightrum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    blendedwhiskey = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    cocacola = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    guinnessstout = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guinness stout').first().id
        )
    limejuice = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    aperol = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Aperol').first().id
        )
    kahlua = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee Fillip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    coffee = RecipeIngredient(
            amount=NaN,
            unit='cold',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee Fillip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    bourbon = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    orangejuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jam Donut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    chambordraspberryliqueur = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jam Donut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jam Donut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    sugar = RecipeIngredient(
            amount=2,
            unit='pinches',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jam Donut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='jiggers',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='jigger',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    grenadine = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='rim put 1 pinch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='to top with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    jackdaniels = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jackhammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jack Daniels').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jackhammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    blackberrybrandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jelly Bean').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberry brandy').first().id
        )
    anis = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jelly Bean').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anis').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jello shots').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    jello = RecipeIngredient(
            amount=3,
            unit='packages',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jello shots').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jello').first().id
        )
    water = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jello shots').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    coffeeliqueur = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaica Kiss').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee liqueur').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='shot jamaican',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaica Kiss').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaica Kiss').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    bourbon = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    clubsoda = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    blendedwhiskey = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    port = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Port').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    rum = RecipeIngredient(
            amount=NaN,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaican Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    coffee = RecipeIngredient(
            amount=NaN,
            unit='glass strong black',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaican Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    water = RecipeIngredient(
            amount=NaN,
            unit='glass cold',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaican Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    milk = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Just a Moonmint').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jewel Of The Nile').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    greenchartreuse = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jewel Of The Nile').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    yellowchartreuse = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jewel Of The Nile').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yellow Chartreuse').first().id
        )
    applebrandy = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple brandy').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack's Vanilla Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    tennesseewhiskey = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack's Vanilla Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tennessee whiskey').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack's Vanilla Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    cocacola = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack's Vanilla Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    cremedecassis = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kir').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    champagne = RecipeIngredient(
            amount=5,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kir').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    coffee = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Karsk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    grainalcohol = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Karsk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grain alcohol').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kamikaze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kamikaze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kamikaze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    cremedecassis = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kir Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    champagne = RecipeIngredient(
            amount=5,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kir Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    kiwiliqueur = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kiwi liqueur').first().id
        )
    bitterlemon = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitter lemon').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    absolutkurant = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kurant Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Kurant').first().id
        )
    tea = RecipeIngredient(
            amount=NaN,
            unit='apple',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kurant Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    sugar = RecipeIngredient(
            amount=0,
            unit='(if needed)
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kurant Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kioki Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    brandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kioki Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    kiwi = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kiwi').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    kiwi = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kiwi').first().id
        )
    cranberryvodka = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiss me Quick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry vodka').first().id
        )
    apfelkorn = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiss me Quick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apfelkorn').first().id
        )
    schweppesrusschian = RecipeIngredient(
            amount=7,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiss me Quick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Schweppes Russchian').first().id
        )
    applejuice = RecipeIngredient(
            amount=8,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiss me Quick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiss me Quick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    sloegin = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    151proofrum = RecipeIngredient(
            amount=2,
            unit='oz light',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool First Aid').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    koolaid = RecipeIngredient(
            amount=NaN,
            unit='tsp tropical',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool First Aid').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kool-Aid').first().id
        )
    bourbon = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky B And B').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    benedictine = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky B And B').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    bourbon = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky Colonel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    benedictine = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky Colonel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky Colonel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    koolaid = RecipeIngredient(
            amount=NaN,
            unit='oz grape',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kool-Aid').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    kiwi = RecipeIngredient(
            amount=3,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Papaya Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kiwi').first().id
        )
    papaya = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Papaya Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Papaya').first().id
        )
    ginger = RecipeIngredient(
            amount=1,
            unit='inch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kill the cold Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kill the cold Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    water = RecipeIngredient(
            amount=1,
            unit='cup hot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kill the cold Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1',
            recipe_id=Recipe.query.filter(Recipe.name == 'Limeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Limeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    sodawater = RecipeIngredient(
            amount=0,
            unit='(seltzer water)
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Limeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    beer = RecipeIngredient(
            amount=NaN,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lunch Box').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Beer').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lunch Box').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lunch Box').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='1/2 shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Drop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    cointreau = RecipeIngredient(
            amount=1,
            unit='1/2 shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Drop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1 wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Drop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    galliano = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    absolutcitron = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    lemon = RecipeIngredient(
            amount=0,
            unit='wedge
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    vodka = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=4,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura bitters').first().id
        )
    tonicwater = RecipeIngredient(
            amount=1,
            unit='dl schweppes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic water').first().id
        )
    ice = RecipeIngredient(
            amount=4,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    yoghurt = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Khara').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    water = RecipeIngredient(
            amount=2,
            unit='cups cold',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Khara').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    salt = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Khara').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    asafoetida = RecipeIngredient(
            amount=1,
            unit='pinch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Khara').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Asafoetida').first().id
        )
    yoghurt = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Raita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Raita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ginger = RecipeIngredient(
            amount=2,
            unit='pieces',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemouroudji').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    water = RecipeIngredient(
            amount=1,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemouroudji').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='lb',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemouroudji').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemouroudji').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cayennepepper = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemouroudji').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cayenne pepper').first().id
        )
    scotch = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    drambuie = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Drambuie').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'London Town').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'London Town').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    orangebitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'London Town').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    mango = RecipeIngredient(
            amount=2,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Mango').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mango').first().id
        )
    yoghurt = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Mango').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Mango').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    water = RecipeIngredient(
            amount=1,
            unit='cup iced',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Mango').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    yoghurt = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    water = RecipeIngredient(
            amount=2,
            unit='cups cold',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    sugar = RecipeIngredient(
            amount=4,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    salt = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    corona = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Limona Corona').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Corona').first().id
        )
    bacardilimon = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Limona Corona').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bacardi Limon').first().id
        )
    darkrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lord And Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    tiamaria = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lord And Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tia maria').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lady Love Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lightcream = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lady Love Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lady Love Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lady Love Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lady Love Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    lightrum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    gin = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    tequila = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    cocacola = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lone Tree Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lone Tree Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    coconutliqueur = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lazy Coconut Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut Liqueur').first().id
        )
    grapefruitjuice = RecipeIngredient(
            amount=75,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lazy Coconut Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lazy Coconut Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    tequila = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    lightrum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    gin = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    cocacola = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=NaN,
            unit='of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    elderflowercordial = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Elderflower Spritzer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Elderflower cordial').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Elderflower Spritzer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Elderflower Spritzer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    freshlemonjuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Elderflower Spritzer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lemon Juice').first().id
        )
    yoghurt = RecipeIngredient(
            amount=NaN,
            unit='cup plain',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    water = RecipeIngredient(
            amount=1,
            unit='1/4 cup cold',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    cuminseed = RecipeIngredient(
            amount=NaN,
            unit='tsp ground roasted',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cumin seed').first().id
        )
    salt = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    mint = RecipeIngredient(
            amount=NaN,
            unit='tsp dried',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    honey = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Melya').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    lightrum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    sugar = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    mint = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    champagne = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mimosa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    orangejuice = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mimosa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    orgeatsyrup = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orgeat syrup').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='2/3 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    olive = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive').first().id
        )
    beer = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Beer').first().id
        )
    tomatojuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato Juice').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    hotsauce = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot Sauce').first().id
        )
    worcestershiresauce = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Worcestershire Sauce').first().id
        )
    soysauce = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soy Sauce').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    bourbon = RecipeIngredient(
            amount=2,
            unit='1/2 oz blended',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura bitters').first().id
        )
    ice = RecipeIngredient(
            amount=2,
            unit='or 3',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    orangepeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    tequila = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    ricard = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mauresque').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ricard').first().id
        )
    orgeatsyrup = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mauresque').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orgeat Syrup').first().id
        )
    water = RecipeIngredient(
            amount=NaN,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mauresque').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    mint = RecipeIngredient(
            amount=4,
            unit='fresh',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mint Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    bourbon = RecipeIngredient(
            amount=2,
            unit='1/2 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mint Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mint Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    water = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mint Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    southerncomfort = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mudslinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mudslinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    pepsicola = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mudslinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepsi Cola').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez 2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez 2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez 2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Liqueur').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez 2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    absinthe = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moranguito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absinthe').first().id
        )
    tequila = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moranguito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    grenadine = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moranguito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    151proofrum = RecipeIngredient(
            amount=5,
            unit='oz bacardi',
            recipe_id=Recipe.query.filter(Recipe.name == 'Miami Vice').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    pinacoladamix = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Miami Vice').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pina colada mix').first().id
        )
    daiquirimix = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Miami Vice').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Daiquiri mix').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moscow Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    limejuice = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moscow Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    gingerale = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moscow Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    water = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cloves = RecipeIngredient(
            amount=12,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    cinnamon = RecipeIngredient(
            amount=2,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    redwine = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    brandy = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    water = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    tea = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    ginger = RecipeIngredient(
            amount=1,
            unit='chunk dried',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    cardamom = RecipeIngredient(
            amount=NaN,
            unit='crushed',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cardamom').first().id
        )
    cloves = RecipeIngredient(
            amount=3,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    cinnamon = RecipeIngredient(
            amount=1,
            unit='piece',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    blackpepper = RecipeIngredient(
            amount=NaN,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Black pepper').first().id
        )
    sugar = RecipeIngredient(
            amount=0,
            unit='to taste
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    milk = RecipeIngredient(
            amount=NaN,
            unit='taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    gin = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    limejuice = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    gingerbeer = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger Beer').first().id
        )
    cucumber = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cucumber').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    coffee = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mocha-Berry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    chambordraspberryliqueur = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mocha-Berry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    cocoapowder = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mocha-Berry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cocoa powder').first().id
        )
    lime = RecipeIngredient(
            amount=3,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    mango = RecipeIngredient(
            amount=1,
            unit='fresh',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mango').first().id
        )
    mint = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    whiterum = RecipeIngredient(
            amount=200,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Rum').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    mango = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mango').first().id
        )
    mint = RecipeIngredient(
            amount=NaN,
            unit='handful',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    darkrum = RecipeIngredient(
            amount=NaN,
            unit='l jamaican',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    clubsoda = RecipeIngredient(
            amount=NaN,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=8,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura bitters').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Gland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    benedictine = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Gland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    orangejuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Gland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Gland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Mint').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    whitecremedementhe = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Mint').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    cream = RecipeIngredient(
            amount=NaN,
            unit='oz double',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Mint').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    lightrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    grenadine = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    lightrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Wrench').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    grapefruitjuice = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Wrench').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    bitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Wrench').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    goldschlager = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mother's Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    butterscotchschnapps = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mother's Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butterscotch schnapps').first().id
        )
    milk = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mother's Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Manx').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Manx').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    goldschlager = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Manx').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    heavycream = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Manx').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    coffee = RecipeIngredient(
            amount=2,
            unit='oz hazlenut',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Manx').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    maliburum = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Malibu Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    tropicana = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Malibu Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tropicana').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Malibu Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    bourbon = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Cowboy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    darkrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Cowboy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    heavycream = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Cowboy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    blackberries = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberries').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    mint = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    orangebitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martinez Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    sugar = RecipeIngredient(
            amount=5,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cocoapowder = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cocoa powder').first().id
        )
    salt = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    water = RecipeIngredient(
            amount=3,
            unit='tbsp hot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    milk = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    mango = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Orange Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mango').first().id
        )
    orange = RecipeIngredient(
            amount=2,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Orange Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    brandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    lightrum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    bourbon = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    campari = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    blendedwhiskey = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    redwine = RecipeIngredient(
            amount=0,
            unit='(claret)
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nutty Irishman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    frangelico = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nutty Irishman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Frangelico').first().id
        )
    milk = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nutty Irishman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    rum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    gin = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    sourmix = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    lemonlimesoda = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    absolutcitron = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    grandmarnier = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=2,
            unit='oz sweetened',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    clubsoda = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    cocoapowder = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nuked Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cocoa powder').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nuked Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nuked Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    milk = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Nuked Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=NaN,
            unit='oz white',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    amaretto = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    vodka = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    lightcream = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    ryewhiskey = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Pal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rye whiskey').first().id
        )
    campari = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Pal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Pal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    whiterum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Cuban').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Rum').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Cuban').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Cuban').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Cuban').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    prosecco = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Cuban').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orangeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    orangejuice = RecipeIngredient(
            amount=15,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orangeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=NaN,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orangeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    orangejuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Whip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    rum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Whip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Whip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    cream = RecipeIngredient(
            amount=1,
            unit='package',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Whip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Whip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Crush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Crush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Crush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    cherrybrandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Oasis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Oasis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    orangejuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Oasis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    bourbon = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura bitters').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='cube',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    water = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Old Fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oreo Mudslide').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oreo Mudslide').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oreo Mudslide').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    vanillaicecream = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oreo Mudslide').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla ice-cream').first().id
        )
    oreocookie = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oreo Mudslide').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Oreo cookie').first().id
        )
    kahlua = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oatmeal Cookie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oatmeal Cookie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    butterscotchschnapps = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oatmeal Cookie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butterscotch schnapps').first().id
        )
    jagermeister = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oatmeal Cookie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jagermeister').first().id
        )
    goldschlager = RecipeIngredient(
            amount=NaN,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Oatmeal Cookie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    spicedrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Push-up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Spiced rum').first().id
        )
    grenadine = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Push-up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    orangejuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Push-up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    sourmix = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Push-up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    orangejuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    rosemarysyrup = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosemary Syrup').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    rosemary = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosemary').first().id
        )
    orangepeel = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    milk = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    chocolate = RecipeIngredient(
            amount=4,
            unit='oz chopped bittersweet or semi-sweet',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    orangepeel = RecipeIngredient(
            amount=3,
            unit='2-inch strips',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    espresso = RecipeIngredient(
            amount=NaN,
            unit='tsp instant',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Espresso').first().id
        )
    nutmeg = RecipeIngredient(
            amount=NaN,
            unit='tsp ground',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    whiskey = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen's Grandmother's Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whiskey').first().id
        )
    beer = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen's Grandmother's Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Beer').first().id
        )
    lemonade = RecipeIngredient(
            amount=12,
            unit='oz frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen's Grandmother's Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='cup crushed',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen's Grandmother's Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    grapesoda = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grape Soda').first().id
        )
    tequila = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    gin = RecipeIngredient(
            amount=7,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Paradise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    apricotbrandy = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Paradise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot Brandy').first().id
        )
    orangejuice = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Paradise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    bitters = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Gin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Gin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    orangecuracao = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Curacao').first().id
        )
    limejuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    orangebitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Bitters').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    lightcream = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    coconutliqueur = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut Liqueur').first().id
        )
    elderflowercordial = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Elderflower cordial').first().id
        )
    limejuice = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    blackberries = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberries').first().id
        )
    blendedscotch = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended Scotch').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    honeysyrup = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey syrup').first().id
        )
    gingersyrup = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger Syrup').first().id
        )
    islaysinglemaltscotch = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Islay single malt Scotch').first().id
        )
    pisco = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pisco').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    brandy = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Porto flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    port = RecipeIngredient(
            amount=9,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Porto flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Port').first().id
        )
    eggyolk = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Porto flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg Yolk').first().id
        )
    lightrum = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pina Colada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    coconutmilk = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pina Colada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut milk').first().id
        )
    pineapple = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pina Colada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    everclear = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Penocha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Everclear').first().id
        )
    vodka = RecipeIngredient(
            amount=1750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Penocha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=1750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Penocha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Penocha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=1,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Penocha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    rum = RecipeIngredient(
            amount=40,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    passoa = RecipeIngredient(
            amount=20,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passoa').first().id
        )
    limejuice = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    passionfruitsyrup = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit syrup').first().id
        )
    peachbitters = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach Bitters').first().id
        )
    mint = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Popped cherry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    cherryliqueur = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Popped cherry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry liqueur').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Popped cherry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    orangejuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Popped cherry').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Poppy Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=NaN,
            unit='oz white',
            recipe_id=Recipe.query.filter(Recipe.name == 'Poppy Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    port = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Port').first().id
        )
    lightcream = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    egg = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    darkrum = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    orgeatsyrup = RecipeIngredient(
            amount=NaN,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orgeat syrup').first().id
        )
    orangejuice = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter's Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    tequila = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    grapefruitjuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    freshlimejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lime Juice').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    pepper = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepper').first().id
        )
    vodka = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pornstar Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    passoa = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pornstar Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passoa').first().id
        )
    passionfruitjuice = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pornstar Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit juice').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pornstar Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    prosecco = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pornstar Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    darkrum = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter’s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    orangejuice = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter’s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=3.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter’s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter’s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter’s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=4,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter’s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port And Starboard').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    greencremedementhe = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port And Starboard').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Creme de Menthe').first().id
        )
    port = RecipeIngredient(
            amount=2,
            unit='1/2 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Port').first().id
        )
    brandy = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pysch Vitamin Light').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    applejuice = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pysch Vitamin Light').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pysch Vitamin Light').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    sprite = RecipeIngredient(
            amount=1,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Panty Pulldowns').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    pinklemonade = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Panty Pulldowns').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pink lemonade').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Panty Pulldowns').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Passion Fruit Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=NaN,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Passion Fruit Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    passionfruitjuice = RecipeIngredient(
            amount=NaN,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Passion Fruit Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit juice').first().id
        )
    ginger = RecipeIngredient(
            amount=NaN,
            unit='inch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Gingerale Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    pineapple = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Gingerale Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    darkrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quentin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    kahlua = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quentin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    lightcream = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quentin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    nutmeg = RecipeIngredient(
            amount=NaN,
            unit='tsp grated',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quentin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    coffeebrandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee brandy').first().id
        )
    limevodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime vodka').first().id
        )
    sherry = RecipeIngredient(
            amount=NaN,
            unit='oz cream',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    kahlua = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quick F**K').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    midorimelonliqueur = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quick F**K').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quick F**K').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    blacksambuca = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quick-sand').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Black Sambuca').first().id
        )
    orangejuice = RecipeIngredient(
            amount=NaN,
            unit='250 ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quick-sand').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    redwine = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Charlotte').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Charlotte').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Elizabeth').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Elizabeth').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    benedictine = RecipeIngredient(
            amount=1,
            unit='1/2 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Elizabeth').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    lightrum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker's Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    brandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker's Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/4',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker's Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    raspberrysyrup = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker's Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry syrup').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quarter Deck Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    sherry = RecipeIngredient(
            amount=NaN,
            unit='oz cream',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quarter Deck Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quarter Deck Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    apricotbrandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    beer = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Beer').first().id
        )
    7up = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '7-Up').first().id
        )
    lightrum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    rum = RecipeIngredient(
            amount=NaN,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    gingerale = RecipeIngredient(
            amount=NaN,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    fruitpunch = RecipeIngredient(
            amount=355,
            unit='ml frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fruit punch').first().id
        )
    orangejuice = RecipeIngredient(
            amount=355,
            unit='ml frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    rum = RecipeIngredient(
            amount=2,
            unit='oz light or dark',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    water = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    egg = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    rum = RecipeIngredient(
            amount=2,
            unit='oz light or dark',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    lemonlimesoda = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    maliburum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    blackberrybrandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberry brandy').first().id
        )
    orangejuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    scotch = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rusty Nail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    drambuie = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rusty Nail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Drambuie').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rusty Nail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    crownroyal = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Red Snapper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Crown Royal').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Red Snapper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Red Snapper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    frangelico = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Bitch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Frangelico').first().id
        )
    crownroyal = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Bitch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Crown Royal').first().id
        )
    crownroyal = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Flush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Crown Royal').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Flush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    chambordraspberryliqueur = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Flush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Flush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    clubsoda = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    darkrum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ruby Tuesday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ruby Tuesday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=2,
            unit='splashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ruby Tuesday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rail Splitter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    gin = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rosemary Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rosemary Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    tonicwater = RecipeIngredient(
            amount=100,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rosemary Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic Water').first().id
        )
    rosemary = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rosemary Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosemary').first().id
        )
    gin = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    cream = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg White').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=2,
            unit='drop',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    sodawater = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    egg = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    lightrum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Milk Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    milk = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Milk Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Milk Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    bourbon = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    raspberrysyrup = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry syrup').first().id
        )
    mint = RecipeIngredient(
            amount=8,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Julep').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    lightrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Screwdriver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    orangejuice = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Screwdriver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    raspberryvodka = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry vodka').first().id
        )
    lemonlimesoda = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    lightrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    151proofrum = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    bitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    water = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    limepeel = RecipeIngredient(
            amount=NaN,
            unit='of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime peel').first().id
        )
    vodka = RecipeIngredient(
            amount=2.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Russian Spring Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    cremedecassis = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Russian Spring Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Russian Spring Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=2.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Russian Spring Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    rum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    tequila = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    chambordraspberryliqueur = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    midorimelonliqueur = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    maliburum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    redwine = RecipeIngredient(
            amount=NaN,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    pepsicola = RecipeIngredient(
            amount=NaN,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepsi Cola').first().id
        )
    orangejuice = RecipeIngredient(
            amount=NaN,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    prosecco = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    campari = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    brandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    amaretto = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    lightcream = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    redwine = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    brandy = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Stinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    whitecremedementhe = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Stinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    ricard = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ricard').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    peychaudbitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peychaud bitters').first().id
        )
    water = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    bourbon = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    cognac = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    cointreau = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    amaromontenegro = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaro Montenegro').first().id
        )
    rubyport = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ruby Port').first().id
        )
    bloodorange = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blood Orange').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    orangepeel = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    sugar = RecipeIngredient(
            amount=60,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    allspice = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Allspice').first().id
        )
    rum = RecipeIngredient(
            amount=20,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    limejuice = RecipeIngredient(
            amount=90,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    champagne = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    orangespiral = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange spiral').first().id
        )
    advocaat = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Advocaat').first().id
        )
    lemonade = RecipeIngredient(
            amount=NaN,
            unit='oz cold',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    jimbeam = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shot-gun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jim Beam').first().id
        )
    jackdaniels = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shot-gun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jack Daniels').first().id
        )
    wildturkey = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shot-gun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wild Turkey').first().id
        )
    grapefruitjuice = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salty Dog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salty Dog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    salt = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salty Dog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    apricotbrandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sea breeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sea breeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    grapefruitjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sea breeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    scotch = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    godivaliqueur = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Tooth').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Godiva liqueur').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Screwdriver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    sherry = RecipeIngredient(
            amount=1,
            unit='1/2 oz cream',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    lightcream = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    egg = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    brandy = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sol Y Sombra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    anisette = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sol Y Sombra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anisette').first().id
        )
    lemonade = RecipeIngredient(
            amount=1,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shark Attack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    water = RecipeIngredient(
            amount=3,
            unit='cans',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shark Attack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shark Attack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'San Francisco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    cremedebanane = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'San Francisco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Banane').first().id
        )
    151proofrum = RecipeIngredient(
            amount=1,
            unit='shot bacardi',
            recipe_id=Recipe.query.filter(Recipe.name == 'Space Odyssey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    maliburum = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Space Odyssey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Space Odyssey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    sherry = RecipeIngredient(
            amount=2,
            unit='oz cream',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Eggnog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Eggnog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    egg = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Eggnog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    milk = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Bananas').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    banana = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Bananas').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    honey = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Bananas').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    redwine = RecipeIngredient(
            amount=2,
            unit='bottles',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    water = RecipeIngredient(
            amount=2,
            unit='cups hot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    apple = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple').first().id
        )
    orange = RecipeIngredient(
            amount=0,
            unit='wedges
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    lime = RecipeIngredient(
            amount=0,
            unit='wedges
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    scotch = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    brandy = RecipeIngredient(
            amount=4,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    curacao = RecipeIngredient(
            amount=4,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Curacao').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    mint = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    coffee = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Swedish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    aquavit = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Swedish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Aquavit').first().id
        )
    sugar = RecipeIngredient(
            amount=NaN,
            unit='taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Swedish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cherrybrandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Singapore Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    grenadine = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Singapore Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Singapore Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Singapore Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    sambuca = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Slippery Nipple').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    irishcream = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Slippery Nipple').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish cream').first().id
        )
    lager = RecipeIngredient(
            amount=NaN,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snake Bite (UK)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    cider = RecipeIngredient(
            amount=NaN,
            unit='pint sweet or dry',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snake Bite (UK)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Screaming Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Screaming Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    kahlua = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Screaming Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sex on the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sex on the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    brandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/4',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    prosecco = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz Veneziano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    aperol = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz Veneziano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Aperol').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spritz Veneziano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    sloegin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sloe Gin Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sloe Gin Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    orangebitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sloe Gin Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    milk = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spanish chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    chocolate = RecipeIngredient(
            amount=2,
            unit='oz sweet',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spanish chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    cinnamon = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spanish chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    eggyolk = RecipeIngredient(
            amount=2,
            unit='beaten',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spanish chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg yolk').first().id
        )
    redwine = RecipeIngredient(
            amount=1,
            unit='1/2 l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='large',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='large',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    apple = RecipeIngredient(
            amount=1,
            unit='large',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple').first().id
        )
    brandy = RecipeIngredient(
            amount=NaN,
            unit='oz plain',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='oz jamaican',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shanghai Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    anisette = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shanghai Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anisette').first().id
        )
    grenadine = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shanghai Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/4',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shanghai Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    peachnectar = RecipeIngredient(
            amount=46,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach nectar').first().id
        )
    orangejuice = RecipeIngredient(
            amount=20,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    brownsugar = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brown sugar').first().id
        )
    cinnamon = RecipeIngredient(
            amount=3,
            unit='3-inch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    cloves = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    limejuice = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    strawberries = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Shivers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    honey = RecipeIngredient(
            amount=4,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Shivers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    water = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Shivers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    strawberryschnapps = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberry schnapps').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    strawberries = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    strawberries = RecipeIngredient(
            amount=NaN,
            unit='ripe',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    water = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    lager = RecipeIngredient(
            amount=NaN,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snakebite and Black').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    cider = RecipeIngredient(
            amount=NaN,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snakebite and Black').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    blackcurrantsquash = RecipeIngredient(
            amount=NaN,
            unit='little bit of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snakebite and Black').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackcurrant squash').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=46,
            unit='oz chilled',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    clubsoda = RecipeIngredient(
            amount=28,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    orangejuice = RecipeIngredient(
            amount=6,
            unit='oz frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    berries = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Berries').first().id
        )
    champagne = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    ouzo = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Surf City Lifesaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ouzo').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Surf City Lifesaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Surf City Lifesaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    grandmarnier = RecipeIngredient(
            amount=NaN,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Surf City Lifesaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    strawberryschnapps = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberry schnapps').first().id
        )
    tequila = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    strawberries = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    gin = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    chocolateliqueur = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate liqueur').first().id
        )
    amaretto = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    chocolatesauce = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate Sauce').first().id
        )
    saltedchocolate = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salted Chocolate').first().id
        )
    johnniewalker = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Johnnie Walker').first().id
        )
    honey = RecipeIngredient(
            amount=1,
            unit='1/2 cup mild',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    angelicaroot = RecipeIngredient(
            amount=2,
            unit='tsp dried and chopped',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angelica root').first().id
        )
    fennelseeds = RecipeIngredient(
            amount=NaN,
            unit='tsp crushed',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fennel seeds').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=2,
            unit='2 inch strips',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    watermelon = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Watermelon').first().id
        )
    mint = RecipeIngredient(
            amount=5,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    grapefruitjuice = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    lime = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    tequila = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    watermelon = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Watermelon').first().id
        )
    mint = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    scotch = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thriller').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    wine = RecipeIngredient(
            amount=1,
            unit='oz green ginger',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thriller').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thriller').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    darkrum = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    campari = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    cremedebanane = RecipeIngredient(
            amount=NaN,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme De Banane').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    limejuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    water = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tia-Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    brownsugar = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tia-Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brown sugar').first().id
        )
    coffee = RecipeIngredient(
            amount=4,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tia-Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    rum = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tia-Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=4,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tia-Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    irishwhiskey = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tipperary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish Whiskey').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tipperary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    greenchartreuse = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tipperary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    wildturkey = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turkeyball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wild Turkey').first().id
        )
    amaretto = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turkeyball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turkeyball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    kahlua = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    irishcream = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish cream').first().id
        )
    amaretto = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    151proofrum = RecipeIngredient(
            amount=NaN,
            unit='oz bacardi',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    cream = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    coffee = RecipeIngredient(
            amount=6,
            unit='tbsp ground',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    coriander = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coriander').first().id
        )
    cardamom = RecipeIngredient(
            amount=NaN,
            unit='whole green',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cardamom').first().id
        )
    gin = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp superfine',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    clubsoda = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    tomatojuice = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tomato Tang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato juice').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tomato Tang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    celerysalt = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tomato Tang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Celery salt').first().id
        )
    grandmarnier = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Talos Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    coffee = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Talos Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    coffee = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tennesee Mud').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    jackdaniels = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tennesee Mud').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jack Daniels').first().id
        )
    amaretto = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tennesee Mud').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    tequila = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    tequila = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    tea = RecipeIngredient(
            amount=NaN,
            unit='cup thai',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    water = RecipeIngredient(
            amount=NaN,
            unit='cup boiling',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    condensedmilk = RecipeIngredient(
            amount=2,
            unit='tsp sweetened',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Condensed milk').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    mint = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    greenchartreuse = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Last Word').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Last Word').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Liqueur').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Last Word').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Last Word').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    anis = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anis').first().id
        )
    bitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    orangepeel = RecipeIngredient(
            amount=NaN,
            unit='of',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    gin = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    elderflowercordial = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Elderflower cordial').first().id
        )
    rossovermouth = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosso Vermouth').first().id
        )
    tonicwater = RecipeIngredient(
            amount=75,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic Water').first().id
        )
    lime = RecipeIngredient(
            amount=2,
            unit='wedges',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ginger = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    mint = RecipeIngredient(
            amount=1,
            unit='large sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    tequila = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    7up = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '7-up').first().id
        )
    tequila = RecipeIngredient(
            amount=2,
            unit='measures',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    melonliqueur = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Melon Liqueur').first().id
        )
    orangebitters = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Bitters').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    prosecco = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    anis = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anis').first().id
        )
    orangebitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    tequila = RecipeIngredient(
            amount=NaN,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Surprise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    tabascosauce = RecipeIngredient(
            amount=NaN,
            unit='8 drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Surprise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    coffee = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    cream = RecipeIngredient(
            amount=0,
            unit='pods
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    irishwhiskey = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Jimmy Conway').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish Whiskey').first().id
        )
    amaretto = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Jimmy Conway').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Jimmy Conway').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry Juice').first().id
        )
    yukonjack = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Rattlesnake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yukon Jack').first().id
        )
    cherrybrandy = RecipeIngredient(
            amount=NaN,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Rattlesnake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    southerncomfort = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Rattlesnake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    sweetandsour = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Rattlesnake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    tequila = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tommy's Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    limejuice = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tommy's Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    agavesyrup = RecipeIngredient(
            amount=2,
            unit='spoons',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tommy's Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Agave syrup').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light Rum').first().id
        )
    gin = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    campari = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    orgeatsyrup = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orgeat Syrup').first().id
        )
    orangepeel = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Evil Blue Thing').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Evil Blue Thing').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    lightrum = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Evil Blue Thing').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    gin = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    lilletblanc = RecipeIngredient(
            amount=0.75,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lillet Blanc').first().id
        )
    gin = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victor').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victor').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    brandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victor').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    tequila = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    tomatojuice = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato Juice').first().id
        )
    orangejuice = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    limejuice = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    salt = RecipeIngredient(
            amount=1,
            unit='pinch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    eggwhite = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    darkrum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Veteran').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    cherrybrandy = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Veteran').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    lightrum = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Van Vleet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    maplesyrup = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Van Vleet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maple syrup').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Van Vleet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    halfandhalf = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Half-and-half').first().id
        )
    limeade = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Limeade').first().id
        )
    vodka = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=7,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Peel').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    sprite = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Slime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    limejuice = RecipeIngredient(
            amount=NaN,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Slime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='1/2 shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Slime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    vodka = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    tonicwater = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic Water').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Peel').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    olive = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Olive').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vermouth Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    cremedecassis = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vermouth Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    vodka = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victory Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victory Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    grapejuice = RecipeIngredient(
            amount=3,
            unit='oz unsweetened',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victory Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grape juice').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victory Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victory Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka And Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    apricotbrandy = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Valencia Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Valencia Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    orangebitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Valencia Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    scotch = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whisky Mac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    wine = RecipeIngredient(
            amount=1,
            unit='oz green ginger',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whisky Mac').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    gin = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    redwine = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    lemon = RecipeIngredient(
            amount=2,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    orange = RecipeIngredient(
            amount=3,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    redwine = RecipeIngredient(
            amount=2,
            unit='oz white or',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    lemonlimesoda = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    tequila = RecipeIngredient(
            amount=1,
            unit='2/3 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    campari = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    limejuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    orangejuice = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    rosemarysyrup = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosemary Syrup').first().id
        )
    salt = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    blendedwhiskey = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='of 1/2',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=NaN,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    cherry = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    lemon = RecipeIngredient(
            amount=NaN,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    coffeeliqueur = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee liqueur').first().id
        )
    tequila = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    grapefruitjuice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    limejuice = RecipeIngredient(
            amount=NaN,
            unit='of 1',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    agavesyrup = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Agave Syrup').first().id
        )
    pepper = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepper').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    whitewine = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Wine').first().id
        )
    strawberries = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    apple = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple').first().id
        )
    applebrandy = RecipeIngredient(
            amount=3,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple Brandy').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whitecap Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    tequila = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whitecap Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    creamofcoconut = RecipeIngredient(
            amount=NaN,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whitecap Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream of coconut').first().id
        )
    limejuice = RecipeIngredient(
            amount=3,
            unit='tbsp fresh',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whitecap Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    triplesec = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Waikiki Beachcomber').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    gin = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Waikiki Beachcomber').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Waikiki Beachcomber').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    whiterum = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yellow Bird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Rum').first().id
        )
    galliano = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yellow Bird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    triplesec = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yellow Bird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    limejuice = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yellow Bird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    yoghurt = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yoghurt Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    fruit = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Yoghurt Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fruit').first().id
        )
    sambuca = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    whitecremedementhe = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorro').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    peachtreeschnapps = RecipeIngredient(
            amount=4,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peachtree schnapps').first().id
        )
    surge = RecipeIngredient(
            amount=4,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Surge').first().id
        )
    cocacola = RecipeIngredient(
            amount=0,
            unit='slice
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zoksel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    rum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    goldrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gold rum').first().id
        )
    151proofrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    pernod = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pernod').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=1,
            unit='drop',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    sambuca = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zambeer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    rootbeer = RecipeIngredient(
            amount=NaN,
            unit='10 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zambeer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Root beer').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zambeer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='1/4 oz stoli',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorbatini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ouzo = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorbatini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ouzo').first().id
        )
    jägermeister = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zenmeister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    rootbeer = RecipeIngredient(
            amount=NaN,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zenmeister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Root beer').first().id
        )
    chambordraspberryliqueur = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zipperhead').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    vodka = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zipperhead').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    sodawater = RecipeIngredient(
            amount=NaN,
            unit='with',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zipperhead').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    zima = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zima Blaster').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Zima').first().id
        )
    chambordraspberryliqueur = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zima Blaster').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    cointreau = RecipeIngredient(
            amount=5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zizi Coin-coin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    lemonjuice = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zizi Coin-coin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ice = RecipeIngredient(
            amount=NaN,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zizi Coin-coin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    lemon = RecipeIngredient(
            amount=0,
            unit='or lime
    ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zizi Coin-coin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    midorimelonliqueur = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zimadori Zinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    zima = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zimadori Zinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Zima').first().id
        )
    amaretto = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zippy's Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    rum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zippy's Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    koolaid = RecipeIngredient(
            amount=4,
            unit='oz grape',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zippy's Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kool-Aid').first().id
        )
    vermouth = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ziemes Martini Apfelsaft').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vermouth').first().id
        )
    applejuice = RecipeIngredient(
            amount=16,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ziemes Martini Apfelsaft').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )


    db.session.add(gin)
    db.session.add(grandmarnier)

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
