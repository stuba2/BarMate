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


    a = RecipeIngredient(
            amount=0.75,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    b = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    c = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    d = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    e = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'ABC').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    f = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'ABC').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    g = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'ABC').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    h = RecipeIngredient(
            amount=2,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    i = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    j = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    k = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    l = RecipeIngredient(
            amount=1,
            unit='fresh',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg White').first().id
        )
    m = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'ACID').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    n = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'ACID').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wild Turkey').first().id
        )
    o = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    p = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    q = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    r = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'AT&T').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    s = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'AT&T').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    t = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'AT&T').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic water').first().id
        )
    u = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A. J.').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Applejack').first().id
        )
    v = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A. J.').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    w = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affair').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberry schnapps').first().id
        )
    x = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affair').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    y = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affair').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    z = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    aa = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit juice').first().id
        )
    ab = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    ac = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ad = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ae = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pisang Ambon').first().id
        )
    af = RecipeIngredient(
            amount=6,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    ag = RecipeIngredient(
            amount=0.5,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ah = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abilene').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    ai = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abilene').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach nectar').first().id
        )
    aj = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abilene').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ak = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    al = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vermouth').first().id
        )
    am = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almeria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    an = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almeria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ao = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almeria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ap = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    aq = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    ar = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    as1 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    at = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    au = RecipeIngredient(
            amount=1,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    av = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    aw = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    ax = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ay = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    az = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Applejack').first().id
        )
    ba = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    bb = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    bc = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aviation').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    bd = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aviation').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon juice').first().id
        )
    be = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aviation').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'maraschino liqueur').first().id
        )
    bf = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    bg = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    bh = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    bi = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    bj = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    bk = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addington').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    bl = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addington').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    bm = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addington').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    bn = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'After sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    bo = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'After sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Banane').first().id
        )
    bp = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afterglow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    bq = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afterglow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    br = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afterglow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    bs = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    bt = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    bu = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Frangelico').first().id
        )
    bv = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    bw = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    bx = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    by = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    bz = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Algonquin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    ca = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Algonquin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    cb = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Algonquin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    cc = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    cd = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    ce = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberry brandy').first().id
        )
    cf = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    cg = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ch = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ci = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    cj = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ck = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    cl = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applejack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jack Daniels').first().id
        )
    cm = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applejack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    cn = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Applejack').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    co = RecipeIngredient(
            amount=1.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    cp = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    cq = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    cr = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autodafé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    cs = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autodafé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    ct = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalanche').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Crown Royal').first().id
        )
    cu = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalanche').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    cv = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Avalanche').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    cw = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    cx = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    cy = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    cz = RecipeIngredient(
            amount=0.125,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lemon Juice').first().id
        )
    da = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Joy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    dc = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Joy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    dd = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Joy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    de = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angel Face').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    df = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angel Face').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple brandy').first().id
        )
    dg = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angel Face').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dh = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aquamarine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hpnotiq').first().id
        )
    di = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aquamarine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    dj = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aquamarine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana Liqueur').first().id
        )
    dk = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dl = RecipeIngredient(
            amount=1,
            unit='oz green ginger',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    dm = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    dn = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    do = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    dp = RecipeIngredient(
            amount=50,
            unit='gr',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    dq = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anise').first().id
        )
    dr = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Licorice root').first().id
        )
    ds = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wormwood').first().id
        )
    dt = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Kurant').first().id
        )
    du = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    dv = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    dw = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    dx = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    dy = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grape soda').first().id
        )
    dz = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ea = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    eb = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Candy').first().id
        )
    ec = RecipeIngredient(
            amount=1,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ed = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ee = RecipeIngredient(
            amount=7,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ef = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    eg = RecipeIngredient(
            amount=0.5,
            unit='blender',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    eh = RecipeIngredient(
            amount=0.5,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ei = RecipeIngredient(
            amount=0.5,
            unit='blender',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    ej = RecipeIngredient(
            amount=10,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ek = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    el = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    em = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped cream').first().id
        )
    en = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Grande').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    eo = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Grande').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple cider').first().id
        )
    ep = RecipeIngredient(
            amount=2,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Karate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    eq = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Karate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Carrot').first().id
        )
    er = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    es = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    et = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    eu = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ev = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    ew = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    ex = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ey = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ez = RecipeIngredient(
            amount=45,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice cordial').first().id
        )
    fa = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    fb = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    fc = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    fd = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit syrup').first().id
        )
    fe = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ff = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    fg = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    fh = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    fi = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    fj = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    fk = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    fl = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    fm = RecipeIngredient(
            amount=15,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Wine').first().id
        )
    fn = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    fo = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Mist').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    fp = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Mist').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    fq = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    fr = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    fs = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    ft = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    fu = RecipeIngredient(
            amount=100,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aperol Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Aperol').first().id
        )
    fv = RecipeIngredient(
            amount=150,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aperol Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    fw = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aperol Spritz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    fx = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '7-Up').first().id
        )
    fy = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple schnapps').first().id
        )
    fz = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    ga = RecipeIngredient(
            amount=4,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    gb = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    gc = RecipeIngredient(
            amount=4,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '7-Up').first().id
        )
    gd = RecipeIngredient(
            amount=0.5,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ge = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arise My Love').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    gf = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arise My Love').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Creme de Menthe').first().id
        )
    gg = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    gh = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    gi = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    gj = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    gk = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Piece of Ass').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    gl = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Piece of Ass').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    gm = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Piece of Ass').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    gn = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    go = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    gp = RecipeIngredient(
            amount=0.25,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    gq = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    gr = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alfie Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon vodka').first().id
        )
    gs = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alfie Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    gt = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alfie Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    gu = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    gv = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    gw = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    gx = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream').first().id
        )
    gy = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate ice-cream').first().id
        )
    gz = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    ha = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    hb = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    hc = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple Schnapps').first().id
        )
    hd = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    he = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    hf = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    hg = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    hh = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Addison Special').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    hi = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adonis Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    hj = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adonis Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    hk = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adonis Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    hl = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    hm = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    hn = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    ho = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    hp = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    hq = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    hr = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yellow Chartreuse').first().id
        )
    hs = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ht = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allies Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    hu = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allies Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    hv = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Allies Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kummel').first().id
        )
    hw = RecipeIngredient(
            amount=0.5,
            unit='jigger',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    hx = RecipeIngredient(
            amount=3,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    hy = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    hz = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ia = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ib = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    ic = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gold tequila').first().id
        )
    ie = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ig = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    ih = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream of coconut').first().id
        )
    ii = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ij = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ik = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    il = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    im = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    io = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ip = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    iq = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    ir = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rye whiskey').first().id
        )
    it = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Red wine').first().id
        )
    iu = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    iv = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    iw = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    ix = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    iy = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    iz = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ja = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    jb = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    jc = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Banane').first().id
        )
    jd = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    je = RecipeIngredient(
            amount=0.75,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    jf = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot').first().id
        )
    jg = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Almond flavoring').first().id
        )
    jh = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grain alcohol').first().id
        )
    ji = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    jj = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    jk = RecipeIngredient(
            amount=3,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    jl = RecipeIngredient(
            amount=6,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    jm = RecipeIngredient(
            amount=2,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    jn = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Glycerine').first().id
        )
    jo = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    jp = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stinger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    jq = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    jr = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    js = RecipeIngredient(
            amount=0.25,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunrise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    jt = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angelica root').first().id
        )
    ju = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Almond').first().id
        )
    jv = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Allspice').first().id
        )
    jw = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    jx = RecipeIngredient(
            amount=3,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Anise').first().id
        )
    jy = RecipeIngredient(
            amount=0.125,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coriander').first().id
        )
    jz = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Marjoram leaves').first().id
        )
    ka = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    kb = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    kc = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    kd = RecipeIngredient(
            amount=1,
            unit='drop',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    ke = RecipeIngredient(
            amount=1,
            unit='drop',
            recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    kf = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Mouthwash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maui').first().id
        )
    kg = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Mouthwash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mountain Dew').first().id
        )
    kh = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Mouthwash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ki = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Stingers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    kj = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Stingers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Iced tea').first().id
        )
    kk = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    kl = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    km = RecipeIngredient(
            amount=2.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger Beer').first().id
        )
    kn = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    ko = RecipeIngredient(
            amount=0.67,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Evergreen').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    kp = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Evergreen').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pisang Ambon').first().id
        )
    kq = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Evergreen').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    kr = RecipeIngredient(
            amount=0.67,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    ks = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    kt = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    ku = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tonic water').first().id
        )
    kv = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    kw = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    kx = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut liqueur').first().id
        )
    ky = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    kz = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    la = RecipeIngredient(
            amount=0.75,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    lb = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    lc = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guava juice').first().id
        )
    ld = RecipeIngredient(
            amount=1.5,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    le = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple').first().id
        )
    lf = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    lg = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    lh = RecipeIngredient(
            amount=4,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple cider').first().id
        )
    li = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brown sugar').first().id
        )
    lj = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    lk = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ll = RecipeIngredient(
            amount=6,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cloves').first().id
        )
    lm = RecipeIngredient(
            amount=6,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Allspice').first().id
        )
    ln = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    lo = RecipeIngredient(
            amount=3,
            unit='sticks',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    lp = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Auburn Headbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    lq = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Auburn Headbanger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    lr = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut rum').first().id
        )
    ls = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    lt = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    lu = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    lv = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Furlong Too Late').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    lw = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Furlong Too Late').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger beer').first().id
        )
    lx = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Furlong Too Late').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ly = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    lz = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    ma = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    mb = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    mc = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    md = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto And Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    me = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto And Cream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    mf = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Antifreeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    mg = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Antifreeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    mh = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Antifreeze').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and sour').first().id
        )
    mi = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan\'s Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    mj = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan\'s Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    mk = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan\'s Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ml = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan\'s Island').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    mm = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Fabulous').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    mn = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Fabulous').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry Juice').first().id
        )
    mo = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Fabulous').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    mp = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice in Wonderland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    mq = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice in Wonderland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    mr = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Alice in Wonderland').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    ms = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    mt = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    mu = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    mv = RecipeIngredient(
            amount=1,
            unit='jigger',
            recipe_id=Recipe.query.filter(Recipe.name == 'A True Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    mw = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'A True Amaretto Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    mx = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    my = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    mz = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    na = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    nb = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Berry Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Berries').first().id
        )
    nc = RecipeIngredient(
            amount=2,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Berry Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple').first().id
        )
    nd = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    ne = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    nf = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    ng = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    nh = RecipeIngredient(
            amount=0.25,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lime Juice').first().id
        )
    ni = RecipeIngredient(
            amount=0.25,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    nj = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    nk = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    nl = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    nm = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    nn = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    no = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Supper Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    np = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Supper Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    nq = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'After Supper Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    nr = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ns = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kirschwasser').first().id
        )
    nt = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberry liqueur').first().id
        )
    nu = RecipeIngredient(
            amount=5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    nv = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Pie with A Crust').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    nw = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Pie with A Crust').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu rum').first().id
        )
    nx = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Apple Pie with A Crust').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    ny = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    nz = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Añejo rum').first().id
        )
    oa = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ob = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    oc = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    od = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    oe = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Chocolate Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    of = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Chocolate Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Creme de Cacao').first().id
        )
    og = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Almond Chocolate Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    oh = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    oi = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    oj = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ok = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot chocolate').first().id
        )
    ol = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Vodka').first().id
        )
    om = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    on = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    oo = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    op = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    oq = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    os = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    ot = RecipeIngredient(
            amount=1,
            unit='splash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ou = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-52').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    ov = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-52').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    ow = RecipeIngredient(
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-52').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ox = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-53').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    oy = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-53').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    oz = RecipeIngredient(
            amount=0.33,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'B-53').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    pa = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Bitters').first().id
        )
    pb = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    pc = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    pd = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    pe = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    pf = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    pg = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ph = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    pi = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    pj = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Big Red').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish cream').first().id
        )
    pk = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Big Red').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    pl = RecipeIngredient(
            amount=6,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    pm = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    pn = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    po = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon juice').first().id
        )
    pp = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    pq = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Mure').first().id
        )
    pr = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    ps = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    pt = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    pu = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    pv = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    pw = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    px = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    py = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    pz = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    qa = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    qb = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rye Whiskey').first().id
        )
    qc = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    qd = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Liqueur').first().id
        )
    qe = RecipeIngredient(
            amount=3,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    qf = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Cherry').first().id
        )
    qg = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    qh = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit juice').first().id
        )
    qi = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    qj = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    qk = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    ql = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    qm = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    qn = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    qo = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    qp = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    qq = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    qr = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    qs = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    qt = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    qu = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brigadier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot Chocolate').first().id
        )
    qv = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brigadier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    qw = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brigadier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry Heering').first().id
        )
    qx = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    qy = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    qz = RecipeIngredient(
            amount=3,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    ra = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wormwood').first().id
        )
    rb = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    rc = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Buccaneer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Corona').first().id
        )
    rd = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Buccaneer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bacardi Limon').first().id
        )
    re = RecipeIngredient(
            amount=1,
            unit='fifth',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Everclear').first().id
        )
    rf = RecipeIngredient(
            amount=1,
            unit='fifth smirnoff red label',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    rg = RecipeIngredient(
            amount=2,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mountain Dew').first().id
        )
    rh = RecipeIngredient(
            amount=2,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Surge').first().id
        )
    ri = RecipeIngredient(
            amount=1,
            unit='small bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    rj = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    rk = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blackthorn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    rl = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blackthorn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    rn = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blackthorn').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    ro = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bob Marley').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Midori melon liqueur').first().id
        )
    rp = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bob Marley').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    rq = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bob Marley').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    rr = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Southern Comfort').first().id
        )
    rs = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    rt = RecipeIngredient(
            amount=2,
            unit='wedges',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ru = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sour mix').first().id
        )
    rv = RecipeIngredient(
            amount=0.25,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    rw = RecipeIngredient(
            amount=0.25,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana liqueur').first().id
        )
    rx = RecipeIngredient(
            amount=0.25,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    ry = RecipeIngredient(
            amount=0.25,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    rz = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bumble Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    sa = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bumble Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    sb = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bumble Bee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    sc = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Eskimo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    sd = RecipeIngredient(
            amount=8,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Eskimo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    se = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Eskimo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla ice-cream').first().id
        )
    sf = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    sg = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    sh = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    si = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    sj = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    sk = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    sl = RecipeIngredient(
            amount=3,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    sm = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    sn = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana liqueur').first().id
        )
    so = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    sp = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    sq = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    sr = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and Sour').first().id
        )
    ss = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brainteaser').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    st = RecipeIngredient(
            amount=30,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brainteaser').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Erin Cream').first().id
        )
    su = RecipeIngredient(
            amount=5,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brainteaser').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Advocaat').first().id
        )
    sv = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    sw = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato juice').first().id
        )
    sx = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sy = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Worcestershire sauce').first().id
        )
    sz = RecipeIngredient(
            amount=2,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    ta = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    tb = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black & Tan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ale').first().id
        )
    tc = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black & Tan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guinness stout').first().id
        )
    td = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Lagoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    te = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Lagoon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    tf = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee\'s Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gold rum').first().id
        )
    tg = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee\'s Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    th = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee\'s Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ti = RecipeIngredient(
            amount=2,
            unit='jiggers',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bee\'s Knees').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    tj = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    tk = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    tl = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    tm = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    tn = RecipeIngredient(
            amount=0.125,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    to = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    tp = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    tq = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    tr = RecipeIngredient(
            amount=0.5,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    ts = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    tt = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla Ice-Cream').first().id
        )
    tu = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butterscotch schnapps').first().id
        )
    tv = RecipeIngredient(
            amount=1,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    tw = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    tx = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    ty = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    tz = RecipeIngredient(
            amount=1.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rye whiskey').first().id
        )
    ua = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    ub = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    uc = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ud = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    ue = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    uf = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    ug = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    uh = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut liqueur').first().id
        )
    ui = RecipeIngredient(
            amount=1,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    uj = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sprite').first().id
        )
    uk = RecipeIngredient(
            amount=10,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ul = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    um = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    un = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    uo = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    up = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raisins').first().id
        )
    uq = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blueberries').first().id
        )
    ur = RecipeIngredient(
            amount=2,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Everclear').first().id
        )
    us = RecipeIngredient(
            amount=1,
            unit='bottle boone strawberry hill',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    ut = RecipeIngredient(
            amount=0.5,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    uu = RecipeIngredient(
            amount=1,
            unit='gal',
            recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kool-Aid').first().id
        )
    uv = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    uw = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tomato juice').first().id
        )
    ux = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    uy = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    uz = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Celery salt').first().id
        )
    va = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    vb = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    vc = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Godiva liqueur').first().id
        )
    vd = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    ve = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butterscotch schnapps').first().id
        )
    vf = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    vg = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Añejo rum').first().id
        )
    vh = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tia maria').first().id
        )
    vi = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    vj = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    vk = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    vl = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    vm = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coconut Liqueur').first().id
        )
    vn = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blueberries').first().id
        )
    vo = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    vp = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    vq = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    vr = RecipeIngredient(
            amount=20,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cassis').first().id
        )
    vs = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lime Juice').first().id
        )
    vt = RecipeIngredient(
            amount=75,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger beer').first().id
        )
    vu = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    vv = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    vw = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    vx = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    vy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    vz = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    wa = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    wb = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    wc = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chambord raspberry liqueur').first().id
        )
    wd = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peachtree schnapps').first().id
        )
    we = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    wf = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee liqueur').first().id
        )
    wg = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    wh = RecipeIngredient(
            amount=2,
            unit='1/2 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Guinness').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    wi = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Baby Guinness').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    wj = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    wk = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    wl = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    wm = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    wn = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    wo = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    wp = RecipeIngredient(
            amount=4,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    wq = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    wr = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passoa').first().id
        )
    ws = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    wt = RecipeIngredient(
            amount=6,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet and Sour').first().id
        )
    wu = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    wv = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    ww = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    wx = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    wy = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    wz = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    xa = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    xb = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    xc = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    xd = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cream Pi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Malibu Rum').first().id
        )
    xe = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cream Pi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana Liqueur').first().id
        )
    xf = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cream Pi').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    xg = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    xh = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    xi = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    xj = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    xk = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    xl = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    xm = RecipeIngredient(
            amount=8,
            unit='cubes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    xn = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    xo = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach nectar').first().id
        )
    xp = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach schnapps').first().id
        )
    xq = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    xr = RecipeIngredient(
            amount=0.5,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black and Brown').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guinness stout').first().id
        )
    xs = RecipeIngredient(
            amount=0.5,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black and Brown').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Root beer').first().id
        )
    xt = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    xu = RecipeIngredient(
            amount=1,
            unit='oz white',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    xv = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Alexander').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    xw = RecipeIngredient(
            amount=1,
            unit='3/4 oz bacardi',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    xx = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    xy = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    xz = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    ya = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    yb = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    yc = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Surge').first().id
        )
    yd = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    ye = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark Rum').first().id
        )
    yf = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    yg = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    yh = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blueberries').first().id
        )
    yi = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon-lime soda').first().id
        )
    yj = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bermuda Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    yk = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bermuda Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    yl = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bermuda Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    ym = RecipeIngredient(
            amount=50,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry Vodka').first().id
        )
    yn = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry Juice').first().id
        )
    yo = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    yp = RecipeIngredient(
            amount=10,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blue Curacao').first().id
        )
    yq = RecipeIngredient(
            amount=10,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    yr = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    ys = RecipeIngredient(
            amount=1,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    yt = RecipeIngredient(
            amount=10,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    yu = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    yv = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar syrup').first().id
        )
    yw = RecipeIngredient(
            amount=0.5,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    yx = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brave Bull Shooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    yy = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brave Bull Shooter').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    yz = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Black Forest Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    za = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    zb = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    zc = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    zd = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ze = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bailey\'s Dream Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    zf = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bailey\'s Dream Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla ice-cream').first().id
        )
    zg = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    zh = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Scotch').first().id
        )
    zi = RecipeIngredient(
            amount=1,
            unit='1/4 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    zj = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    zk = RecipeIngredient(
            amount=0.5,
            unit='lb',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    zl = RecipeIngredient(
            amount=1,
            unit='frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    zm = RecipeIngredient(
            amount=1,
            unit='cup plain',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    zn = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    zo = RecipeIngredient(
            amount=0,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    zp = RecipeIngredient(
            amount=3,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla Ice-Cream').first().id
        )
    zq = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    zr = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Godiva liqueur').first().id
        )
    zs = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped Cream').first().id
        )
    zt = RecipeIngredient(
            amount=4,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'caramel sauce').first().id
        )
    zu = RecipeIngredient(
            amount=4,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'chocolate sauce').first().id
        )
    zv = RecipeIngredient(
            amount=15,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mini-snickers bars').first().id
        )
    zw = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cantaloupe Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cantaloupe').first().id
        )
    zx = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cantaloupe Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    zy = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandon and Will\'s Coke Float').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla ice-cream').first().id
        )
    zz = RecipeIngredient(
            amount=1,
            unit='can',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandon and Will\'s Coke Float').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    qqq = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Brandon and Will\'s Coke Float').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    qqw = RecipeIngredient(
            amount=0.5,
            unit='lb',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Strawberries').first().id
        )
    qqe = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    qqr = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake Daiquiri').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apple juice').first().id
        )
    qqt = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    qqy = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    qqu = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    qqi = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    qqo = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    qqp = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cafe Savoy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    qqa = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cafe Savoy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    qqs = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    qqd = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    qqf = RecipeIngredient(
            amount=2,
            unit='1/2 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirinha').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cachaca').first().id
        )
    qqg = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cream Soda').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Spiced rum').first().id
        )
    qqh = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    qqj = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    qqk = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    qql = RecipeIngredient(
            amount=1.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Rum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    qqz = RecipeIngredient(
            amount=1,
            unit='1/2 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Rum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    qqx = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Rum').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light cream').first().id
        )
    qqc = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libre').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    qqv = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libre').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    qqb = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    qqn = RecipeIngredient(
            amount=.033,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Falernum').first().id
        )
    qqm = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    qwq = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Añejo rum').first().id
        )
    qww = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'blackstrap rum').first().id
        )
    qwe = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Citrus Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bacardi Limon').first().id
        )
    qwr = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Citrus Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    qwt = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    qwy = RecipeIngredient(
            amount=1,
            unit='1/2 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    qwu = RecipeIngredient(
            amount=1,
            unit='1/2 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    qwi = RecipeIngredient(
            amount=1,
            unit='1/2 tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    qwo = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    qwp = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    qwa = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    qws = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    qwd = RecipeIngredient(
            amount=2,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    qwf = RecipeIngredient(
            amount=2,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    qwg = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White rum').first().id
        )
    qwh = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    qwj = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'City Slicker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    qwk = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'City Slicker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    qwl = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'City Slicker').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    qwz = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Campari Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    qwx = RecipeIngredient(
            amount=1,
            unit='1/2 cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Campari Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    qwc = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    qwv = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Port').first().id
        )
    qwb = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    qwn = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    qwm = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    qeq = RecipeIngredient(
            amount=1.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    qew = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    qee = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    qer = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    qet = RecipeIngredient(
            amount=2,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    qey = RecipeIngredient(
            amount=2,
            unit='cups white',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    qeu = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    qei = RecipeIngredient(
            amount=0.5,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla').first().id
        )
    qeo = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    qep = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    qea = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    qes = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    qed = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange bitters').first().id
        )
    qef = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg yolk').first().id
        )
    qeg = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    qeh = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    qej = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lillet Blanc').first().id
        )
    qek = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    qel = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absinthe').first().id
        )
    qez = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate liqueur').first().id
        )
    qex = RecipeIngredient(
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    qec = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    qev = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clove Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    qeb = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clove Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sloe gin').first().id
        )
    qen = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Clove Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Wine').first().id
        )
    qem = RecipeIngredient(
            amount=10,
            unit='tbsp instant',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    qrq = RecipeIngredient(
            amount=4,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    qrw = RecipeIngredient(
            amount=2,
            unit='1/2 cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    qre = RecipeIngredient(
            amount=1,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    qrr = RecipeIngredient(
            amount=2,
            unit='1/2 cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    qrt = RecipeIngredient(
            amount=1,
            unit='dl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coke and Drops').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coca-Cola').first().id
        )
    qry = RecipeIngredient(
            amount=7,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Coke and Drops').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    qru = RecipeIngredient(
            amount=125,
            unit='gr',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    qri = RecipeIngredient(
            amount=0.75,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    qro = RecipeIngredient(
            amount=4,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberry juice').first().id
        )
    qrp = RecipeIngredient(
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    qra = RecipeIngredient(
            amount=4,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    qrs = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Almond flavoring').first().id
        )
    qrd = RecipeIngredient(
            amount=2,
            unit='qt',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    qrf = RecipeIngredient(
            amount=8,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    qrg = RecipeIngredient(
            amount=6,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    qrh = RecipeIngredient(
            amount=1,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grain alcohol').first().id
        )
    qrj = RecipeIngredient(
            amount=1,
            unit='oz pure',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peppermint extract').first().id
        )
    qrk = RecipeIngredient(
            amount=1,
            unit='tbsp green',
            recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Food coloring').first().id
        )
    qrl = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana liqueur').first().id
        )
    qrz = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    qrx = RecipeIngredient(
            amount=2,
            unit='scoops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate ice-cream').first().id
        )
    qrc = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate syrup').first().id
        )
    qrv = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate milk').first().id
        )
    qrb = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whipped cream').first().id
        )
    qrn = RecipeIngredient(
            amount=1,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry').first().id
        )
    qrm = RecipeIngredient(
            amount=1,
            unit='piece',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Banana').first().id
        )
    qtq = RecipeIngredient(
            amount=0.5,
            unit='kg',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Cordial').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cranberries').first().id
        )
    qtw = RecipeIngredient(
            amount=0.75,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Cordial').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    qte = RecipeIngredient(
            amount=0.5,
            unit='l',
            recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Cordial').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    qtr = RecipeIngredient(
            amount=6,
            unit='cups',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    qtt = RecipeIngredient(
            amount=3,
            unit='oz mexican',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    qty = RecipeIngredient(
            amount=1,
            unit='tsp powdered',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cinnamon').first().id
        )
    qtu = RecipeIngredient(
            amount=3,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg').first().id
        )
    qti = RecipeIngredient(
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    qto = RecipeIngredient(
            amount=1,
            unit='piece',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    qtp = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    qta = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    qts = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cognac').first().id
        )
    qtd = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended whiskey').first().id
        )
    qtf = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    qtg = RecipeIngredient(
            amount=1,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    qth = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    qtj = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    qtk = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Root Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    qtl = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Root Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    qtz = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'California Root Beer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    qtx = RecipeIngredient(
            amount=2,
            unit='shots',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    qtc = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    qtv = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg White').first().id
        )
    qtb = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bitters').first().id
        )
    qtn = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    qtm = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    cointreau = RecipeIngredient(
            amount=0.5,
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
            amount=0.5,
            unit='juice',
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
            amount=0.5,
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
            amount=1.33,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Orange Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cocoapowder = RecipeIngredient(
            amount=0.5,
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
            amount=0.5,
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
    gin28 = RecipeIngredient(
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
    gin29 = RecipeIngredient(
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
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Diesel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    cider = RecipeIngredient(
            amount=0.5,
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
            amount=0.5,
            unit='juice',
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
    proofrum = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Downshift').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    gin30 = RecipeIngredient(
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
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dragonfly').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    gin31 = RecipeIngredient(
            amount=1.67,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=0.33,
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
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Dry Rob Roy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    vodka = RecipeIngredient(
            amount=2,
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
            amount=1,
            unit='top off',
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
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pisco').first().id
        )
    limejuice = RecipeIngredient(
            amount=2.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    pineapplesyrup = RecipeIngredient(
            amount=2.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Syrup').first().id
        )
    stgermain = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'St. Germain').first().id
        )
    angosturabitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    pepper = RecipeIngredient(
            amount=1,
            unit='pinch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepper').first().id
        )
    lavender = RecipeIngredient(
            amount=2,
            unit='sprigs',
            recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
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
    gin32 = RecipeIngredient(
            amount=0.75,
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
            unit='twist',
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
            amount=6,
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
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla').first().id
        )
    chocolate = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate').first().id
        )
    whippedcream = RecipeIngredient(
            amount=1,
            unit='garnish',
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
            amount=1,
            unit='top off',
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
            unit='oz',
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
            amount=0.25,
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
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    bourbon = RecipeIngredient(
            amount=0.25,
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
            amount=0.25,
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
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    sugar = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    nutmeg = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    brandy = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    gin33 = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Highball').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=0.75,
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
            amount=0.5,
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
            amount=0.5,
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
            amount=0.75,
            unit='cup',
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
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    gin34 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=0.75,
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
    lemonjuice30 = RecipeIngredient(
            amount=0.25,
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
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    salt = RecipeIngredient(
            amount=0.25,
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
            recipe_id=Recipe.query.filter(Recipe.name == 'Empellón Cocina\'s Fat-Washed Mezcal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mezcal').first().id
        )
    chocolateliqueur = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Empellón Cocina\'s Fat-Washed Mezcal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate liqueur').first().id
        )
    coffeeliqueur = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Empellón Cocina\'s Fat-Washed Mezcal').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee liqueur').first().id
        )
    rose = RecipeIngredient(
            amount=750,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frosé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rose').first().id
        )
    sugar = RecipeIngredient(
            amount=0.5,
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
    lemonjuice31 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frosé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    coffee = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frappé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    milk = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frappé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frappé').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    amaretto = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Foxy Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=0.5,
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
    gin35 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sugar = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    lemonjuice32 = RecipeIngredient(
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
            amount=1,
            unit='top off',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    lemon = RecipeIngredient(
            amount=0.25,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    lime = RecipeIngredient(
            amount=0.5,
            unit='juice',
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
            amount=0.5,
            unit='unit',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Freddy Kruger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    sambuca = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Freddy Kruger').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    vodka = RecipeIngredient(
            amount=0.5,
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
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    sodawater = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    coffee = RecipeIngredient(
            amount=0.5,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fuzzy Asshole').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    peachschnapps = RecipeIngredient(
            amount=0.5,
            unit='glass',
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
    gin36 = RecipeIngredient(
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Fahrenheit 5000').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Firewater').first().id
        )
    absolutpeppar = RecipeIngredient(
            amount=0.5,
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
    gin37 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flying Dutchman').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=0.5,
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
            amount=0.25,
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
            amount=0.75,
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
    proofrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    drpepper = RecipeIngredient(
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
            amount=0.25,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flander\'s Flake-Out').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sambuca').first().id
        )
    sarsaparilla = RecipeIngredient(
            amount=0.75,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Flander\'s Flake-Out').first().id,
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
            amount=0.5,
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
    gin38 = RecipeIngredient(
            amount=2,
            unit='1/2 oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    limejuice = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='unit',
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
    gin39 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemon = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    gin40 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice33 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    orange = RecipeIngredient(
            amount=1,
            unit='slice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino cherry').first().id
        )
    peachvodka = RecipeIngredient(
            amount=5,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gagliardo').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach Vodka').first().id
        )
    lemonjuice34 = RecipeIngredient(
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
            amount=0.75,
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
            amount=0.75,
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
    gin41 = RecipeIngredient(
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Tonic').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    gin42 = RecipeIngredient(
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
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    gin43 = RecipeIngredient(
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
    gin44 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice35 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    grenadine = RecipeIngredient(
            amount=0.5,
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
    gin103 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice36 = RecipeIngredient(
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Lemon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    gin45 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemon = RecipeIngredient(
            amount=0.5,
            unit='juice',
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
            amount=1,
            unit='twist',
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
    gin46 = RecipeIngredient(
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
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'lemon').first().id
        )
    sodawater = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    gin47 = RecipeIngredient(
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
    gin48 = RecipeIngredient(
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
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    gin49 = RecipeIngredient(
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
    gin50 = RecipeIngredient(
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
            amount=0.5,
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
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grasshopper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Creme de Menthe').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grasshopper').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    lightcream = RecipeIngredient(
            amount=0.75,
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
    proofrum = RecipeIngredient(
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
    gin51 = RecipeIngredient(
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
            amount=0.25,
            unit='juice',
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
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Green Goblin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    lager = RecipeIngredient(
            amount=0.5,
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
    gin52 = RecipeIngredient(
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
    gin53 = RecipeIngredient(
            amount=6,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Basil Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice37 = RecipeIngredient(
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
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gin Basil Smash').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Basil').first().id
        )
    gin54 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman\'s Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    brandy = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman\'s Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman\'s Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    clubsoda = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman\'s Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Club soda').first().id
        )
    cachaca = RecipeIngredient(
            amount=25,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Girl From Ipanema').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cachaca').first().id
        )
    lemonjuice38 = RecipeIngredient(
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Girl From Ipanema').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Champagne').first().id
        )
    gin55 = RecipeIngredient(
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
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Garibaldi Negroni').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Peel').first().id
        )
    darkrum = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    vodka = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    triplesec = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    tequila = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    melonliqueur = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Melon liqueur').first().id
        )
    mountaindew = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mountain Dew').first().id
        )
    grapes = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grape lemon pineapple Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapes').first().id
        )
    lemon = RecipeIngredient(
            amount=0.25,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Grape lemon pineapple Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    pineapple = RecipeIngredient(
            amount=0.5,
            unit='unit',
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
    lemonjuice39 = RecipeIngredient(
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Herbal flame').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='long strip',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse\'s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    brandy = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse\'s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    gingerale = RecipeIngredient(
            amount=5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse\'s Neck').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    bitters = RecipeIngredient(
            amount=2,
            unit='dashes',
            recipe_id=Recipe.query.filter(Recipe.name == 'Horse\'s Neck').first().id,
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
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter\'s Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vermouth').first().id
        )
    maraschinocherry = RecipeIngredient(
            amount=15,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter\'s Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino Cherry').first().id
        )
    sugarsyrup = RecipeIngredient(
            amount=10,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter\'s Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    lemonade = RecipeIngredient(
            amount=100,
            unit='ml',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter\'s Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    blackberries = RecipeIngredient(
            amount=2,
            unit='',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hunter\'s Moon').first().id,
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
    lemonjuice40 = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Havana Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    carbonatedsoftdrink = RecipeIngredient(
            amount=1,
            unit='top off',
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
            amount=0.75,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Creamy Bush').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    coffee = RecipeIngredient(
            amount=6,
            unit='oz',
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
            amount=0.5,
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
    gin56 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hawaiian Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=0.5,
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
            amount=0.75,
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
            amount=0.5,
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
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Marshmallows').first().id
        )
    lime = RecipeIngredient(
            amount=0.5,
            unit='unit',
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger ale').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='top off',
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
    lemonjuice41 = RecipeIngredient(
            amount=1,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ice Pick').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    coffee = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    sugar = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    water = RecipeIngredient(
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    milk = RecipeIngredient(
            amount=4,
            unit='cups',
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
             amount=1.25,
            unit='cup',
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
            amount=0.5,
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
            amount=0.5,
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
            amount=0.5,
            unit='juice',
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Russian').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Guinness stout').first().id
        )
    limejuice = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    gin104 = RecipeIngredient(
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee Fillip').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    bourbon = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    vodka = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    orangejuice = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    baileysirishcream = RecipeIngredient(
            amount=0.67,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jam Donut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Baileys irish cream').first().id
        )
    chambordraspberryliqueur = RecipeIngredient(
            amount=0.33,
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
    gin57 = RecipeIngredient(
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
            amount=1,
            unit='pinch',
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
            amount=1,
            unit='top off',
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaica Kiss').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    bourbon = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    lemonjuice42 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp',
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
            amount=0.5,
            unit='juice',
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
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Egg white').first().id
        )
    rum = RecipeIngredient(
            amount=0.167,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaican Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    coffee = RecipeIngredient(
            amount=0.167,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jamaican Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    water = RecipeIngredient(
            amount=0.5,
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
    gin58 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jewel Of The Nile').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    greenchartreuse = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jewel Of The Nile').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Green Chartreuse').first().id
        )
    yellowchartreuse = RecipeIngredient(
            amount=0.5,
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
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack Rose Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack\'s Vanilla Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    tennesseewhiskey = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack\'s Vanilla Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tennessee whiskey').first().id
        )
    vanillaextract = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack\'s Vanilla Coke').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vanilla extract').first().id
        )
    cocacola = RecipeIngredient(
            amount=4,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Jack\'s Vanilla Coke').first().id,
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
            amount=1,
            unit='top off',
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kurant Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='to taste',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kioki Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    kiwi = RecipeIngredient(
            amount=0.5,
            unit='unit',
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
            amount=1,
            unit='garnish',
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
            amount=1,
            unit='top off',
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
    proofrum = RecipeIngredient(
            amount=2,
            unit='oz light',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool First Aid').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    koolaid = RecipeIngredient(
            amount=0.5,
            unit='tsp',
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
            amount=0.5,
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky Colonel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Benedictine').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky Colonel').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    koolaid = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Slammer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kool-Aid').first().id
        )
    vodka = RecipeIngredient(
            amount=0.5,
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
            amount=0.5,
            unit='unit',
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
            amount=0.25,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kill the cold Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    water = RecipeIngredient(
            amount=1,
            unit='cup ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Kill the cold Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='juice',
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
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Limeade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda water').first().id
        )
    beer = RecipeIngredient(
            amount=0.75,
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
             amount=1.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Drop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    cointreau = RecipeIngredient(
             amount=1.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Drop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Drop').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    galliano = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Galliano').first().id
        )
    absolutcitron = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absolut Citron').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='wedge',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='garnish',
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
            amount=0.5,
            unit='whole',
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
            amount=1,
            unit='top off',
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
            amount=1,
            unit='garnish',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Drambuie').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    gin59 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'London Town').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=0.5,
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
            amount=0.5,
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
            amount=1,
            unit='pinch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    lemonjuice43 = RecipeIngredient(
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lord And Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tia maria').first().id
        )
    gin60 = RecipeIngredient(
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
            amount=0.5,
            unit='juice',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    lightrum = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    gin61 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    tequila = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    lemon = RecipeIngredient(
            amount=0.5,
            unit='juice',
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
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lone Tree Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    gin62 = RecipeIngredient(
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lazy Coconut Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    vodka = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    tequila = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    lightrum = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    gin63 = RecipeIngredient(
            amount=0.5,
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
            amount=1,
            unit='twist',
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
            amount=0.33,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Elderflower Spritzer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    freshlemonjuice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Elderflower Spritzer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fresh Lemon Juice').first().id
        )
    yoghurt = RecipeIngredient(
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Yoghurt').first().id
        )
    water = RecipeIngredient(
            amount=1.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    cuminseed = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cumin seed').first().id
        )
    salt = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Salt').first().id
        )
    mint = RecipeIngredient(
            amount=0.25,
            unit='tsp ',
            recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    honey = RecipeIngredient(
            amount=1,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Melya').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    lightrum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='juice',
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
            amount=2,
            unit='sprig',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    champagne = RecipeIngredient(
            amount=1,
            unit='glass',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orgeat syrup').first().id
        )
    triplesec = RecipeIngredient(
            amount=0.5,
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
    gin64 = RecipeIngredient(
            amount=1.67,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    olive = RecipeIngredient(
            amount=1,
            unit='unit',
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
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Hot Sauce').first().id
        )
    worcestershiresauce = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Worcestershire Sauce').first().id
        )
    soysauce = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soy Sauce').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=0.75,
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
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura bitters').first().id
        )
    ice = RecipeIngredient(
            amount=2,
            unit='cube',
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
            unit='twist',
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
            amount=0.5,
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
            amount=1,
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
    gin65 = RecipeIngredient(
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
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moranguito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Absinthe').first().id
        )
    tequila = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moranguito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    grenadine = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Moranguito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    proofrum = RecipeIngredient(
            amount=5,
            unit='oz bacardi',
            recipe_id=Recipe.query.filter(Recipe.name == 'Miami Vice').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    pinacoladamix = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Miami Vice').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pina colada mix').first().id
        )
    daiquirimix = RecipeIngredient(
            amount=1,
            unit='unit',
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
            amount=0.25,
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
            amount=3,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    ginger = RecipeIngredient(
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    cardamom = RecipeIngredient(
            amount=3,
            unit='units',
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
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Black pepper').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    milk = RecipeIngredient(
            amount=1,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Milk').first().id
        )
    gin66 = RecipeIngredient(
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
            amount=1,
            unit='unit',
            recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cucumber').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='unit',
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
            amount=1,
            unit='sprig',
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    sodawater = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    mango = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mango').first().id
        )
    mint = RecipeIngredient(
            amount=0.5,
            unit='handful',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    lemonjuice44 = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    darkrum = RecipeIngredient(
            amount=.0125,
            unit='l jamaican',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    clubsoda = RecipeIngredient(
            amount=.0125,
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
    gin67 = RecipeIngredient(
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
            amount=0.5,
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
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Mint').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'White Creme de Menthe').first().id
        )
    cream = RecipeIngredient(
            amount=0.75,
            unit='oz',
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
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    grenadine = RecipeIngredient(
            amount=0.5,
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
            recipe_id=Recipe.query.filter(Recipe.name == 'Mother\'s Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Goldschlager').first().id
        )
    butterscotchschnapps = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mother\'s Milk').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Butterscotch schnapps').first().id
        )
    milk = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mother\'s Milk').first().id,
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
            amount=1,
            unit='dash',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Cowboy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Heavy cream').first().id
        )
    gin68 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice45 = RecipeIngredient(
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
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberries').first().id
        )
    sodawater = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    mint = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Mint').first().id
        )
    gin69 = RecipeIngredient(
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
            amount=0.25,
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
            amount=0.25,
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    bourbon = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Bourbon').first().id
        )
    lemon = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    gin70 = RecipeIngredient(
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
            amount=0.5,
            unit='juice',
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
            amount=1,
            unit='top off',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    vodka = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    gin71 = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    bluecuracao = RecipeIngredient(
            amount=0.5,
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
    grandmarnier6 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'New York Lemonade').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    lemonjuice46 = RecipeIngredient(
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
            amount=0.5,
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme de Cacao').first().id
        )
    amaretto = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    triplesec = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    vodka = RecipeIngredient(
            amount=0.5,
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
    lemonjuice47 = RecipeIngredient(
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
            amount=2,
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
            amount=1,
            unit='top off',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Oasis').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    gin72 = RecipeIngredient(
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
            amount=1,
            unit='dash',
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
            amount=0.5,
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
    gin73 = RecipeIngredient(
            amount=1,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    orangejuice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    lemonjuice48 = RecipeIngredient(
            amount=1,
            unit='top off',
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Soda Water').first().id
        )
    rosemary = RecipeIngredient(
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosemary').first().id
        )
    orangepeel = RecipeIngredient(
            amount=1,
            unit='garnish',
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
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Espresso').first().id
        )
    nutmeg = RecipeIngredient(
            amount=0.125,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Nutmeg').first().id
        )
    whiskey = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen\'s Grandmother\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Whiskey').first().id
        )
    beer = RecipeIngredient(
            amount=12,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen\'s Grandmother\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Beer').first().id
        )
    lemonade = RecipeIngredient(
            amount=12,
            unit='oz frozen',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen\'s Grandmother\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemonade').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='cup crushed',
            recipe_id=Recipe.query.filter(Recipe.name == 'Owen\'s Grandmother\'s Revenge').first().id,
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
    gin74 = RecipeIngredient(
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
    gin75 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Gin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    gin76 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    orangecuracao = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Curacao').first().id
        )
    limejuice = RecipeIngredient(
            amount=0.75,
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
    gin77 = RecipeIngredient(
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
    gin78 = RecipeIngredient(
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
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blackberries').first().id
        )
    blendedscotch = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Blended Scotch').first().id
        )
    lemonjuice49 = RecipeIngredient(
            amount=0.75,
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
            amount=0.25,
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
    lemonjuice50 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pisco Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
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
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Peach Bitters').first().id
        )
    mint = RecipeIngredient(
            amount=1,
            unit='garnish',
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
    gin79 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Poppy Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    cremedecacao = RecipeIngredient(
            amount=0.75,
            unit='oz',
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
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dark rum').first().id
        )
    orgeatsyrup = RecipeIngredient(
            amount=0.5,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orgeat syrup').first().id
        )
    orangejuice = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
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
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    pepper = RecipeIngredient(
            amount=1,
            unit='garnish',
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
            amount=0.5,
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
            amount=0.5,
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
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Passion Fruit Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar Syrup').first().id
        )
    passionfruitjuice = RecipeIngredient(
            amount=1,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Passion Fruit Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Passion fruit juice').first().id
        )
    ginger = RecipeIngredient(
            amount=0.25,
            unit='inch',
            recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Gingerale Smoothie').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ginger').first().id
        )
    pineapple = RecipeIngredient(
            amount=0.5,
            unit='unit',
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
            amount=0.5,
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
            amount=0.125,
            unit='tsp',
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
            amount=0.5,
            unit='oz',
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
            amount=250,
            unit='ml',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Queen Elizabeth').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    gin80 = RecipeIngredient(
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
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker\'s Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    brandy = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker\'s Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    lemon = RecipeIngredient(
            amount=0.25,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker\'s Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    raspberrysyrup = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quaker\'s Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Raspberry syrup').first().id
        )
    lightrum = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quarter Deck Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    sherry = RecipeIngredient(
            amount=0.33,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quarter Deck Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sherry').first().id
        )
    lime = RecipeIngredient(
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Quarter Deck Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    gin81 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    apricotbrandy = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Apricot brandy').first().id
        )
    lemonjuice51 = RecipeIngredient(
            amount=0.5,
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
    up = RecipeIngredient(
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
    lemonjuice52 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=0.5,
            unit='tsp',
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
            amount=1,
            unit='bottle',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    gingerale = RecipeIngredient(
            amount=1,
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
            amount=1,
            unit='top off',
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
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    water = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Toddy').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    gin82 = RecipeIngredient(
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
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange juice').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple juice').first().id
        )
    cranberryjuice = RecipeIngredient(
            amount=3,
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rusty Nail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Drambuie').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=1,
            unit='twist',
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
            amount=0.5,
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
            unit='tsp',
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
    gin83 = RecipeIngredient(
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
    gin84 = RecipeIngredient(
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
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rosemary Blue').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosemary').first().id
        )
    gin85 = RecipeIngredient(
            amount=4.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice53 = RecipeIngredient(
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
    gin86 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Royal Gin Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemon = RecipeIngredient(
            amount=0.5,
            unit='juice',
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
            amount=0.5,
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
    proofrum = RecipeIngredient(
            amount=1,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == '151 proof rum').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=0.5,
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
            amount=1,
            unit='twist',
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
    lemonjuice54 = RecipeIngredient(
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
    gin87 = RecipeIngredient(
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
            amount=0.33,
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
            amount=0.33,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smut').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepsi Cola').first().id
        )
    orangejuice = RecipeIngredient(
            amount=0.33,
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
            amount=1,
            unit='splash',
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
            amount=0.5,
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
    lemonjuice55 = RecipeIngredient(
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
            amount=0.5,
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
            amount=0.5,
            unit='tsp',
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
            unit='twist',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cointreau').first().id
        )
    lemonjuice56 = RecipeIngredient(
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
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angostura Bitters').first().id
        )
    orangepeel = RecipeIngredient(
            amount=1,
            unit='garnish',
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
            amount=1,
            unit='garnish',
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
            amount=8,
            unit='oz',
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
            amount=1,
            unit='top off',
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
    gin88 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salty Dog').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    salt = RecipeIngredient(
            amount=0.25,
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
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Powdered sugar').first().id
        )
    lemon = RecipeIngredient(
            amount=0.5,
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
    proofrum = RecipeIngredient(
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
            unit='wedges',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange').first().id
        )
    lime = RecipeIngredient(
            amount=0,
            unit='wedges',
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
            amount=1,
            unit='to taste',
            recipe_id=Recipe.query.filter(Recipe.name == 'Swedish Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sugar').first().id
        )
    cherrybrandy = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Singapore Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cherry brandy').first().id
        )
    grenadine = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Singapore Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    gin89 = RecipeIngredient(
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
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snake Bite (UK)').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    cider = RecipeIngredient(
            amount=0.5,
            unit='pint',
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
            amount=0.5,
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
            amount=0.75,
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lemon = RecipeIngredient(
            amount=0.25,
            unit='juice',
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
            amount=1,
            unit='top off',
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
            amount=0.25,
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
            amount=0.5,
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
            amount=3,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Brandy').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='oz',
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
            amount=0.5,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Shanghai Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grenadine').first().id
        )
    lemon = RecipeIngredient(
            amount=0.25,
            unit='juice',
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
            amount=0.5,
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
            amount=0.5,
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
            amount=0.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Shivers').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Water').first().id
        )
    strawberryschnapps = RecipeIngredient(
            amount=0.5,
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
            amount=1,
            unit='juice',
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
            amount=8,
            unit='units',
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
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snakebite and Black').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lager').first().id
        )
    cider = RecipeIngredient(
            amount=0.5,
            unit='pint',
            recipe_id=Recipe.query.filter(Recipe.name == 'Snakebite and Black').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cider').first().id
        )
    blackcurrantsquash = RecipeIngredient(
            amount=1,
            unit='splash',
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
    gin90 = RecipeIngredient(
            amount=2,
            unit='parts',
            recipe_id=Recipe.query.filter(Recipe.name == 'Surf City Lifesaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    grandmarnier7 = RecipeIngredient(
            amount=0.5,
            unit='part',
            recipe_id=Recipe.query.filter(Recipe.name == 'Surf City Lifesaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grand Marnier').first().id
        )
    strawberryschnapps = RecipeIngredient(
            amount=0.5,
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    lemonjuice57 = RecipeIngredient(
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
    gin91 = RecipeIngredient(
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
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Chocolate Sauce').first().id
        )
    saltedchocolate = RecipeIngredient(
            amount=1,
            unit='garnish',
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
            amount=1.5,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Honey').first().id
        )
    angelicaroot = RecipeIngredient(
            amount=2,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Angelica root').first().id
        )
    fennelseeds = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Fennel seeds').first().id
        )
    lemonpeel = RecipeIngredient(
            amount=2,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon peel').first().id
        )
    watermelon = RecipeIngredient(
            amount=0.5,
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
            amount=0.33,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    lime = RecipeIngredient(
            amount=0.5,
            unit='juice',
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
            amount=1,
            unit='garnish',
            recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Watermelon').first().id
        )
    mint = RecipeIngredient(
            amount=1,
            unit='garnish',
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
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Creme De Banane').first().id
        )
    pineapplejuice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pineapple Juice').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='top off',
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
            amount=0.75,
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
            amount=0.5,
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
            amount=0.75,
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Kahlua').first().id
        )
    irishcream = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Irish cream').first().id
        )
    amaretto = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    proofrum = RecipeIngredient(
            amount=0.5,
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
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    coriander = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coriander').first().id
        )
    cardamom = RecipeIngredient(
            amount=4,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cardamom').first().id
        )
    gin92 = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    lemonjuice58 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    sugar = RecipeIngredient(
            amount=1,
            unit='tsp',
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
    lemonjuice59 = RecipeIngredient(
            amount=1,
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
    grandmarnier8 = RecipeIngredient(
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
    lemonjuice60 = RecipeIngredient(
            amount=1,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Fizz').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    grenadine = RecipeIngredient(
            amount=0.75,
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
            amount=0.5,
            unit='juice',
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
            amount=0.5,
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
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tea').first().id
        )
    water = RecipeIngredient(
            amount=0.5,
            unit='cup',
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    mint = RecipeIngredient(
            amount=1,
            unit='garnish',
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
    gin93 = RecipeIngredient(
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
    gin94 = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    anis = RecipeIngredient(
            amount=0.25,
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
            amount=1,
            unit='twist',
            recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange peel').first().id
        )
    gin95 = RecipeIngredient(
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
    up = RecipeIngredient(
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
    gin96 = RecipeIngredient(
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
    lemonjuice61 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    prosecco = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Prosecco').first().id
        )
    dryvermouth = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Dry Vermouth').first().id
        )
    gin97 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    maraschinoliqueur = RecipeIngredient(
            amount=0.25,
            unit='tsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Maraschino liqueur').first().id
        )
    anis = RecipeIngredient(
            amount=0.25,
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
            amount=1,
            unit='glass',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Surprise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    tabascosauce = RecipeIngredient(
            amount=8,
            unit='drops',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Surprise').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tabasco sauce').first().id
        )
    coffee = RecipeIngredient(
            amount=1,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Coffee').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Coffee').first().id
        )
    cream = RecipeIngredient(
            amount=2,
            unit='pods',
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
            amount=0.5,
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
            recipe_id=Recipe.query.filter(Recipe.name == 'Tommy\'s Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    limejuice = RecipeIngredient(
            amount=1.5,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tommy\'s Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    agavesyrup = RecipeIngredient(
            amount=2,
            unit='spoons',
            recipe_id=Recipe.query.filter(Recipe.name == 'Tommy\'s Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Agave syrup').first().id
        )
    lightrum = RecipeIngredient(
            amount=1,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light Rum').first().id
        )
    gin98 = RecipeIngredient(
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
    lemonjuice62 = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first().id
        )
    orgeatsyrup = RecipeIngredient(
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orgeat Syrup').first().id
        )
    orangepeel = RecipeIngredient(
            amount=1,
            unit='garnish',
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'The Evil Blue Thing').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Light rum').first().id
        )
    gin99 = RecipeIngredient(
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
    gin100 = RecipeIngredient(
            amount=1.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victor').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    sweetvermouth = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Victor').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    brandy = RecipeIngredient(
            amount=0.5,
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
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Sweet Vermouth').first().id
        )
    lemon = RecipeIngredient(
            amount=0.5,
            unit='juice',
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
            amount=0.5,
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
    lemonjuice63 = RecipeIngredient(
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
    lemonjuice64 = RecipeIngredient(
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
            amount=1,
            unit='top off',
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
            amount=0.5,
            unit='shot',
            recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Slime').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    vodka = RecipeIngredient(
             amount=1.5,
            unit='shot',
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
            amount=0.75,
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
            amount=0.75,
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
    lemonjuice65 = RecipeIngredient(
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
    gin101 = RecipeIngredient(
            amount=4,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Gin').first().id
        )
    triplesec = RecipeIngredient(
            amount=3,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Lady').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple Sec').first().id
        )
    lemonjuice66 = RecipeIngredient(
            amount=2,
            unit='cl',
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Wine Cooler').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    tequila = RecipeIngredient(
            amount=1.67,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Tequila').first().id
        )
    campari = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Campari').first().id
        )
    limejuice = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime Juice').first().id
        )
    orangejuice = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Orange Juice').first().id
        )
    rosemarysyrup = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rosemary Syrup').first().id
        )
    salt = RecipeIngredient(
            amount=1,
            unit='dash',
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
            amount=0.5,
            unit='juice',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon').first().id
        )
    powderedsugar = RecipeIngredient(
            amount=0.5,
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
            amount=0.5,
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
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Grapefruit Juice').first().id
        )
    limejuice = RecipeIngredient(
            amount=1,
            unit='juice',
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
            amount=1,
            unit='dash',
            recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Pepper').first().id
        )
    lime = RecipeIngredient(
            amount=1,
            unit='whole',
            recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime').first().id
        )
    lemon = RecipeIngredient(
            amount=1,
            unit='whole',
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
            amount=1,
            unit='top off',
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
            amount=0.25,
            unit='cup',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whitecap Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Cream of coconut').first().id
        )
    limejuice = RecipeIngredient(
            amount=3,
            unit='tbsp',
            recipe_id=Recipe.query.filter(Recipe.name == 'Whitecap Margarita').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lime juice').first().id
        )
    triplesec = RecipeIngredient(
            amount=0.75,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Waikiki Beachcomber').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Triple sec').first().id
        )
    gin102 = RecipeIngredient(
            amount=0.75,
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
            unit='slice',
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
    proofrum = RecipeIngredient(
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
            amount=10,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zambeer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Root beer').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zambeer').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    vodka = RecipeIngredient(
            amount=1.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorbatini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Vodka').first().id
        )
    ouzo = RecipeIngredient(
            amount=0.25,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zorbatini').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ouzo').first().id
        )
    jägermeister = RecipeIngredient(
            amount=0.5,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zenmeister').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Jägermeister').first().id
        )
    rootbeer = RecipeIngredient(
            amount=0.5,
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
            amount=1,
            unit='top off',
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
    lemonjuice67 = RecipeIngredient(
            amount=2,
            unit='cl',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zizi Coin-coin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Lemon juice').first().id
        )
    ice = RecipeIngredient(
            amount=1,
            unit='top off',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zizi Coin-coin').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Ice').first().id
        )
    lemon = RecipeIngredient(
            amount=0,
            unit='or lime',
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
            recipe_id=Recipe.query.filter(Recipe.name == 'Zippy\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Amaretto').first().id
        )
    rum = RecipeIngredient(
            amount=2,
            unit='oz',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zippy\'s Revenge').first().id,
            ingredient_id=Ingredient.query.filter(Ingredient.name == 'Rum').first().id
        )
    koolaid = RecipeIngredient(
            amount=4,
            unit='oz grape',
            recipe_id=Recipe.query.filter(Recipe.name == 'Zippy\'s Revenge').first().id,
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


    db.session.add(gin1)
    db.session.add(grandmarnier1)
    db.session.add(lemonjuice1)
    db.session.add(grenadine)
    db.session.add(amaretto)
    db.session.add(baileysirishcream)
    db.session.add(cognac)
    db.session.add(gin2)
    db.session.add(grenadine)
    db.session.add(heavycream)
    db.session.add(milk)
    db.session.add(eggwhite)
    db.session.add(proofrum)
    db.session.add(wildturkey)
    db.session.add(darkrum)
    db.session.add(lemonjuice2)
    db.session.add(grenadine)
    db.session.add(absolutvodka)
    db.session.add(gin3)
    db.session.add(tonicwater)
    db.session.add(applejack)
    db.session.add(grapefruitjuice)
    db.session.add(strawberryschnapps)
    db.session.add(orangejuice)
    db.session.add(cranberryjuice)
    db.session.add(orangejuice)
    db.session.add(grapefruitjuice)
    db.session.add(applejuice)
    db.session.add(maraschinocherry)
    db.session.add(vodka)
    db.session.add(pisangambon)
    db.session.add(applejuice)
    db.session.add(lemonjuice3)
    db.session.add(darkrum)
    db.session.add(peachnectar)
    db.session.add(orangejuice)
    db.session.add(gin4)
    db.session.add(vermouth)
    db.session.add(darkrum)
    db.session.add(kahlua)
    db.session.add(eggwhite)
    db.session.add(lightrum)
    db.session.add(triplesec)
    db.session.add(limejuice)
    db.session.add(sugar)
    db.session.add(eggwhite)
    db.session.add(mint)
    db.session.add(scotch)
    db.session.add(sweetvermouth)
    db.session.add(dryvermouth)
    db.session.add(orangebitters)
    db.session.add(applejack)
    db.session.add(triplesec)
    db.session.add(lemonjuice4)
    db.session.add(gin5)
    db.session.add(lemonjuice5)
    db.session.add(maraschinoliqueur)
    db.session.add(rum)
    db.session.add(vodka)
    db.session.add(tequila)
    db.session.add(triplesec)
    db.session.add(salt)
    db.session.add(sweetvermouth)
    db.session.add(dryvermouth)
    db.session.add(sodawater)
    db.session.add(vodka)
    db.session.add(cremedebanane)
    db.session.add(grenadine)
    db.session.add(orangejuice)
    db.session.add(pineapplejuice)
    db.session.add(kahlua)
    db.session.add(baileysirishcream)
    db.session.add(frangelico)
    db.session.add(coffee)
    db.session.add(gin6)
    db.session.add(cremedecacao)
    db.session.add(lightcream)
    db.session.add(blendedwhiskey)
    db.session.add(dryvermouth)
    db.session.add(pineapplejuice)
    db.session.add(dryvermouth)
    db.session.add(bourbon)
    db.session.add(blackberrybrandy)
    db.session.add(lemonjuice6)
    db.session.add(lemonpeel)
    db.session.add(campari)
    db.session.add(sweetvermouth)
    db.session.add(lemonpeel)
    db.session.add(orangepeel)
    db.session.add(jackdaniels)
    db.session.add(midorimelonliqueur)
    db.session.add(sourmix)
    db.session.add(sweetvermouth)
    db.session.add(gin7)
    db.session.add(bitters)
    db.session.add(vodka)
    db.session.add(limejuice)
    db.session.add(crownroyal)
    db.session.add(kahlua)
    db.session.add(cream)
    db.session.add(gin8)
    db.session.add(cognac)
    db.session.add(cremedecassis)
    db.session.add(freshlemonjuice)
    db.session.add(amaretto)
    db.session.add(cremedecacao)
    db.session.add(lightcream)
    db.session.add(apricotbrandy)
    db.session.add(applebrandy)
    db.session.add(gin9)
    db.session.add(hpnotiq)
    db.session.add(pineapplejuice)
    db.session.add(bananaliqueur)
    db.session.add(gin10)
    db.session.add(wine)
    db.session.add(benedictine)
    db.session.add(lime)
    db.session.add(vodka)
    db.session.add(sugar)
    db.session.add(anise)
    db.session.add(licoriceroot)
    db.session.add(wormwood)
    db.session.add(absolutkurant)
    db.session.add(midorimelonliqueur)
    db.session.add(cranberryjuice)
    db.session.add(sprite)
    db.session.add(vodka)
    db.session.add(grapesoda)
    db.session.add(orangejuice)
    db.session.add(ice)
    db.session.add(candy)
    db.session.add(lemonade)
    db.session.add(vodka)
    db.session.add(rum)
    db.session.add(gingerale)
    db.session.add(vodka)
    db.session.add(lemonade)
    db.session.add(water)
    db.session.add(sugar)
    db.session.add(tea)
    db.session.add(amaretto)
    db.session.add(whippedcream)
    db.session.add(tequila)
    db.session.add(applecider)
    db.session.add(applejuice)
    db.session.add(carrot)
    db.session.add(lightrum)
    db.session.add(apricotbrandy)
    db.session.add(triplesec)
    db.session.add(lemonjuice7)
    db.session.add(eggwhite)
    db.session.add(orange)
    db.session.add(vodka)
    db.session.add(gin11)
    db.session.add(limejuicecordial)
    db.session.add(ice)
    db.session.add(vodka)
    db.session.add(southerncomfort)
    db.session.add(passionfruitsyrup)
    db.session.add(sweetandsour)
    db.session.add(clubsoda)
    db.session.add(gin12)
    db.session.add(sweetvermouth)
    db.session.add(orangejuice)
    db.session.add(angosturabitters)
    db.session.add(amaretto)
    db.session.add(orangejuice)
    db.session.add(whitewine)
    db.session.add(orangepeel)
    db.session.add(amaretto)
    db.session.add(lime)
    db.session.add(amaretto)
    db.session.add(limejuice)
    db.session.add(amaretto)
    db.session.add(sourmix)
    db.session.add(aperol)
    db.session.add(prosecco)
    db.session.add(sodawater)
    db.session.add(up)
    db.session.add(appleschnapps)
    db.session.add(apricotbrandy)
    db.session.add(champagne)
    db.session.add(vodka)
    db.session.add(up)
    db.session.add(orangejuice)
    db.session.add(champagne)
    db.session.add(greencremedementhe)
    db.session.add(lemonade)
    db.session.add(vodka)
    db.session.add(bluecuracao)
    db.session.add(triplesec)
    db.session.add(amaretto)
    db.session.add(southerncomfort)
    db.session.add(ice)
    db.session.add(gin13)
    db.session.add(orangebitters)
    db.session.add(orange)
    db.session.add(cherry)
    db.session.add(lemonvodka)
    db.session.add(triplesec)
    db.session.add(pineapplejuice)
    db.session.add(grenadine)
    db.session.add(orangejuice)
    db.session.add(pineapplejuice)
    db.session.add(cream)
    db.session.add(chocolateicecream)
    db.session.add(brandy)
    db.session.add(amaretto)
    db.session.add(lime)
    db.session.add(appleschnapps)
    db.session.add(cognac)
    db.session.add(ginger)
    db.session.add(vodka)
    db.session.add(grenadine)
    db.session.add(orangejuice)
    db.session.add(sweetvermouth)
    db.session.add(sherry)
    db.session.add(orangebitters)
    db.session.add(southerncomfort)
    db.session.add(amaretto)
    db.session.add(sloegin)
    db.session.add(lemonjuice8)
    db.session.add(orangebitters)
    db.session.add(gin14)
    db.session.add(yellowchartreuse)
    db.session.add(lemonpeel)
    db.session.add(dryvermouth)
    db.session.add(gin15)
    db.session.add(kummel)
    db.session.add(triplesec)
    db.session.add(amaretto)
    db.session.add(cider)
    db.session.add(ice)
    db.session.add(vodka)
    db.session.add(maliburum)
    db.session.add(goldtequila)
    db.session.add(orangejuice)
    db.session.add(pineapplejuice)
    db.session.add(creamofcoconut)
    db.session.add(grenadine)
    db.session.add(ice)
    db.session.add(pineapple)
    db.session.add(gin16)
    db.session.add(grandmarnier2)
    db.session.add(lemonjuice9)
    db.session.add(lemonpeel)
    db.session.add(tea)
    db.session.add(ryewhiskey)
    db.session.add(redwine)
    db.session.add(rum)
    db.session.add(brandy)
    db.session.add(benedictine)
    db.session.add(orangejuice)
    db.session.add(lemonjuice10)
    db.session.add(cranberryjuice)
    db.session.add(sodawater)
    db.session.add(midorimelonliqueur)
    db.session.add(cremedebanane)
    db.session.add(sugar)
    db.session.add(water)
    db.session.add(apricot)
    db.session.add(almondflavoring)
    db.session.add(grainalcohol)
    db.session.add(water)
    db.session.add(brandy)
    db.session.add(foodcoloring)
    db.session.add(foodcoloring)
    db.session.add(foodcoloring)
    db.session.add(glycerine)
    db.session.add(amaretto)
    db.session.add(whitecremedementhe)
    db.session.add(amaretto)
    db.session.add(orangejuice)
    db.session.add(grenadine)
    db.session.add(angelicaroot)
    db.session.add(almond)
    db.session.add(allspice)
    db.session.add(cinnamon)
    db.session.add(anise)
    db.session.add(coriander)
    db.session.add(marjoramleaves)
    db.session.add(vodka)
    db.session.add(sugar)
    db.session.add(water)
    db.session.add(foodcoloring)
    db.session.add(foodcoloring)
    db.session.add(maui)
    db.session.add(mountaindew)
    db.session.add(ice)
    db.session.add(absolutvodka)
    db.session.add(icedtea)
    db.session.add(campari)
    db.session.add(orangejuice)
    db.session.add(gingerbeer)
    db.session.add(orangepeel)
    db.session.add(absolutcitron)
    db.session.add(pisangambon)
    db.session.add(ice)
    db.session.add(absolutcitron)
    db.session.add(limejuice)
    db.session.add(ice)
    db.session.add(tonicwater)
    db.session.add(absolutvodka)
    db.session.add(peachschnapps)
    db.session.add(coconutliqueur)
    db.session.add(cranberryjuice)
    db.session.add(pineapplejuice)
    db.session.add(water)
    db.session.add(ginger)
    db.session.add(guavajuice)
    db.session.add(lemonjuice11)
    db.session.add(pineapple)
    db.session.add(sugar)
    db.session.add(pineapplejuice)
    db.session.add(applecider)
    db.session.add(brownsugar)
    db.session.add(lemonade)
    db.session.add(orangejuice)
    db.session.add(cloves)
    db.session.add(allspice)
    db.session.add(nutmeg)
    db.session.add(cinnamon)
    db.session.add(jägermeister)
    db.session.add(goldschlager)
    db.session.add(coconutrum)
    db.session.add(amaretto)
    db.session.add(orangejuice)
    db.session.add(grenadine)
    db.session.add(lightrum)
    db.session.add(gingerbeer)
    db.session.add(lemonpeel)
    db.session.add(absolutcitron)
    db.session.add(sweetandsour)
    db.session.add(sprite)
    db.session.add(sodawater)
    db.session.add(lemon)
    db.session.add(amaretto)
    db.session.add(lightcream)
    db.session.add(vodka)
    db.session.add(midorimelonliqueur)
    db.session.add(sweetandsour)
    db.session.add(vodka)
    db.session.add(peachschnapps)
    db.session.add(orangejuice)
    db.session.add(cranberryjuice)
    db.session.add(vodka)
    db.session.add(cranberryjuice)
    db.session.add(champagne)
    db.session.add(amaretto)
    db.session.add(grandmarnier3)
    db.session.add(southerncomfort)
    db.session.add(amaretto)
    db.session.add(sourmix)
    db.session.add(orangejuice)
    db.session.add(amaretto)
    db.session.add(lemon)
    db.session.add(absolutcitron)
    db.session.add(orangejuice)
    db.session.add(triplesec)
    db.session.add(gingerale)
    db.session.add(berries)
    db.session.add(apple)
    db.session.add(rum)
    db.session.add(dryvermouth)
    db.session.add(cognac)
    db.session.add(gin17)
    db.session.add(freshlimejuice)
    db.session.add(sugarsyrup)
    db.session.add(water)
    db.session.add(apricotbrandy)
    db.session.add(triplesec)
    db.session.add(lime)
    db.session.add(lime)
    db.session.add(triplesec)
    db.session.add(apricotbrandy)
    db.session.add(lemonjuice12)
    db.session.add(vodka)
    db.session.add(kirschwasser)
    db.session.add(strawberryliqueur)
    db.session.add(strawberries)
    db.session.add(applejuice)
    db.session.add(maliburum)
    db.session.add(cinnamon)
    db.session.add(lightrum)
    db.session.add(añejorum)
    db.session.add(orangejuice)
    db.session.add(lemonjuice13)
    db.session.add(gingerale)
    db.session.add(lemonpeel)
    db.session.add(amaretto)
    db.session.add(darkcremedecacao)
    db.session.add(coffee)
    db.session.add(whitecremedementhe)
    db.session.add(southerncomfort)
    db.session.add(vodka)
    db.session.add(hotchocolate)
    db.session.add(absolutvodka)
    db.session.add(cranberryjuice)
    db.session.add(gingerale)
    db.session.add(ice)
    db.session.add(sourmix)
    db.session.add(amaretto)
    db.session.add(tequila)
    db.session.add(orangejuice)
    db.session.add(baileysirishcream)
    db.session.add(grandmarnier4)
    db.session.add(kahlua)
    db.session.add(kahlua)
    db.session.add(sambuca)
    db.session.add(grandmarnier5)
    db.session.add(orangebitters)
    db.session.add(greenchartreuse)
    db.session.add(gin18)
    db.session.add(sweetvermouth)
    db.session.add(gin19)
    db.session.add(triplesec)
    db.session.add(lemonjuice14)
    db.session.add(grenadine)
    db.session.add(eggwhite)
    db.session.add(irishcream)
    db.session.add(goldschlager)
    db.session.add(champagne)
    db.session.add(peachschnapps)
    db.session.add(gin20)
    db.session.add(lemonjuice15)
    db.session.add(sugarsyrup)
    db.session.add(cremedemure)
    db.session.add(scotch)
    db.session.add(sweetvermouth)
    db.session.add(dryvermouth)
    db.session.add(bitters)
    db.session.add(gin21)
    db.session.add(triplesec)
    db.session.add(bluecuracao)
    db.session.add(bitters)
    db.session.add(maraschinocherry)
    db.session.add(lemonpeel)
    db.session.add(ryewhiskey)
    db.session.add(dryvermouth)
    db.session.add(maraschinoliqueur)
    db.session.add(angosturabitters)
    db.session.add(maraschinocherry)
    db.session.add(pineapplejuice)
    db.session.add(passionfruitjuice)
    db.session.add(lemonjuice16)
    db.session.add(grenadine)
    db.session.add(gin22)
    db.session.add(dryvermouth)
    db.session.add(bitters)
    db.session.add(maraschinoliqueur)
    db.session.add(maraschinocherry)
    db.session.add(rum)
    db.session.add(galliano)
    db.session.add(pineapplejuice)
    db.session.add(limejuice)
    db.session.add(prosecco)
    db.session.add(hotchocolate)
    db.session.add(greenchartreuse)
    db.session.add(cherryheering)
    db.session.add(proofrum)
    db.session.add(scotch)
    db.session.add(bitters)
    db.session.add(wormwood)
    db.session.add(ice)
    db.session.add(corona)
    db.session.add(bacardilimon)
    db.session.add(everclear)
    db.session.add(vodka)
    db.session.add(mountaindew)
    db.session.add(surge)
    db.session.add(lemonjuice17)
    db.session.add(rum)
    db.session.add(sweetvermouth)
    db.session.add(sloegin)
    db.session.add(lemonpeel)
    db.session.add(midorimelonliqueur)
    db.session.add(jägermeister)
    db.session.add(goldschlager)
    db.session.add(southerncomfort)
    db.session.add(triplesec)
    db.session.add(lime)
    db.session.add(sourmix)
    db.session.add(vodka)
    db.session.add(bananaliqueur)
    db.session.add(orangejuice)
    db.session.add(peachschnapps)
    db.session.add(baileysirishcream)
    db.session.add(kahlua)
    db.session.add(sambuca)
    db.session.add(kahlua)
    db.session.add(milk)
    db.session.add(vanillaicecream)
    db.session.add(blendedwhiskey)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(eggwhite)
    db.session.add(lemon)
    db.session.add(cherry)
    db.session.add(rum)
    db.session.add(darkrum)
    db.session.add(bananaliqueur)
    db.session.add(grenadine)
    db.session.add(pineapplejuice)
    db.session.add(orangejuice)
    db.session.add(sweetandsour)
    db.session.add(sambuca)
    db.session.add(erincream)
    db.session.add(advocaat)
    db.session.add(vodka)
    db.session.add(tomatojuice)
    db.session.add(lemonjuice18)
    db.session.add(worcestershiresauce)
    db.session.add(tabascosauce)
    db.session.add(lime)
    db.session.add(ale)
    db.session.add(guinnessstout)
    db.session.add(vodka)
    db.session.add(bluecuracao)
    db.session.add(goldrum)
    db.session.add(orangejuice)
    db.session.add(limejuice)
    db.session.add(triplesec)
    db.session.add(brandy)
    db.session.add(egg)
    db.session.add(sugar)
    db.session.add(lightcream)
    db.session.add(nutmeg)
    db.session.add(brandy)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(lemon)
    db.session.add(cherry)
    db.session.add(vanillaicecream)
    db.session.add(butterscotchschnapps)
    db.session.add(milk)
    db.session.add(vodka)
    db.session.add(campari)
    db.session.add(sweetvermouth)
    db.session.add(ryewhiskey)
    db.session.add(orangepeel)
    db.session.add(bourbon)
    db.session.add(lemonjuice19)
    db.session.add(sugar)
    db.session.add(orange)
    db.session.add(maraschinocherry)
    db.session.add(vodka)
    db.session.add(coconutliqueur)
    db.session.add(bluecuracao)
    db.session.add(sprite)
    db.session.add(vodka)
    db.session.add(strawberries)
    db.session.add(limejuice)
    db.session.add(lemonlimesoda)
    db.session.add(lemonlimesoda)
    db.session.add(raisins)
    db.session.add(blueberries)
    db.session.add(everclear)
    db.session.add(wine)
    db.session.add(orangejuice)
    db.session.add(koolaid)
    db.session.add(tequila)
    db.session.add(tomatojuice)
    db.session.add(lemonjuice20)
    db.session.add(tabascosauce)
    db.session.add(celerysalt)
    db.session.add(lemon)
    db.session.add(baileysirishcream)
    db.session.add(godivaliqueur)
    db.session.add(kahlua)
    db.session.add(butterscotchschnapps)
    db.session.add(milk)
    db.session.add(añejorum)
    db.session.add(tiamaria)
    db.session.add(vodka)
    db.session.add(orangejuice)
    db.session.add(lemonjuice21)
    db.session.add(rum)
    db.session.add(coconutliqueur)
    db.session.add(blueberries)
    db.session.add(pineapplejuice)
    db.session.add(prosecco)
    db.session.add(gin23)
    db.session.add(cremedecassis)
    db.session.add(freshlimejuice)
    db.session.add(gingerbeer)
    db.session.add(lime)
    db.session.add(ginger)
    db.session.add(sugar)
    db.session.add(water)
    db.session.add(lemonjuice22)
    db.session.add(bourbon)
    db.session.add(lemonpeel)
    db.session.add(vodka)
    db.session.add(chambordraspberryliqueur)
    db.session.add(peachtreeschnapps)
    db.session.add(cranberryjuice)
    db.session.add(coffeeliqueur)
    db.session.add(vodka)
    db.session.add(kahlua)
    db.session.add(baileysirishcream)
    db.session.add(sugar)
    db.session.add(clubsoda)
    db.session.add(lemon)
    db.session.add(brandy)
    db.session.add(maraschinocherry)
    db.session.add(orange)
    db.session.add(rum)
    db.session.add(darkrum)
    db.session.add(passoa)
    db.session.add(bluecuracao)
    db.session.add(sweetandsour)
    db.session.add(ice)
    db.session.add(lightrum)
    db.session.add(brandy)
    db.session.add(triplesec)
    db.session.add(lime)
    db.session.add(tequila)
    db.session.add(bluecuracao)
    db.session.add(limejuice)
    db.session.add(salt)
    db.session.add(maliburum)
    db.session.add(bananaliqueur)
    db.session.add(pineapplejuice)
    db.session.add(lightrum)
    db.session.add(triplesec)
    db.session.add(banana)
    db.session.add(limejuice)
    db.session.add(sugar)
    db.session.add(cherry)
    db.session.add(ice)
    db.session.add(vodka)
    db.session.add(peachnectar)
    db.session.add(peachschnapps)
    db.session.add(lemonpeel)
    db.session.add(guinnessstout)
    db.session.add(rootbeer)
    db.session.add(brandy)
    db.session.add(cremedecacao)
    db.session.add(lightcream)
    db.session.add(lightrum)
    db.session.add(limejuice)
    db.session.add(sugarsyrup)
    db.session.add(grenadine)
    db.session.add(darkrum)
    db.session.add(orange)
    db.session.add(surge)
    db.session.add(cranberryjuice)
    db.session.add(darkrum)
    db.session.add(limejuice)
    db.session.add(sugar)
    db.session.add(blueberries)
    db.session.add(lemonlimesoda)
    db.session.add(brandy)
    db.session.add(gin24)
    db.session.add(dryvermouth)
    db.session.add(raspberryvodka)
    db.session.add(cranberryjuice)
    db.session.add(lemonade)
    db.session.add(bluecuracao)
    db.session.add(sugarsyrup)
    db.session.add(limejuice)
    db.session.add(mint)
    db.session.add(milk)
    db.session.add(orangejuice)
    db.session.add(sugarsyrup)
    db.session.add(banana)
    db.session.add(tequila)
    db.session.add(tabascosauce)
    db.session.add(ice)
    db.session.add(brandy)
    db.session.add(lightrum)
    db.session.add(triplesec)
    db.session.add(lemonjuice23)
    db.session.add(baileysirishcream)
    db.session.add(vanillaicecream)
    db.session.add(sweetvermouth)
    db.session.add(scotch)
    db.session.add(benedictine)
    db.session.add(lemonpeel)
    db.session.add(strawberries)
    db.session.add(banana)
    db.session.add(yoghurt)
    db.session.add(milk)
    db.session.add(honey)
    db.session.add(vanillaicecream)
    db.session.add(milk)
    db.session.add(godivaliqueur)
    db.session.add(whippedcream)
    db.session.add(caramelsauce)
    db.session.add(chocolatesauce)
    db.session.add(minisnickersbars)
    db.session.add(cantaloupe)
    db.session.add(banana)
    db.session.add(vanillaicecream)
    db.session.add(cocacola)
    db.session.add(bourbon)
    db.session.add(strawberries)
    db.session.add(banana)
    db.session.add(applejuice)
    db.session.add(gin25)
    db.session.add(maraschinoliqueur)
    db.session.add(lemonjuice24)
    db.session.add(orangebitters)
    db.session.add(cherry)
    db.session.add(milk)
    db.session.add(triplesec)
    db.session.add(sugar)
    db.session.add(lime)
    db.session.add(cachaca)
    db.session.add(spicedrum)
    db.session.add(darkrum)
    db.session.add(lime)
    db.session.add(cocacola)
    db.session.add(lightrum)
    db.session.add(cherrybrandy)
    db.session.add(lightcream)
    db.session.add(lightrum)
    db.session.add(lime)
    db.session.add(lime)
    db.session.add(falernum)
    db.session.add(angosturabitters)
    db.session.add(añejorum)
    db.session.add(blackstraprum)
    db.session.add(bacardilimon)
    db.session.add(cocacola)
    db.session.add(lightrum)
    db.session.add(triplesec)
    db.session.add(limejuice)
    db.session.add(maraschinoliqueur)
    db.session.add(gin26)
    db.session.add(grenadine)
    db.session.add(lemon)
    db.session.add(eggwhite)
    db.session.add(lime)
    db.session.add(sugar)
    db.session.add(whiterum)
    db.session.add(ice)
    db.session.add(brandy)
    db.session.add(triplesec)
    db.session.add(lemonjuice25)
    db.session.add(lager)
    db.session.add(campari)
    db.session.add(lightrum)
    db.session.add(port)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(eggwhite)
    db.session.add(vodka)
    db.session.add(limejuice)
    db.session.add(cointreau)
    db.session.add(cranberryjuice)
    db.session.add(water)
    db.session.add(sugar)
    db.session.add(coffee)
    db.session.add(vanilla)
    db.session.add(vodka)
    db.session.add(gin27)
    db.session.add(lemonjuice26)
    db.session.add(maraschinoliqueur)
    db.session.add(orangebitters)
    db.session.add(eggyolk)
    db.session.add(gin28)
    db.session.add(triplesec)
    db.session.add(lilletblanc)
    db.session.add(lemonjuice27)
    db.session.add(absinthe)
    db.session.add(chocolateliqueur)
    db.session.add(milk)
    db.session.add(amaretto)
    db.session.add(sweetvermouth)
    db.session.add(sloegin)
    db.session.add(wine)
    db.session.add(coffee)
    db.session.add(vanillaextract)
    db.session.add(sugar)
    db.session.add(vodka)
    db.session.add(water)
    db.session.add(cocacola)
    db.session.add(lemonjuice28)
    db.session.add(chocolate)
    db.session.add(milk)
    db.session.add(cranberryjuice)
    db.session.add(sugar)
    db.session.add(pineapplejuice)
    db.session.add(almondflavoring)
    db.session.add(gingerale)
    db.session.add(sugar)
    db.session.add(water)
    db.session.add(grainalcohol)
    db.session.add(peppermintextract)
    db.session.add(foodcoloring)
    db.session.add(bananaliqueur)
    db.session.add(cremedecacao)
    db.session.add(chocolateicecream)
    db.session.add(chocolatesyrup)
    db.session.add(chocolatemilk)
    db.session.add(whippedcream)
    db.session.add(cherry)
    db.session.add(banana)
    db.session.add(cranberries)
    db.session.add(sugar)
    db.session.add(lightrum)
    db.session.add(milk)
    db.session.add(chocolate)
    db.session.add(cinnamon)
    db.session.add(egg)
    db.session.add(champagne)
    db.session.add(sugar)
    db.session.add(bitters)
    db.session.add(lemonpeel)
    db.session.add(cognac)
    db.session.add(blendedwhiskey)
    db.session.add(lemon)
    db.session.add(lime)
    db.session.add(powderedsugar)
    db.session.add(grenadine)
    db.session.add(kahlua)
    db.session.add(galliano)
    db.session.add(sodawater)
    db.session.add(rum)
    db.session.add(limejuice)
    db.session.add(eggwhite)
    db.session.add(bitters)
    db.session.add(sugar)
    db.session.add(nutmeg)
    db.session.add(cointreau)
    db.session.add(vodka)
    db.session.add(lime)
    db.session.add(cranberryjuice)
    db.session.add(corona)
    db.session.add(lightrum)
    db.session.add(bitters)
    db.session.add(water)
    db.session.add(sugar)
    db.session.add(bourbon)
    db.session.add(orange)
    db.session.add(maraschinocherry)
    db.session.add(kahlua)
    db.session.add(vodka)
    db.session.add(chocolateicecream)
    db.session.add(cognac)
    db.session.add(gingerbeer)
    db.session.add(angosturabitters)
    db.session.add(lemonpeel)
    db.session.add(orange)
    db.session.add(vodka)
    db.session.add(sugar)
    db.session.add(cocoapowder)
    db.session.add(sugar)
    db.session.add(cornstarch)
    db.session.add(water)
    db.session.add(milk)
    db.session.add(gin29)
    db.session.add(tequila)
    db.session.add(vodka)
    db.session.add(whiterum)
    db.session.add(triplesec)
    db.session.add(cherrygrenadine)
    db.session.add(sweetandsour)
    db.session.add(clubsoda)
    db.session.add(gin30)
    db.session.add(peachbitters)
    db.session.add(mint)
    db.session.add(lager)
    db.session.add(cider)
    db.session.add(blackcurrantcordial)
    db.session.add(lightrum)
    db.session.add(lime)
    db.session.add(powderedsugar)
    db.session.add(coffee)
    db.session.add(everclear)
    db.session.add(fruitpunch)
    db.session.add(sprite)
    db.session.add(tequila)
    db.session.add(proofrum)
    db.session.add(gin31)
    db.session.add(gingerale)
    db.session.add(lime)
    db.session.add(gin32)
    db.session.add(dryvermouth)
    db.session.add(olive)
    db.session.add(scotch)
    db.session.add(dryvermouth)
    db.session.add(lemonpeel)
    db.session.add(vodka)
    db.session.add(dryvermouth)
    db.session.add(olivebrine)
    db.session.add(lemon)
    db.session.add(olive)
    db.session.add(cherryheering)
    db.session.add(sodawater)
    db.session.add(orangejuice)
    db.session.add(ice)
    db.session.add(darkrum)
    db.session.add(gingerbeer)
    db.session.add(demerarasugar)
    db.session.add(lime)
    db.session.add(cachaca)
    db.session.add(pisco)
    db.session.add(limejuice)
    db.session.add(pineapplesyrup)
    db.session.add(stgermain)
    db.session.add(angosturabitters)
    db.session.add(pepper)
    db.session.add(lavender)
    db.session.add(whiskey)
    db.session.add(hotdamn)
    db.session.add(dubonnetrouge)
    db.session.add(gin33)
    db.session.add(bitters)
    db.session.add(lemonpeel)
    db.session.add(heavycream)
    db.session.add(milk)
    db.session.add(cinnamon)
    db.session.add(vanilla)
    db.session.add(chocolate)
    db.session.add(whippedcream)
    db.session.add(absinthe)
    db.session.add(champagne)
    db.session.add(chocolatesyrup)
    db.session.add(milk)
    db.session.add(sodawater)
    db.session.add(eggyolk)
    db.session.add(sugar)
    db.session.add(milk)
    db.session.add(lightrum)
    db.session.add(bourbon)
    db.session.add(vanillaextract)
    db.session.add(salt)
    db.session.add(whippingcream)
    db.session.add(eggwhite)
    db.session.add(sugar)
    db.session.add(nutmeg)
    db.session.add(brandy)
    db.session.add(gin34)
    db.session.add(sweetvermouth)
    db.session.add(vodka)
    db.session.add(kahlua)
    db.session.add(sugarsyrup)
    db.session.add(rum)
    db.session.add(vanillasyrup)
    db.session.add(espresso)
    db.session.add(coffee)
    db.session.add(egg)
    db.session.add(sugar)
    db.session.add(condensedmilk)
    db.session.add(milk)
    db.session.add(vanillaextract)
    db.session.add(rum)
    db.session.add(nutmeg)
    db.session.add(apricotbrandy)
    db.session.add(gin35)
    db.session.add(dryvermouth)
    db.session.add(grenadine)
    db.session.add(lemonjuice29)
    db.session.add(cherry)
    db.session.add(cachaca)
    db.session.add(lime)
    db.session.add(elderflowercordial)
    db.session.add(egg)
    db.session.add(sugar)
    db.session.add(salt)
    db.session.add(milk)
    db.session.add(vanillaextract)
    db.session.add(mezcal)
    db.session.add(chocolateliqueur)
    db.session.add(coffeeliqueur)
    db.session.add(rose)
    db.session.add(sugar)
    db.session.add(strawberries)
    db.session.add(lemonjuice30)
    db.session.add(coffee)
    db.session.add(milk)
    db.session.add(sugar)
    db.session.add(amaretto)
    db.session.add(cremedecacao)
    db.session.add(lightcream)
    db.session.add(gin36)
    db.session.add(sugar)
    db.session.add(lemonjuice31)
    db.session.add(champagne)
    db.session.add(orange)
    db.session.add(maraschinocherry)
    db.session.add(vodka)
    db.session.add(honey)
    db.session.add(figs)
    db.session.add(thyme)
    db.session.add(angosturabitters)
    db.session.add(tonicwater)
    db.session.add(blendedwhiskey)
    db.session.add(benedictine)
    db.session.add(lemon)
    db.session.add(lime)
    db.session.add(lemon)
    db.session.add(lime)
    db.session.add(yoghurt)
    db.session.add(banana)
    db.session.add(orangejuice)
    db.session.add(fruit)
    db.session.add(ice)
    db.session.add(applejuice)
    db.session.add(strawberries)
    db.session.add(sugar)
    db.session.add(lemon)
    db.session.add(apple)
    db.session.add(sodawater)
    db.session.add(jägermeister)
    db.session.add(sambuca)
    db.session.add(vodka)
    db.session.add(rum)
    db.session.add(apricotnectar)
    db.session.add(pomegranatejuice)
    db.session.add(lemon)
    db.session.add(sodawater)
    db.session.add(coffee)
    db.session.add(peachschnapps)
    db.session.add(vodka)
    db.session.add(raspberryliqueur)
    db.session.add(pineapplejuice)
    db.session.add(gin37)
    db.session.add(lillet)
    db.session.add(sweetvermouth)
    db.session.add(orangepeel)
    db.session.add(firewater)
    db.session.add(absolutpeppar)
    db.session.add(tabascosauce)
    db.session.add(gin38)
    db.session.add(triplesec)
    db.session.add(lightrum)
    db.session.add(triplesec)
    db.session.add(limejuice)
    db.session.add(sugar)
    db.session.add(cherry)
    db.session.add(ice)
    db.session.add(yoghurt)
    db.session.add(fruitjuice)
    db.session.add(scotch)
    db.session.add(sweetvermouth)
    db.session.add(bitters)
    db.session.add(sugarsyrup)
    db.session.add(cognac)
    db.session.add(amaretto)
    db.session.add(amaretto)
    db.session.add(vodka)
    db.session.add(proofrum)
    db.session.add(drpepper)
    db.session.add(beer)
    db.session.add(kahlua)
    db.session.add(sambuca)
    db.session.add(bluecuracao)
    db.session.add(baileysirishcream)
    db.session.add(sambuca)
    db.session.add(sarsaparilla)
    db.session.add(lightrum)
    db.session.add(limejuice)
    db.session.add(mint)
    db.session.add(sugar)
    db.session.add(lightrum)
    db.session.add(pineapple)
    db.session.add(limejuice)
    db.session.add(sugar)
    db.session.add(galliano)
    db.session.add(gin39)
    db.session.add(limejuice)
    db.session.add(sugarsyrup)
    db.session.add(lime)
    db.session.add(vodka)
    db.session.add(amaretto)
    db.session.add(heavycream)
    db.session.add(gin40)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(gin)
    db.session.add(lemonjuice32)
    db.session.add(sugar)
    db.session.add(orange)
    db.session.add(maraschinocherry)
    db.session.add(peachvodka)
    db.session.add(lemonjuice33)
    db.session.add(galliano)
    db.session.add(sirupofroses)
    db.session.add(vodka)
    db.session.add(amaretto)
    db.session.add(scotch)
    db.session.add(amaretto)
    db.session.add(redwine)
    db.session.add(water)
    db.session.add(sugar)
    db.session.add(cinnamon)
    db.session.add(cloves)
    db.session.add(lemonpeel)
    db.session.add(gin41)
    db.session.add(tonicwater)
    db.session.add(lemonpeel)
    db.session.add(ice)
    db.session.add(gin42)
    db.session.add(water)
    db.session.add(powderedsugar)
    db.session.add(lemonpeel)
    db.session.add(gin43)
    db.session.add(carbonatedwater)
    db.session.add(sugar)
    db.session.add(mint)
    db.session.add(orange)
    db.session.add(cherry)
    db.session.add(gin44)
    db.session.add(lemonjuice34)
    db.session.add(sugar)
    db.session.add(grenadine)
    db.session.add(maraschinocherry)
    db.session.add(orange)
    db.session.add(gin45)
    db.session.add(lemonjuice35)
    db.session.add(lemonpeel)
    db.session.add(ice)
    db.session.add(gin46)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(water)
    db.session.add(orangepeel)
    db.session.add(vodka)
    db.session.add(grapefruitjuice)
    db.session.add(gin47)
    db.session.add(grenadine)
    db.session.add(lemon)
    db.session.add(sodawater)
    db.session.add(lime)
    db.session.add(gin48)
    db.session.add(grenadine)
    db.session.add(powderedsugar)
    db.session.add(pineapple)
    db.session.add(strawberries)
    db.session.add(maliburum)
    db.session.add(peachschnapps)
    db.session.add(bluecuracao)
    db.session.add(sweetandsour)
    db.session.add(gin49)
    db.session.add(limejuice)
    db.session.add(sugar)
    db.session.add(gin50)
    db.session.add(bitters)
    db.session.add(clubsoda)
    db.session.add(gin51)
    db.session.add(triplesec)
    db.session.add(pineapplejuice)
    db.session.add(grenadine)
    db.session.add(pineapple)
    db.session.add(greencremedementhe)
    db.session.add(cremedecacao)
    db.session.add(lightcream)
    db.session.add(kahlua)
    db.session.add(proofrum)
    db.session.add(grenadine)
    db.session.add(gin52)
    db.session.add(sodawater)
    db.session.add(lime)
    db.session.add(galliano)
    db.session.add(triplesec)
    db.session.add(orangejuice)
    db.session.add(cream)
    db.session.add(cider)
    db.session.add(lager)
    db.session.add(bluecuracao)
    db.session.add(amaretto)
    db.session.add(jägermeister)
    db.session.add(kahlua)
    db.session.add(milk)
    db.session.add(gin53)
    db.session.add(tonicwater)
    db.session.add(lime)
    db.session.add(gin54)
    db.session.add(lemonjuice36)
    db.session.add(sugarsyrup)
    db.session.add(basil)
    db.session.add(gin55)
    db.session.add(brandy)
    db.session.add(sweetvermouth)
    db.session.add(clubsoda)
    db.session.add(cachaca)
    db.session.add(lemonjuice37)
    db.session.add(agavesyrup)
    db.session.add(champagne)
    db.session.add(gin56)
    db.session.add(campari)
    db.session.add(orangejuice)
    db.session.add(orangepeel)
    db.session.add(darkrum)
    db.session.add(vodka)
    db.session.add(triplesec)
    db.session.add(tequila)
    db.session.add(melonliqueur)
    db.session.add(mountaindew)
    db.session.add(grapes)
    db.session.add(lemon)
    db.session.add(pineapple)
    db.session.add(whisky)
    db.session.add(baileysirishcream)
    db.session.add(whiterum)
    db.session.add(honey)
    db.session.add(lemonjuice38)
    db.session.add(whiskey)
    db.session.add(honey)
    db.session.add(cinnamon)
    db.session.add(lemon)
    db.session.add(cloves)
    db.session.add(hotdamn)
    db.session.add(tea)
    db.session.add(lemonpeel)
    db.session.add(brandy)
    db.session.add(gingerale)
    db.session.add(bitters)
    db.session.add(spicedrum)
    db.session.add(vermouth)
    db.session.add(maraschinocherry)
    db.session.add(sugarsyrup)
    db.session.add(lemonade)
    db.session.add(blackberries)
    db.session.add(cherryjuice)
    db.session.add(orangepeel)
    db.session.add(redchiliflakes)
    db.session.add(cloves)
    db.session.add(ginger)
    db.session.add(vodka)
    db.session.add(lightrum)
    db.session.add(pineapplejuice)
    db.session.add(lemonjuice39)
    db.session.add(carbonatedsoftdrink)
    db.session.add(sugar)
    db.session.add(cornsyrup)
    db.session.add(coffee)
    db.session.add(vanillaextract)
    db.session.add(water)
    db.session.add(vodka)
    db.session.add(irishwhiskey)
    db.session.add(baileysirishcream)
    db.session.add(coffee)
    db.session.add(vodka)
    db.session.add(galliano)
    db.session.add(orangejuice)
    db.session.add(gin57)
    db.session.add(triplesec)
    db.session.add(pineapplejuice)
    db.session.add(rum)
    db.session.add(grapefruitjuice)
    db.session.add(maraschinoliqueur)
    db.session.add(limejuice)
    db.session.add(scotch)
    db.session.add(sweetvermouth)
    db.session.add(orangebitters)
    db.session.add(olive)
    db.session.add(chocolate)
    db.session.add(butter)
    db.session.add(vanillaextract)
    db.session.add(halfandhalf)
    db.session.add(marshmallows)
    db.session.add(lime)
    db.session.add(brownsugar)
    db.session.add(passionfruitjuice)
    db.session.add(gingerale)
    db.session.add(ice)
    db.session.add(vodka)
    db.session.add(icedtea)
    db.session.add(lemonjuice40)
    db.session.add(coffee)
    db.session.add(sugar)
    db.session.add(water)
    db.session.add(milk)
    db.session.add(scotch)
    db.session.add(halfandhalf)
    db.session.add(condensedmilk)
    db.session.add(coconutsyrup)
    db.session.add(chocolatesyrup)
    db.session.add(irishwhiskey)
    db.session.add(coffee)
    db.session.add(sugar)
    db.session.add(whippedcream)
    db.session.add(irishwhiskey)
    db.session.add(peachbrandy)
    db.session.add(orangejuice)
    db.session.add(sweetandsour)
    db.session.add(orange)
    db.session.add(cherry)
    db.session.add(lightrum)
    db.session.add(blendedwhiskey)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(vodka)
    db.session.add(kahlua)
    db.session.add(cocacola)
    db.session.add(guinnessstout)
    db.session.add(limejuice)
    db.session.add(gin58)
    db.session.add(aperol)
    db.session.add(kahlua)
    db.session.add(coffee)
    db.session.add(baileysirishcream)
    db.session.add(bourbon)
    db.session.add(vodka)
    db.session.add(orangejuice)
    db.session.add(baileysirishcream)
    db.session.add(chambordraspberryliqueur)
    db.session.add(sugarsyrup)
    db.session.add(sugar)
    db.session.add(gin59)
    db.session.add(vodka)
    db.session.add(grenadine)
    db.session.add(limejuice)
    db.session.add(sugar)
    db.session.add(sugarsyrup)
    db.session.add(sodawater)
    db.session.add(jackdaniels)
    db.session.add(amaretto)
    db.session.add(blackberrybrandy)
    db.session.add(anis)
    db.session.add(vodka)
    db.session.add(jello)
    db.session.add(water)
    db.session.add(coffeeliqueur)
    db.session.add(lightrum)
    db.session.add(ice)
    db.session.add(bourbon)
    db.session.add(lemonjuice41)
    db.session.add(sugar)
    db.session.add(clubsoda)
    db.session.add(maraschinocherry)
    db.session.add(orange)
    db.session.add(blendedwhiskey)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(port)
    db.session.add(eggwhite)
    db.session.add(rum)
    db.session.add(coffee)
    db.session.add(water)
    db.session.add(milk)
    db.session.add(gin60)
    db.session.add(greenchartreuse)
    db.session.add(yellowchartreuse)
    db.session.add(applebrandy)
    db.session.add(grenadine)
    db.session.add(lime)
    db.session.add(ice)
    db.session.add(tennesseewhiskey)
    db.session.add(vanillaextract)
    db.session.add(cocacola)
    db.session.add(cremedecassis)
    db.session.add(champagne)
    db.session.add(coffee)
    db.session.add(grainalcohol)
    db.session.add(vodka)
    db.session.add(triplesec)
    db.session.add(limejuice)
    db.session.add(cremedecassis)
    db.session.add(champagne)
    db.session.add(kiwiliqueur)
    db.session.add(bitterlemon)
    db.session.add(ice)
    db.session.add(absolutkurant)
    db.session.add(tea)
    db.session.add(sugar)
    db.session.add(kahlua)
    db.session.add(brandy)
    db.session.add(kiwi)
    db.session.add(sugarsyrup)
    db.session.add(vodka)
    db.session.add(kiwi)
    db.session.add(cranberryvodka)
    db.session.add(apfelkorn)
    db.session.add(schweppesrusschian)
    db.session.add(applejuice)
    db.session.add(ice)
    db.session.add(vodka)
    db.session.add(amaretto)
    db.session.add(sloegin)
    db.session.add(triplesec)
    db.session.add(proofrum)
    db.session.add(koolaid)
    db.session.add(bourbon)
    db.session.add(benedictine)
    db.session.add(bourbon)
    db.session.add(benedictine)
    db.session.add(lemonpeel)
    db.session.add(koolaid)
    db.session.add(vodka)
    db.session.add(kiwi)
    db.session.add(papaya)
    db.session.add(ginger)
    db.session.add(lemon)
    db.session.add(water)
    db.session.add(lime)
    db.session.add(sugar)
    db.session.add(sodawater)
    db.session.add(beer)
    db.session.add(amaretto)
    db.session.add(orangejuice)
    db.session.add(vodka)
    db.session.add(cointreau)
    db.session.add(lemon)
    db.session.add(galliano)
    db.session.add(absolutcitron)
    db.session.add(lemon)
    db.session.add(sugar)
    db.session.add(vodka)
    db.session.add(lime)
    db.session.add(angosturabitters)
    db.session.add(tonicwater)
    db.session.add(ice)
    db.session.add(yoghurt)
    db.session.add(water)
    db.session.add(salt)
    db.session.add(asafoetida)
    db.session.add(yoghurt)
    db.session.add(ice)
    db.session.add(ginger)
    db.session.add(water)
    db.session.add(lemon)
    db.session.add(sugar)
    db.session.add(cayennepepper)
    db.session.add(scotch)
    db.session.add(drambuie)
    db.session.add(dryvermouth)
    db.session.add(lemonpeel)
    db.session.add(gin61)
    db.session.add(maraschinoliqueur)
    db.session.add(orangebitters)
    db.session.add(mango)
    db.session.add(yoghurt)
    db.session.add(sugar)
    db.session.add(water)
    db.session.add(yoghurt)
    db.session.add(water)
    db.session.add(sugar)
    db.session.add(salt)
    db.session.add(lemonjuice42)
    db.session.add(corona)
    db.session.add(bacardilimon)
    db.session.add(darkrum)
    db.session.add(tiamaria)
    db.session.add(gin62)
    db.session.add(lightcream)
    db.session.add(powderedsugar)
    db.session.add(lemon)
    db.session.add(eggwhite)
    db.session.add(vodka)
    db.session.add(lightrum)
    db.session.add(gin63)
    db.session.add(tequila)
    db.session.add(lemon)
    db.session.add(cocacola)
    db.session.add(sweetvermouth)
    db.session.add(gin64)
    db.session.add(coconutliqueur)
    db.session.add(grapefruitjuice)
    db.session.add(sodawater)
    db.session.add(vodka)
    db.session.add(tequila)
    db.session.add(lightrum)
    db.session.add(gin65)
    db.session.add(cocacola)
    db.session.add(lemonpeel)
    db.session.add(elderflowercordial)
    db.session.add(vodka)
    db.session.add(sodawater)
    db.session.add(freshlemonjuice)
    db.session.add(yoghurt)
    db.session.add(water)
    db.session.add(cuminseed)
    db.session.add(salt)
    db.session.add(mint)
    db.session.add(honey)
    db.session.add(lightrum)
    db.session.add(lime)
    db.session.add(sugar)
    db.session.add(mint)
    db.session.add(champagne)
    db.session.add(orangejuice)
    db.session.add(lightrum)
    db.session.add(orgeatsyrup)
    db.session.add(triplesec)
    db.session.add(sweetandsour)
    db.session.add(cherry)
    db.session.add(gin66)
    db.session.add(dryvermouth)
    db.session.add(olive)
    db.session.add(beer)
    db.session.add(tomatojuice)
    db.session.add(limejuice)
    db.session.add(hotsauce)
    db.session.add(worcestershiresauce)
    db.session.add(soysauce)
    db.session.add(sweetvermouth)
    db.session.add(bourbon)
    db.session.add(angosturabitters)
    db.session.add(ice)
    db.session.add(maraschinocherry)
    db.session.add(orangepeel)
    db.session.add(tequila)
    db.session.add(triplesec)
    db.session.add(limejuice)
    db.session.add(ricard)
    db.session.add(orgeatsyrup)
    db.session.add(water)
    db.session.add(mint)
    db.session.add(bourbon)
    db.session.add(powderedsugar)
    db.session.add(water)
    db.session.add(southerncomfort)
    db.session.add(orangejuice)
    db.session.add(pepsicola)
    db.session.add(gin67)
    db.session.add(sweetvermouth)
    db.session.add(maraschinoliqueur)
    db.session.add(angosturabitters)
    db.session.add(absinthe)
    db.session.add(tequila)
    db.session.add(grenadine)
    db.session.add(proofrum)
    db.session.add(pinacoladamix)
    db.session.add(daiquirimix)
    db.session.add(vodka)
    db.session.add(limejuice)
    db.session.add(gingerale)
    db.session.add(water)
    db.session.add(sugar)
    db.session.add(cloves)
    db.session.add(cinnamon)
    db.session.add(lemonpeel)
    db.session.add(redwine)
    db.session.add(brandy)
    db.session.add(water)
    db.session.add(tea)
    db.session.add(ginger)
    db.session.add(cardamom)
    db.session.add(cloves)
    db.session.add(cinnamon)
    db.session.add(blackpepper)
    db.session.add(sugar)
    db.session.add(milk)
    db.session.add(gin68)
    db.session.add(limejuice)
    db.session.add(gingerbeer)
    db.session.add(cucumber)
    db.session.add(lemon)
    db.session.add(coffee)
    db.session.add(chambordraspberryliqueur)
    db.session.add(cocoapowder)
    db.session.add(lime)
    db.session.add(mango)
    db.session.add(mint)
    db.session.add(whiterum)
    db.session.add(ice)
    db.session.add(sodawater)
    db.session.add(mango)
    db.session.add(mint)
    db.session.add(lemonjuice43)
    db.session.add(darkrum)
    db.session.add(clubsoda)
    db.session.add(angosturabitters)
    db.session.add(gin69)
    db.session.add(benedictine)
    db.session.add(orangejuice)
    db.session.add(grenadine)
    db.session.add(baileysirishcream)
    db.session.add(whitecremedementhe)
    db.session.add(cream)
    db.session.add(lightrum)
    db.session.add(pineapplejuice)
    db.session.add(maraschinoliqueur)
    db.session.add(grenadine)
    db.session.add(maraschinocherry)
    db.session.add(lightrum)
    db.session.add(grapefruitjuice)
    db.session.add(bitters)
    db.session.add(goldschlager)
    db.session.add(butterscotchschnapps)
    db.session.add(milk)
    db.session.add(kahlua)
    db.session.add(baileysirishcream)
    db.session.add(goldschlager)
    db.session.add(heavycream)
    db.session.add(coffee)
    db.session.add(maliburum)
    db.session.add(tropicana)
    db.session.add(cranberryjuice)
    db.session.add(bourbon)
    db.session.add(darkrum)
    db.session.add(heavycream)
    db.session.add(gin70)
    db.session.add(lemonjuice44)
    db.session.add(sugarsyrup)
    db.session.add(blackberries)
    db.session.add(sodawater)
    db.session.add(mint)
    db.session.add(gin71)
    db.session.add(dryvermouth)
    db.session.add(triplesec)
    db.session.add(orangebitters)
    db.session.add(cherry)
    db.session.add(sugar)
    db.session.add(cocoapowder)
    db.session.add(salt)
    db.session.add(water)
    db.session.add(milk)
    db.session.add(vanillaextract)
    db.session.add(mango)
    db.session.add(orange)
    db.session.add(brandy)
    db.session.add(lightrum)
    db.session.add(bourbon)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(gin72)
    db.session.add(campari)
    db.session.add(sweetvermouth)
    db.session.add(blendedwhiskey)
    db.session.add(lemon)
    db.session.add(sugar)
    db.session.add(redwine)
    db.session.add(baileysirishcream)
    db.session.add(frangelico)
    db.session.add(milk)
    db.session.add(rum)
    db.session.add(vodka)
    db.session.add(gin73)
    db.session.add(bluecuracao)
    db.session.add(sourmix)
    db.session.add(lemonlimesoda)
    db.session.add(absolutcitron)
    db.session.add(grandmarnier6)
    db.session.add(lemonjuice45)
    db.session.add(clubsoda)
    db.session.add(cocoapowder)
    db.session.add(sugar)
    db.session.add(vanillaextract)
    db.session.add(milk)
    db.session.add(cremedecacao)
    db.session.add(amaretto)
    db.session.add(triplesec)
    db.session.add(vodka)
    db.session.add(lightcream)
    db.session.add(ryewhiskey)
    db.session.add(campari)
    db.session.add(dryvermouth)
    db.session.add(whiterum)
    db.session.add(sugarsyrup)
    db.session.add(limejuice)
    db.session.add(angosturabitters)
    db.session.add(prosecco)
    db.session.add(lemonjuice46)
    db.session.add(orangejuice)
    db.session.add(sugarsyrup)
    db.session.add(orangejuice)
    db.session.add(rum)
    db.session.add(vodka)
    db.session.add(cream)
    db.session.add(ice)
    db.session.add(vodka)
    db.session.add(triplesec)
    db.session.add(orangejuice)
    db.session.add(cherrybrandy)
    db.session.add(gin74)
    db.session.add(orangejuice)
    db.session.add(bourbon)
    db.session.add(angosturabitters)
    db.session.add(sugar)
    db.session.add(water)
    db.session.add(vodka)
    db.session.add(kahlua)
    db.session.add(baileysirishcream)
    db.session.add(vanillaicecream)
    db.session.add(oreocookie)
    db.session.add(kahlua)
    db.session.add(baileysirishcream)
    db.session.add(butterscotchschnapps)
    db.session.add(jagermeister)
    db.session.add(goldschlager)
    db.session.add(spicedrum)
    db.session.add(grenadine)
    db.session.add(orangejuice)
    db.session.add(sourmix)
    db.session.add(gin75)
    db.session.add(orangejuice)
    db.session.add(lemonjuice47)
    db.session.add(rosemarysyrup)
    db.session.add(sodawater)
    db.session.add(rosemary)
    db.session.add(orangepeel)
    db.session.add(milk)
    db.session.add(chocolate)
    db.session.add(orangepeel)
    db.session.add(espresso)
    db.session.add(nutmeg)
    db.session.add(whiskey)
    db.session.add(beer)
    db.session.add(lemonade)
    db.session.add(ice)
    db.session.add(grapesoda)
    db.session.add(tequila)
    db.session.add(gin76)
    db.session.add(apricotbrandy)
    db.session.add(orangejuice)
    db.session.add(bitters)
    db.session.add(gin77)
    db.session.add(gin78)
    db.session.add(orangecuracao)
    db.session.add(limejuice)
    db.session.add(angosturabitters)
    db.session.add(orangebitters)
    db.session.add(gin79)
    db.session.add(grenadine)
    db.session.add(lightcream)
    db.session.add(eggwhite)
    db.session.add(gin80)
    db.session.add(coconutliqueur)
    db.session.add(elderflowercordial)
    db.session.add(limejuice)
    db.session.add(blackberries)
    db.session.add(blendedscotch)
    db.session.add(lemonjuice48)
    db.session.add(honeysyrup)
    db.session.add(gingersyrup)
    db.session.add(islaysinglemaltscotch)
    db.session.add(pisco)
    db.session.add(lemonjuice49)
    db.session.add(sugar)
    db.session.add(ice)
    db.session.add(brandy)
    db.session.add(port)
    db.session.add(eggyolk)
    db.session.add(lightrum)
    db.session.add(coconutmilk)
    db.session.add(pineapple)
    db.session.add(everclear)
    db.session.add(vodka)
    db.session.add(peachschnapps)
    db.session.add(orangejuice)
    db.session.add(cranberryjuice)
    db.session.add(rum)
    db.session.add(passoa)
    db.session.add(limejuice)
    db.session.add(passionfruitsyrup)
    db.session.add(peachbitters)
    db.session.add(mint)
    db.session.add(vodka)
    db.session.add(cherryliqueur)
    db.session.add(cranberryjuice)
    db.session.add(orangejuice)
    db.session.add(gin81)
    db.session.add(cremedecacao)
    db.session.add(port)
    db.session.add(lightcream)
    db.session.add(powderedsugar)
    db.session.add(egg)
    db.session.add(darkrum)
    db.session.add(orgeatsyrup)
    db.session.add(orangejuice)
    db.session.add(pineapplejuice)
    db.session.add(tequila)
    db.session.add(grapefruitjuice)
    db.session.add(freshlimejuice)
    db.session.add(pineapplejuice)
    db.session.add(lime)
    db.session.add(pepper)
    db.session.add(vodka)
    db.session.add(passoa)
    db.session.add(passionfruitjuice)
    db.session.add(lime)
    db.session.add(prosecco)
    db.session.add(darkrum)
    db.session.add(orangejuice)
    db.session.add(pineapplejuice)
    db.session.add(grenadine)
    db.session.add(sugarsyrup)
    db.session.add(angosturabitters)
    db.session.add(grenadine)
    db.session.add(greencremedementhe)
    db.session.add(port)
    db.session.add(brandy)
    db.session.add(orangejuice)
    db.session.add(applejuice)
    db.session.add(pineapplejuice)
    db.session.add(sprite)
    db.session.add(pinklemonade)
    db.session.add(vodka)
    db.session.add(vodka)
    db.session.add(sugarsyrup)
    db.session.add(passionfruitjuice)
    db.session.add(ginger)
    db.session.add(pineapple)
    db.session.add(darkrum)
    db.session.add(kahlua)
    db.session.add(lightcream)
    db.session.add(nutmeg)
    db.session.add(coffeebrandy)
    db.session.add(limevodka)
    db.session.add(sherry)
    db.session.add(kahlua)
    db.session.add(midorimelonliqueur)
    db.session.add(baileysirishcream)
    db.session.add(blacksambuca)
    db.session.add(orangejuice)
    db.session.add(redwine)
    db.session.add(grenadine)
    db.session.add(dryvermouth)
    db.session.add(gin82)
    db.session.add(benedictine)
    db.session.add(lightrum)
    db.session.add(brandy)
    db.session.add(lemon)
    db.session.add(raspberrysyrup)
    db.session.add(lightrum)
    db.session.add(sherry)
    db.session.add(lime)
    db.session.add(dryvermouth)
    db.session.add(gin83)
    db.session.add(apricotbrandy)
    db.session.add(lemonjuice50)
    db.session.add(grenadine)
    db.session.add(beer)
    db.session.add(up)
    db.session.add(lightrum)
    db.session.add(lemonjuice51)
    db.session.add(sugar)
    db.session.add(orange)
    db.session.add(maraschinocherry)
    db.session.add(rum)
    db.session.add(gingerale)
    db.session.add(fruitpunch)
    db.session.add(orangejuice)
    db.session.add(ice)
    db.session.add(rum)
    db.session.add(powderedsugar)
    db.session.add(lemonpeel)
    db.session.add(water)
    db.session.add(gin84)
    db.session.add(sweetandsour)
    db.session.add(egg)
    db.session.add(rum)
    db.session.add(lemonlimesoda)
    db.session.add(lemon)
    db.session.add(maliburum)
    db.session.add(blackberrybrandy)
    db.session.add(orangejuice)
    db.session.add(pineapplejuice)
    db.session.add(cranberryjuice)
    db.session.add(scotch)
    db.session.add(drambuie)
    db.session.add(lemonpeel)
    db.session.add(crownroyal)
    db.session.add(amaretto)
    db.session.add(cranberryjuice)
    db.session.add(frangelico)
    db.session.add(crownroyal)
    db.session.add(crownroyal)
    db.session.add(peachschnapps)
    db.session.add(chambordraspberryliqueur)
    db.session.add(cranberryjuice)
    db.session.add(sugar)
    db.session.add(clubsoda)
    db.session.add(lemon)
    db.session.add(darkrum)
    db.session.add(maraschinocherry)
    db.session.add(orange)
    db.session.add(gin85)
    db.session.add(cranberryjuice)
    db.session.add(grenadine)
    db.session.add(sugarsyrup)
    db.session.add(gin86)
    db.session.add(bluecuracao)
    db.session.add(tonicwater)
    db.session.add(rosemary)
    db.session.add(gin87)
    db.session.add(lemonjuice52)
    db.session.add(sugarsyrup)
    db.session.add(cream)
    db.session.add(eggwhite)
    db.session.add(vanillaextract)
    db.session.add(sodawater)
    db.session.add(gin88)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(egg)
    db.session.add(lightrum)
    db.session.add(milk)
    db.session.add(powderedsugar)
    db.session.add(bourbon)
    db.session.add(raspberrysyrup)
    db.session.add(mint)
    db.session.add(lightrum)
    db.session.add(orangejuice)
    db.session.add(raspberryvodka)
    db.session.add(lemonlimesoda)
    db.session.add(lightrum)
    db.session.add(proofrum)
    db.session.add(powderedsugar)
    db.session.add(bitters)
    db.session.add(water)
    db.session.add(limepeel)
    db.session.add(vodka)
    db.session.add(cremedecassis)
    db.session.add(sugarsyrup)
    db.session.add(lemonjuice53)
    db.session.add(rum)
    db.session.add(vodka)
    db.session.add(tequila)
    db.session.add(gin89)
    db.session.add(triplesec)
    db.session.add(chambordraspberryliqueur)
    db.session.add(midorimelonliqueur)
    db.session.add(maliburum)
    db.session.add(redwine)
    db.session.add(peachschnapps)
    db.session.add(pepsicola)
    db.session.add(orangejuice)
    db.session.add(prosecco)
    db.session.add(campari)
    db.session.add(sodawater)
    db.session.add(brandy)
    db.session.add(amaretto)
    db.session.add(lightcream)
    db.session.add(redwine)
    db.session.add(sugar)
    db.session.add(orangejuice)
    db.session.add(lemonjuice54)
    db.session.add(brandy)
    db.session.add(whitecremedementhe)
    db.session.add(ricard)
    db.session.add(sugar)
    db.session.add(peychaudbitters)
    db.session.add(water)
    db.session.add(bourbon)
    db.session.add(lemonpeel)
    db.session.add(cognac)
    db.session.add(cointreau)
    db.session.add(lemonjuice55)
    db.session.add(vodka)
    db.session.add(amaromontenegro)
    db.session.add(rubyport)
    db.session.add(bloodorange)
    db.session.add(angosturabitters)
    db.session.add(orangepeel)
    db.session.add(sugar)
    db.session.add(allspice)
    db.session.add(rum)
    db.session.add(limejuice)
    db.session.add(champagne)
    db.session.add(orangespiral)
    db.session.add(advocaat)
    db.session.add(lemonade)
    db.session.add(lemon)
    db.session.add(ice)
    db.session.add(jimbeam)
    db.session.add(jackdaniels)
    db.session.add(wildturkey)
    db.session.add(grapefruitjuice)
    db.session.add(gin90)
    db.session.add(salt)
    db.session.add(apricotbrandy)
    db.session.add(orangejuice)
    db.session.add(sweetandsour)
    db.session.add(vodka)
    db.session.add(cranberryjuice)
    db.session.add(grapefruitjuice)
    db.session.add(scotch)
    db.session.add(lime)
    db.session.add(powderedsugar)
    db.session.add(lemon)
    db.session.add(cherry)
    db.session.add(godivaliqueur)
    db.session.add(vodka)
    db.session.add(sherry)
    db.session.add(lightcream)
    db.session.add(powderedsugar)
    db.session.add(egg)
    db.session.add(brandy)
    db.session.add(anisette)
    db.session.add(lemonade)
    db.session.add(water)
    db.session.add(vodka)
    db.session.add(vodka)
    db.session.add(cremedebanane)
    db.session.add(proofrum)
    db.session.add(maliburum)
    db.session.add(pineapplejuice)
    db.session.add(sherry)
    db.session.add(powderedsugar)
    db.session.add(egg)
    db.session.add(milk)
    db.session.add(banana)
    db.session.add(honey)
    db.session.add(redwine)
    db.session.add(sugar)
    db.session.add(water)
    db.session.add(apple)
    db.session.add(orange)
    db.session.add(lime)
    db.session.add(scotch)
    db.session.add(brandy)
    db.session.add(curacao)
    db.session.add(orange)
    db.session.add(mint)
    db.session.add(coffee)
    db.session.add(aquavit)
    db.session.add(sugar)
    db.session.add(cherrybrandy)
    db.session.add(grenadine)
    db.session.add(gin91)
    db.session.add(sweetandsour)
    db.session.add(sambuca)
    db.session.add(irishcream)
    db.session.add(lager)
    db.session.add(cider)
    db.session.add(vodka)
    db.session.add(baileysirishcream)
    db.session.add(kahlua)
    db.session.add(vodka)
    db.session.add(peachschnapps)
    db.session.add(brandy)
    db.session.add(triplesec)
    db.session.add(lemon)
    db.session.add(prosecco)
    db.session.add(aperol)
    db.session.add(sodawater)
    db.session.add(sloegin)
    db.session.add(dryvermouth)
    db.session.add(orangebitters)
    db.session.add(milk)
    db.session.add(chocolate)
    db.session.add(cinnamon)
    db.session.add(eggyolk)
    db.session.add(redwine)
    db.session.add(sugar)
    db.session.add(lemon)
    db.session.add(orange)
    db.session.add(apple)
    db.session.add(brandy)
    db.session.add(lightrum)
    db.session.add(anisette)
    db.session.add(grenadine)
    db.session.add(lemon)
    db.session.add(peachnectar)
    db.session.add(orangejuice)
    db.session.add(brownsugar)
    db.session.add(cinnamon)
    db.session.add(cloves)
    db.session.add(limejuice)
    db.session.add(strawberries)
    db.session.add(honey)
    db.session.add(water)
    db.session.add(strawberryschnapps)
    db.session.add(lightrum)
    db.session.add(limejuice)
    db.session.add(powderedsugar)
    db.session.add(strawberries)
    db.session.add(lemon)
    db.session.add(sugar)
    db.session.add(strawberries)
    db.session.add(water)
    db.session.add(lager)
    db.session.add(cider)
    db.session.add(blackcurrantsquash)
    db.session.add(pineapplejuice)
    db.session.add(clubsoda)
    db.session.add(orangejuice)
    db.session.add(lemon)
    db.session.add(berries)
    db.session.add(champagne)
    db.session.add(ouzo)
    db.session.add(baileysirishcream)
    db.session.add(gin92)
    db.session.add(grandmarnier7)
    db.session.add(strawberryschnapps)
    db.session.add(tequila)
    db.session.add(triplesec)
    db.session.add(lemonjuice56)
    db.session.add(strawberries)
    db.session.add(gin93)
    db.session.add(chocolateliqueur)
    db.session.add(amaretto)
    db.session.add(chocolatesauce)
    db.session.add(saltedchocolate)
    db.session.add(johnniewalker)
    db.session.add(honey)
    db.session.add(angelicaroot)
    db.session.add(fennelseeds)
    db.session.add(lemonpeel)
    db.session.add(watermelon)
    db.session.add(mint)
    db.session.add(grapefruitjuice)
    db.session.add(lime)
    db.session.add(tequila)
    db.session.add(watermelon)
    db.session.add(mint)
    db.session.add(scotch)
    db.session.add(wine)
    db.session.add(orangejuice)
    db.session.add(darkrum)
    db.session.add(campari)
    db.session.add(cremedebanane)
    db.session.add(pineapplejuice)
    db.session.add(limejuice)
    db.session.add(water)
    db.session.add(brownsugar)
    db.session.add(coffee)
    db.session.add(rum)
    db.session.add(vanillaextract)
    db.session.add(irishwhiskey)
    db.session.add(sweetvermouth)
    db.session.add(greenchartreuse)
    db.session.add(wildturkey)
    db.session.add(amaretto)
    db.session.add(pineapplejuice)
    db.session.add(kahlua)
    db.session.add(irishcream)
    db.session.add(amaretto)
    db.session.add(proofrum)
    db.session.add(cream)
    db.session.add(coffee)
    db.session.add(coriander)
    db.session.add(cardamom)
    db.session.add(gin94)
    db.session.add(lemonjuice57)
    db.session.add(sugar)
    db.session.add(clubsoda)
    db.session.add(maraschinocherry)
    db.session.add(orange)
    db.session.add(tomatojuice)
    db.session.add(lemonjuice58)
    db.session.add(celerysalt)
    db.session.add(grandmarnier8)
    db.session.add(coffee)
    db.session.add(coffee)
    db.session.add(jackdaniels)
    db.session.add(amaretto)
    db.session.add(tequila)
    db.session.add(lemonjuice59)
    db.session.add(grenadine)
    db.session.add(eggwhite)
    db.session.add(tequila)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(lemon)
    db.session.add(cherry)
    db.session.add(tea)
    db.session.add(water)
    db.session.add(condensedmilk)
    db.session.add(ice)
    db.session.add(mint)
    db.session.add(greenchartreuse)
    db.session.add(maraschinoliqueur)
    db.session.add(limejuice)
    db.session.add(gin95)
    db.session.add(dryvermouth)
    db.session.add(gin96)
    db.session.add(anis)
    db.session.add(bitters)
    db.session.add(orangepeel)
    db.session.add(gin97)
    db.session.add(elderflowercordial)
    db.session.add(rossovermouth)
    db.session.add(tonicwater)
    db.session.add(lime)
    db.session.add(ginger)
    db.session.add(mint)
    db.session.add(tequila)
    db.session.add(up)
    db.session.add(tequila)
    db.session.add(gin98)
    db.session.add(melonliqueur)
    db.session.add(orangebitters)
    db.session.add(lemonjuice60)
    db.session.add(prosecco)
    db.session.add(dryvermouth)
    db.session.add(gin99)
    db.session.add(maraschinoliqueur)
    db.session.add(anis)
    db.session.add(orangebitters)
    db.session.add(cherry)
    db.session.add(tequila)
    db.session.add(tabascosauce)
    db.session.add(coffee)
    db.session.add(cream)
    db.session.add(irishwhiskey)
    db.session.add(amaretto)
    db.session.add(cranberryjuice)
    db.session.add(yukonjack)
    db.session.add(cherrybrandy)
    db.session.add(southerncomfort)
    db.session.add(sweetandsour)
    db.session.add(tequila)
    db.session.add(limejuice)
    db.session.add(agavesyrup)
    db.session.add(lightrum)
    db.session.add(gin100)
    db.session.add(sweetvermouth)
    db.session.add(campari)
    db.session.add(lemonjuice61)
    db.session.add(orgeatsyrup)
    db.session.add(orangepeel)
    db.session.add(cremedecacao)
    db.session.add(bluecuracao)
    db.session.add(lightrum)
    db.session.add(gin101)
    db.session.add(vodka)
    db.session.add(lilletblanc)
    db.session.add(gin102)
    db.session.add(sweetvermouth)
    db.session.add(brandy)
    db.session.add(tequila)
    db.session.add(tomatojuice)
    db.session.add(orangejuice)
    db.session.add(limejuice)
    db.session.add(sugarsyrup)
    db.session.add(salt)
    db.session.add(lightrum)
    db.session.add(sweetvermouth)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(eggwhite)
    db.session.add(darkrum)
    db.session.add(cherrybrandy)
    db.session.add(lightrum)
    db.session.add(maplesyrup)
    db.session.add(lemonjuice62)
    db.session.add(vodka)
    db.session.add(halfandhalf)
    db.session.add(limeade)
    db.session.add(vodka)
    db.session.add(lemonjuice63)
    db.session.add(lemonpeel)
    db.session.add(ice)
    db.session.add(sprite)
    db.session.add(limejuice)
    db.session.add(vodka)
    db.session.add(vodka)
    db.session.add(tonicwater)
    db.session.add(lemonpeel)
    db.session.add(vodka)
    db.session.add(dryvermouth)
    db.session.add(olive)
    db.session.add(vodka)
    db.session.add(dryvermouth)
    db.session.add(cremedecassis)
    db.session.add(vodka)
    db.session.add(lemonjuice64)
    db.session.add(grapejuice)
    db.session.add(powderedsugar)
    db.session.add(orange)
    db.session.add(vodka)
    db.session.add(apricotbrandy)
    db.session.add(orangejuice)
    db.session.add(orangebitters)
    db.session.add(scotch)
    db.session.add(wine)
    db.session.add(gin103)
    db.session.add(triplesec)
    db.session.add(lemonjuice65)
    db.session.add(redwine)
    db.session.add(lemon)
    db.session.add(orangejuice)
    db.session.add(orange)
    db.session.add(pineapplejuice)
    db.session.add(redwine)
    db.session.add(lemonlimesoda)
    db.session.add(ice)
    db.session.add(tequila)
    db.session.add(campari)
    db.session.add(limejuice)
    db.session.add(orangejuice)
    db.session.add(rosemarysyrup)
    db.session.add(salt)
    db.session.add(blendedwhiskey)
    db.session.add(lemon)
    db.session.add(powderedsugar)
    db.session.add(cherry)
    db.session.add(lemon)
    db.session.add(vodka)
    db.session.add(coffeeliqueur)
    db.session.add(tequila)
    db.session.add(grapefruitjuice)
    db.session.add(limejuice)
    db.session.add(agavesyrup)
    db.session.add(pepper)
    db.session.add(lime)
    db.session.add(lemon)
    db.session.add(whitewine)
    db.session.add(strawberries)
    db.session.add(apple)
    db.session.add(applebrandy)
    db.session.add(sodawater)
    db.session.add(ice)
    db.session.add(tequila)
    db.session.add(creamofcoconut)
    db.session.add(limejuice)
    db.session.add(triplesec)
    db.session.add(gin104)
    db.session.add(pineapplejuice)
    db.session.add(whiterum)
    db.session.add(galliano)
    db.session.add(triplesec)
    db.session.add(limejuice)
    db.session.add(yoghurt)
    db.session.add(fruit)
    db.session.add(sambuca)
    db.session.add(baileysirishcream)
    db.session.add(whitecremedementhe)
    db.session.add(peachtreeschnapps)
    db.session.add(surge)
    db.session.add(cocacola)
    db.session.add(rum)
    db.session.add(goldrum)
    db.session.add(proofrum)
    db.session.add(pernod)
    db.session.add(grenadine)
    db.session.add(limejuice)
    db.session.add(angosturabitters)
    db.session.add(sambuca)
    db.session.add(rootbeer)
    db.session.add(ice)
    db.session.add(vodka)
    db.session.add(ouzo)
    db.session.add(jägermeister)
    db.session.add(rootbeer)
    db.session.add(chambordraspberryliqueur)
    db.session.add(vodka)
    db.session.add(sodawater)
    db.session.add(zima)
    db.session.add(chambordraspberryliqueur)
    db.session.add(cointreau)
    db.session.add(lemonjuice66)
    db.session.add(ice)
    db.session.add(lemon)
    db.session.add(midorimelonliqueur)
    db.session.add(zima)
    db.session.add(amaretto)
    db.session.add(rum)
    db.session.add(koolaid)
    db.session.add(vermouth)
    db.session.add(applejuice)


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
