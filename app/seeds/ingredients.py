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

    gin = Ingredient(
        name='gin')
    grandmarnier = Ingredient(
        name='grand marnier')
    lemonjuice = Ingredient(
        name='lemon juice')
    grenadine = Ingredient(
        name='grenadine')
    amaretto = Ingredient(
        name='amaretto')
    baileysirishcream = Ingredient(
        name='baileys irish cream')
    cognac = Ingredient(
        name='cognac')
    heavycream = Ingredient(
        name='heavy cream')
    milk = Ingredient(
        name='milk')
    eggwhite = Ingredient(
        name='egg white')
    proofrum = Ingredient(
        name='151 proof rum')
    wildturkey = Ingredient(
        name='wild turkey')
    darkrum = Ingredient(
        name='dark rum')
    absolutvodka = Ingredient(
        name='absolut vodka')
    tonicwater = Ingredient(
        name='tonic water')
    applejack = Ingredient(
        name='applejack')
    grapefruitjuice = Ingredient(
        name='grapefruit juice')
    strawberryschnapps = Ingredient(
        name='strawberry schnapps')
    orangejuice = Ingredient(
        name='orange juice')
    cranberryjuice = Ingredient(
        name='cranberry juice')
    clubsoda = Ingredient(
        name='club soda')
    applejuice = Ingredient(
        name='apple juice')
    maraschinocherry = Ingredient(
        name='maraschino cherry')
    vodka = Ingredient(
        name='vodka')
    pisangambon = Ingredient(
        name='pisang ambon')
    lemonade = Ingredient(
        name='lemonade')
    peachnectar = Ingredient(
        name='peach nectar')
    vermouth = Ingredient(
        name='vermouth')
    kahlua = Ingredient(
        name='kahlua')
    lightrum = Ingredient(
        name='light rum')
    triplesec = Ingredient(
        name='triple sec')
    limejuice = Ingredient(
        name='lime juice')
    sugar = Ingredient(
        name='sugar')
    mint = Ingredient(
        name='mint')
    scotch = Ingredient(
        name='scotch')
    sweetvermouth = Ingredient(
        name='sweet vermouth')
    dryvermouth = Ingredient(
        name='dry vermouth')
    orangebitters = Ingredient(
        name='orange bitters')
    maraschinoliqueur = Ingredient(
        name='maraschino liqueur')
    rum = Ingredient(
        name='rum')
    tequila = Ingredient(
        name='tequila')
    fruit = Ingredient(
        name='fruit')
    ice = Ingredient(
        name='ice')
    salt = Ingredient(
        name='salt')
    fruitjuice = Ingredient(
        name='fruit juice')
    sodawater = Ingredient(
        name='soda water')
    cremedebanane = Ingredient(
        name='creme de banane')
    pineapplejuice = Ingredient(
        name='pineapple juice')
    frangelico = Ingredient(
        name='frangelico')
    coffee = Ingredient(
        name='coffee')
    cream = Ingredient(
        name='cream')
    cremedecacao = Ingredient(
        name='creme de cacao')
    lightcream = Ingredient(
        name='light cream')
    nutmeg = Ingredient(
        name='nutmeg')
    blendedwhiskey = Ingredient(
        name='blended whiskey')
    bourbon = Ingredient(
        name='bourbon')
    blackberrybrandy = Ingredient(
        name='blackberry brandy')
    lemonpeel = Ingredient(
        name='lemon peel')
    campari = Ingredient(
        name='campari')
    orangepeel = Ingredient(
        name='orange peel')
    jackdaniels = Ingredient(
        name='jack daniels')
    midorimelonliqueur = Ingredient(
        name='midori melon liqueur')
    sourmix = Ingredient(
        name='sour mix')
    bitters = Ingredient(
        name='bitters')
    crownroyal = Ingredient(
        name='crown royal')
    cremedecassis = Ingredient(
        name='creme de cassis')
    freshlemonjuice = Ingredient(
        name='fresh lemon juice')
    peppermintschnapps = Ingredient(
        name='peppermint schnapps')
    apricotbrandy = Ingredient(
        name='apricot brandy')
    applebrandy = Ingredient(
        name='apple brandy')
    hpnotiq = Ingredient(
        name='hpnotiq')
    bananaliqueur = Ingredient(
        name='banana liqueur')
    wine = Ingredient(
        name='wine')
    benedictine = Ingredient(
        name='benedictine')
    lime = Ingredient(
        name='lime')
    anise = Ingredient(
        name='anise')
    licoriceroot = Ingredient(
        name='licorice root')
    wormwood = Ingredient(
        name='wormwood')
    absolutkurant = Ingredient(
        name='absolut kurant')
    sprite = Ingredient(
        name='sprite')
    grapesoda = Ingredient(
        name='grape soda')
    candy = Ingredient(
        name='candy')
    gingerale = Ingredient(
        name='ginger ale')
    water = Ingredient(
        name='water')
    tea = Ingredient(
        name='tea')
    whippedcream = Ingredient(
        name='whipped cream')
    applecider = Ingredient(
        name='apple cider')
    carrot = Ingredient(
        name='carrot')
    orange = Ingredient(
        name='orange')
    limejuicecordial = Ingredient(
        name='lime juice cordial')
    southerncomfort = Ingredient(
        name='southern comfort')
    passionfruitsyrup = Ingredient(
        name='passion fruit syrup')
    sweetandsour = Ingredient(
        name='sweet and sour')
    angosturabitters = Ingredient(
        name='angostura bitters')
    whitewine = Ingredient(
        name='white wine')
    aperol = Ingredient(
        name='aperol')
    prosecco = Ingredient(
        name='prosecco')
    up = Ingredient(
        name='7-up')
    appleschnapps = Ingredient(
        name='apple schnapps')
    champagne = Ingredient(
        name='champagne')
    greencremedementhe = Ingredient(
        name='green creme de menthe')
    bluecuracao = Ingredient(
        name='blue curacao')
    cherry = Ingredient(
        name='cherry')
    lemonvodka = Ingredient(
        name='lemon vodka')
    chocolateicecream = Ingredient(
        name='chocolate ice-cream')
    brandy = Ingredient(
        name='brandy')
    ginger = Ingredient(
        name='ginger')
    sherry = Ingredient(
        name='sherry')
    sloegin = Ingredient(
        name='sloe gin')
    yellowchartreuse = Ingredient(
        name='yellow chartreuse')
    kummel = Ingredient(
        name='kummel')
    cider = Ingredient(
        name='cider')
    maliburum = Ingredient(
        name='malibu rum')
    goldtequila = Ingredient(
        name='gold tequila')
    creamofcoconut = Ingredient(
        name='cream of coconut')
    pineapple = Ingredient(
        name='pineapple')
    ryewhiskey = Ingredient(
        name='rye whiskey')
    redwine = Ingredient(
        name='red wine')
    apricot = Ingredient(
        name='apricot')
    almondflavoring = Ingredient(
        name='almond flavoring')
    grainalcohol = Ingredient(
        name='grain alcohol')
    foodcoloring = Ingredient(
        name='food coloring')
    glycerine = Ingredient(
        name='glycerine')
    whitecremedementhe = Ingredient(
        name='white creme de menthe')
    angelicaroot = Ingredient(
        name='angelica root')
    almond = Ingredient(
        name='almond')
    allspice = Ingredient(
        name='allspice')
    cinnamon = Ingredient(
        name='cinnamon')
    coriander = Ingredient(
        name='coriander')
    marjoramleaves = Ingredient(
        name='marjoram leaves')
    maui = Ingredient(
        name='maui')
    mountaindew = Ingredient(
        name='mountain dew')
    icedtea = Ingredient(
        name='iced tea')
    gingerbeer = Ingredient(
        name='ginger beer')
    absolutcitron = Ingredient(
        name='absolut citron')
    bitterlemon = Ingredient(
        name='bitter lemon')
    peachschnapps = Ingredient(
        name='peach schnapps')
    coconutliqueur = Ingredient(
        name='coconut liqueur')
    guavajuice = Ingredient(
        name='guava juice')
    brownsugar = Ingredient(
        name='brown sugar')
    cloves = Ingredient(
        name='cloves')
    jägermeister = Ingredient(
        name='jägermeister')
    goldschlager = Ingredient(
        name='goldschlager')
    coconutrum = Ingredient(
        name='coconut rum')
    lemon = Ingredient(
        name='lemon')
    berries = Ingredient(
        name='berries')
    apple = Ingredient(
        name='apple')
    freshlimejuice = Ingredient(
        name='fresh lime juice')
    sugarsyrup = Ingredient(
        name='sugar syrup')
    kirschwasser = Ingredient(
        name='kirschwasser')
    strawberryliqueur = Ingredient(
        name='strawberry liqueur')
    strawberries = Ingredient(
        name='strawberries')
    schweppesrusschian = Ingredient(
        name='schweppes russchian')
    añejorum = Ingredient(
        name='añejo rum')
    darkcremedecacao = Ingredient(
        name='dark creme de cacao')
    hotchocolate = Ingredient(
        name='hot chocolate')
    sambuca = Ingredient(
        name='sambuca')
    greenchartreuse = Ingredient(
        name='green chartreuse')
    irishcream = Ingredient(
        name='irish cream')
    cremedemure = Ingredient(
        name='creme de mure')
    passionfruitjuice = Ingredient(
        name='passion fruit juice')
    galliano = Ingredient(
        name='galliano')
    cherryheering = Ingredient(
        name='cherry heering')
    corona = Ingredient(
        name='corona')
    bacardilimon = Ingredient(
        name='bacardi limon')
    everclear = Ingredient(
        name='everclear')
    surge = Ingredient(
        name='surge')
    vanillaicecream = Ingredient(
        name='vanilla ice-cream')
    powderedsugar = Ingredient(
        name='powdered sugar')
    erincream = Ingredient(
        name='erin cream')
    advocaat = Ingredient(
        name='advocaat')
    tomatojuice = Ingredient(
        name='tomato juice')
    worcestershiresauce = Ingredient(
        name='worcestershire sauce')
    tabascosauce = Ingredient(
        name='tabasco sauce')
    ale = Ingredient(
        name='ale')
    guinnessstout = Ingredient(
        name='guinness stout')
    goldrum = Ingredient(
        name='gold rum')
    egg = Ingredient(
        name='egg')
    butterscotchschnapps = Ingredient(
        name='butterscotch schnapps')
    lemonlimesoda = Ingredient(
        name='lemon-lime soda')
    raisins = Ingredient(
        name='raisins')
    blueberries = Ingredient(
        name='blueberries')
    koolaid = Ingredient(
        name='kool-aid')
    celerysalt = Ingredient(
        name='celery salt')
    godivaliqueur = Ingredient(
        name='godiva liqueur')
    tiamaria = Ingredient(
        name='tia maria')
    chambordraspberryliqueur = Ingredient(
        name='chambord raspberry liqueur')
    peachtreeschnapps = Ingredient(
        name='peachtree schnapps')
    coffeeliqueur = Ingredient(
        name='coffee liqueur')
    passoa = Ingredient(
        name='passoa')
    banana = Ingredient(
        name='banana')
    rootbeer = Ingredient(
        name='root beer')
    carbonatedwater = Ingredient(
        name='carbonated water')
    raspberryvodka = Ingredient(
        name='raspberry vodka')
    chocolatesyrup = Ingredient(
        name='chocolate syrup')
    cherrybrandy = Ingredient(
        name='cherry brandy')
    yoghurt = Ingredient(
        name='yoghurt')
    honey = Ingredient(
        name='honey')
    caramelsauce = Ingredient(
        name='caramel sauce')
    chocolatesauce = Ingredient(
        name='chocolate sauce')
    minisnickersbars = Ingredient(
        name='mini-snickers bars')
    cantaloupe = Ingredient(
        name='cantaloupe')
    cocacola = Ingredient(
        name='coca-cola')
    cachaca = Ingredient(
        name='cachaca')
    spicedrum = Ingredient(
        name='spiced rum')
    falernum = Ingredient(
        name='falernum')
    blackstraprum = Ingredient(
        name='blackstrap rum')
    whiterum = Ingredient(
        name='white rum')
    lager = Ingredient(
        name='lager')
    port = Ingredient(
        name='port')
    cointreau = Ingredient(
        name='cointreau')
    vanilla = Ingredient(
        name='vanilla')
    caramelcoloring = Ingredient(
        name='caramel coloring')
    eggyolk = Ingredient(
        name='egg yolk')
    lilletblanc = Ingredient(
        name='lillet blanc')
    absinthe = Ingredient(
        name='absinthe')
    chocolateliqueur = Ingredient(
        name='chocolate liqueur')
    vanillaextract = Ingredient(
        name='vanilla extract')
    chocolate = Ingredient(
        name='chocolate')
    peppermintextract = Ingredient(
        name='peppermint extract')
    chocolatemilk = Ingredient(
        name='chocolate milk')
    cranberries = Ingredient(
        name='cranberries')
    cocoapowder = Ingredient(
        name='cocoa powder')
    cornstarch = Ingredient(
        name='cornstarch')
    cherrygrenadine = Ingredient(
        name='cherry grenadine')
    peachbitters = Ingredient(
        name='peach bitters')
    blackcurrantcordial = Ingredient(
        name='blackcurrant cordial')
    fruitpunch = Ingredient(
        name='fruit punch')
    olive = Ingredient(
        name='olive')
    olivebrine = Ingredient(
        name='olive brine')
    demerarasugar = Ingredient(
        name='demerara sugar')
    pisco = Ingredient(
        name='pisco')
    pineapplesyrup = Ingredient(
        name='pineapple syrup')
    stgermain = Ingredient(
        name='st. germain')
    pepper = Ingredient(
        name='pepper')
    lavender = Ingredient(
        name='lavender')
    whiskey = Ingredient(
        name='whiskey')
    hotdamn = Ingredient(
        name='hot damn')
    dubonnetrouge = Ingredient(
        name='dubonnet rouge')
    whippingcream = Ingredient(
        name='whipping cream')
    vanillasyrup = Ingredient(
        name='vanilla syrup')
    espresso = Ingredient(
        name='espresso')
    condensedmilk = Ingredient(
        name='condensed milk')
    elderflowercordial = Ingredient(
        name='elderflower cordial')
    mezcal = Ingredient(
        name='mezcal')
    rose = Ingredient(
        name='rose')
    figs = Ingredient(
        name='figs')
    thyme = Ingredient(
        name='thyme')
    apricotnectar = Ingredient(
        name='apricot nectar')
    pomegranatejuice = Ingredient(
        name='pomegranate juice')
    raspberryliqueur = Ingredient(
        name='raspberry liqueur')
    lillet = Ingredient(
        name='lillet')
    firewater = Ingredient(
        name='firewater')
    absolutpeppar = Ingredient(
        name='absolut peppar')
    drpepper = Ingredient(
        name='dr. pepper')
    beer = Ingredient(
        name='beer')
    sarsaparilla = Ingredient(
        name='sarsaparilla')
    peachvodka = Ingredient(
        name='peach vodka')
    sirupofroses = Ingredient(
        name='sirup of roses')
    orangespiral = Ingredient(
        name='orange spiral')
    basil = Ingredient(
        name='basil')
    agavesyrup = Ingredient(
        name='agave syrup')
    melonliqueur = Ingredient(
        name='melon liqueur')
    grapes = Ingredient(
        name='grapes')
    whisky = Ingredient(
        name='whisky')
    blackberries = Ingredient(
        name='blackberries')
    cherryjuice = Ingredient(
        name='cherry juice')
    redchiliflakes = Ingredient(
        name='red chili flakes')
    grapejuice = Ingredient(
        name='grape juice')
    carbonatedsoftdrink = Ingredient(
        name='carbonated soft drink')
    sherbet = Ingredient(
        name='sherbet')
    cornsyrup = Ingredient(
        name='corn syrup')
    irishwhiskey = Ingredient(
        name='irish whiskey')
    butter = Ingredient(
        name='butter')
    halfandhalf = Ingredient(
        name='half-and-half')
    marshmallows = Ingredient(
        name='marshmallows')
    coconutsyrup = Ingredient(
        name='coconut syrup')
    peachbrandy = Ingredient(
        name='peach brandy')
    anis = Ingredient(
        name='anis')
    jello = Ingredient(
        name='jello')
    mintsyrup = Ingredient(
        name='mint syrup')
    tennesseewhiskey = Ingredient(
        name='tennessee whiskey')
    kiwiliqueur = Ingredient(
        name='kiwi liqueur')
    kiwi = Ingredient(
        name='kiwi')
    cranberryvodka = Ingredient(
        name='cranberry vodka')
    apfelkorn = Ingredient(
        name='apfelkorn')
    papaya = Ingredient(
        name='papaya')
    limepeel = Ingredient(
        name='lime peel')
    asafoetida = Ingredient(
        name='asafoetida')
    cayennepepper = Ingredient(
        name='cayenne pepper')
    drambuie = Ingredient(
        name='drambuie')
    mango = Ingredient(
        name='mango')
    cuminseed = Ingredient(
        name='cumin seed')
    orgeatsyrup = Ingredient(
        name='orgeat syrup')
    hotsauce = Ingredient(
        name='hot sauce')
    soysauce = Ingredient(
        name='soy sauce')
    ricard = Ingredient(
        name='ricard')
    pepsicola = Ingredient(
        name='pepsi cola')
    pinacoladamix = Ingredient(
        name='pina colada mix')
    daiquirimix = Ingredient(
        name='daiquiri mix')
    cardamom = Ingredient(
        name='cardamom')
    blackpepper = Ingredient(
        name='black pepper')
    cucumber = Ingredient(
        name='cucumber')
    tropicana = Ingredient(
        name='tropicana')
    oreocookie = Ingredient(
        name='oreo cookie')
    jagermeister = Ingredient(
        name='jagermeister')
    rosemarysyrup = Ingredient(
        name='rosemary syrup')
    rosemary = Ingredient(
        name='rosemary')
    orangecuracao = Ingredient(
        name='orange curacao')
    blendedscotch = Ingredient(
        name='blended scotch')
    honeysyrup = Ingredient(
        name='honey syrup')
    gingersyrup = Ingredient(
        name='ginger syrup')
    islaysinglemaltscotch = Ingredient(
        name='islay single malt scotch')
    coconutmilk = Ingredient(
        name='coconut milk')
    cherryliqueur = Ingredient(
        name='cherry liqueur')
    pinklemonade = Ingredient(
        name='pink lemonade')
    coffeebrandy = Ingredient(
        name='coffee brandy')
    limevodka = Ingredient(
        name='lime vodka')
    blacksambuca = Ingredient(
        name='black sambuca')
    raspberrysyrup = Ingredient(
        name='raspberry syrup')
    peychaudbitters = Ingredient(
        name='peychaud bitters')
    amaromontenegro = Ingredient(
        name='amaro montenegro')
    rubyport = Ingredient(
        name='ruby port')
    bloodorange = Ingredient(
        name='blood orange')
    jimbeam = Ingredient(
        name='jim beam')
    anisette = Ingredient(
        name='anisette')
    cherries = Ingredient(
        name='cherries')
    fresca = Ingredient(
        name='fresca')
    curacao = Ingredient(
        name='curacao')
    aquavit = Ingredient(
        name='aquavit')
    blackcurrantsquash = Ingredient(
        name='blackcurrant squash')
    ouzo = Ingredient(
        name='ouzo')
    saltedchocolate = Ingredient(
        name='salted chocolate')
    johnniewalker = Ingredient(
        name='johnnie walker')
    fennelseeds = Ingredient(
        name='fennel seeds')
    watermelon = Ingredient(
        name='watermelon')
    rossovermouth = Ingredient(
        name='rosso vermouth')
    yukonjack = Ingredient(
        name='yukon jack')
    maplesyrup = Ingredient(
        name='maple syrup')
    limeade = Ingredient(
        name='limeade')
    pernod = Ingredient(
        name='pernod')
    zima = Ingredient(
        name='zima')

    db.session.add(gin)
    db.session.add(grandmarnier)
    db.session.add(lemonjuice)
    db.session.add(grenadine)
    db.session.add(amaretto)
    db.session.add(baileysirishcream)
    db.session.add(cognac)
    db.session.add(heavycream)
    db.session.add(milk)
    db.session.add(eggwhite)
    db.session.add(proofrum)
    db.session.add(wildturkey)
    db.session.add(darkrum)
    db.session.add(absolutvodka)
    db.session.add(tonicwater)
    db.session.add(applejack)
    db.session.add(grapefruitjuice)
    db.session.add(strawberryschnapps)
    db.session.add(orangejuice)
    db.session.add(cranberryjuice)
    db.session.add(clubsoda)
    db.session.add(applejuice)
    db.session.add(maraschinocherry)
    db.session.add(vodka)
    db.session.add(pisangambon)
    db.session.add(lemonade)
    db.session.add(peachnectar)
    db.session.add(vermouth)
    db.session.add(kahlua)
    db.session.add(lightrum)
    db.session.add(triplesec)
    db.session.add(limejuice)
    db.session.add(sugar)
    db.session.add(mint)
    db.session.add(scotch)
    db.session.add(sweetvermouth)
    db.session.add(dryvermouth)
    db.session.add(orangebitters)
    db.session.add(maraschinoliqueur)
    db.session.add(rum)
    db.session.add(tequila)
    db.session.add(fruit)
    db.session.add(ice)
    db.session.add(salt)
    db.session.add(fruitjuice)
    db.session.add(sodawater)
    db.session.add(cremedebanane)
    db.session.add(pineapplejuice)
    db.session.add(frangelico)
    db.session.add(coffee)
    db.session.add(cream)
    db.session.add(cremedecacao)
    db.session.add(lightcream)
    db.session.add(nutmeg)
    db.session.add(blendedwhiskey)
    db.session.add(bourbon)
    db.session.add(blackberrybrandy)
    db.session.add(lemonpeel)
    db.session.add(campari)
    db.session.add(orangepeel)
    db.session.add(jackdaniels)
    db.session.add(midorimelonliqueur)
    db.session.add(sourmix)
    db.session.add(bitters)
    db.session.add(crownroyal)
    db.session.add(cremedecassis)
    db.session.add(freshlemonjuice)
    db.session.add(peppermintschnapps)
    db.session.add(apricotbrandy)
    db.session.add(applebrandy)
    db.session.add(hpnotiq)
    db.session.add(bananaliqueur)
    db.session.add(wine)
    db.session.add(benedictine)
    db.session.add(lime)
    db.session.add(anise)
    db.session.add(licoriceroot)
    db.session.add(wormwood)
    db.session.add(absolutkurant)
    db.session.add(sprite)
    db.session.add(grapesoda)
    db.session.add(candy)
    db.session.add(gingerale)
    db.session.add(water)
    db.session.add(tea)
    db.session.add(whippedcream)
    db.session.add(applecider)
    db.session.add(carrot)
    db.session.add(orange)
    db.session.add(limejuicecordial)
    db.session.add(southerncomfort)
    db.session.add(passionfruitsyrup)
    db.session.add(sweetandsour)
    db.session.add(angosturabitters)
    db.session.add(whitewine)
    db.session.add(aperol)
    db.session.add(prosecco)
    db.session.add(up)
    db.session.add(appleschnapps)
    db.session.add(champagne)
    db.session.add(greencremedementhe)
    db.session.add(bluecuracao)
    db.session.add(cherry)
    db.session.add(lemonvodka)
    db.session.add(chocolateicecream)
    db.session.add(brandy)
    db.session.add(ginger)
    db.session.add(sherry)
    db.session.add(sloegin)
    db.session.add(yellowchartreuse)
    db.session.add(kummel)
    db.session.add(cider)
    db.session.add(maliburum)
    db.session.add(goldtequila)
    db.session.add(creamofcoconut)
    db.session.add(pineapple)
    db.session.add(ryewhiskey)
    db.session.add(redwine)
    db.session.add(apricot)
    db.session.add(almondflavoring)
    db.session.add(grainalcohol)
    db.session.add(foodcoloring)
    db.session.add(glycerine)
    db.session.add(whitecremedementhe)
    db.session.add(angelicaroot)
    db.session.add(almond)
    db.session.add(allspice)
    db.session.add(cinnamon)
    db.session.add(coriander)
    db.session.add(marjoramleaves)
    db.session.add(maui)
    db.session.add(mountaindew)
    db.session.add(icedtea)
    db.session.add(gingerbeer)
    db.session.add(absolutcitron)
    db.session.add(bitterlemon)
    db.session.add(peachschnapps)
    db.session.add(coconutliqueur)
    db.session.add(guavajuice)
    db.session.add(brownsugar)
    db.session.add(cloves)
    db.session.add(jägermeister)
    db.session.add(goldschlager)
    db.session.add(coconutrum)
    db.session.add(lemon)
    db.session.add(berries)
    db.session.add(apple)
    db.session.add(freshlimejuice)
    db.session.add(sugarsyrup)
    db.session.add(kirschwasser)
    db.session.add(strawberryliqueur)
    db.session.add(strawberries)
    db.session.add(schweppesrusschian)
    db.session.add(añejorum)
    db.session.add(darkcremedecacao)
    db.session.add(hotchocolate)
    db.session.add(sambuca)
    db.session.add(greenchartreuse)
    db.session.add(irishcream)
    db.session.add(cremedemure)
    db.session.add(passionfruitjuice)
    db.session.add(galliano)
    db.session.add(cherryheering)
    db.session.add(corona)
    db.session.add(bacardilimon)
    db.session.add(everclear)
    db.session.add(surge)
    db.session.add(vanillaicecream)
    db.session.add(powderedsugar)
    db.session.add(erincream)
    db.session.add(advocaat)
    db.session.add(tomatojuice)
    db.session.add(worcestershiresauce)
    db.session.add(tabascosauce)
    db.session.add(ale)
    db.session.add(guinnessstout)
    db.session.add(goldrum)
    db.session.add(egg)
    db.session.add(butterscotchschnapps)
    db.session.add(lemonlimesoda)
    db.session.add(raisins)
    db.session.add(blueberries)
    db.session.add(koolaid)
    db.session.add(celerysalt)
    db.session.add(godivaliqueur)
    db.session.add(tiamaria)
    db.session.add(chambordraspberryliqueur)
    db.session.add(peachtreeschnapps)
    db.session.add(coffeeliqueur)
    db.session.add(passoa)
    db.session.add(banana)
    db.session.add(rootbeer)
    db.session.add(carbonatedwater)
    db.session.add(raspberryvodka)
    db.session.add(chocolatesyrup)
    db.session.add(cherrybrandy)
    db.session.add(yoghurt)
    db.session.add(honey)
    db.session.add(caramelsauce)
    db.session.add(chocolatesauce)
    db.session.add(minisnickersbars)
    db.session.add(cantaloupe)
    db.session.add(cocacola)
    db.session.add(cachaca)
    db.session.add(spicedrum)
    db.session.add(falernum)
    db.session.add(blackstraprum)
    db.session.add(whiterum)
    db.session.add(lager)
    db.session.add(port)
    db.session.add(cointreau)
    db.session.add(vanilla)
    db.session.add(caramelcoloring)
    db.session.add(eggyolk)
    db.session.add(lilletblanc)
    db.session.add(absinthe)
    db.session.add(chocolateliqueur)
    db.session.add(vanillaextract)
    db.session.add(chocolate)
    db.session.add(peppermintextract)
    db.session.add(chocolatemilk)
    db.session.add(cranberries)
    db.session.add(cocoapowder)
    db.session.add(cornstarch)
    db.session.add(cherrygrenadine)
    db.session.add(peachbitters)
    db.session.add(blackcurrantcordial)
    db.session.add(fruitpunch)
    db.session.add(olive)
    db.session.add(olivebrine)
    db.session.add(demerarasugar)
    db.session.add(pisco)
    db.session.add(pineapplesyrup)
    db.session.add(stgermain)
    db.session.add(pepper)
    db.session.add(lavender)
    db.session.add(whiskey)
    db.session.add(hotdamn)
    db.session.add(dubonnetrouge)
    db.session.add(whippingcream)
    db.session.add(vanillasyrup)
    db.session.add(espresso)
    db.session.add(condensedmilk)
    db.session.add(elderflowercordial)
    db.session.add(mezcal)
    db.session.add(rose)
    db.session.add(figs)
    db.session.add(thyme)
    db.session.add(apricotnectar)
    db.session.add(pomegranatejuice)
    db.session.add(raspberryliqueur)
    db.session.add(lillet)
    db.session.add(firewater)
    db.session.add(absolutpeppar)
    db.session.add(drpepper)
    db.session.add(beer)
    db.session.add(sarsaparilla)
    db.session.add(peachvodka)
    db.session.add(sirupofroses)
    db.session.add(orangespiral)
    db.session.add(basil)
    db.session.add(agavesyrup)
    db.session.add(melonliqueur)
    db.session.add(grapes)
    db.session.add(whisky)
    db.session.add(blackberries)
    db.session.add(cherryjuice)
    db.session.add(redchiliflakes)
    db.session.add(grapejuice)
    db.session.add(carbonatedsoftdrink)
    db.session.add(sherbet)
    db.session.add(cornsyrup)
    db.session.add(irishwhiskey)
    db.session.add(butter)
    db.session.add(halfandhalf)
    db.session.add(marshmallows)
    db.session.add(coconutsyrup)
    db.session.add(peachbrandy)
    db.session.add(anis)
    db.session.add(jello)
    db.session.add(mintsyrup)
    db.session.add(tennesseewhiskey)
    db.session.add(kiwiliqueur)
    db.session.add(kiwi)
    db.session.add(cranberryvodka)
    db.session.add(apfelkorn)
    db.session.add(papaya)
    db.session.add(limepeel)
    db.session.add(asafoetida)
    db.session.add(cayennepepper)
    db.session.add(drambuie)
    db.session.add(mango)
    db.session.add(cuminseed)
    db.session.add(orgeatsyrup)
    db.session.add(hotsauce)
    db.session.add(soysauce)
    db.session.add(ricard)
    db.session.add(pepsicola)
    db.session.add(pinacoladamix)
    db.session.add(daiquirimix)
    db.session.add(cardamom)
    db.session.add(blackpepper)
    db.session.add(cucumber)
    db.session.add(tropicana)
    db.session.add(oreocookie)
    db.session.add(jagermeister)
    db.session.add(rosemarysyrup)
    db.session.add(rosemary)
    db.session.add(orangecuracao)
    db.session.add(blendedscotch)
    db.session.add(honeysyrup)
    db.session.add(gingersyrup)
    db.session.add(islaysinglemaltscotch)
    db.session.add(coconutmilk)
    db.session.add(cherryliqueur)
    db.session.add(pinklemonade)
    db.session.add(coffeebrandy)
    db.session.add(limevodka)
    db.session.add(blacksambuca)
    db.session.add(raspberrysyrup)
    db.session.add(peychaudbitters)
    db.session.add(amaromontenegro)
    db.session.add(rubyport)
    db.session.add(bloodorange)
    db.session.add(jimbeam)
    db.session.add(anisette)
    db.session.add(cherries)
    db.session.add(fresca)
    db.session.add(curacao)
    db.session.add(aquavit)
    db.session.add(blackcurrantsquash)
    db.session.add(ouzo)
    db.session.add(saltedchocolate)
    db.session.add(johnniewalker)
    db.session.add(fennelseeds)
    db.session.add(watermelon)
    db.session.add(rossovermouth)
    db.session.add(yukonjack)
    db.session.add(maplesyrup)
    db.session.add(limeade)
    db.session.add(pernod)
    db.session.add(zima)

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
