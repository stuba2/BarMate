from app.models import db, environment, SCHEMA, User
from app.models.ingredient import Ingredient
from sqlalchemy.sql import text
from app.seeds.users import ex
from app.models.ingredient import bar_ingredients

# Adds a demo user, you can add other ingredients here if you want
def seed_ingredients():
    malortt = Ingredient( #1
        name='Jeppson\'s Malort')
    red_bulll = Ingredient( #2
        name='Red Bull')
    hammss = Ingredient( #3
        name='Hamm\'s Beer')
    mountain_deww = Ingredient( #4
        name='Mountain Dew')
    vodkaa = Ingredient( #5
        name='Vodka')
    ginn = Ingredient( #6
        name='Gin')
    apple_ciderr = Ingredient( #7
        name='Apple Cider')
    lemon_juicee = Ingredient( #8
        name='Lemon Juice')
    maple_syrupp = Ingredient( #9
        name='Maple Syrup')
    bourbonn = Ingredient( #10
        name='Bourbon')
    lime_juicee = Ingredient( #11
        name='Lime Juice')
    ginger_beerr = Ingredient( #12
        name='Ginger Beer')
    mintt = Ingredient( #13
        name='Mint')
    tequilaa = Ingredient( #14
        name='Tequila')
    orange_juicee = Ingredient( #15
        name='Orange Juice')

    mountain_deww.bar_ingredients_users.append(ex[0])
    red_bulll.bar_ingredients_users.append(ex[0])
    vodkaa.bar_ingredients_users.append(ex[0])
    hammss.bar_ingredients_users.append(ex[0])

    ginn.bar_ingredients_users.append(ex[1])
    apple_ciderr.bar_ingredients_users.append(ex[1])
    lemon_juicee.bar_ingredients_users.append(ex[1])
    maple_syrupp.bar_ingredients_users.append(ex[1])

    bourbonn.bar_ingredients_users.append(ex[2])
    lime_juicee.bar_ingredients_users.append(ex[2])
    ginger_beerr.bar_ingredients_users.append(ex[2])
    mintt.bar_ingredients_users.append(ex[2])

    tequilaa.bar_ingredients_users.append(ex[3])
    lime_juicee.bar_ingredients_users.append(ex[3])
    orange_juicee.bar_ingredients_users.append(ex[3])
    malortt.bar_ingredients_users.append(ex[3])
    ginger_beerr.bar_ingredients_users.append(ex[3])


    db.session.add(malortt)
    db.session.add(red_bulll)
    db.session.add(hammss)
    db.session.add(mountain_deww)
    db.session.add(vodkaa)
    db.session.add(ginn)
    db.session.add(apple_ciderr)
    db.session.add(lemon_juicee)
    db.session.add(maple_syrupp)
    db.session.add(bourbonn)
    db.session.add(lime_juicee)
    db.session.add(ginger_beerr)
    db.session.add(mintt)
    db.session.add(tequilaa)
    db.session.add(orange_juicee)


    GrandMarnier = Ingredient(
        name='Grand Marnier')
    Grenadine = Ingredient(
        name='Grenadine')
    Amaretto = Ingredient(
        name='Amaretto')
    Baileysirishcream = Ingredient(
        name='Baileys Irish Cream')
    Cognac = Ingredient(
        name='Cognac')
    Heavycream = Ingredient(
        name='Heavy Cream')
    Milk = Ingredient(
        name='Milk')
    EggWhite = Ingredient(
        name='Egg White')
    proofrum = Ingredient(
        name='151 Proof Rum')
    WildTurkey = Ingredient(
        name='Wild Turkey')
    AbsolutVodka = Ingredient(
        name='Absolut Vodka')
    Applejack = Ingredient(
        name='Applejack')
    Strawberryschnapps = Ingredient(
        name='Strawberry Schnapps')
    Clubsoda = Ingredient(
        name='Club Soda')
    Applejuice = Ingredient(
        name='Apple Juice')
    PisangAmbon = Ingredient(
        name='Pisang Ambon')
    Lemonade = Ingredient(
        name='Lemonade')
    Peachnectar = Ingredient(
        name='Peach Nectar')
    Vermouth = Ingredient(
        name='Vermouth')
    Kahlua = Ingredient(
        name='Kahlua')
    Sugar = Ingredient(
        name='Sugar')
    Scotch = Ingredient(
        name='Scotch')
    SweetVermouth = Ingredient(
        name='Sweet Vermouth')
    DryVermouth = Ingredient(
        name='Dry Vermouth')
    Rum = Ingredient(
        name='Rum')
    Fruit = Ingredient(
        name='Fruit')
    Ice = Ingredient(
        name='Ice')
    Salt = Ingredient(
        name='Salt')
    Fruitjuice = Ingredient(
        name='Fruit Juice')
    SodaWater = Ingredient(
        name='Soda Water')
    CremedeBanane = Ingredient(
        name='Creme de Banane')
    Frangelico = Ingredient(
        name='Frangelico')
    Coffee = Ingredient(
        name='Coffee')
    Cream = Ingredient(
        name='Cream')
    CremedeCacao = Ingredient(
        name='Creme de Cacao')
    Lightcream = Ingredient(
        name='Light Cream')
    Nutmeg = Ingredient(
        name='Nutmeg')
    Blendedwhiskey = Ingredient(
        name='Blended Whiskey')
    Blackberrybrandy = Ingredient(
        name='Blackberry Brandy')
    Campari = Ingredient(
        name='Campari')
    JackDaniels = Ingredient(
        name='Jack Daniels')
    Midorimelonliqueur = Ingredient(
        name='Midori Melon Liqueur')
    Sourmix = Ingredient(
        name='Sour Mix')
    Bitters = Ingredient(
        name='Bitters')
    CrownRoyal = Ingredient(
        name='Crown Royal')
    CremedeCassis = Ingredient(
        name='Creme de Cassis')
    FreshLemonJuice = Ingredient(
        name='Fresh Lemon Juice')
    Peppermintschnapps = Ingredient(
        name='Peppermint Schnapps')
    Apricotbrandy = Ingredient(
        name='Apricot Brandy')
    Applebrandy = Ingredient(
        name='Apple Brandy')
    Hpnotiq = Ingredient(
        name='Hpnotiq')
    PineappleJuice = Ingredient(
        name='Pineapple Juice')
    BananaLiqueur = Ingredient(
        name='Banana Liqueur')
    Wine = Ingredient(
        name='Wine')
    Benedictine = Ingredient(
        name='Benedictine')
    Lime = Ingredient(
        name='Lime')
    Anise = Ingredient(
        name='Anise')
    Licoriceroot = Ingredient(
        name='Licorice Root')
    Wormwood = Ingredient(
        name='Wormwood')
    AbsolutKurant = Ingredient(
        name='Absolut Kurant')
    Sprite = Ingredient(
        name='Sprite')
    Candy = Ingredient(
        name='Candy')
    Gingerale = Ingredient(
        name='Ginger Ale')
    Water = Ingredient(
        name='Water')
    Tea = Ingredient(
        name='Tea')
    Carrot = Ingredient(
        name='Carrot')
    Orange = Ingredient(
        name='Orange')
    Limejuicecordial = Ingredient(
        name='Lime Juice Cordial')
    SouthernComfort = Ingredient(
        name='Southern Comfort')
    Passionfruitsyrup = Ingredient(
        name='Passion Fruit Syrup')
    AngosturaBitters = Ingredient(
        name='Angostura Bitters')
    WhiteWine = Ingredient(
        name='White Wine')
    OrangePeel = Ingredient(
        name='Orange Peel')
    Aperol = Ingredient(
        name='Aperol')
    Prosecco = Ingredient(
        name='Prosecco')
    Up = Ingredient(
        name='7-Up')
    Appleschnapps = Ingredient(
        name='Apple Schnapps')
    Champagne = Ingredient(
        name='Champagne')
    GreenCremedeMenthe = Ingredient(
        name='Green Creme de Menthe')
    BlueCuracao = Ingredient(
        name='Blue Curacao')
    Cherry = Ingredient(
        name='Cherry')
    Lemonvodka = Ingredient(
        name='Lemon Vodka')
    Chocolateicecream = Ingredient(
        name='Chocolate Ice Cream')
    Brandy = Ingredient(
        name='Brandy')
    Ginger = Ingredient(
        name='Ginger')
    Sherry = Ingredient(
        name='Sherry')
    Sloegin = Ingredient(
        name='Sloe Gin')
    YellowChartreuse = Ingredient(
        name='Yellow Chartreuse')
    Kummel = Ingredient(
        name='Kummel')
    Cider = Ingredient(
        name='Cider')
    Goldtequila = Ingredient(
        name='Gold Tequila')
    Creamofcoconut = Ingredient(
        name='Cream of Coconut')
    Pineapple = Ingredient(
        name='Pineapple')
    Redwine = Ingredient(
        name='Red Wine')
    Apricot = Ingredient(
        name='Apricot')
    Almondflavoring = Ingredient(
        name='Almond Flavoring')
    Grainalcohol = Ingredient(
        name='Grain Alcohol')
    Foodcoloring = Ingredient(
        name='Food Coloring')
    Glycerine = Ingredient(
        name='Glycerine')
    WhiteCremedeMenthe = Ingredient(
        name='White Creme de Menthe')
    Angelicaroot = Ingredient(
        name='Angelica Root')
    Almond = Ingredient(
        name='Almond')
    Allspice = Ingredient(
        name='Allspice')
    Cinnamon = Ingredient(
        name='Cinnamon')
    Coriander = Ingredient(
        name='Coriander')
    Marjoramleaves = Ingredient(
        name='Marjoram Leaves')
    Maui = Ingredient(
        name='Maui')
    Icedtea = Ingredient(
        name='Iced Tea')
    AbsolutCitron = Ingredient(
        name='Absolut Citron')
    Bitterlemon = Ingredient(
        name='Bitter Lemon')
    Peachschnapps = Ingredient(
        name='Peach Schnapps')
    Guavajuice = Ingredient(
        name='Guava Juice')
    Brownsugar = Ingredient(
        name='Brown Sugar')
    Cloves = Ingredient(
        name='Cloves')
    Jägermeister = Ingredient(
        name='Jägermeister')
    Goldschlager = Ingredient(
        name='Goldschläger')
    Coconutrum = Ingredient(
        name='Coconut Rum')
    Lemon = Ingredient(
        name='Lemon')
    CranberryJuice = Ingredient(
        name='Cranberry Juice')
    Berries = Ingredient(
        name='Berries')
    Apple = Ingredient(
        name='Apple')
    SugarSyrup = Ingredient(
        name='Sugar Syrup')
    Kirschwasser = Ingredient(
        name='Kirschwasser')
    Strawberryliqueur = Ingredient(
        name='Strawberry Liqueur')
    Strawberries = Ingredient(
        name='Strawberries')
    SchweppesRusschian = Ingredient(
        name='Schweppes Russchian')
    Añejorum = Ingredient(
        name='Añejo rum')
    DarkCremedeCacao = Ingredient(
        name='Dark Creme de Cacao')
    Sambuca = Ingredient(
        name='Sambuca')
    OrangeBitters = Ingredient(
        name='Orange Bitters')
    GreenChartreuse = Ingredient(
        name='Green Chartreuse')
    Irishcream = Ingredient(
        name='Irish Cream')
    CremedeMure = Ingredient(
        name='Creme de Mure')
    RyeWhiskey = Ingredient(
        name='Rye Whiskey')
    MaraschinoLiqueur = Ingredient(
        name='Maraschino Liqueur')
    MaraschinoCherry = Ingredient(
        name='Maraschino Cherry')
    Passionfruitjuice = Ingredient(
        name='Passion Fruit Juice')
    Galliano = Ingredient(
        name='Galliano')
    HotChocolate = Ingredient(
        name='Hot Chocolate')
    CherryHeering = Ingredient(
        name='Cherry Heering')
    Corona = Ingredient(
        name='Corona')
    BacardiLimon = Ingredient(
        name='Bacardi Limon')
    Everclear = Ingredient(
        name='Everclear')
    Surge = Ingredient(
        name='Surge')
    Powderedsugar = Ingredient(
        name='Powdered Sugar')
    DarkRum = Ingredient(
        name='Dark Rum')
    SweetandSour = Ingredient(
        name='Sweet & Sour')
    ErinCream = Ingredient(
        name='Erin Cream')
    Advocaat = Ingredient(
        name='Advocaat')
    Tabascosauce = Ingredient(
        name='Tabasco Sauce')
    Ale = Ingredient(
        name='Ale')
    Guinnessstout = Ingredient(
        name='Guinness Stout')
    Goldrum = Ingredient(
        name='Gold Rum')
    TripleSec = Ingredient(
        name='Triple Sec')
    Egg = Ingredient(
        name='Egg')
    VanillaIceCream = Ingredient(
        name='Vanilla Ice Cream')
    Butterscotchschnapps = Ingredient(
        name='Butterscotch Schnapps')
    Lemonlimesoda = Ingredient(
        name='Lemon-Lime Soda')
    Raisins = Ingredient(
        name='Raisins')
    Blueberries = Ingredient(
        name='Blueberries')
    KoolAid = Ingredient(
        name='Kool-Aid')
    Celerysalt = Ingredient(
        name='Celery Salt')
    Godivaliqueur = Ingredient(
        name='Godiva Liqueur')
    Tiamaria = Ingredient(
        name='Tia Maria')
    CoconutLiqueur = Ingredient(
        name='Coconut Liqueur')
    Chambordraspberryliqueur = Ingredient(
        name='Chambord Raspberry Liqueur')
    Peachtreeschnapps = Ingredient(
        name='Peachtree Schnapps')
    Coffeeliqueur = Ingredient(
        name='Coffee Liqueur')
    Passoa = Ingredient(
        name='Passoa')
    MalibuRum = Ingredient(
        name='Malibu Rum')
    Banana = Ingredient(
        name='Banana')
    Rootbeer = Ingredient(
        name='Root Beer')
    Carbonatedwater = Ingredient(
        name='Carbonated Water')
    RaspberryVodka = Ingredient(
        name='Raspberry Vodka')
    Chocolatesyrup = Ingredient(
        name='Chocolate Syrup')
    Cherrybrandy = Ingredient(
        name='Cherry Brandy')
    Yoghurt = Ingredient(
        name='Yogurt')
    Honey = Ingredient(
        name='Honey')
    WhippedCream = Ingredient(
        name='Whipped Cream')
    caramelsauce = Ingredient(
        name='Caramel Sauce')
    Minisnickersbars = Ingredient(
        name='Mini Snickers Bars')
    Cantaloupe = Ingredient(
        name='Cantaloupe')
    CocaCola = Ingredient(
        name='Coca-Cola')
    Cachaca = Ingredient(
        name='Cachaca')
    Spicedrum = Ingredient(
        name='Spiced Rum')
    Falernum = Ingredient(
        name='Falernum')
    blackstraprum = Ingredient(
        name='Blackstrap Rum')
    Lager = Ingredient(
        name='Lager')
    Port = Ingredient(
        name='Port')
    Cointreau = Ingredient(
        name='Cointreau')
    Vanilla = Ingredient(
        name='Vanilla')
    Caramelcoloring = Ingredient(
        name='Caramel Coloring')
    LilletBlanc = Ingredient(
        name='Lillet Blanc')
    Absinthe = Ingredient(
        name='Absinthe')
    Chocolateliqueur = Ingredient(
        name='Chocolate Liqueur')
    Vanillaextract = Ingredient(
        name='Vanilla Extract')
    Chocolate = Ingredient(
        name='Chocolate')
    Peppermintextract = Ingredient(
        name='Peppermint Extract')
    Chocolatemilk = Ingredient(
        name='Chocolate Milk')
    Cranberries = Ingredient(
        name='Cranberries')
    LemonPeel = Ingredient(
        name='Lemon Peel')
    Cocoapowder = Ingredient(
        name='Cocoa Powder')
    Cornstarch = Ingredient(
        name='Cornstarch')
    CherryGrenadine = Ingredient(
        name='Cherry Grenadine')
    PeachBitters = Ingredient(
        name='Peach Bitters')
    Blackcurrantcordial = Ingredient(
        name='Blackcurrant Cordial')
    Fruitpunch = Ingredient(
        name='Fruit Punch')
    Olive = Ingredient(
        name='Olive')
    OliveBrine = Ingredient(
        name='Olive Brine')
    demeraraSugar = Ingredient(
        name='Demerara Sugar')
    Pisco = Ingredient(
        name='Pisco')
    PineappleSyrup = Ingredient(
        name='Pineapple Syrup')
    StGermain = Ingredient(
        name='St. Germain')
    Pepper = Ingredient(
        name='Pepper')
    Lavender = Ingredient(
        name='Lavender')
    Whiskey = Ingredient(
        name='Whiskey')
    HotDamn = Ingredient(
        name='Hot Damn')
    DubonnetRouge = Ingredient(
        name='Dubonnet Rouge')
    Vanillasyrup = Ingredient(
        name='Vanilla Syrup')
    Espresso = Ingredient(
        name='Espresso')
    Condensedmilk = Ingredient(
        name='Condensed Milk')
    Elderflowercordial = Ingredient(
        name='Elderflower Cordial')
    Mezcal = Ingredient(
        name='Mezcal')
    Rose = Ingredient(
        name='Rose')
    Figs = Ingredient(
        name='Figs')
    Thyme = Ingredient(
        name='Thyme')
    TonicWater = Ingredient(
        name='Tonic Water')
    ApricotNectar = Ingredient(
        name='Apricot Nectar')
    Pomegranatejuice = Ingredient(
        name='Pomegranate Juice')
    RaspberryLiqueur = Ingredient(
        name='Raspberry Liqueur')
    Lillet = Ingredient(
        name='Lillet')
    Firewater = Ingredient(
        name='Firewater')
    AbsolutPeppar = Ingredient(
        name='Absolut Peppar')
    DrPepper = Ingredient(
        name='Dr. Pepper')
    Beer = Ingredient(
        name='Beer')
    Sarsaparilla = Ingredient(
        name='Sarsaparilla')
    PeachVodka = Ingredient(
        name='Peach Vodka')
    Sirupofroses = Ingredient(
        name='Sirup of Roses')
    GrapefruitJuice = Ingredient(
        name='Grapefruit Juice')
    Orangespiral = Ingredient(
        name='Orange Spiral')
    Basil = Ingredient(
        name='Basil')
    AgaveSyrup = Ingredient(
        name='Agave Syrup')
    Grapes = Ingredient(
        name='Grapes')
    WhiteRum = Ingredient(
        name='White Rum')
    Blackberries = Ingredient(
        name='Blackberries')
    CherryJuice = Ingredient(
        name='Cherry Juice')
    RedChiliFlakes = Ingredient(
        name='Red Chili Flakes')
    Grapejuice = Ingredient(
        name='Grape Juice')
    Carbonatedsoftdrink = Ingredient(
        name='Carbonated Soft Drink')
    Sherbet = Ingredient(
        name='Sherbet')
    Cornsyrup = Ingredient(
        name='Corn Syrup')
    Butter = Ingredient(
        name='Butter')
    Halfandhalf = Ingredient(
        name='Half-and-Half')
    Marshmallows = Ingredient(
        name='Marshmallows')
    Coconutsyrup = Ingredient(
        name='Coconut Syrup')
    Peachbrandy = Ingredient(
        name='Peach Brandy')
    Jello = Ingredient(
        name='Jello')
    Mintsyrup = Ingredient(
        name='Mint Syrup')
    Tennesseewhiskey = Ingredient(
        name='Tennessee Whiskey')
    Kiwiliqueur = Ingredient(
        name='Kiwi Liqueur')
    Kiwi = Ingredient(
        name='Kiwi')
    Cranberryvodka = Ingredient(
        name='Cranberry Vodka')
    Apfelkorn = Ingredient(
        name='Apfelkorn')
    Papaya = Ingredient(
        name='Papaya')
    Limepeel = Ingredient(
        name='Lime Peel')
    Asafoetida = Ingredient(
        name='Asafoetida')
    Cayennepepper = Ingredient(
        name='Cayenne Pepper')
    Drambuie = Ingredient(
        name='Drambuie')
    Mango = Ingredient(
        name='Mango')
    Cuminseed = Ingredient(
        name='Cumin Seed')
    TomatoJuice = Ingredient(
        name='Tomato Juice')
    HotSauce = Ingredient(
        name='Hot Sauce')
    WorcestershireSauce = Ingredient(
        name='Worcestershire Sauce')
    SoySauce = Ingredient(
        name='Soy Sauce')
    Ricard = Ingredient(
        name='Ricard')
    OrgeatSyrup = Ingredient(
        name='Orgeat Syrup')
    PepsiCola = Ingredient(
        name='Pepsi Cola')
    Pinacoladamix = Ingredient(
        name='Piña Colada Mix')
    Daiquirimix = Ingredient(
        name='Daiquiri Mix')
    Cardamom = Ingredient(
        name='Cardamom')
    Blackpepper = Ingredient(
        name='Black Pepper')
    Cucumber = Ingredient(
        name='Cucumber')
    Tropicana = Ingredient(
        name='Tropicana')
    Oreocookie = Ingredient(
        name='Oreo Cookie')
    RosemarySyrup = Ingredient(
        name='Rosemary Syrup')
    Rosemary = Ingredient(
        name='Rosemary')
    GrapeSoda = Ingredient(
        name='Grape Soda')
    OrangeCuracao = Ingredient(
        name='Orange Curacao')
    BlendedScotch = Ingredient(
        name='Blended Scotch')
    Honeysyrup = Ingredient(
        name='Honey Syrup')
    GingerSyrup = Ingredient(
        name='Ginger Syrup')
    IslaysinglemaltScotch = Ingredient(
        name='Islay Single Malt Scotch')
    EggYolk = Ingredient(
        name='Egg Yolk')
    Coconutmilk = Ingredient(
        name='Coconut Milk')
    Cherryliqueur = Ingredient(
        name='Cherry Liqueur')
    Pinklemonade = Ingredient(
        name='Pink Lemonade')
    Coffeebrandy = Ingredient(
        name='Coffee Brandy')
    Limevodka = Ingredient(
        name='Lime Vodka')
    BlackSambuca = Ingredient(
        name='Black Sambuca')
    Raspberrysyrup = Ingredient(
        name='Raspberry Syrup')
    Peychaudbitters = Ingredient(
        name='Peychaud Bitters')
    AmaroMontenegro = Ingredient(
        name='Amaro Montenegro')
    RubyPort = Ingredient(
        name='Ruby Port')
    BloodOrange = Ingredient(
        name='Blood Orange')
    JimBeam = Ingredient(
        name='Jim Beam')
    Anisette = Ingredient(
        name='Anisette')
    Fresca = Ingredient(
        name='Fresca')
    Curacao = Ingredient(
        name='Curacao')
    Aquavit = Ingredient(
        name='Aquavit')
    Blackcurrantsquash = Ingredient(
        name='Blackcurrant Squash')
    Ouzo = Ingredient(
        name='Ouzo')
    ChocolateSauce = Ingredient(
        name='Chocolate Sauce')
    SaltedChocolate = Ingredient(
        name='Salted Chocolate')
    JohnnieWalker = Ingredient(
        name='Johnnie Walker')
    Fennelseeds = Ingredient(
        name='Fennel Seeds')
    Watermelon = Ingredient(
        name='Watermelon')
    IrishWhiskey = Ingredient(
        name='Irish Whiskey')
    RossoVermouth = Ingredient(
        name='Rosso Vermouth')
    MelonLiqueur = Ingredient(
        name='Melon Liqueur')
    YukonJack = Ingredient(
        name='Yukon Jack')
    LightRum = Ingredient(
        name='Light Rum')
    Limeade = Ingredient(
        name='Limeade')
    Pernod = Ingredient(
        name='Pernod')
    Zima = Ingredient(
        name='Zima')

    db.session.add(GrandMarnier)
    db.session.add(Grenadine)
    db.session.add(Amaretto)
    db.session.add(Baileysirishcream)
    db.session.add(Cognac)
    db.session.add(Heavycream)
    db.session.add(Milk)
    db.session.add(EggWhite)
    db.session.add(proofrum)
    db.session.add(WildTurkey)
    db.session.add(AbsolutVodka)
    db.session.add(Applejack)
    db.session.add(Strawberryschnapps)
    db.session.add(Clubsoda)
    db.session.add(Applejuice)
    db.session.add(Maraschinocherry)
    db.session.add(PisangAmbon)
    db.session.add(Lemonade)
    db.session.add(Peachnectar)
    db.session.add(Vermouth)
    db.session.add(Kahlua)
    db.session.add(Lightrum)
    db.session.add(Triplesec)
    db.session.add(Sugar)
    db.session.add(Scotch)
    db.session.add(SweetVermouth)
    db.session.add(DryVermouth)
    db.session.add(Orangebitters)
    db.session.add(maraschinoliqueur)
    db.session.add(Rum)
    db.session.add(Fruit)
    db.session.add(Ice)
    db.session.add(Salt)
    db.session.add(Fruitjuice)
    db.session.add(SodaWater)
    db.session.add(CremedeBanane)
    db.session.add(Pineapplejuice)
    db.session.add(Frangelico)
    db.session.add(Coffee)
    db.session.add(Cream)
    db.session.add(CremedeCacao)
    db.session.add(Lightcream)
    db.session.add(Nutmeg)
    db.session.add(Blendedwhiskey)
    db.session.add(Blackberrybrandy)
    db.session.add(Lemonpeel)
    db.session.add(Campari)
    db.session.add(Orangepeel)
    db.session.add(JackDaniels)
    db.session.add(Midorimelonliqueur)
    db.session.add(Sourmix)
    db.session.add(Bitters)
    db.session.add(Sodawater)
    db.session.add(CrownRoyal)
    db.session.add(CremedeCassis)
    db.session.add(FreshLemonJuice)
    db.session.add(Peppermintschnapps)
    db.session.add(Apricotbrandy)
    db.session.add(Applebrandy)
    db.session.add(Hpnotiq)
    db.session.add(PineappleJuice)
    db.session.add(BananaLiqueur)
    db.session.add(Wine)
    db.session.add(Benedictine)
    db.session.add(Lime)
    db.session.add(Anise)
    db.session.add(Licoriceroot)
    db.session.add(Wormwood)
    db.session.add(AbsolutKurant)
    db.session.add(Sprite)
    db.session.add(Grapesoda)
    db.session.add(Candy)
    db.session.add(Gingerale)
    db.session.add(Water)
    db.session.add(Tea)
    db.session.add(Whippedcream)
    db.session.add(Carrot)
    db.session.add(Orange)
    db.session.add(Limejuicecordial)
    db.session.add(SouthernComfort)
    db.session.add(Passionfruitsyrup)
    db.session.add(Sweetandsour)
    db.session.add(AngosturaBitters)
    db.session.add(WhiteWine)
    db.session.add(OrangePeel)
    db.session.add(Aperol)
    db.session.add(Prosecco)
    db.session.add(Up)
    db.session.add(Appleschnapps)
    db.session.add(Champagne)
    db.session.add(GreenCremedeMenthe)
    db.session.add(BlueCuracao)
    db.session.add(Cherry)
    db.session.add(Lemonvodka)
    db.session.add(Chocolateicecream)
    db.session.add(Brandy)
    db.session.add(AppleSchnapps)
    db.session.add(Ginger)
    db.session.add(Sherry)
    db.session.add(Sloegin)
    db.session.add(YellowChartreuse)
    db.session.add(Kummel)
    db.session.add(Cider)
    db.session.add(Maliburum)
    db.session.add(Goldtequila)
    db.session.add(Creamofcoconut)
    db.session.add(Pineapple)
    db.session.add(Ryewhiskey)
    db.session.add(Redwine)
    db.session.add(Apricot)
    db.session.add(Almondflavoring)
    db.session.add(Grainalcohol)
    db.session.add(Foodcoloring)
    db.session.add(Glycerine)
    db.session.add(WhiteCremedeMenthe)
    db.session.add(Angelicaroot)
    db.session.add(Almond)
    db.session.add(Allspice)
    db.session.add(Cinnamon)
    db.session.add(Coriander)
    db.session.add(Marjoramleaves)
    db.session.add(Maui)
    db.session.add(Icedtea)
    db.session.add(AbsolutCitron)
    db.session.add(Bitterlemon)
    db.session.add(Peachschnapps)
    db.session.add(Coconutliqueur)
    db.session.add(Guavajuice)
    db.session.add(Brownsugar)
    db.session.add(Cloves)
    db.session.add(Jägermeister)
    db.session.add(Goldschlager)
    db.session.add(Coconutrum)
    db.session.add(Lemon)
    db.session.add(CranberryJuice)
    db.session.add(Berries)
    db.session.add(Apple)
    db.session.add(SugarSyrup)
    db.session.add(Kirschwasser)
    db.session.add(Strawberryliqueur)
    db.session.add(Strawberries)
    db.session.add(SchweppesRusschian)
    db.session.add(Añejorum)
    db.session.add(DarkCremedeCacao)
    db.session.add(Hotchocolate)
    db.session.add(Sambuca)
    db.session.add(OrangeBitters)
    db.session.add(GreenChartreuse)
    db.session.add(Irishcream)
    db.session.add(Sugarsyrup)
    db.session.add(CremedeMure)
    db.session.add(RyeWhiskey)
    db.session.add(MaraschinoLiqueur)
    db.session.add(MaraschinoCherry)
    db.session.add(Passionfruitjuice)
    db.session.add(Maraschinoliqueur)
    db.session.add(Galliano)
    db.session.add(HotChocolate)
    db.session.add(CherryHeering)
    db.session.add(Corona)
    db.session.add(BacardiLimon)
    db.session.add(Everclear)
    db.session.add(Surge)
    db.session.add(Bananaliqueur)
    db.session.add(Vanillaicecream)
    db.session.add(Powderedsugar)
    db.session.add(DarkRum)
    db.session.add(SweetandSour)
    db.session.add(ErinCream)
    db.session.add(Advocaat)
    db.session.add(Tomatojuice)
    db.session.add(Worcestershiresauce)
    db.session.add(Tabascosauce)
    db.session.add(Ale)
    db.session.add(Guinnessstout)
    db.session.add(Goldrum)
    db.session.add(TripleSec)
    db.session.add(Egg)
    db.session.add(VanillaIceCream)
    db.session.add(Butterscotchschnapps)
    db.session.add(Lemonlimesoda)
    db.session.add(Raisins)
    db.session.add(Blueberries)
    db.session.add(KoolAid)
    db.session.add(Celerysalt)
    db.session.add(Godivaliqueur)
    db.session.add(Tiamaria)
    db.session.add(CoconutLiqueur)
    db.session.add(Chambordraspberryliqueur)
    db.session.add(Peachtreeschnapps)
    db.session.add(Coffeeliqueur)
    db.session.add(Passoa)
    db.session.add(MalibuRum)
    db.session.add(Banana)
    db.session.add(Rootbeer)
    db.session.add(Carbonatedwater)
    db.session.add(RaspberryVodka)
    db.session.add(Chocolatesyrup)
    db.session.add(Cherrybrandy)
    db.session.add(Yoghurt)
    db.session.add(Honey)
    db.session.add(WhippedCream)
    db.session.add(caramelsauce)
    db.session.add(chocolatesauce)
    db.session.add(Minisnickersbars)
    db.session.add(Cantaloupe)
    db.session.add(CocaCola)
    db.session.add(Cachaca)
    db.session.add(Spicedrum)
    db.session.add(Falernum)
    db.session.add(blackstraprum)
    db.session.add(Whiterum)
    db.session.add(Lager)
    db.session.add(Port)
    db.session.add(Cointreau)
    db.session.add(Vanilla)
    db.session.add(Caramelcoloring)
    db.session.add(Eggyolk)
    db.session.add(LilletBlanc)
    db.session.add(Absinthe)
    db.session.add(Chocolateliqueur)
    db.session.add(Vanillaextract)
    db.session.add(Chocolate)
    db.session.add(Peppermintextract)
    db.session.add(Chocolatemilk)
    db.session.add(Cranberries)
    db.session.add(LemonPeel)
    db.session.add(Cocoapowder)
    db.session.add(Cornstarch)
    db.session.add(CherryGrenadine)
    db.session.add(PeachBitters)
    db.session.add(Blackcurrantcordial)
    db.session.add(Fruitpunch)
    db.session.add(Olive)
    db.session.add(OliveBrine)
    db.session.add(demeraraSugar)
    db.session.add(Pisco)
    db.session.add(PineappleSyrup)
    db.session.add(StGermain)
    db.session.add(Pepper)
    db.session.add(Lavender)
    db.session.add(Whiskey)
    db.session.add(HotDamn)
    db.session.add(DubonnetRouge)
    db.session.add(Whippingcream)
    db.session.add(Vanillasyrup)
    db.session.add(Espresso)
    db.session.add(Condensedmilk)
    db.session.add(Elderflowercordial)
    db.session.add(Mezcal)
    db.session.add(Rose)
    db.session.add(Figs)
    db.session.add(Thyme)
    db.session.add(TonicWater)
    db.session.add(ApricotNectar)
    db.session.add(Pomegranatejuice)
    db.session.add(lemon)
    db.session.add(RaspberryLiqueur)
    db.session.add(pineapplejuice)
    db.session.add(Lillet)
    db.session.add(Firewater)
    db.session.add(AbsolutPeppar)
    db.session.add(DrPepper)
    db.session.add(Beer)
    db.session.add(Sarsaparilla)
    db.session.add(PeachVodka)
    db.session.add(Sirupofroses)
    db.session.add(GrapefruitJuice)
    db.session.add(Orangespiral)
    db.session.add(Basil)
    db.session.add(AgaveSyrup)
    db.session.add(Melonliqueur)
    db.session.add(Grapes)
    db.session.add(Whisky)
    db.session.add(WhiteRum)
    db.session.add(Blackberries)
    db.session.add(CherryJuice)
    db.session.add(RedChiliFlakes)
    db.session.add(Grapejuice)
    db.session.add(Carbonatedsoftdrink)
    db.session.add(Sherbet)
    db.session.add(Cornsyrup)
    db.session.add(Irishwhiskey)
    db.session.add(Butter)
    db.session.add(Halfandhalf)
    db.session.add(Marshmallows)
    db.session.add(Coconutsyrup)
    db.session.add(Peachbrandy)
    db.session.add(Anis)
    db.session.add(Jello)
    db.session.add(Mintsyrup)
    db.session.add(Tennesseewhiskey)
    db.session.add(Kiwiliqueur)
    db.session.add(Kiwi)
    db.session.add(Cranberryvodka)
    db.session.add(Apfelkorn)
    db.session.add(Papaya)
    db.session.add(Limepeel)
    db.session.add(Angosturabitters)
    db.session.add(Asafoetida)
    db.session.add(Cayennepepper)
    db.session.add(Drambuie)
    db.session.add(Mango)
    db.session.add(Cuminseed)
    db.session.add(Orgeatsyrup)
    db.session.add(TomatoJuice)
    db.session.add(HotSauce)
    db.session.add(WorcestershireSauce)
    db.session.add(SoySauce)
    db.session.add(Ricard)
    db.session.add(OrgeatSyrup)
    db.session.add(PepsiCola)
    db.session.add(Pinacoladamix)
    db.session.add(Daiquirimix)
    db.session.add(Cardamom)
    db.session.add(Blackpepper)
    db.session.add(Cucumber)
    db.session.add(Tropicana)
    db.session.add(Oreocookie)
    db.session.add(Jagermeister)
    db.session.add(RosemarySyrup)
    db.session.add(Rosemary)
    db.session.add(GrapeSoda)
    db.session.add(ApricotBrandy)
    db.session.add(OrangeCuracao)
    db.session.add(BlendedScotch)
    db.session.add(Honeysyrup)
    db.session.add(GingerSyrup)
    db.session.add(IslaysinglemaltScotch)
    db.session.add(EggYolk)
    db.session.add(Coconutmilk)
    db.session.add(Cherryliqueur)
    db.session.add(Pinklemonade)
    db.session.add(Coffeebrandy)
    db.session.add(Limevodka)
    db.session.add(BlackSambuca)
    db.session.add(Raspberrysyrup)
    db.session.add(Raspberryvodka)
    db.session.add(Peychaudbitters)
    db.session.add(AmaroMontenegro)
    db.session.add(RubyPort)
    db.session.add(BloodOrange)
    db.session.add(JimBeam)
    db.session.add(Anisette)
    db.session.add(Cherries)
    db.session.add(Fresca)
    db.session.add(Curacao)
    db.session.add(Aquavit)
    db.session.add(Blackcurrantsquash)
    db.session.add(Ouzo)
    db.session.add(ChocolateSauce)
    db.session.add(SaltedChocolate)
    db.session.add(JohnnieWalker)
    db.session.add(Fennelseeds)
    db.session.add(Watermelon)
    db.session.add(CremeDeBanane)
    db.session.add(IrishWhiskey)
    db.session.add(RossoVermouth)
    db.session.add(up)
    db.session.add(MelonLiqueur)
    db.session.add(YukonJack)
    db.session.add(Agavesyrup)
    db.session.add(LightRum)
    db.session.add(Limeade)
    db.session.add(AppleBrandy)
    db.session.add(Pernod)
    db.session.add(Zima)

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

        # mountain_deww = Ingredient.query.filter(Ingredient.name == 'Mountain Dew').first()
        # red_bulll = Ingredient.query.filter(Ingredient.name == 'Red Bull').first()
        # vodkaa = Ingredient.query.filter(Ingredient.name == 'Vodka').first()
        # hammss = Ingredient.query.filter(Ingredient.name == 'Hamm\'s Beer').first()
        # ginn = Ingredient.query.filter(Ingredient.name == 'Gin').first()
        # apple_ciderr = Ingredient.query.filter(Ingredient.name == 'Apple Cider').first()
        # lemon_juicee = Ingredient.query.filter(Ingredient.name == 'Lemon Juice').first()
        # maple_syrupp = Ingredient.query.filter(Ingredient.name == 'Maple Syrup').first()
        # bourbonn = Ingredient.query.filter(Ingredient.name == 'Bourbon').first()
        # lime_juicee = Ingredient.query.filter(Ingredient.name == 'Lime Juice').first()
        # ginger_beerr = Ingredient.query.filter(Ingredient.name == 'Ginger Beer').first()
        # mintt = Ingredient.query.filter(Ingredient.name == 'Mint').first()
        # tequilaa = Ingredient.query.filter(Ingredient.name == 'Tequila').first()
        # orange_juicee = Ingredient.query.filter(Ingredient.name == 'Orange Juice').first()
        # malortt = Ingredient.query.filter(Ingredient.name == 'Malort').first()

        # all_ingredients = Ingredient.query.all()
        # print('\n ========', all_ingredients)
        # print('\n ========', lemon_juicee)
        # print('\n ========', lemon_juicee.bar_ingredients_users)

        # print('\n row1::::hi::::',)
        # row1 = db.session.query(bar_ingredients).filter(bar_ingredients.user_id=1, ingredient_id=1).one()
        # table = db.session.query(bar_ingredients).all()
        # print('\n ;;;;;;;;;;', table)
        # print('\n row1::::::::', row1)

        # db.session.delete(row1)

        # print('\n hamms:::::::::::::', ginn)
        # hammss.bar_ingredients_users.remove(ex[0])
        # vodkaa.bar_ingredients_users.remove(ex[0])
        # red_bulll.bar_ingredients_users.remove(ex[0])
        # mountain_deww.bar_ingredients_users.remove(ex[0])
        # user1 = User.query.get(1)
        # user2 = User.query.get(2)
        # user3 = User.query.get(3)
        # user4 = User.query.get(4)
        # print('\n +++++++++++', ex)
        # print('\n +++++++++++', User.query.get(2))
        # lemon_juicee.bar_ingredients_users.remove(user2)
        # apple_ciderr.bar_ingredients_users.remove(ex[1])
        # print('\n **********', lemon_juicee.bar_ingredients_users)
        # maple_syrupp.bar_ingredients_users.remove(ex[1])
        # ginn.bar_ingredients_users.remove(ex[1])


        # mintt.bar_ingredients_users.remove(ex[2])
        # ginger_beerr.bar_ingredients_users.remove(ex[2])
        # lime_juicee.bar_ingredients_users.remove(ex[2])
        # bourbonn.bar_ingredients_users.remove(ex[2])

        # ginger_beerr.bar_ingredients_users.remove(ex[3])
        # malortt.bar_ingredients_users.remove(ex[3])
        # orange_juicee.bar_ingredients_users.remove(ex[3])
        # lime_juicee.bar_ingredients_users.remove(ex[3])
        # tequilaa.bar_ingredients_users.remove(ex[3])

        db.session.execute(text("DELETE FROM bar_ingredients"))
        db.session.execute(text("DELETE FROM ingredients"))

    db.session.commit()
