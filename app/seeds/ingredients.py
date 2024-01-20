from app.models import db, environment, SCHEMA
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
        name='Baileys irish cream')
    Cognac = Ingredient(
        name='Cognac')
    Heavycream = Ingredient(
        name='Heavy cream')
    Milk = Ingredient(
        name='Milk')
    EggWhite = Ingredient(
        name='Egg White')
    proofrum = Ingredient(
        name='151 proof rum')
    WildTurkey = Ingredient(
        name='Wild Turkey')
    Darkrum = Ingredient(
        name='Dark rum')
    Lemonjuice = Ingredient(
        name='Lemon juice')
    AbsolutVodka = Ingredient(
        name='Absolut Vodka')
    Tonicwater = Ingredient(
        name='Tonic water')
    Applejack = Ingredient(
        name='Applejack')
    Grapefruitjuice = Ingredient(
        name='Grapefruit juice')
    Strawberryschnapps = Ingredient(
        name='Strawberry schnapps')
    Cranberryjuice = Ingredient(
        name='Cranberry juice')
    Clubsoda = Ingredient(
        name='Club soda')
    Applejuice = Ingredient(
        name='Apple juice')
    Maraschinocherry = Ingredient(
        name='Maraschino cherry')
    PisangAmbon = Ingredient(
        name='Pisang Ambon')
    Lemonade = Ingredient(
        name='Lemonade')
    Peachnectar = Ingredient(
        name='Peach nectar')
    Vermouth = Ingredient(
        name='Vermouth')
    Kahlua = Ingredient(
        name='Kahlua')
    Eggwhite = Ingredient(
        name='Egg white')
    Lightrum = Ingredient(
        name='Light rum')
    Triplesec = Ingredient(
        name='Triple sec')
    Sugar = Ingredient(
        name='Sugar')
    Scotch = Ingredient(
        name='Scotch')
    SweetVermouth = Ingredient(
        name='Sweet Vermouth')
    DryVermouth = Ingredient(
        name='Dry Vermouth')
    Orangebitters = Ingredient(
        name='Orange bitters')
    lemonjuice = Ingredient(
        name='lemon juice')
    maraschinoliqueur = Ingredient(
        name='maraschino liqueur')
    Rum = Ingredient(
        name='Rum')
    Fruit = Ingredient(
        name='Fruit')
    Ice = Ingredient(
        name='Ice')
    Salt = Ingredient(
        name='Salt')
    Fruitjuice = Ingredient(
        name='Fruit juice')
    SodaWater = Ingredient(
        name='Soda Water')
    CremedeBanane = Ingredient(
        name='Creme de Banane')
    Pineapplejuice = Ingredient(
        name='Pineapple juice')
    Frangelico = Ingredient(
        name='Frangelico')
    Coffee = Ingredient(
        name='Coffee')
    Cream = Ingredient(
        name='Cream')
    CremedeCacao = Ingredient(
        name='Creme de Cacao')
    Lightcream = Ingredient(
        name='Light cream')
    Nutmeg = Ingredient(
        name='Nutmeg')
    Blendedwhiskey = Ingredient(
        name='Blended whiskey')
    Blackberrybrandy = Ingredient(
        name='Blackberry brandy')
    Lemonpeel = Ingredient(
        name='Lemon peel')
    Campari = Ingredient(
        name='Campari')
    Orangepeel = Ingredient(
        name='Orange peel')
    JackDaniels = Ingredient(
        name='Jack Daniels')
    Midorimelonliqueur = Ingredient(
        name='Midori melon liqueur')
    Sourmix = Ingredient(
        name='Sour mix')
    Bitters = Ingredient(
        name='Bitters')
    Sodawater = Ingredient(
        name='Soda water')
    CrownRoyal = Ingredient(
        name='Crown Royal')
    CremedeCassis = Ingredient(
        name='Creme de Cassis')
    FreshLemonJuice = Ingredient(
        name='Fresh Lemon Juice')
    Peppermintschnapps = Ingredient(
        name='Peppermint schnapps')
    Apricotbrandy = Ingredient(
        name='Apricot brandy')
    Applebrandy = Ingredient(
        name='Apple brandy')
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
        name='Licorice root')
    Wormwood = Ingredient(
        name='Wormwood')
    AbsolutKurant = Ingredient(
        name='Absolut Kurant')
    Sprite = Ingredient(
        name='Sprite')
    Grapesoda = Ingredient(
        name='Grape soda')
    Candy = Ingredient(
        name='Candy')
    Gingerale = Ingredient(
        name='Ginger ale')
    Water = Ingredient(
        name='Water')
    Tea = Ingredient(
        name='Tea')
    Whippedcream = Ingredient(
        name='Whipped cream')
    Applecider = Ingredient(
        name='Apple cider')
    Carrot = Ingredient(
        name='Carrot')
    Orange = Ingredient(
        name='Orange')
    Limejuicecordial = Ingredient(
        name='Lime juice cordial')
    SouthernComfort = Ingredient(
        name='Southern Comfort')
    Passionfruitsyrup = Ingredient(
        name='Passion fruit syrup')
    Sweetandsour = Ingredient(
        name='Sweet and sour')
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
        name='Apple schnapps')
    Champagne = Ingredient(
        name='Champagne')
    GreenCremedeMenthe = Ingredient(
        name='Green Creme de Menthe')
    BlueCuracao = Ingredient(
        name='Blue Curacao')
    Cherry = Ingredient(
        name='Cherry')
    Lemonvodka = Ingredient(
        name='Lemon vodka')
    Chocolateicecream = Ingredient(
        name='Chocolate ice-cream')
    Brandy = Ingredient(
        name='Brandy')
    AppleSchnapps = Ingredient(
        name='Apple Schnapps')
    Ginger = Ingredient(
        name='Ginger')
    Sherry = Ingredient(
        name='Sherry')
    Sloegin = Ingredient(
        name='Sloe gin')
    YellowChartreuse = Ingredient(
        name='Yellow Chartreuse')
    Kummel = Ingredient(
        name='Kummel')
    Cider = Ingredient(
        name='Cider')
    Maliburum = Ingredient(
        name='Malibu rum')
    Goldtequila = Ingredient(
        name='Gold tequila')
    Creamofcoconut = Ingredient(
        name='Cream of coconut')
    Pineapple = Ingredient(
        name='Pineapple')
    Ryewhiskey = Ingredient(
        name='Rye whiskey')
    Redwine = Ingredient(
        name='Red wine')
    Apricot = Ingredient(
        name='Apricot')
    Almondflavoring = Ingredient(
        name='Almond flavoring')
    Grainalcohol = Ingredient(
        name='Grain alcohol')
    Foodcoloring = Ingredient(
        name='Food coloring')
    Glycerine = Ingredient(
        name='Glycerine')
    WhiteCremedeMenthe = Ingredient(
        name='White Creme de Menthe')
    Angelicaroot = Ingredient(
        name='Angelica root')
    Almond = Ingredient(
        name='Almond')
    Allspice = Ingredient(
        name='Allspice')
    Cinnamon = Ingredient(
        name='Cinnamon')
    Coriander = Ingredient(
        name='Coriander')
    Marjoramleaves = Ingredient(
        name='Marjoram leaves')
    Maui = Ingredient(
        name='Maui')
    Icedtea = Ingredient(
        name='Iced tea')
    AbsolutCitron = Ingredient(
        name='Absolut Citron')
    Bitterlemon = Ingredient(
        name='Bitter lemon')
    Peachschnapps = Ingredient(
        name='Peach schnapps')
    Coconutliqueur = Ingredient(
        name='Coconut liqueur')
    Guavajuice = Ingredient(
        name='Guava juice')
    Brownsugar = Ingredient(
        name='Brown sugar')
    Cloves = Ingredient(
        name='Cloves')
    Jägermeister = Ingredient(
        name='Jägermeister')
    Goldschlager = Ingredient(
        name='Goldschlager')
    Coconutrum = Ingredient(
        name='Coconut rum')
    Gingerbeer = Ingredient(
        name='Ginger beer')
    Lemon = Ingredient(
        name='Lemon')
    CranberryJuice = Ingredient(
        name='Cranberry Juice')
    Berries = Ingredient(
        name='Berries')
    Apple = Ingredient(
        name='Apple')
    FreshLimeJuice = Ingredient(
        name='Fresh Lime Juice')
    SugarSyrup = Ingredient(
        name='Sugar Syrup')
    Kirschwasser = Ingredient(
        name='Kirschwasser')
    Strawberryliqueur = Ingredient(
        name='Strawberry liqueur')
    Strawberries = Ingredient(
        name='Strawberries')
    SchweppesRusschian = Ingredient(
        name='Schweppes Russchian')
    Añejorum = Ingredient(
        name='Añejo rum')
    DarkCremedeCacao = Ingredient(
        name='Dark Creme de Cacao')
    Hotchocolate = Ingredient(
        name='Hot chocolate')
    Sambuca = Ingredient(
        name='Sambuca')
    OrangeBitters = Ingredient(
        name='Orange Bitters')
    GreenChartreuse = Ingredient(
        name='Green Chartreuse')
    Irishcream = Ingredient(
        name='Irish cream')
    Sugarsyrup = Ingredient(
        name='Sugar syrup')
    CremedeMure = Ingredient(
        name='Creme de Mure')
    RyeWhiskey = Ingredient(
        name='Rye Whiskey')
    MaraschinoLiqueur = Ingredient(
        name='Maraschino Liqueur')
    MaraschinoCherry = Ingredient(
        name='Maraschino Cherry')
    Passionfruitjuice = Ingredient(
        name='Passion fruit juice')
    Maraschinoliqueur = Ingredient(
        name='Maraschino liqueur')
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
    Bananaliqueur = Ingredient(
        name='Banana liqueur')
    Vanillaicecream = Ingredient(
        name='Vanilla ice-cream')
    Powderedsugar = Ingredient(
        name='Powdered sugar')
    DarkRum = Ingredient(
        name='Dark Rum')
    SweetandSour = Ingredient(
        name='Sweet and Sour')
    ErinCream = Ingredient(
        name='Erin Cream')
    Advocaat = Ingredient(
        name='Advocaat')
    Tomatojuice = Ingredient(
        name='Tomato juice')
    Worcestershiresauce = Ingredient(
        name='Worcestershire sauce')
    Tabascosauce = Ingredient(
        name='Tabasco sauce')
    Ale = Ingredient(
        name='Ale')
    Guinnessstout = Ingredient(
        name='Guinness stout')
    Goldrum = Ingredient(
        name='Gold rum')
    TripleSec = Ingredient(
        name='Triple Sec')
    Egg = Ingredient(
        name='Egg')
    VanillaIceCream = Ingredient(
        name='Vanilla Ice-Cream')
    Butterscotchschnapps = Ingredient(
        name='Butterscotch schnapps')
    Lemonlimesoda = Ingredient(
        name='Lemon-lime soda')
    Raisins = Ingredient(
        name='Raisins')
    Blueberries = Ingredient(
        name='Blueberries')
    KoolAid = Ingredient(
        name='Kool-Aid')
    Celerysalt = Ingredient(
        name='Celery salt')
    Godivaliqueur = Ingredient(
        name='Godiva liqueur')
    Tiamaria = Ingredient(
        name='Tia maria')
    CoconutLiqueur = Ingredient(
        name='Coconut Liqueur')
    Chambordraspberryliqueur = Ingredient(
        name='Chambord raspberry liqueur')
    Peachtreeschnapps = Ingredient(
        name='Peachtree schnapps')
    Coffeeliqueur = Ingredient(
        name='Coffee liqueur')
    Passoa = Ingredient(
        name='Passoa')
    MalibuRum = Ingredient(
        name='Malibu Rum')
    Banana = Ingredient(
        name='Banana')
    Rootbeer = Ingredient(
        name='Root beer')
    Carbonatedwater = Ingredient(
        name='Carbonated water')
    RaspberryVodka = Ingredient(
        name='Raspberry Vodka')
    Chocolatesyrup = Ingredient(
        name='Chocolate syrup')
    Cherrybrandy = Ingredient(
        name='Cherry brandy')
    Yoghurt = Ingredient(
        name='Yoghurt')
    Honey = Ingredient(
        name='Honey')
    WhippedCream = Ingredient(
        name='Whipped Cream')
    caramelsauce = Ingredient(
        name='caramel sauce')
    chocolatesauce = Ingredient(
        name='chocolate sauce')
    Minisnickersbars = Ingredient(
        name='Mini-snickers bars')
    Cantaloupe = Ingredient(
        name='Cantaloupe')
    CocaCola = Ingredient(
        name='Coca-Cola')
    Cachaca = Ingredient(
        name='Cachaca')
    Spicedrum = Ingredient(
        name='Spiced rum')
    Falernum = Ingredient(
        name='Falernum')
    blackstraprum = Ingredient(
        name='blackstrap rum')
    Whiterum = Ingredient(
        name='White rum')
    Lager = Ingredient(
        name='Lager')
    Port = Ingredient(
        name='Port')
    Cointreau = Ingredient(
        name='Cointreau')
    Vanilla = Ingredient(
        name='Vanilla')
    Caramelcoloring = Ingredient(
        name='Caramel coloring')
    Eggyolk = Ingredient(
        name='Egg yolk')
    LilletBlanc = Ingredient(
        name='Lillet Blanc')
    Absinthe = Ingredient(
        name='Absinthe')
    Chocolateliqueur = Ingredient(
        name='Chocolate liqueur')
    Vanillaextract = Ingredient(
        name='Vanilla extract')
    Chocolate = Ingredient(
        name='Chocolate')
    Peppermintextract = Ingredient(
        name='Peppermint extract')
    Chocolatemilk = Ingredient(
        name='Chocolate milk')
    Cranberries = Ingredient(
        name='Cranberries')
    LemonPeel = Ingredient(
        name='Lemon Peel')
    Cocoapowder = Ingredient(
        name='Cocoa powder')
    Cornstarch = Ingredient(
        name='Cornstarch')
    CherryGrenadine = Ingredient(
        name='Cherry Grenadine')
    gin = Ingredient(
        name='gin')
    PeachBitters = Ingredient(
        name='Peach Bitters')
    Blackcurrantcordial = Ingredient(
        name='Blackcurrant cordial')
    Fruitpunch = Ingredient(
        name='Fruit punch')
    Olive = Ingredient(
        name='Olive')
    OliveBrine = Ingredient(
        name='Olive Brine')
    demeraraSugar = Ingredient(
        name='demerara Sugar')
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
    Whippingcream = Ingredient(
        name='Whipping cream')
    Vanillasyrup = Ingredient(
        name='Vanilla syrup')
    Espresso = Ingredient(
        name='Espresso')
    Condensedmilk = Ingredient(
        name='Condensed milk')
    Elderflowercordial = Ingredient(
        name='Elderflower cordial')
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
        name='Pomegranate juice')
    lemon = Ingredient(
        name='lemon')
    RaspberryLiqueur = Ingredient(
        name='Raspberry Liqueur')
    pineapplejuice = Ingredient(
        name='pineapple juice')
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
        name='Sirup of roses')
    GrapefruitJuice = Ingredient(
        name='Grapefruit Juice')
    Orangespiral = Ingredient(
        name='Orange spiral')
    Basil = Ingredient(
        name='Basil')
    AgaveSyrup = Ingredient(
        name='Agave Syrup')
    Melonliqueur = Ingredient(
        name='Melon liqueur')
    Grapes = Ingredient(
        name='Grapes')
    Whisky = Ingredient(
        name='Whisky')
    WhiteRum = Ingredient(
        name='White Rum')
    Blackberries = Ingredient(
        name='Blackberries')
    CherryJuice = Ingredient(
        name='Cherry Juice')
    RedChiliFlakes = Ingredient(
        name='Red Chili Flakes')
    Grapejuice = Ingredient(
        name='Grape juice')
    Carbonatedsoftdrink = Ingredient(
        name='Carbonated soft drink')
    Sherbet = Ingredient(
        name='Sherbet')
    Cornsyrup = Ingredient(
        name='Corn syrup')
    Irishwhiskey = Ingredient(
        name='Irish whiskey')
    Butter = Ingredient(
        name='Butter')
    Halfandhalf = Ingredient(
        name='Half-and-half')
    Marshmallows = Ingredient(
        name='Marshmallows')
    Coconutsyrup = Ingredient(
        name='Coconut syrup')
    Peachbrandy = Ingredient(
        name='Peach brandy')
    Anis = Ingredient(
        name='Anis')
    Jello = Ingredient(
        name='Jello')
    Mintsyrup = Ingredient(
        name='Mint syrup')
    Tennesseewhiskey = Ingredient(
        name='Tennessee whiskey')
    Kiwiliqueur = Ingredient(
        name='Kiwi liqueur')
    Kiwi = Ingredient(
        name='Kiwi')
    Cranberryvodka = Ingredient(
        name='Cranberry vodka')
    Apfelkorn = Ingredient(
        name='Apfelkorn')
    Papaya = Ingredient(
        name='Papaya')
    Limepeel = Ingredient(
        name='Lime peel')
    Angosturabitters = Ingredient(
        name='Angostura bitters')
    Asafoetida = Ingredient(
        name='Asafoetida')
    Cayennepepper = Ingredient(
        name='Cayenne pepper')
    Drambuie = Ingredient(
        name='Drambuie')
    Mango = Ingredient(
        name='Mango')
    Cuminseed = Ingredient(
        name='Cumin seed')
    Orgeatsyrup = Ingredient(
        name='Orgeat syrup')
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
        name='Pina colada mix')
    Daiquirimix = Ingredient(
        name='Daiquiri mix')
    Cardamom = Ingredient(
        name='Cardamom')
    Blackpepper = Ingredient(
        name='Black pepper')
    Cucumber = Ingredient(
        name='Cucumber')
    Tropicana = Ingredient(
        name='Tropicana')
    Oreocookie = Ingredient(
        name='Oreo cookie')
    Jagermeister = Ingredient(
        name='Jagermeister')
    RosemarySyrup = Ingredient(
        name='Rosemary Syrup')
    Rosemary = Ingredient(
        name='Rosemary')
    GrapeSoda = Ingredient(
        name='Grape Soda')
    ApricotBrandy = Ingredient(
        name='Apricot Brandy')
    OrangeCuracao = Ingredient(
        name='Orange Curacao')
    BlendedScotch = Ingredient(
        name='Blended Scotch')
    Honeysyrup = Ingredient(
        name='Honey syrup')
    GingerSyrup = Ingredient(
        name='Ginger Syrup')
    IslaysinglemaltScotch = Ingredient(
        name='Islay single malt Scotch')
    EggYolk = Ingredient(
        name='Egg Yolk')
    Coconutmilk = Ingredient(
        name='Coconut milk')
    Cherryliqueur = Ingredient(
        name='Cherry liqueur')
    Pinklemonade = Ingredient(
        name='Pink lemonade')
    Coffeebrandy = Ingredient(
        name='Coffee brandy')
    Limevodka = Ingredient(
        name='Lime vodka')
    BlackSambuca = Ingredient(
        name='Black Sambuca')
    Raspberrysyrup = Ingredient(
        name='Raspberry syrup')
    Raspberryvodka = Ingredient(
        name='Raspberry vodka')
    Peychaudbitters = Ingredient(
        name='Peychaud bitters')
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
    Cherries = Ingredient(
        name='Cherries')
    Fresca = Ingredient(
        name='Fresca')
    Curacao = Ingredient(
        name='Curacao')
    Aquavit = Ingredient(
        name='Aquavit')
    Blackcurrantsquash = Ingredient(
        name='Blackcurrant squash')
    Ouzo = Ingredient(
        name='Ouzo')
    ChocolateSauce = Ingredient(
        name='Chocolate Sauce')
    SaltedChocolate = Ingredient(
        name='Salted Chocolate')
    JohnnieWalker = Ingredient(
        name='Johnnie Walker')
    Fennelseeds = Ingredient(
        name='Fennel seeds')
    Watermelon = Ingredient(
        name='Watermelon')
    CremeDeBanane = Ingredient(
        name='Creme De Banane')
    IrishWhiskey = Ingredient(
        name='Irish Whiskey')
    RossoVermouth = Ingredient(
        name='Rosso Vermouth')
    up = Ingredient(
        name='7-up')
    MelonLiqueur = Ingredient(
        name='Melon Liqueur')
    YukonJack = Ingredient(
        name='Yukon Jack')
    Agavesyrup = Ingredient(
        name='Agave syrup')
    LightRum = Ingredient(
        name='Light Rum')
    Maplesyrup = Ingredient(
        name='Maple syrup')
    Limeade = Ingredient(
        name='Limeade')
    AppleBrandy = Ingredient(
        name='Apple Brandy')
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
    db.session.add(Darkrum)
    db.session.add(Lemonjuice)
    db.session.add(AbsolutVodka)
    db.session.add(Tonicwater)
    db.session.add(Applejack)
    db.session.add(Grapefruitjuice)
    db.session.add(Strawberryschnapps)
    db.session.add(Cranberryjuice)
    db.session.add(Clubsoda)
    db.session.add(Applejuice)
    db.session.add(Maraschinocherry)
    db.session.add(PisangAmbon)
    db.session.add(Lemonade)
    db.session.add(Peachnectar)
    db.session.add(Vermouth)
    db.session.add(Kahlua)
    db.session.add(Eggwhite)
    db.session.add(Lightrum)
    db.session.add(Triplesec)
    db.session.add(Sugar)
    db.session.add(Scotch)
    db.session.add(SweetVermouth)
    db.session.add(DryVermouth)
    db.session.add(Orangebitters)
    db.session.add(lemonjuice)
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
    db.session.add(Applecider)
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
    db.session.add(Gingerbeer)
    db.session.add(Lemon)
    db.session.add(CranberryJuice)
    db.session.add(Berries)
    db.session.add(Apple)
    db.session.add(FreshLimeJuice)
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
    db.session.add(gin)
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
    db.session.add(Maplesyrup)
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
        db.session.execute(text("DELETE FROM ingredients"))

    db.session.commit()
