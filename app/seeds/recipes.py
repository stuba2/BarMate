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

    Aone = Recipe(
      name='A1',
      description=None,
      instructions='Pour all ingredients into a cocktail shaker, mix and serve over ice into a chilled glass.',
      user_id=4
    )
    Abc = Recipe(
      name='ABC',
      description=None,
      instructions='Layered in a shot glass.',
      user_id=2
    )
    Ace = Recipe(
      name='Ace',
      description=None,
      instructions='Shake all the ingredients in a cocktail shaker and ice then strain in a cold glass.',
      user_id=3
    )
    Acid = Recipe(
      name='ACID',
      description=None,
      instructions='Poor in the 151 first followed by the 101 served with a Coke or Dr Pepper chaser.',
      user_id=1
    )
    Adam = Recipe(
      name='Adam',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine all of the ingredients. Shake well. Strain into a cocktail glass.',
      user_id=3
    )
    Att = Recipe(
      name='AT&T',
      description=None,
      instructions='Pour Vodka and Gin over ice, add Tonic and Stir',
      user_id=4
    )
    Aj = Recipe(
      name='A. J.',
      description=None,
      instructions='Shake ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=1
    )
    Affair = Recipe(
      name='Affair',
      description=None,
      instructions='Pour schnapps, orange juice, and cranberry juice over ice in a highball glass. Top with club soda and serve.',
      user_id=2
    )
    Apello = Recipe(
      name='Apello',
      description=None,
      instructions='Stirr. Grnish with maraschino cherry.',
      user_id=4
    )
    Avalon = Recipe(
      name='Avalon',
      description=None,
      instructions='Fill a tall glass with ice. Layer the Finlandia Vodka, lemon and apple juices, Pisang Ambon, and top up with lemonade. Stir slightly and garnish with a spiralled cucumber skin and a red cherry. The cucumber provides zest and looks attractive. This drink, created by Timo Haimi, took first prize in the 1991 Finlandia Vodka Long Drink Competition.',
      user_id=3
    )
    Abilene = Recipe(
      name='Abilene',
      description=None,
      instructions='Pour all of the ingredients into a highball glass almost filled with ice cubes. Stir well.',
      user_id=4
    )
    Addison = Recipe(
      name='Addison',
      description=None,
      instructions='Shake together all the ingredients and strain into a cold glass.',
      user_id=2
    )
    Almeria = Recipe(
      name='Almeria',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine all of the ingredients. Shake well. Strain into a cocktail glass.',
      user_id=3
    )
    Acapulco = Recipe(
      name='Acapulco',
      description=None,
      instructions='Combine and shake all ingredients (except mint) with ice and strain into an old-fashioned glass over ice cubes. Add the sprig of mint and serve.',
      user_id=2
    )
    Affinity = Recipe(
      name='Affinity',
      description=None,
      instructions='In a mixing glass half-filled with ice cubes, combine all of the ingredients. Stir well. Strain into a cocktail glass.',
      user_id=4
    )
    Applecar = Recipe(
      name='Applecar',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=4
    )
    Aviation = Recipe(
      name='Aviation',
      description=None,
      instructions='Add all ingredients into cocktail shaker filled with ice. Shake well and strain into cocktail glass. Garnish with a cherry.',
      user_id=4
    )
    AdamBomb = Recipe(
      name='Adam Bomb',
      description=None,
      instructions='Add ice to blender (or to glass if prefer on the rocks) then fruit, and fruite juice depending on personal prefference then add the Rum, Vodka, Tequila, and triple sec. blend till smooth, rim glass with sugar or salt and pour mixture in. garnish with lemon or lime slice.',
      user_id=3
    )
    Addington = Recipe(
      name='Addington',
      description=None,
      instructions='Mix both the vermouth\'s in a shaker and strain into a cold glass. Top up with a squirt of Soda Water. ',
      user_id=4
    )
    Aftersex = Recipe(
      name='After sex',
      description=None,
      instructions='Pour the vodka and creme over some ice cubes in a tall glass and fill up with juice. to make it beuty full make the top of the glass with a grenadine and sugar',
      user_id=2
    )
    Afterglow = Recipe(
      name='Afterglow',
      description=None,
      instructions='Mix. Serve over ice.',
      user_id=4
    )
    Afternoon = Recipe(
      name='Afternoon',
      description=None,
      instructions='Build into a suiting glass, with no ice. Cream on top if wanted. Served directly.',
      user_id=2
    )
    Alexander = Recipe(
      name='Alexander',
      description=None,
      instructions='Shake all ingredients with ice and strain contents into a cocktail glass. Sprinkle nutmeg on top and serve.',
      user_id=3
    )
    Algonquin = Recipe(
      name='Algonquin',
      description=None,
      instructions='Combine and shake all ingredients with ice, strain contents into a cocktail glass, and serve.',
      user_id=4
    )
    Allegheny = Recipe(
      name='Allegheny',
      description=None,
      instructions='Shake all ingredients (except lemon peel) with ice and strain into a cocktail glass. Top with the twist of lemon peel and serve.',
      user_id=2
    )
    Americano = Recipe(
      name='Americano',
      description=None,
      instructions='Pour the Campari and vermouth over ice into glass, add a splash of soda water and garnish with half orange slice.',
      user_id=3
    )
    Applejack = Recipe(
      name='Applejack',
      description=None,
      instructions='Add all ingredients into mixing glass, chill and strain into cocktail glass',
      user_id=3
    )
    Artillery = Recipe(
      name='Artillery',
      description=None,
      instructions='Stir all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=3
    )
    Autodaf = Recipe(
      name='Autodafé',
      description=None,
      instructions='Mix and fill up with soda water. Drunk by finns on a sunny day any time of the year and day.',
      user_id=3
    )
    Avalanche = Recipe(
      name='Avalanche',
      description=None,
      instructions='Mix in highball glass over ice, shake well.',
      user_id=4
    )
    AdamEve = Recipe(
      name='Adam & Eve',
      description=None,
      instructions='Shake together all the ingredients and strain into a cold glass.',
      user_id=2
    )
    AlmondJoy = Recipe(
      name='Almond Joy',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=3
    )
    AngelFace = Recipe(
      name='Angel Face',
      description=None,
      instructions='Shake all ingredients with ice and strain contents into a cocktail glass.',
      user_id=3
    )
    Aquamarine = Recipe(
      name='Aquamarine',
      description=None,
      instructions='Shake well in a shaker with ice. Strain in a martini glass.',
      user_id=1
    )
    Archbishop = Recipe(
      name='Archbishop',
      description=None,
      instructions='In an old-fashioned glass almost filled with ice cubes, combine all of the ingredients. Stir well.',
      user_id=4
    )
    Absinthe2 = Recipe(
      name='Absinthe #2',
      description=None,
      instructions='Mix together and let sit a few days. Strain through a coffee filter. To serve mix 1 part absinthe to 4 parts water, add ice, enjoy.',
      user_id=4
    )
    AbsolutSex = Recipe(
      name='Absolut Sex',
      description=None,
      instructions='Shake Absolut Kurant, Midori, and Cranberry juice in shaker with ice: Strain into rocks glass: Splash of seven on top.Absolut Sex.',
      user_id=3
    )
    ArcticFish = Recipe(
      name='Arctic Fish',
      description=None,
      instructions='Fill glass with ice and fish, add vodka, grape soda and orange juice. DO NOT STIR!!!!! Serve well chilled.',
      user_id=1
    )
    AztecPunch = Recipe(
      name='Aztec Punch',
      description=None,
      instructions='Mix all ingredients in a pitcher. Mix thoroughly and pour into whatever is available, the bigger the better! This drink packs a big punch, so don\'t over do it.',
      user_id=3
    )
    AdamSunrise = Recipe(
      name='Adam Sunrise',
      description=None,
      instructions='Fill blender up with ice. Fill half with Bartons Vodka. Put 10 tsp of sugar, add 1/2 can lemonade concentrate, fill to top with water. Blend for 60 seconds.',
      user_id=4
    )
    AmarettoTea = Recipe(
      name='Amaretto Tea',
      description=None,
      instructions='Pour hot tea into a pousse-cafe glass, using a spoon in glass to prevent cracking. Add amaretto, but do not stir. Top with chilled whipped cream and serve.',
      user_id=1
    )
    AppleGrande = Recipe(
      name='Apple Grande',
      description=None,
      instructions='Chill both ingredients!! Mix in a tumbler and enjoy!',
      user_id=2
    )
    AppleKarate = Recipe(
      name='Apple Karate',
      description=None,
      instructions='Place all ingredients in the blender jar - cover and whiz on medium speed until well blended. Pour in one tall, 2 medium or 3 small glasses and drink up.',
      user_id=3
    )
    ApricotLady = Recipe(
      name='Apricot Lady',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the rum, apricot brandy, triple sec, lemon juice, and egg white. Shake well. Strain into an old-fashioned glass almost filled with ice cubes. Garnish with the orange slice.',
      user_id=1
    )
    Armyspecial = Recipe(
      name='Army special',
      description=None,
      instructions='Pour Vodka, Gin and lime cordial into glass, and top up with crushed ice. Wait for ice to melt slightly and sip without a straw.',
      user_id=4
    )
    AtlanticSun = Recipe(
      name='Atlantic Sun',
      description=None,
      instructions='Shake all the ingredients, top the drink with soda. Garnish with a slice of orange.',
      user_id=1
    )
    AbbeyMartini = Recipe(
      name='Abbey Martini',
      description=None,
      instructions='Put all ingredients into a shaker and mix, then strain contents into a chilled cocktail glass.',
      user_id=2
    )
    Amarettofizz = Recipe(
      name='Amaretto fizz',
      description=None,
      instructions='Mix Amaretto, orange juice and sparkling wine in a jug. Add a strip orange zest to each glass, if you like.',
      user_id=2
    )
    AmarettoMist = Recipe(
      name='Amaretto Mist',
      description=None,
      instructions='Pour amaretto in an old-fashioned glass over crushed ice. Add the wedge of lime and serve. (A wedge of lemon may be substituted for lime, if preferred.)',
      user_id=4
    )
    AmarettoRose = Recipe(
      name='Amaretto Rose',
      description=None,
      instructions='Pour amaretto and lime juice over ice in a collins glass. Fill with club soda and serve.',
      user_id=4
    )
    AmarettoSour = Recipe(
      name='Amaretto Sour',
      description=None,
      instructions='Shake and strain. Garnish with a cherry and an orange slice.',
      user_id=4
    )
    AperolSpritz = Recipe(
      name='Aperol Spritz',
      description=None,
      instructions='Put a couple of cubes of ice into 2 glasses and add a 50 ml measure of Aperol to each. Divide the prosecco between the glasses and then top up with soda, if you like.',
      user_id=2
    )
    AppleSlammer = Recipe(
      name='Apple Slammer',
      description=None,
      instructions='pour into a shot glass and present to consumer, they are expected to cover the top of the shotglass with thier palm, raise the glass, slam it on the bar and the swallow quickly.',
      user_id=4
    )
    Apricotpunch = Recipe(
      name='Apricot punch',
      description=None,
      instructions='Pour all ingredients into a large punch bowl. Add ice and 4 oranges that are peeled and divided.',
      user_id=1
    )
    AriseMyLove = Recipe(
      name='Arise My Love',
      description=None,
      instructions='Put creme de menthe into a champagne flute. Fill with chilled champagne and serve.',
      user_id=3
    )
    AtomicLokade = Recipe(
      name='Atomic Lokade',
      description=None,
      instructions='In a shaker, place lemonade, vodka, blue Curacao, and triple sec together. Shake with ice and strain into glass. Add sugar to taste',
      user_id=1
    )
    APieceofAss = Recipe(
      name='A Piece of Ass',
      description=None,
      instructions='Put ice in glass. Pour in shots. Fill with Sour Mix.',
      user_id=2
    )
    AbbeyCocktail = Recipe(
      name='Abbey Cocktail',
      description=None,
      instructions='Shake all ingredients (except for the cherry) with ice and strain into a cocktail glass. Top with the cherry and serve.',
      user_id=4
    )
    AlfieCocktail = Recipe(
      name='Alfie Cocktail',
      description=None,
      instructions='Combine and shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=2
    )
    AliceCocktail = Recipe(
      name='Alice Cocktail',
      description=None,
      instructions='Shake well, strain into a large cocktail glass.',
      user_id=2
    )
    AmarettoShake = Recipe(
      name='Amaretto Shake',
      description=None,
      instructions='Combine all ingredients in a blender and blend at high speed until smooth. Serve in chilled glass garnished with bittersweet chocolate shavings.',
      user_id=3
    )
    AppleHighball = Recipe(
      name='Apple Highball',
      description=None,
      instructions='Add ice in a highball glass. Rub a wedge of fresh lime around rim and place it in the glass. Add a shot of Apple schnapps, a shot of Courvoisier and top up with ginger ale.',
      user_id=2
    )
    AddisonSpecial = Recipe(
      name='Addison Special',
      description=None,
      instructions='Combine ingredients in the order listed into a shaker. Fill half full with ice and shake well. Strain into glass with ice and garnish with a cherry and orange wedge.',
      user_id=2
    )
    AdonisCocktail = Recipe(
      name='Adonis Cocktail',
      description=None,
      instructions='Stir all ingredients with ice, strain contents into a cocktail glass, and serve.',
      user_id=4
    )
    AlabamaSlammer = Recipe(
      name='Alabama Slammer',
      description=None,
      instructions='Pour all ingredients (except for lemon juice) over ice in a highball glass. Stir, add a dash of lemon juice, and serve.',
      user_id=2
    )
    AlaskaCocktail = Recipe(
      name='Alaska Cocktail',
      description=None,
      instructions='Stir all ingredients with ice, strain contents into a cocktail glass. Drop in a twist of lemon and serve.',
      user_id=4
    )
    AlliesCocktail = Recipe(
      name='Allies Cocktail',
      description=None,
      instructions='Stir all ingredients with ice, strain contents into a cocktail glass, and serve.',
      user_id=2
    )
    AmarettoSunset = Recipe(
      name='Amaretto Sunset',
      description=None,
      instructions='Shake ingredients in bartender\'s mixer quickly, just 5 shakes. Strain out ice, serve in glass immediately with a slice of orange.',
      user_id=3
    )
    ArizonaTwister = Recipe(
      name='Arizona Twister',
      description=None,
      instructions='Just mix in the shots of rum, vodka, and tequila. Add splashes of the three juices, heavy on the pineapple. Top off with grenadine. Crushed ice should already be in glass. Top off the glass with a pineapple wedge.',
      user_id=1
    )
    ArthurTompkins = Recipe(
      name='Arthur Tompkins',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the gin, Grand Marnier, and lemon juice. Shake well. Strain into a sour glass and garnish with the lemon twist.',
      user_id=1
    )
    ArtilleryPunch = Recipe(
      name='Artillery Punch',
      description=None,
      instructions='Combine all the ingredients in a large punch bowl with a block of ice. If found too dry, sugar syrup may be added. Decorate with twists of lemon peel.',
      user_id=4
    )
    ASplashofNash = Recipe(
      name='A Splash of Nash',
      description=None,
      instructions='Drop shot glass with banana & melon liquers into a 9 oz hi- ball glass containing soda water and cranberry juice. Drink in one shot.',
      user_id=2
    )
    AmarettoLiqueur = Recipe(
      name='Amaretto Liqueur',
      description=None,
      instructions='Combine sugar and 3/4 cup water in a small saucepan. Bring to a boil, stirring constantly. Reduce heat and simmer until all sugar is dissolved. Remove from heat and cool. In an aging container, combine apricot halves, almond extract, grain alcohol with 1/2 cup water, and brandy. Stir in cooled sugar syrup mixture. Cap and let age for 2 days. Remove apricot halves. (Save apricot halves, can be used for cooking). Add food coloring and glycerine. Stir, recap and continue aging for 1 to 2 months. Re-bottle as desired. Liqueur is ready to serve but will continue to improve with additional aging.',
      user_id=4
    )
    AmarettoStinger = Recipe(
      name='Amaretto Stinger',
      description=None,
      instructions='Shake ingredients well with cracked ice, strain into a cocktail glass, and serve.',
      user_id=3
    )
    AmarettoSunrise = Recipe(
      name='Amaretto Sunrise',
      description=None,
      instructions='Mix together the amaretto and orange juice. Pour into glass and then add the grenadine untill you see the sunrise.',
      user_id=1
    )
    AngelicaLiqueur = Recipe(
      name='Angelica Liqueur',
      description=None,
      instructions='Combine all herbs, nuts and spices with vodka in a 1 quart or larger aging container. Cap tightly and shake daily for 2 weeks. Strain through a fine muslin cloth or coffee filter, discarding solids. Clean out aging container. Place liquid back in container. Place sugar and water in saucepan and stir to combine over medium heat. When sugar is completely dissolved, set aside and let cool. When cool combine with food coloring and add to liqueur liquid. Cap and allow to age and mellow in a cool, dark place for one month.',
      user_id=1
    )
    ArcticMouthwash = Recipe(
      name='Arctic Mouthwash',
      description=None,
      instructions='Blend all ingredients in a blender on high until ice is finely crushed. It should be of a slushy consistency. Pour immediately and serve.',
      user_id=3
    )
    ArizonaStingers = Recipe(
      name='Arizona Stingers',
      description=None,
      instructions='Place ice cubes in the hurricane glass . Add the 2 HEAPING shots of Absolute Vodka (Note: You can add as many shots of Absolute as you want!) Fill the rest of glass with the Arizona Icetea with lemon. Stir to mix using a spoon. Drink up and enjoy!!!!!!!',
      user_id=4
    )
    AutumnGaribaldi = Recipe(
      name='Autumn Garibaldi',
      description=None,
      instructions='Pour all ingredients into a glass over ice and stir with a bar spoon. Garnish with some orange slices.',
      user_id=2
    )
    AbsolutEvergreen = Recipe(
      name='Absolut Evergreen',
      description=None,
      instructions='Mix, pour over ice and top up with Bitter Lemon.',
      user_id=3
    )
    Absolutlimousine = Recipe(
      name='Absolut limousine',
      description=None,
      instructions='Fill Absolut into a glass. Add Lime juice. Add Ice and lime wedges.',
      user_id=3
    )
    AbsolutStress2 = Recipe(
      name='Absolut Stress #2',
      description=None,
      instructions='Mix well. Garnish with Orange and Cherry. Enjoy',
      user_id=4
    )
    AlohaFruitpunch = Recipe(
      name='Aloha Fruit punch',
      description=None,
      instructions='Add 1/4 cup water to ginger root. Boil 3 minutes. Strain. Add the liquid to the guava, lemon and pineapple juices. Make a syrup of sugar and remaining water. Cool. Combine with juices and pineapple. Chill throroughly.',
      user_id=4
    )
    AppleCiderPunch = Recipe(
      name='Apple Cider Punch',
      description=None,
      instructions='If you use the whole all spice and cloves, tie them in cheesecloth. Heat the mixture. Stir occasionally. If you want an alcoholic drink, rum would be nice.',
      user_id=2
    )
    AuburnHeadbanger = Recipe(
      name='Auburn Headbanger',
      description=None,
      instructions='Mix in spread glass over ice. Strain and pour in shot glass. Sit down before shotting. ENJOY!!',
      user_id=2
    )
    ADayattheBeach = Recipe(
      name='A Day at the Beach',
      description=None,
      instructions='Shake Rum, Amaretto, and Orange Juice in a shaker filled with ice. Strain over ice into a highball glass. Add Grenadine and garnish with a Pineapple Wedge and a Strawberry.',
      user_id=1
    )
    AFurlongTooLate = Recipe(
      name='A Furlong Too Late',
      description=None,
      instructions='Pour the rum and ginger beer into a highball glass almost filled with ice cubes. Stir well. Garnish with the lemon twist.',
      user_id=4
    )
    AbsolutSummertime = Recipe(
      name='Absolut Summertime',
      description=None,
      instructions='Add all ingredients except lemon to shaker filled with ice. Cover and shake vigorously. Strain contents into ice filled collins glass. Garnish with lemon.',
      user_id=2
    )
    AmarettoAndCream = Recipe(
      name='Amaretto And Cream',
      description=None,
      instructions='Shake well with cracked ice, strain contents into a cocktail glass, and serve.',
      user_id=2
    )
    ArizonaAntifreeze = Recipe(
      name='Arizona Antifreeze',
      description=None,
      instructions='Pour all ingredients into shot glass and slam !!!!',
      user_id=3
    )
    AGilligansIsland = Recipe(
      name='A Gilligan\'s Island',
      description=None,
      instructions='Shaken, not stirred!',
      user_id=3
    )
    AbsolutelyFabulous = Recipe(
      name='Absolutely Fabulous',
      description=None,
      instructions='Mix the Vodka and Cranberry juice together in a shaker and strain into a glass. Top up with Champagne.',
      user_id=2
    )
    AliceinWonderland = Recipe(
      name='Alice in Wonderland',
      description=None,
      instructions='Just mix the three ingredients one to one to one',
      user_id=1
    )
    AmarettoStoneSour = Recipe(
      name='Amaretto Stone Sour',
      description=None,
      instructions='Shake and Serve over ice',
      user_id=3
    )
    ATrueAmarettoSour = Recipe(
      name='A True Amaretto Sour',
      description=None,
      instructions='Rub the rim of an old fashioned glass with lemon, and dip repeatedly into granulated sugar until it has a good "frosted" rim. Shake a jigger of Amaretto with the juice of 1/2 a lemon. Strain into glass and add ice. Garnish with a Marachino Cherry.',
      user_id=2
    )
    AbsolutlyScrewedUp = Recipe(
      name='Absolutly Screwed Up',
      description=None,
      instructions='Shake it up it tasts better that way, but you can stir it if you want. 6 of those and you will be wasted for the rest of the night.',
      user_id=1
    )
    AppleBerrySmoothie = Recipe(
      name='Apple Berry Smoothie',
      description=None,
      instructions='Throw everything into a blender and liquify.',
      user_id=4
    )
    AdiosAmigosCocktail = Recipe(
      name='Adios Amigos Cocktail',
      description=None,
      instructions='Shake together all the ingredients and strain into a cold glass.',
      user_id=3
    )
    AfterDinnerCocktail = Recipe(
      name='After Dinner Cocktail',
      description=None,
      instructions='Shake all ingredients (except lime wedge) with ice and strain into a cocktail glass. Add the wedge of lime and serve.',
      user_id=3
    )
    AfterSupperCocktail = Recipe(
      name='After Supper Cocktail',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=1
    )
    Amidsummernightdream = Recipe(
      name='A midsummernight dream',
      description=None,
      instructions='Mix the strawberrys in a blender Pour it together with the vodka,kirch and strawberry liquer over ice in a shaker. Shake well and pour in a highballglass. Fill up with the Russchian water',
      user_id=1
    )
    ApplePiewithACrust = Recipe(
      name='Apple Pie with A Crust',
      description=None,
      instructions='Just mix the two liquids and sprinkle in the cinnamon. Serve either cold or heated.',
      user_id=2
    )
    ANightInOldMandalay = Recipe(
      name='A Night In Old Mandalay',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the light rum, añejo rum, orange juice, and lemon juice. Shake well. Strain into a highball glass almost filled with ice cubes. Top with the ginger ale. Garnish with the lemon twist.',
      user_id=4
    )
    AlmondChocolateCoffee = Recipe(
      name='Almond Chocolate Coffee',
      description=None,
      instructions='Pour in order into coffee cup. Top with whipped creme and chocolate shcvings.',
      user_id=4
    )
    ADMAfterDinnerMint = Recipe(
      name='A.D.M. (After Dinner Mint)',
      description=None,
      instructions='shake vigorously',
      user_id=1
    )
    AbsolutelyCranberrySmash = Recipe(
      name='Absolutely Cranberry Smash',
      description=None,
      instructions='Stir ingredients together. Serve over ice.',
      user_id=2
    )
    AmarettoStoneSourAlternative = Recipe(
      name='Amaretto Stone Sour Alternative',
      description=None,
      instructions='Shake sour mix, tequila and amaretto with ice. Strain into highball glass. Add a splash of OJ. Garnish with orange slice and a cherry.',
      user_id=4
    )
    bfiftytwo = Recipe(
      name='B-52',
      description=None,
      instructions='Layer ingredients into a shot glass. Serve with a stirrer.',
      user_id=1
    )
    bfiftythree = Recipe(
      name='B-53',
      description=None,
      instructions='Layer the Kahlua, Sambucca and Grand Marnier into a shot glas in that order. Better than B-52',
      user_id=2
    )
    Bijou = Recipe(
      name='Bijou',
      description=None,
      instructions='Stir in mixing glass with ice and strain',
      user_id=3
    )
    Boxcar = Recipe(
      name='Boxcar',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine all of the ingredients. Shake well. Strain into a sour glass.',
      user_id=2
    )
    BigRed = Recipe(
      name='Big Red',
      description=None,
      instructions='Pour ingredients into 1 ounce shot glass',
      user_id=1
    )
    Bellini = Recipe(
      name='Bellini',
      description=None,
      instructions='Pour peach purée into chilled flute, add sparkling wine. Stir gently.',
      user_id=1
    )
    Bramble = Recipe(
      name='Bramble',
      description=None,
      instructions='Fill glass with crushed ice. Build gin, lemon juice and simple syrup over. Stir, and then pour blackberry liqueur over in a circular fashion to create marbling effect. Garnish with two blackberries and lemon slice.',
      user_id=2
    )
    Balmoral = Recipe(
      name='Balmoral',
      description=None,
      instructions='In a mixing glass half-filled with ice cubes, combine all of the ingredients. Stir well. Strain into a cocktail glass.',
      user_id=2
    )
    Bluebird = Recipe(
      name='Bluebird',
      description=None,
      instructions='In a mixing glass half-filled with crushed ice, combine the gin, triple sec, Curacao, and bitters. Stir well. Strain into a cocktail glass and garnish with the lemon twist and the cherry.',
      user_id=3
    )
    Brooklyn = Recipe(
      name='Brooklyn',
      description=None,
      instructions='Combine ingredients with ice and stir until well-chilled. Strain into a chilled cocktail glass.',
      user_id=3
    )
    BoraBora = Recipe(
      name='Bora Bora',
      description=None,
      instructions='Prepare in a blender or shaker, serve in a highball glass on the rocks. Garnish with 1 slice of pineapple and one cherry.',
      user_id=2
    )
    Boomerang = Recipe(
      name='Boomerang',
      description=None,
      instructions='In a mixing glass half-filled with ice cubes, combine the gin, vermouth, bitters, and maraschino liqueur. Stir well. Strain into a cocktail glass and garnish with the cherry.',
      user_id=4
    )
    Barracuda = Recipe(
      name='Barracuda',
      description=None,
      instructions='Shake pour ingredients with ice. Strain into glass, top with Sparkling wine.',
      user_id=4
    )
    Brigadier = Recipe(
      name='Brigadier',
      description=None,
      instructions='Mix ingredients in a warmed mug and stir.',
      user_id=1
    )
    Broadside = Recipe(
      name='Broadside',
      description=None,
      instructions='Half fill the glass with ice cubes. Crush the wormwood and add to ice. Pour rum, scotch and butters, then serve!',
      user_id=4
    )
    Buccaneer = Recipe(
      name='Buccaneer',
      description=None,
      instructions='Pour the corona into an 18oz beer glass pour the bacardi limon into the beer stir very gently',
      user_id=1
    )
    BrainFart = Recipe(
      name='Brain Fart',
      description=None,
      instructions='Mix all ingredients together. Slowly and gently. Works best if ice is added to punch bowl and soda\'s are very cold.',
      user_id=4
    )
    Blackthorn = Recipe(
      name='Blackthorn',
      description=None,
      instructions='Stir sloe gin and vermouth with ice and strain into a cocktail glass. Add the twist of lemon peel and serve.',
      user_id=1
    )
    BobMarley = Recipe(
      name='Bob Marley',
      description=None,
      instructions='Layer in a 2 oz shot glass or pony glass',
      user_id=3
    )
    BibleBelt = Recipe(
      name='Bible Belt',
      description=None,
      instructions='Mix all ingredients, and pour over ice.',
      user_id=2
    )
    BubbleGum = Recipe(
      name='Bubble Gum',
      description=None,
      instructions='Layer in order into a shot glass.',
      user_id=1
    )
    BumbleBee = Recipe(
      name='Bumble Bee',
      description=None,
      instructions='This is a layered shot. First pour the Bailey\'s into the shot glass. Then take an upside down spoon and touch it to the inside wall of the glass. Carefully add the Kahlua. Repeat this process for the Sambuca. If done properly, the alcohol will stay separated and resemble a bumble bee. Enjoy!!!',
      user_id=3
    )
    BabyEskimo = Recipe(
      name='Baby Eskimo',
      description=None,
      instructions='Leave ice-cream out for about 10 minutes. Add ingredients in order, stir with chopstick (butter knife or spoon works too). Consume immediately and often. Nice and light, great for following a heavy drink.',
      user_id=4
    )
    BostonSour = Recipe(
      name='Boston Sour',
      description=None,
      instructions='Shake juice of lemon, powdered sugar, blended whiskey, and egg white with cracked ice and strain into a whiskey sour glass. Add the slice of lemon, top with the cherry, and serve.',
      user_id=3
    )
    BahamaMama = Recipe(
      name='Bahama Mama',
      description=None,
      instructions='Add 2 parts club soda or more or less to taste. Mix it all together and pour over a bunch of ice. Drink with a straw.',
      user_id=2
    )
    Brainteaser = Recipe(
      name='Brainteaser',
      description=None,
      instructions='layered erin first, then sambuca and then avocart(should sit in middle of other two. To drink: use a straw to suck up avocart then shot the rest and then suck fumes up through straw.',
      user_id=1
    )
    BloodyMary = Recipe(
      name='Bloody Mary',
      description=None,
      instructions='Stirring gently, pour all ingredients into highball glass. Garnish.',
      user_id=2
    )
    BlackTan = Recipe(
      name='Black & Tan',
      description=None,
      instructions='Fill pint glass half full with Bass. Next pour Guiness over a spoon slowly until glass is full. If done correctly the Guiness will stay on top and the Bass on bottom hence the name Black & Tan.',
      user_id=1
    )
    BlueLagoon = Recipe(
      name='Blue Lagoon',
      description=None,
      instructions='Pour vodka and curacao over ice in a highball glass. Fill with lemonade, top with the cherry, and serve.',
      user_id=2
    )
    BeesKnees = Recipe(
      name='Bee\'s Knees',
      description=None,
      instructions='Shake ingredients with crushed ice. Garnish with orange peel',
      user_id=2
    )
    BrandyFlip = Recipe(
      name='Brandy Flip',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the brandy, egg, sugar, and cream. Shake well. Strain into a sour glass and garnish with the nutmeg.',
      user_id=2
    )
    BrandySour = Recipe(
      name='Brandy Sour',
      description=None,
      instructions='Shake brandy, juice of lemon, and powdered sugar with ice and strain into a whiskey sour glass. Decorate with the lemon slice, top with the cherry, and serve.',
      user_id=4
    )
    ButterBaby = Recipe(
      name='Butter Baby',
      description=None,
      instructions='Blend together in a blender. Serve in a chilled Beer mug with Fresh Blueberries and caramel for topping.',
      user_id=2
    )
    Boulevardier = Recipe(
      name='Boulevardier',
      description=None,
      instructions='Stir with ice, strain, garnish and serve.',
      user_id=2
    )
    BourbonSour = Recipe(
      name='Bourbon Sour',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the bourbon, lemon juice, and sugar. Shake well. Strain into a whiskey sour glass, garnish with the orange slice and cherry.',
      user_id=1
    )
    BelgianBlue = Recipe(
      name='Belgian Blue',
      description=None,
      instructions='Just pour all ingredients in the glass and stir...',
      user_id=2
    )
    BloodyPunch = Recipe(
      name='Bloody Punch',
      description=None,
      instructions='Place the thawed strawberries in a large bowl. Mash them with a fork to ensure no large chunks. Step 2 In a punch bowl or pitcher, combine mashed strawberries, lime pulp and soda. Mix well. Step 3 Add blueberries and raisins. They will float and look like bugs in the punch.',
      user_id=3
    )
    BerryDeadly = Recipe(
      name='Berry Deadly',
      description=None,
      instructions='Add all ingredients to large bowl. Stir gently. Serve chilled.',
      user_id=4
    )
    BloodyMaria = Recipe(
      name='Bloody Maria',
      description=None,
      instructions='Shake all ingredients (except lemon slice) with cracked ice and strain into an old-fashioned glass over ice cubes. Add the slice of lemon and serve.',
      user_id=1
    )
    BlindRussian = Recipe(
      name='Blind Russian',
      description=None,
      instructions='Fill glass with ice. Add all liquers. Add milk. shake.',
      user_id=1
    )
    BlueMountain = Recipe(
      name='Blue Mountain',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine all of the ingredients. Shake well. Strain into an old-fashioned glass almost filled with ice cubes.',
      user_id=2
    )
    BountyHunter = Recipe(
      name='Bounty Hunter',
      description=None,
      instructions='Add the spirits into a shaker as well as the pineapple juice, strain into a Margarita glass. Top with Prosecco and garnish with Blueberries.',
      user_id=4
    )
    BombayCassis = Recipe(
      name='Bombay Cassis',
      description=None,
      instructions='Add the Bombay Sapphire, Crème de Cassis and lime juice to a balloon glass and swirl well to mix. Fill the glass with good quality cubed ice. Top up with chilled and freshly opened Fever-Tree Ginger Beer. Gently stir to combine, top with a gently squeezed lime wedge and finish with a fresh ginger slice.',
      user_id=2
    )
    BourbonSling = Recipe(
      name='Bourbon Sling',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the sugar, water, lemon juice, and bourbon. Shake well. Strain well. Strain into a highball glass. Garnish with the lemon twist.',
      user_id=2
    )
    BruisedHeart = Recipe(
      name='Bruised Heart',
      description=None,
      instructions='Pour all ingredients in a mixing tin over ice, stir, and strain into shot glass',
      user_id=1
    )
    BlackRussian = Recipe(
      name='Black Russian',
      description=None,
      instructions='Pour the ingredients into an old fashioned glass filled with ice cubes. Stir gently.',
      user_id=3
    )
    BabyGuinness = Recipe(
      name='Baby Guinness',
      description=None,
      instructions='Pour Kahlua, almost filling shot glass. Then, carefully pour Baileys, using wall of shot glass. This will give the "Guinness" its "head".',
      user_id=3
    )
    BrandyCobbler = Recipe(
      name='Brandy Cobbler',
      description=None,
      instructions='In an old-fashioned glass, dissolve the sugar in the club soda. Add crushed ice until the glass is almost full. Add the brandy. Stir well. Garnish with the cherry and the orange and lemon slices.',
      user_id=3
    )
    BlueHurricane = Recipe(
      name='Blue Hurricane',
      description=None,
      instructions='If each part is 1/2 oz then use about 2.5 cups of ice. Blend it all together. Drink it with a big straw if you have one.',
      user_id=4
    )
    BostonSidecar = Recipe(
      name='Boston Sidecar',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=3
    )
    BlueMargarita = Recipe(
      name='Blue Margarita',
      description=None,
      instructions='Rub rim of cocktail glass with lime juice. Dip rim in coarse salt. Shake tequila, blue curacao, and lime juice with ice, strain into the salt-rimmed glass, and serve.',
      user_id=3
    )
    BananaCreamPi = Recipe(
      name='Banana Cream Pi',
      description=None,
      instructions='Serve over ice.',
      user_id=4
    )
    BananaDaiquiri = Recipe(
      name='Banana Daiquiri',
      description=None,
      instructions='Pour all ingredients into shaker with ice cubes. Shake well. Strain in chilled cocktail glass.',
      user_id=3
    )
    BelliniMartini = Recipe(
      name='Bellini Martini',
      description=None,
      instructions='Add ice cubes to shaker. Add vodka. Add peach schnapps. Add peach nectar. Shake. Strain into glass. Add lemon twist peel.',
      user_id=2
    )
    BlackandBrown = Recipe(
      name='Black and Brown',
      description=None,
      instructions='CAREFULLY to avoid explosive head formation: Pour Beer glass half full of favorite rootbeer and top off with Guinness.',
      user_id=2
    )
    BrandyAlexander = Recipe(
      name='Brandy Alexander',
      description=None,
      instructions='Shake all ingredients (except nutmeg) with ice and strain contents into a cocktail glass. Sprinkle nutmeg on top and serve.',
      user_id=1
    )
    BacardiCocktail = Recipe(
      name='Bacardi Cocktail',
      description=None,
      instructions='Shake together with ice. Strain into glass and serve.',
      user_id=4
    )
    BleedingSurgeon = Recipe(
      name='Bleeding Surgeon',
      description=None,
      instructions='Pour Shot of Rum over slice of orange. Fill the remaining space in glass half way full of surge or similar drink. Finish off glass with cranberry juice. Be carefull, warm surge may foam over the glass.',
      user_id=4
    )
    BlueberryMojito = Recipe(
      name='Blueberry Mojito',
      description=None,
      instructions='Muddle the blueberries with the other ingredients and serve in a highball glass. Garnish with mint and a half slice of lime.',
      user_id=4
    )
    BermudaHighball = Recipe(
      name='Bermuda Highball',
      description=None,
      instructions='Pour brandy, gin, and dry vermouth into a highball glass over ice cubes. Fill with carbonated water and stir. Add the twist of lemon and serve. (Ginger ale may be substituted for carbonated water, if preferred.)',
      user_id=4
    )
    ButterflyEffect = Recipe(
      name='Butterfly Effect',
      description=None,
      instructions='Grab your boston tin, fill it with cubes ice and then simply chuck in all your ingredients apart from your lemonade. Now it\'s time to shake what your mama gave you until all your ingredients are blended to perfection. Add some cubes of ice to your hurricane glass, give them a swill to cool the whole thing down and then strain your raspberry vodka cocktail of wonder into the glass. Top with lemonade and chuck a sprig of mint on top for garnish. You can either get drinking at this point or go and try and grab a few butterflies to finish, the choice really is yours.',
      user_id=1
    )
    BananaMilkShake = Recipe(
      name='Banana Milk Shake',
      description=None,
      instructions='Blend very well, preferably in a household mixer. Serve in a wine glass, garnish with whipped cream and a piece of banana.',
      user_id=1
    )
    BraveBullShooter = Recipe(
      name='Brave Bull Shooter',
      description=None,
      instructions='Pour Tabasco into bottom of shot glass and fill with tequila.',
      user_id=3
    )
    BlackForestShake = Recipe(
      name='Black Forest Shake',
      description=None,
      instructions='In a blender put ice cubes, chocolate syrup, cherry brandy, vodka, and milk. Blend very well.',
      user_id=2
    )
    BetweenTheSheets = Recipe(
      name='Between The Sheets',
      description=None,
      instructions='Pour all ingredients into shaker with ice cubes, shake, strain into chilled cocktail glass.',
      user_id=3
    )
    BaileysDreamShake = Recipe(
      name='Bailey\'s Dream Shake',
      description=None,
      instructions='Blend ingredients for 30 seconds. Definitely refreshing for a hot summer\'s day !',
      user_id=2
    )
    BobbyBurnsCocktail = Recipe(
      name='Bobby Burns Cocktail',
      description=None,
      instructions='Stir all ingredients (except lemon peel) with ice and strain into a cocktail glass. Add the twist of lemon peel and serve.',
      user_id=3
    )
    BananaStrawberryShake = Recipe(
      name='Banana Strawberry Shake',
      description=None,
      instructions='Blend all together in a blender until smooth.',
      user_id=1
    )
    BoozySnickersMilkshake = Recipe(
      name='Boozy Snickers Milkshake',
      description=None,
      instructions='Place the snickers bars in a plastic bag and roll over them with a rolling pin until crushed. Add crushed snickers pieces, ice cream, milk, caramel sauce, chocolate sauce, and chocolate liquor to a blender. Blend until shake is thick and frothy. Pour into glasses and top with chocolate liquor and whip cream.',
      user_id=1
    )
    BananaCantaloupeSmoothie = Recipe(
      name='Banana Cantaloupe Smoothie',
      description=None,
      instructions='Juice cantaloupe, pour juice into blender, add banana, and liquify.',
      user_id=2
    )
    BrandonandWillsCokeFloat = Recipe(
      name='Brandon and Will\'s Coke Float',
      description=None,
      instructions='Scoop two large scoops of vanilla ice-cream into frosted beer mug. Next, add 2 ounces Maker\'s Mark. Then, pour in coke. Gently stir and enjoy.',
      user_id=3
    )
    BananaStrawberryShakeDaiquiri = Recipe(
      name='Banana Strawberry Shake Daiquiri',
      description=None,
      instructions='Blend all together in a blender until smooth.',
      user_id=3
    )
    Casino = Recipe(
      name='Casino',
      description=None,
      instructions='Pour all ingredients into shaker with ice cubes. Shake well. Strain into chilled cocktail glass. Garnish with a lemon twist and a maraschino cherry. Serve without a straw.',
      user_id=1
    )
    Caipirinha = Recipe(
      name='Caipirinha',
      description=None,
      instructions='Place lime and sugar into old fashioned glass and muddle (mash the two ingredients together using a muddler or a wooden spoon). Fill the glass with ice and add the Cachaça.',
      user_id=3
    )
    CreamSoda = Recipe(
      name='Cream Soda',
      description=None,
      instructions='Pour 1oz of Spiced Rum into a highball glass with ice. Fill with Ginger Ale.',
      user_id=1
    )
    CubaLibra = Recipe(
      name='Cuba Libra',
      description=None,
      instructions='Fill tall glass with ice cubes. Add rum. Rub cut edge of lime on rim of glass then squeeze juice into glass. Fill with Coca-Cola. Garnish with lime slice. Enjoy!',
      user_id=2
    )
    CherryRum = Recipe(
      name='Cherry Rum',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=4
    )
    CubaLibre = Recipe(
      name='Cuba Libre',
      description=None,
      instructions='Build all ingredients in a Collins glass filled with ice. Garnish with lime wedge.',
      user_id=2
    )
    CornnOil = Recipe(
      name='Corn n Oil',
      description=None,
      instructions='Cut the half lime in half again. Add the lime, falernum, and bitters to a rocks glass. Muddle. Add the rum. (Aged Barbados rum such as Plantation 5 Year is recommended). Add ice and stir. Float the blackstrap rum on top. Serve with a straw.',
      user_id=2
    )
    CitrusCoke = Recipe(
      name='Citrus Coke',
      description=None,
      instructions='Pour half of coke in a glass. Then add Bacardi and top it off with the remaining coke. Stir and drink up!',
      user_id=3
    )
    CasaBlanca = Recipe(
      name='Casa Blanca',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=4
    )
    CloverClub = Recipe(
      name='Clover Club',
      description=None,
      instructions='Dry shake ingredients to emulsify, add ice, shake and served straight up.',
      user_id=4
    )
    Caipirissima = Recipe(
      name='Caipirissima',
      description=None,
      instructions='Same as Caipirinha but instead of cachaca you add WHITE RUM. It\'s great!!!!!!!!',
      user_id=2
    )
    CitySlicker = Recipe(
      name='City Slicker',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine all of the ingredients. Shake well. Strain into a cocktail glass.',
      user_id=1
    )
    CampariBeer = Recipe(
      name='Campari Beer',
      description=None,
      instructions='Use a 15 oz glass. Add Campari first. Fill with beer.',
      user_id=4
    )
    ChicagoFizz = Recipe(
      name='Chicago Fizz',
      description=None,
      instructions='Shake all ingredients (except carbonated water) with ice and strain into a highball glass over two ice cubes. Fill with carbonated water, stir, and serve.',
      user_id=4
    )
    Cosmopolitan = Recipe(
      name='Cosmopolitan',
      description=None,
      instructions='Add all ingredients into cocktail shaker filled with ice. Shake well and double strain into large cocktail glass. Garnish with lime wheel.',
      user_id=3
    )
    CoffeeVodka = Recipe(
      name='Coffee-Vodka',
      description=None,
      instructions='Boil water and sugar until dissolved. Turn off heat. Slowly add dry instant coffee and continue stirring. Add a chopped vanilla bean to the vodka, then combine the cooled sugar syrup and coffee solution with the vodka. Cover tightly and shake vigorously each day for 3 weeks. Strain and filter. Its also best to let the sugar mixture cool completely so the vodka won\'t evaporate when its added. If you like a smoother feel to the liqueur you can add about 1 teaspoon of glycerine to the finished product.',
      user_id=1
    )
    CasinoRoyale = Recipe(
      name='Casino Royale',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine all of the ingredients. Shake well. Strain into a sour glass.',
      user_id=3
    )
    CorpseReviver = Recipe(
      name='Corpse Reviver',
      description=None,
      instructions='Shake, strain, straight up, cocktail glass rinsed with absinthe',
      user_id=1
    )
    ChocolateMilk = Recipe(
      name='Chocolate Milk',
      description=None,
      instructions='Put the milk in the bottom, pour the Liquer on top and add the dash of amaretto. Do not mix. SLAM IT!',
      user_id=2
    )
    CloveCocktail = Recipe(
      name='Clove Cocktail',
      description=None,
      instructions='Stir all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=1
    )
    CoffeeLiqueur = Recipe(
      name='Coffee Liqueur',
      description=None,
      instructions='Combine coffee, sugar and water. Simmer 1 hour and let cool. Add vanilla and vodka. Age in sealed jar 2 to 3 weeks.',
      user_id=2
    )
    CokeandDrops = Recipe(
      name='Coke and Drops',
      description=None,
      instructions='Take a glass, pour the Coke in the glass, then you take 7 drops of lemon juice. Granish with a lemon slice on the rim of the glass.',
      user_id=1
    )
    ChocolateDrink = Recipe(
      name='Chocolate Drink',
      description=None,
      instructions='Melt the bar in a small amount of boiling water. Add milk. Cook over low heat, whipping gently (with a whisk, i would assume) until heated well. Don\'t let it boil! Serve in coffee mug.',
      user_id=2
    )
    CranberryPunch = Recipe(
      name='Cranberry Punch',
      description=None,
      instructions='Combine first four ingredients. Stir until sugar is dissolved, chill. Then add ginger ale just before serving. Add ice ring to keep punch cold.',
      user_id=2
    )
    CremedeMenthe = Recipe(
      name='Creme de Menthe',
      description=None,
      instructions='Bring sugar and water to a boil and simmer for 10 minutes. Cool. Add the remaining ingredients and stir. Cover and let ripen for 1 month.',
      user_id=4
    )
    ChocolateMonkey = Recipe(
      name='Chocolate Monkey',
      description=None,
      instructions='blend liqeuors with ice-cream, milk and syrup. pour into parfait glass, top with whipped cream and garnish with banana and cherry.',
      user_id=4
    )
    CranberryCordial = Recipe(
      name='Cranberry Cordial',
      description=None,
      instructions='Place the chopped cranberries in a 2 liter jar that has a tight-fitting lid. Add the sugar and rum. Adjust the lid securely and place the jar in a cool, dark place. Invert the jar and shake it every day for six weeks. Strain the cordial into bottles and seal with corks.',
      user_id=3
    )
    ChocolateBeverage = Recipe(
      name='Chocolate Beverage',
      description=None,
      instructions='Boil milk in the top of a deep double boiler five minutes. Remove from fire and add chocolate, mixed with the cinnamon, a little at a time, beating with molinillo or egg beater after each addition. When the chocolate is thoroughly blended, heat to the boiling point. Place over bottom of double boiler and add eggs, whipping constantly, until they are thoroughly blended and the mixture is frothing. Serve in coffee mug. Serves eight.',
      user_id=3
    )
    ChampagneCocktail = Recipe(
      name='Champagne Cocktail',
      description=None,
      instructions='Add dash of Angostura bitter onto sugar cube and drop it into champagne flute. Add cognac followed by gently pouring chilled champagne. Garnish with orange slice and maraschino cherry.',
      user_id=3
    )
    CaliforniaLemonade = Recipe(
      name='California Lemonade',
      description=None,
      instructions='Shake all ingredients (except carbonated water) with ice and strain into a collins glass over shaved ice. Fill with carbonated water and stir. Decorate with slices of orange and lemon. Add the cherry and serve with a straw.',
      user_id=4
    )
    CaliforniaRootBeer = Recipe(
      name='California Root Beer',
      description=None,
      instructions='Put Kahlua and Galliano in highball glass fill with soda',
      user_id=3
    )
    CaptainKiddsPunch = Recipe(
      name='Captain Kidd\'s Punch',
      description=None,
      instructions='Mix all ingredients together in a shaker and strain into a collins glass. Use Caribbean dark Rum for a sweeter taste.',
      user_id=3
    )
    CosmopolitanMartini = Recipe(
      name='Cosmopolitan Martini',
      description=None,
      instructions='Pour all ingredients in mixing glass half filled with ice, shake and strain into chilled Martini glass.',
      user_id=2
    )
    CaribbeanBoilermaker = Recipe(
      name='Caribbean Boilermaker',
      description=None,
      instructions='Pour the Corona into an 18oz beer glass pour the rum into the beer.',
      user_id=1
    )
    ClassicOldFashioned = Recipe(
      name='Classic Old-Fashioned',
      description=None,
      instructions='In an old-fashioned glass, muddle the bitters and water into the sugar cube, using the back of a teaspoon. Almost fill the glass with ice cubes and add the bourbon. Garnish with the orange slice and the cherry. Serve with a swizzle stick.',
      user_id=4
    )
    ChocolateBlackRussian = Recipe(
      name='Chocolate Black Russian',
      description=None,
      instructions='Combine all ingredients in an electric blender and blend at a low speed for a short length of time. Pour into a chilled champagne flute and serve.',
      user_id=1
    )
    CocktailHorsesNeck = Recipe(
      name='Cocktail Horse\'s Neck',
      description=None,
      instructions='Wash and brush an organic, untreated lemon, then cut a spiral of lemon peel, using a citrus peel. If it is too large, cut it with a sharp knife. Put some ice in a tall tumbler glass, place the lemon peel inside and pour the cognac, add the ginger beer and let 2-3 drops of Angostura fall into it. Easy to do, but once you try it you\'ll love it.',
      user_id=2
    )
    CaribbeanOrangeLiqueur = Recipe(
      name='Caribbean Orange Liqueur',
      description=None,
      instructions='Pare very thinly the bright-colored rind from the oranges (no white). Blot the peel on paper towels to remove any excess oil. Put peel in a 4 cup screw-top jar. Add 2 cups vodka. Close jar. Store in a cool, dark place for 2 days or until the vodka has absorbed the flavor. Remove peel and add remaining vodka. Close jar and add remaining cup of vodka. Close the jar and store in a cool dark place at least 1 month to age.',
      user_id=2
    )
    CastillianHotChocolate = Recipe(
      name='Castillian Hot Chocolate',
      description=None,
      instructions='Shift the cocoa and sugar together into a medium-sized saucepan. Dissolve the cornstarch in the water, and stir into the cocoa and sugar until it is a smooth paste. Begin heating the mixture, stirring it with a whisk, and gradually pour in the milk. Continue stirring with the whisk as you bring the liquid to a simmer. Allow the chocolate to simmer for about 10 minutes, stirring often, until it is thick, glossy and completely smooth. Serve steaming hot in coffee mug. Serves six.',
      user_id=2
    )
    CherryElectricLemonade = Recipe(
      name='Cherry Electric Lemonade',
      description=None,
      instructions='Now stir vigorously and then pour over a large cup of ice. Now drink it with a straw and stir occasionally.',
      user_id=3
    )
    Derby = Recipe(
      name='Derby',
      description=None,
      instructions='Pour all ingredients into a mixing glass with ice. Stir. Strain into a cocktail glass. Garnish with a sprig of fresh mint in the drink.',
      user_id=3
    )
    Diesel = Recipe(
      name='Diesel',
      description=None,
      instructions='Pour the lager first then add the blackcurrant cordial. Top up with the cider. The colour sholud be very dark approaching the colour of Guiness.',
      user_id=2
    )
    Daiquiri = Recipe(
      name='Daiquiri',
      description=None,
      instructions='Pour all ingredients into shaker with ice cubes. Shake well. Strain in chilled cocktail glass.',
      user_id=1
    )
    Danbooka = Recipe(
      name='Danbooka',
      description=None,
      instructions='pour it in and mix it.',
      user_id=1
    )
    Downshift = Recipe(
      name='Downshift',
      description=None,
      instructions='Start with the Sprite. Next comes the tequila. After that, add the Minute Maid Fruit Punch, then float the 151. Rocks optional.',
      user_id=4
    )
    Dragonfly = Recipe(
      name='Dragonfly',
      description=None,
      instructions='In a highball glass almost filled with ice cubes, combine the gin and ginger ale. Stir well. Garnish with the lime wedge.',
      user_id=4
    )
    DryMartini = Recipe(
      name='Dry Martini',
      description=None,
      instructions='Straight: Pour all ingredients into mixing glass with ice cubes. Stir well. Strain in chilled martini cocktail glass. Squeeze oil from lemon peel onto the drink, or garnish with olive.',
      user_id=1
    )
    DryRobRoy = Recipe(
      name='Dry Rob Roy',
      description=None,
      instructions='In a mixing glass half-filled with ice cubes, combine the Scotch and vermouth. Stir well. Strain into a cocktail glass. Garnish with the lemon twist.',
      user_id=1
    )
    DirtyMartini = Recipe(
      name='Dirty Martini',
      description=None,
      instructions='Pour the vodka, dry vermouth and olive brine into a cocktail shaker with a handful of ice and shake well. Rub the rim of a martini glass with the wedge of lemon. Strain the contents of the cocktail shaker into the glass and add the olive. A dirty Martini contains a splash of olive brine or olive juice and is typically garnished with an olive.',
      user_id=1
    )
    DarkwoodSling = Recipe(
      name='Darkwood Sling',
      description=None,
      instructions='There are many good cherry liqueurs you can use, but I prefere Heering. Add one share of the liqueur. Then you add one share of Soda. For a sour sling use Tonic (most people prefer the drink without Tonic). Afterwards you fill the glass with Orange Juice and ice cubes.',
      user_id=2
    )
    DarkandStormy = Recipe(
      name='Dark and Stormy',
      description=None,
      instructions='In a highball glass filled with ice add 6cl dark rum and top with ginger beer. Garnish with lime wedge.',
      user_id=1
    )
    DarkCaipirinha = Recipe(
      name='Dark Caipirinha',
      description=None,
      instructions='Muddle the sugar into the lime wedges in an old-fashioned glass. Fill the glass with ice cubes. Pour the cachaca into the glass. Stir well.',
      user_id=4
    )
    DuchampsPunch = Recipe(
      name='Duchamp\'s Punch',
      description=None,
      instructions='Shake all ingredients. Double strain in a chilled double old fashioned glass with abig ice cube. Garnish with a couple of lavender sprigs',
      user_id=3
    )
    Damnedifyoudo = Recipe(
      name='Damned if you do',
      description=None,
      instructions='Pour into shot glass. Put in mouth. Repeat as deemed necessary.',
      user_id=4
    )
    DubonnetCocktail = Recipe(
      name='Dubonnet Cocktail',
      description=None,
      instructions='Stir all ingredients (except lemon peel) with ice and strain into a cocktail glass. Add the twist of lemon peel and serve.',
      user_id=1
    )
    DrinkingChocolate = Recipe(
      name='Drinking Chocolate',
      description=None,
      instructions='Heat the cream and milk with the cinnamon and vanilla bean very slowly for 15-20 minutes. (If you don\'t have any beans add 1-2 tsp of vanilla after heating). Remove the bean and cinnamon. Add the chocolate. Mix until fully melted. Serve topped with some very dense fresh whipped cream. Serves 1-2 depending upon how much of a glutton you are. For a richer chocolate, use 4 oz of milk, 4 oz of cream, 4 oz of chocolate. Serve in coffee mug.',
      user_id=4
    )
    DeathintheAfternoon = Recipe(
      name='Death in the Afternoon',
      description=None,
      instructions='Easy as you like, pour the absinthe into a chilled glass, top with champagne. Must be drunk mid afternoon for the optimum effect.',
      user_id=1
    )
    EggCream = Recipe(
      name='Egg Cream',
      description=None,
      instructions='Mix syrup and milk in a fountain glass. Add soda water, serve with a straw.',
      user_id=1
    )
    EggNog4 = Recipe(
      name='Egg Nog #4',
      description=None,
      instructions='In a small mixer bowl beat egg yolks till blended. Gradually add 1/4 cup sugar, beating at high speed till thick and lemon colored. Stir in milk, stir in rum, bourbon, vanilla, and salt. Chill thoroughly. Whip cream. Wash beaters well. In a large mixer bowl beat egg whites till soft peaks form. Gradually add remaining 1/4 cup sugar, beating to stiff peaks. Fold yolk mixture and whipped cream into egg whites. Serve immediately. Sprinkle nutmeg over each serving. Serve in a punch bowl or another big bowl. NOTE: For a nonalcoholic eggnog, prepare Eggnog as above, except omit the bourbon and rum and increase the milk to 3 cups.',
      user_id=1
    )
    EnglishHighball = Recipe(
      name='English Highball',
      description=None,
      instructions='Pour brandy, gin, and sweet vermouth into a highball glass over ice cubes. Fill with carbonated water. Add the twist of lemon peel, stir, and serve. (Ginger ale may be substituted for carbonated water, if preferred.)',
      user_id=4
    )
    EspressoMartini = Recipe(
      name='Espresso Martini',
      description=None,
      instructions='Pour ingredients into shaker filled with ice, shake vigorously, and strain into chilled martini glass',
      user_id=1
    )
    EspressoRumtini = Recipe(
      name='Espresso Rumtini',
      description=None,
      instructions='Mix together in a cocktail glass. Garnish with some choclate powder and coffee beans',
      user_id=1
    )
    EggNogHealthy = Recipe(
      name='Egg Nog - Healthy',
      description=None,
      instructions='Whip egg substitute and sugar together, combine with the two kinds of milk, vanilla, and rum. Mix well. Chill over night. Sprinkle with nutmeg. Makes 6 servings.',
      user_id=1
    )
    EnglishRoseCocktail = Recipe(
      name='English Rose Cocktail',
      description=None,
      instructions='Rub rim of cocktail glass with lemon juice and dip rim of glass in powdered sugar. Shake all ingredients (except cherry) with ice and strain into sugar-rimmed glass. Top with the cherry and serve.',
      user_id=4
    )
    ElderflowerCaipirinha = Recipe(
      name='Elderflower Caipirinha',
      description=None,
      instructions='Take the glass and muddle the lime in it. Fill the glass with crushed ice and add the Cachaca. Stir well and top with some more crushed ice. Garnish with lime and enjoy!',
      user_id=2
    )
    EggNogClassicCooked = Recipe(
      name='Egg-Nog - Classic Cooked',
      description=None,
      instructions='In large saucepan, beat together eggs, sugar and salt, if desired. Stir in 2 cups of the milk. Cook over low heat, stirring constantly, until mixture is thick enough to coat a metal spoon and reaches 160 degrees F. Remove from heat. Stir in remaining 2 cups milk and vanilla. Cover and regfigerate until thoroughly chilled, several hours or overnight. Just before serving, pour into bowl or pitcher. Garnish or add stir-ins, if desired. Choose 1 or several of: Chocolate curls, cinnamon sticks, extracts of flavorings, flavored brandy or liqueur, fruit juice or nectar, ground nutmeg, maraschino cherries, orange slices, peppermint sticks or candy canes, plain brandy, run or whiskey, sherbet or ice-cream, whipping cream, whipped. Serve immediately.',
      user_id=1
    )
    EmpellnCocinasFatWashedMezcal = Recipe(
      name='Empellón Cocina\'s Fat-Washed Mezcal',
      description=None,
      instructions='To ensure that your pork fat is just as delicious as theirs, here\'s their adobo marinade and what to do with it (you\'ll also need a rack of ribs): 4 ancho chiles, 8 guajillo chiles and 4 chipotle chiles, plus 4 cloves roasted garlic, half a cup of cider vinegar, a quarter teaspoon of Mexican oregano, 1 teaspoon of ground black pepper, a whole clove, a quarter teaspoon of ground cinnamon and a half teaspoon of ground cumin. Toast the dried chiles and soak in water for at least an hour until they are rehydrated. Drain and discard the soaking liquid. Combine the soaked chiles with the remaining ingredients and purée until smooth. Cold smoke a rack of baby back pork ribs by taking a large hotel pan with woodchips on one side and charcoal on the other. Place another, smaller, pan with pork ribs, above the charcoal/woodchip pan. Ignite the charcoal, being careful to not ignite the woodchips. Cover both pans with foil and allow to smoke for 10-15 minutes, until desired level of smoke is achieved, then coat with adobo marinade and wrap in tin foil prior to placing ribs in a 300 degree oven for 7 hours. When the ribs have cooled, strain off the fat and use for the infusion. If you\'re having a hard time coming up to the same kind of volume of fat, make up the balance with pork lard from a butcher. To get the same depth of flavor without the ribs, heat up the fat in a pot with a few spoons of the marinade. Once you\'ve got your tub of seasoned pork fat in cooled liquid form, pour equal amounts of Ilegal Joven mezcal and fat into a sealable container. Seal the container and give it a really good shake, then put it in the freezer overnight. When the whole thing is separated and congealed, pour it through a fine mesh chinoise. If you don\'t have a chinoise, try a fine mesh strainer, or if you don\'t have one of those, try spooning off most of the fat. There will be some beads of orange fat left in the strained mezcal: run that through a few layers of cheesecloth (or coffee filters in a pinch) to get rid of the last of it. The mezcal is now ready for drinking, straight-up or in a cocktail. Habanero tincture Slice habaneros and add 2 ounces Ilegal Joven mezcal. Allow to sit overnight or until desired level of heat is achieved. Cocktail Combine mezcal and chocolate liqueur in a mixing glass with ice and stir for 45 seconds. Strain into chilled coupe. Carefully "sink" the coffee liqueur down the inside of the coupe over a spoon. Garnish with 5 drops habanero tincture.',
      user_id=4
    )
    Fros = Recipe(
      name='Frosé',
      description=None,
      instructions='Step 1 Pour rosé into a 13x9" pan and freeze until almost solid (it won\'t completely solidify due to the alcohol), at least 6 hours. Step 2 Meanwhile, bring sugar and ½ cup water to a boil in a medium saucepan; cook, stirring constantly, until sugar dissolves, about 3 minutes. Add strawberries, remove from heat, and let sit 30 minutes to infuse syrup with strawberry flavor. Strain through a fine-mesh sieve into a small bowl (do not press on solids); cover and chill until cold, about 30 minutes. Step 3 Scrape rosé into a blender. Add lemon juice, 3½ ounces strawberry syrup, and 1 cup crushed ice and purée until smooth. Transfer blender jar to freezer and freeze until frosé is thickened (aim for milkshake consistency), 25–35 minutes. Step 4 Blend again until frosé is slushy. Divide among glasses. Step 5 Do Ahead: Rosé can be frozen 1 week ahead.',
      user_id=3
    )
    Frapp = Recipe(
      name='Frappé',
      description=None,
      instructions='Mix together. Blend at highest blender speed for about 1 minute. Pour into a glass and drink with a straw. Notes: This works best if everything is cold (if you make fresh coffee, mix it with the milk and let it sit in the fridge for 1/2 hour. If it is not frothy, add more milk, or even just some more milk powder. The froth gradually turns to liquid at the bottom of the glass, so you will find that you can sit and drink this for about 1/2 hour, with more iced coffee continually appearing at the bottom. Very refreshing.',
      user_id=4
    )
    FoxyLady = Recipe(
      name='Foxy Lady',
      description=None,
      instructions='Shake all ingredients with ice, strain into a chilled cocktail glass, and serve.',
      user_id=4
    )
    French75 = Recipe(
      name='French 75',
      description=None,
      instructions='Combine gin, sugar, and lemon juice in a cocktail shaker filled with ice. Shake vigorously and strain into a chilled champagne glass. Top up with Champagne. Stir gently.',
      user_id=4
    )
    FiggyThyme = Recipe(
      name='Figgy Thyme',
      description=None,
      instructions='In a lewis bag, crush up some ice like a baller/maniac (@glacioice). Pour your precious ice into a collins glass. In a cocktail shaker, muddle the figs and thyme together. Add honey vodka, lemon juice, and a large ice cube (@glacioice). Shake until well chilled, and strain into glass. Add tonic water and finally 2 dashes of angostura bitters. Garnish with sliced figs and thyme.',
      user_id=3
    )
    FriscoSour = Recipe(
      name='Frisco Sour',
      description=None,
      instructions='Shake all ingredients (except slices of lemon and lime) with ice and strain into a whiskey sour glass. Decorate with the slices of lemon and lime and serve.',
      user_id=1
    )
    FruitShake = Recipe(
      name='Fruit Shake',
      description=None,
      instructions='Blend til smooth.',
      user_id=1
    )
    FruitCooler = Recipe(
      name='Fruit Cooler',
      description=None,
      instructions='Toss strawberries with sugar, and let sit overnight in refrigerator. Cut lemon, reserve two slices. Juice the rest. Mix together the lemon juice, strawberries, apple juice, and soda water. Add slices of lemon (decor, really). In glasses, put ice cubes, and a slice of apple. Pour drink in, and serve.',
      user_id=3
    )
    FreddyKruger = Recipe(
      name='Freddy Kruger',
      description=None,
      instructions='make it an ample size shot!!',
      user_id=1
    )
    FunkandSoul = Recipe(
      name='Funk and Soul',
      description=None,
      instructions='Mix all ingredients together and strain into a Collins glass. Use Jamaican rum where possible for a more authentic taste.',
      user_id=2
    )
    FuzzyAsshole = Recipe(
      name='Fuzzy Asshole',
      description=None,
      instructions='fill coffe mug half full of coffee. Fill the other half full of Peach Schnapps. Stir and drink while hot.',
      user_id=1
    )
    FrenchMartini = Recipe(
      name='French Martini',
      description=None,
      instructions='Pour all ingredients into shaker with ice cubes. Shake well and strain into a chilled cocktail glass. Squeeze oil from lemon peel onto the drink.',
      user_id=3
    )
    FrenchNegroni = Recipe(
      name='French Negroni',
      description=None,
      instructions='Add ice to a shaker and pour in all ingredients. Using a bar spoon, stir 40 to 45 revolutions or until thoroughly chilled. Strain into a martini glass or over ice into a rocks glass. Garnish with orange twist.',
      user_id=2
    )
    Fahrenheit5000 = Recipe(
      name='Fahrenheit 5000',
      description=None,
      instructions='Cover bottom of shot glass with Tabasco Sauce and then fill with half Firewater and half Absolut Peppar.',
      user_id=1
    )
    FlyingDutchman = Recipe(
      name='Flying Dutchman',
      description=None,
      instructions='In an old-fashioned glass almost filled with ice cubes, combine the gin and triple sec. Stir well.',
      user_id=2
    )
    FrozenDaiquiri = Recipe(
      name='Frozen Daiquiri',
      description=None,
      instructions='Combine all ingredients (except for the cherry) in an electric blender and blend at a low speed for five seconds, then blend at a high speed until firm. Pour contents into a champagne flute, top with the cherry, and serve.',
      user_id=3
    )
    FruitFlipFlop = Recipe(
      name='Fruit Flip-Flop',
      description=None,
      instructions='Place all ingredients in the blender jar - cover and whiz on medium speed until well blended. Pour in one tall, 2 medium or 3 small glasses and drink up.',
      user_id=3
    )
    FlyingScotchman = Recipe(
      name='Flying Scotchman',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=2
    )
    FrenchConnection = Recipe(
      name='French Connection',
      description=None,
      instructions='Pour all ingredients directly into old fashioned glass filled with ice cubes. Stir gently.',
      user_id=1
    )
    FlamingDrPepper = Recipe(
      name='Flaming Dr. Pepper',
      description=None,
      instructions='Add Amaretto, Bacardi, and vodka. Mix in the Dr. Pepper and beer',
      user_id=3
    )
    FlamingLamborghini = Recipe(
      name='Flaming Lamborghini',
      description=None,
      instructions='Pour the Sambuca and Kahlua into the Cocktail Glass and give the drinker a straw. Pour the Baileys and Blue Curacao into two sepsrate shot glasses either side of the cocktail glass. Set light the concotion in the cocktail glass and start to drink through the straw (this drink should be drunk in one) , as the bottom of the glass is reached put out the fire by pouring the Baileys and Blue Curacao into the cocktail glass and keep drinking till it\'s all gone!!',
      user_id=3
    )
    FlandersFlakeOut = Recipe(
      name='Flander\'s Flake-Out',
      description=None,
      instructions='Bang \'em both in.',
      user_id=2
    )
    FrozenMintDaiquiri = Recipe(
      name='Frozen Mint Daiquiri',
      description=None,
      instructions='Combine all ingredients with 1 cup of crushed ice in an electric blender. Blend at a low speed for a short length of time. Pour into an old-fashioned glass and serve.',
      user_id=2
    )
    FrozenPineappleDaiquiri = Recipe(
      name='Frozen Pineapple Daiquiri',
      description=None,
      instructions='Combine all ingredients with 1 cup of crushed ice in an electric blender. Blend at a low speed for a short length of time. Pour into a cocktail glass and serve.',
      user_id=3
    )
    GG = Recipe(
      name='GG',
      description=None,
      instructions='Pour the Galliano liqueur over ice. Fill the remainder of the glass with ginger ale and thats all there is to it. You now have a your very own GG.',
      user_id=2
    )
    Gimlet = Recipe(
      name='Gimlet',
      description=None,
      instructions='Add all the ingredients to a shaker and fill with ice. Shake, and strain into a chilled cocktail glass or an Old Fashioned glass filled with fresh ice. Garnish with a lime wheel.',
      user_id=2
    )
    Godchild = Recipe(
      name='Godchild',
      description=None,
      instructions='Shake all ingredients well with cracked ice, strain into a champagne flute, and serve.',
      user_id=2
    )
    GinFizz = Recipe(
      name='Gin Fizz',
      description=None,
      instructions='Shake all ingredients with ice cubes, except soda water. Pour into glass. Top with soda water.',
      user_id=3
    )
    GinSour = Recipe(
      name='Gin Sour',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the gin, lemon juice, and sugar. Shake well. Strain into a sour glass and garnish with the orange slice and the cherry.',
      user_id=4
    )
    Gagliardo = Recipe(
      name='Gagliardo',
      description=None,
      instructions='Shake well and serve in a cocktail glass. This is a home cocktail of American/Internet Bar del Pozzo, Pavia, Italy.',
      user_id=3
    )
    Godmother = Recipe(
      name='Godmother',
      description=None,
      instructions='Pour vodka and amaretto into an old-fashioned glass over ice and serve.',
      user_id=4
    )
    Godfather = Recipe(
      name='Godfather',
      description=None,
      instructions='Pour all ingredients directly into old fashioned glass filled with ice cubes. Stir gently.',
      user_id=2
    )
    Gluehwein = Recipe(
      name='Gluehwein',
      description=None,
      instructions='Boil sugar and spices in water, leave in the water for 30 minutes. Strain the spiced water and mix with the wine. Heat slowly until short of boiling temperature. (To remove alcohol, let it boil for a while.) You may add lemon or orange juice to taste. Serve in irish coffee cup.',
      user_id=2
    )
    GinTonic = Recipe(
      name='Gin Tonic',
      description=None,
      instructions='Fill a highball glass with ice, pour the gin, top with tonic water and squeeze a lemon wedge and garnish with a lemon wedge.',
      user_id=4
    )
    GinToddy = Recipe(
      name='Gin Toddy',
      description=None,
      instructions='Mix powdered sugar and water in an old-fashioned glass. Add gin and one ice cube. Stir, add the twist of lemon peel, and serve.',
      user_id=3
    )
    GinSmash = Recipe(
      name='Gin Smash',
      description=None,
      instructions='Muddle sugar with carbonated water and mint sprigs in an old-fashioned glass. Add gin and 1 ice cube. Stir, add the orange slice and the cherry, and serve.',
      user_id=2
    )
    GinDaisy = Recipe(
      name='Gin Daisy',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the gin, lemon juice, sugar, and grenadine. Shake well. Pour into an old-fashioned glass and garnish with the cherry and the orange slice.',
      user_id=4
    )
    GinLemon = Recipe(
      name='Gin Lemon',
      description=None,
      instructions='For the preparation of the gin lemon you will not need the shaker. Fill the tumbler with ice, pour the gin and lemonade over it. Gently mix and decorate with a slice of lemon. Those who prefer can also add a few mint leaves. Your gin lemon is ready to be served.',
      user_id=1
    )
    GinSling = Recipe(
      name='Gin Sling',
      description=None,
      instructions='Dissolve powdered sugar in mixture of water and juice of lemon. Add gin. Pour into an old-fashioned glass over ice cubes and stir. Add the twist of orange peel and serve.',
      user_id=2
    )
    Greyhound = Recipe(
      name='Greyhound',
      description=None,
      instructions='Add the vodka to a Collins glass filled with ice. Top with grapefruit juice and stir.',
      user_id=2
    )
    GinRickey = Recipe(
      name='Gin Rickey',
      description=None,
      instructions='Half-fill a tall glass with ice. Mix the gin and Grenadine together and pour over the ice. Add the lime or lemon juice and top off with soda water. Decorate the glass with lime and/or lemon slices.',
      user_id=2
    )
    GinSquirt = Recipe(
      name='Gin Squirt',
      description=None,
      instructions='Stir gin, grenadine, and powdered sugar with ice and strain into a highball glass over ice cubes. Fill with carbonated water and stir. Decorate with the pineapple chunks and the strawberries and serve.',
      user_id=2
    )
    GrandBlue = Recipe(
      name='Grand Blue',
      description=None,
      instructions='Serve in an old fashioned glass.',
      user_id=4
    )
    GinCooler = Recipe(
      name='Gin Cooler',
      description=None,
      instructions='Stir powdered sugar and 2 oz. carbonated water in a collins glass. Fill glass with ice and add gin. Fill with carbonated water and stir. Add the lemon peel and the orange spiral so that the end of the orange spiral dangles over rim of glass.',
      user_id=4
    )
    GinSwizzle = Recipe(
      name='Gin Swizzle',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the lime juice, sugar, gin, and bitters. Shake well. Almost fill a colling glass with ice cubes. Stir until the glass is frosted. Strain the mixture in the shaker into the glass and add the club soda.',
      user_id=2
    )
    GrassSkirt = Recipe(
      name='Grass Skirt',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the gin, triple sec, pineapple juice, and grenadine. Shake well. Pour into an old-fashioned glass and garnish with the pineapple slice.',
      user_id=3
    )
    Grasshopper = Recipe(
      name='Grasshopper',
      description=None,
      instructions='Pour ingredients into a cocktail shaker with ice. Shake briskly and then strain into a chilled cocktail glass.',
      user_id=2
    )
    GrimReaper = Recipe(
      name='Grim Reaper',
      description=None,
      instructions='Mix Kahlua and 151 in glass. Quickly add ice and pour grenadine over ice to give ice red tint.',
      user_id=3
    )
    GinandSoda = Recipe(
      name='Gin and Soda',
      description=None,
      instructions='Pour the Gin and Soda water into a highball glass almost filled with ice cubes. Stir well. Garnish with the lime wedge.',
      user_id=1
    )
    Goldendream = Recipe(
      name='Golden dream',
      description=None,
      instructions='Shake with cracked ice. Strain into glass and serve.',
      user_id=4
    )
    GreenGoblin = Recipe(
      name='Green Goblin',
      description=None,
      instructions='Cider First, Lager then Curacao',
      user_id=2
    )
    GrizzlyBear = Recipe(
      name='Grizzly Bear',
      description=None,
      instructions='Served over ice. Sounds nasty, but tastes great.',
      user_id=3
    )
    GinAndTonic = Recipe(
      name='Gin And Tonic',
      description=None,
      instructions='Pour the gin and the tonic water into a highball glass almost filled with ice cubes. Stir well. Garnish with the lime wedge.',
      user_id=4
    )
    GinBasilSmash = Recipe(
      name='Gin Basil Smash',
      description=None,
      instructions='Muddle Basil leaves (~ 10) with Suggar Syrup in a shaker. Add Gin an Lemon Juice. Filter and serve in a tumbler with ice',
      user_id=2
    )
    GentlemansClub = Recipe(
      name='Gentleman\'s Club',
      description=None,
      instructions='In an old-fashioned glass almost filled with ice cubes, combine all of the ingredients. Stir well.',
      user_id=1
    )
    GirlFromIpanema = Recipe(
      name='Girl From Ipanema',
      description=None,
      instructions='Add the cachaca, lemon juice and syrup to your boston glass. Add ice and shake until ice cold. Pour into a chilled flute and top-up with Champagne',
      user_id=3
    )
    GaribaldiNegroni = Recipe(
      name='Garibaldi Negroni',
      description=None,
      instructions='Mix together in a shaker and garnish with a simple orange slice. Fill your vitamin C and cocktail fix at the same time!',
      user_id=4
    )
    GideonsGreenDinosaur = Recipe(
      name='Gideon\'s Green Dinosaur',
      description=None,
      instructions='Add all ingredients in collins glass with ice and stir.',
      user_id=2
    )
    GrapelemonpineappleSmoothie = Recipe(
      name='Grape lemon pineapple Smoothie',
      description=None,
      instructions='Throw everything into a blender and liquify.',
      user_id=4
    )
    Hd = Recipe(
      name='H.D.',
      description=None,
      instructions='Mix the whisky and Baileys Cream in a beer-glass (at least 50 cl). Fill the rest of the glass with coffee.',
      user_id=2
    )
    HoneyBee = Recipe(
      name='Honey Bee',
      description=None,
      instructions='Shake ingredients with crushed ice',
      user_id=4
    )
    HotToddy = Recipe(
      name='Hot Toddy',
      description=None,
      instructions='STEP 1 Whisk the whisky and honey together and split between 2 heatproof glasses. Add half of the cinnamon stick to each, then top up with 200ml boiling water. STEP 2 Add a splash of lemon juice to each, then taste and add more to your preference. Finish each with a slice of lemon, studded with a clove, and serve immediately.',
      user_id=1
    )
    Herbalflame = Recipe(
      name='Herbal flame',
      description=None,
      instructions='Pour Hot Damn 100 in bottom of a jar or regular glass. Fill the rest of the glass with sweet tea. Stir with spoon, straw, or better yet a cinnamon stick and leave it in.',
      user_id=4
    )
    HorsesNeck = Recipe(
      name='Horse\'s Neck',
      description=None,
      instructions='Pour brandy and ginger ale directly into highball glass with ice cubes. Stir gently. Garnish with lemon zest. If desired, add dashes of Angostura Bitter.',
      user_id=4
    )
    HappySkipper = Recipe(
      name='Happy Skipper',
      description=None,
      instructions='Pour Captain Morgan\'s Spiced Rum over ice, fill glass to top with Ginger Ale. Garnish with lime. Tastes like a cream soda. Named for the Gilligan\'s Island reference ("The Captain" *in* "Ginger" is a Happy Skipper!)',
      user_id=1
    )
    HuntersMoon = Recipe(
      name='Hunter\'s Moon',
      description=None,
      instructions='Put the Bombay Sapphire, Martini Bianco, sugar syrup & blackberries in a cocktail shaker with lots of ice and shake vigorously before pouring into a balloon glass, topping up with lemonade and garnishing with a wedge of orange.',
      user_id=3
    )
    HalloweenPunch = Recipe(
      name='Halloween Punch',
      description=None,
      instructions='Tip the cherry juice, orange peel, chilli, cinnamon sticks, cloves and ginger into a large saucepan. Simmer for 5 mins, then turn off the heat. Leave to cool, then chill for at least 4 hrs, or up to 2 days – the longer you leave it the more intense the flavours. If serving to young children, take the chilli out after a few hours. When you\'re ready to serve, pour the juice into a jug. Serve in glass bottles or glasses and pop a straw in each. If you\'re adding vodka, do so at this stage. Dangle a fangs sweet from each glass.',
      user_id=4
    )
    HavanaCocktail = Recipe(
      name='Havana Cocktail',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine all of the ingredients. Shake well. Strain into a cocktail glass.',
      user_id=1
    )
    HomemadeKahlua = Recipe(
      name='Homemade Kahlua',
      description=None,
      instructions='Dissolve sugar in 2 cups of boiling water and add corn syrup. Dissolve the instant coffee in the remaining water. Pour syrup and coffee in a gallon jug. Let it cool. Add vodka and vanilla when cold. For the best result, let the mixture "mature" for 4-5 weeks.',
      user_id=1
    )
    HotCreamyBush = Recipe(
      name='Hot Creamy Bush',
      description=None,
      instructions='Combine all ingredients in glass',
      user_id=2
    )
    HarveyWallbanger = Recipe(
      name='Harvey Wallbanger',
      description=None,
      instructions='Stir the vodka and orange juice with ice in the glass, then float the Galliano on top. Garnish and serve.',
      user_id=1
    )
    HawaiianCocktail = Recipe(
      name='Hawaiian Cocktail',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=3
    )
    HemingwaySpecial = Recipe(
      name='Hemingway Special',
      description=None,
      instructions='Pour all ingredients into a shaker with ice. Shake.',
      user_id=4
    )
    HighlandFlingCocktail = Recipe(
      name='Highland Fling Cocktail',
      description=None,
      instructions='Stir all ingredients (except olive) with ice and strain into a cocktail glass. Add the olive and serve.',
      user_id=1
    )
    HotChocolatetoDiefor = Recipe(
      name='Hot Chocolate to Die for',
      description=None,
      instructions='Melt the chocolate, butter and vanilla in a double boiler. When just smooth stir in the cream.',
      user_id=4
    )
    Ipamena = Recipe(
      name='Ipamena',
      description=None,
      instructions='Cut half a lime into pieces, place in a shaker, add the sugar and crush. Measure the passion fruit juice, add it to the shaker and fill up with ice cubes. Close the shaker and shake vigorously. Pour the liquid into a glass, top up with ginger ale, stir with a teaspoon and then garnish the rim of the glass with a slice of lime',
      user_id=3
    )
    IcePick = Recipe(
      name='Ice Pick',
      description=None,
      instructions='Put Vodka in glass fill with iced tea. Stir in lemon to taste.',
      user_id=1
    )
    IcedCoffee = Recipe(
      name='Iced Coffee',
      description=None,
      instructions='Mix together until coffee and sugar is dissolved. Add milk. Shake well. Using a blender or milk shake maker produces a very foamy drink. Serve in coffee mug.',
      user_id=2
    )
    IrishCream = Recipe(
      name='Irish Cream',
      description=None,
      instructions='Mix scotch and milk. Add half-and-half. Add rest.',
      user_id=3
    )
    IrishCoffee = Recipe(
      name='Irish Coffee',
      description=None,
      instructions='Heat the coffee, whiskey and sugar; do not boil. Pour into glass and top with cream; serve hot.',
      user_id=4
    )
    IrishSpring = Recipe(
      name='Irish Spring',
      description=None,
      instructions='Pour all ingredients (except orange slice and cherry) into a collins glass over ice cubes. Garnish with the slice of orange, add the cherry on top, and serve.',
      user_id=3
    )
    ImperialFizz = Recipe(
      name='Imperial Fizz',
      description=None,
      instructions='Shake all ingredients (except carbonated water) with ice and strain into a highball glass over two ice cubes. Fill with carbonated water, stir, and serve.',
      user_id=1
    )
    IrishRussian = Recipe(
      name='Irish Russian',
      description=None,
      instructions='Add the ingredients in the order listed in the recipe. Care must be taken when adding the Guinness to prevent an excess of foam. Do Not add ice.',
      user_id=1
    )
    ImperialCocktail = Recipe(
      name='Imperial Cocktail',
      description=None,
      instructions='Shake with ice and strain into cocktail glass.',
      user_id=4
    )
    IcedCoffeeFillip = Recipe(
      name='Iced Coffee Fillip',
      description=None,
      instructions='Mix together in a coffee mug and chill before serving.',
      user_id=3
    )
    IrishCurdlingCow = Recipe(
      name='Irish Curdling Cow',
      description=None,
      instructions='Pour Irish Cream, Vodka, and Bourbon in a glass. Add some ice and mix in the orange juice.',
      user_id=1
    )
    JamDonut = Recipe(
      name='Jam Donut',
      description=None,
      instructions='Coat the rim of a shot glass with sugar using sugar syrup to stick. Add the Chambord raspberry liqueur to the shot glass, and carefully layer the Baileys Irish Cream on top. Serve.',
      user_id=3
    )
    Jitterbug = Recipe(
      name='Jitterbug',
      description=None,
      instructions='Wet glass, dip rim in sugar. Then add Ice. Then add everything else. It\'s that simple!',
      user_id=3
    )
    Jackhammer = Recipe(
      name='Jackhammer',
      description=None,
      instructions='Serve over ice- Warning,Deadly!',
      user_id=2
    )
    JellyBean = Recipe(
      name='Jelly Bean',
      description=None,
      instructions='mix equal parts in pony glass-tastes just like a jelly bean!',
      user_id=2
    )
    Jelloshots = Recipe(
      name='Jello shots',
      description=None,
      instructions='Boil 3 cups of water then add jello. Mix jello and water until jello is completely disolved. Add the two cups of vodka and mix together. Pour mixture into plastic shot glasses and chill until firm. Then, eat away...',
      user_id=4
    )
    JamaicaKiss = Recipe(
      name='Jamaica Kiss',
      description=None,
      instructions='Fill a tumbler with ice cubes. Add a shot of Tia Maria and a shot of Jamaican light rum. Fill the tumbler with milk. Blend until smooth and serve immediately.',
      user_id=1
    )
    JohnCollins = Recipe(
      name='John Collins',
      description=None,
      instructions='Pour all ingredients directly into highball glass filled with ice. Stir gently. Garnish. Add a dash of Angostura bitters.',
      user_id=2
    )
    JapaneseFizz = Recipe(
      name='Japanese Fizz',
      description=None,
      instructions='Shake all ingredients (except carbonated water) with ice and strain into a highball glass over two ice cubes. Fill with carbonated water, stir, and serve.',
      user_id=2
    )
    JamaicanCoffee = Recipe(
      name='Jamaican Coffee',
      description=None,
      instructions='Stir the rum, coffee and water together. Top with the whipped cream. Sprinkle with a pinch of well ground coffee and drink with a straw.',
      user_id=1
    )
    JustaMoonmint = Recipe(
      name='Just a Moonmint',
      description=None,
      instructions='Place all ingredients in the blender jar - cover and whiz on medium speed until well blended. Pour in one tall, 2 medium or 3 small glasses and drink up.',
      user_id=3
    )
    JewelOfTheNile = Recipe(
      name='Jewel Of The Nile',
      description=None,
      instructions='In a mixing glass half-filled with ice cubes, combine all of the ingredients. Stir well. Strain into a cocktail glass.',
      user_id=3
    )
    JackRoseCocktail = Recipe(
      name='Jack Rose Cocktail',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=1
    )
    JacksVanillaCoke = Recipe(
      name='Jack\'s Vanilla Coke',
      description=None,
      instructions='After pouring in your ingredients, and adding 3-5 ice cubes, according to taste. Stir the drink with a stirrer to get the Vanilla off the bottom.',
      user_id=3
    )
    Kir = Recipe(
      name='Kir',
      description=None,
      instructions='Add the crème de cassis to the bottom of the glass, then top up with wine.',
      user_id=3
    )
    Karsk = Recipe(
      name='Karsk',
      description=None,
      instructions='Put a copper coin in a coffe-cup and fill up with coffee until you no longer see the coin, then add alcohol until you see the coin. Norwegian speciality.',
      user_id=2
    )
    Kamikaze = Recipe(
      name='Kamikaze',
      description=None,
      instructions='Shake all ingredients together with ice. Strain into glass, garnish and serve.',
      user_id=1
    )
    KirRoyale = Recipe(
      name='Kir Royale',
      description=None,
      instructions='Pour Creme de cassis in glass, gently pour champagne on top',
      user_id=1
    )
    KiwiLemon = Recipe(
      name='Kiwi Lemon',
      description=None,
      instructions='Mix in highball glass. Stirr. Garnish with slice of kiwi.',
      user_id=2
    )
    KurantTea = Recipe(
      name='Kurant Tea',
      description=None,
      instructions='Pour Absolut Kurant into a comfortably big tea-cup. Add the not too hot(!) apple tea and, if you like, some sugar. Enjoy!',
      user_id=1
    )
    KiokiCoffee = Recipe(
      name='Kioki Coffee',
      description=None,
      instructions='Stir. Add whipped cream to the top.',
      user_id=2
    )
    KiwiMartini = Recipe(
      name='Kiwi Martini',
      description=None,
      instructions='The kiwi martini is a very fun vodka cocktail and it is one of the best drinks that makes use of fresh fruit. Though there are a few recipes floating around, this is one of the easiest and it is an absolutely delightful green martini to drink. For this recipe, you\'ll simply muddle slices of kiwi with simple syrup, then shake it with vodka. It\'s a drink that anyone can mix up in minutes and a perfect cocktail to show off your favorite vodka.',
      user_id=3
    )
    KissmeQuick = Recipe(
      name='Kiss me Quick',
      description=None,
      instructions='mix in the glass',
      user_id=1
    )
    KoolAidShot = Recipe(
      name='Kool-Aid Shot',
      description=None,
      instructions='Pour into a large glass with ice and stir. Add a little cranberry juice to taste.',
      user_id=3
    )
    KoolFirstAid = Recipe(
      name='Kool First Aid',
      description=None,
      instructions='Add Kool Aid to a double shot glass, and top with rum. Slam and shoot.',
      user_id=3
    )
    KentuckyBAndB = Recipe(
      name='Kentucky B And B',
      description=None,
      instructions='Pour the bourbon and Benedictine into a brandy snifter.',
      user_id=3
    )
    KentuckyColonel = Recipe(
      name='Kentucky Colonel',
      description=None,
      instructions='In a shaker half-filled with ice cubes combine the courbon and Benedictine. Shake and strain into a cocktail glass. Garnish with the lemon twist.',
      user_id=1
    )
    KoolAidSlammer = Recipe(
      name='Kool-Aid Slammer',
      description=None,
      instructions='Fill half the shot glass with the kool-aid first. Then put a paper towel over the top of the glass and slowly pour in the vodka. If you do it right, you should be able to see that the two liquids are separated, with the vodka on top. Now slam it! The last thing you\'ll taste is the kool-aid.',
      user_id=1
    )
    KiwiPapayaSmoothie = Recipe(
      name='Kiwi Papaya Smoothie',
      description=None,
      instructions='Throw everything into a blender and liquify.',
      user_id=2
    )
    KillthecoldSmoothie = Recipe(
      name='Kill the cold Smoothie',
      description=None,
      instructions='Juice ginger and lemon and add it to hot water. You may add cardomom.',
      user_id=3
    )
    Limeade = Recipe(
      name='Limeade',
      description=None,
      instructions='In a large glass, put the lime juice and sugar, and stir well. Add cold seltzer water to fill. Put the lime peels in the glass. Drink. Repeat until limes or soda run out.',
      user_id=3
    )
    LunchBox = Recipe(
      name='Lunch Box',
      description=None,
      instructions='Fill a pint glass almost full with beer. Then fill the rest with orange juice (careful not to fill it to the top). Then take the shot of Amaretto and drop it in.',
      user_id=3
    )
    LemonDrop = Recipe(
      name='Lemon Drop',
      description=None,
      instructions='Shake and strain into a chilled cocktail glass rimmed with sugar.',
      user_id=3
    )
    LemonShot = Recipe(
      name='Lemon Shot',
      description=None,
      instructions='Mix Galliano and Absolut Citron in a shot glass, lay lemon wedge sprinkled with sugar over glass and pour a rum over wedge and glass. light rum with a lighter and let burn for a second. Do shot quickly and suck on lemon. If it is done correctly, this will taste like a shot of sweet lemonade.',
      user_id=3
    )
    Longvodka = Recipe(
      name='Long vodka',
      description=None,
      instructions='Shake a tall glass with ice cubes and Angostura, coating the inside of the glass. Por the vodka onto this, add 1 slice of lime and squeeze juice out of remainder, mix with tonic, stir and voila you have a Long Vodka',
      user_id=2
    )
    LassiKhara = Recipe(
      name='Lassi Khara',
      description=None,
      instructions='Blend (frappe) in blender until frothy. Add torn curry leaves and serve cold.',
      user_id=3
    )
    LassiRaita = Recipe(
      name='Lassi Raita',
      description=None,
      instructions='Blend the yoghurt and ice cubes together, until the yoghurt becomes more liquid. Add sugar to taste. The lemon/lime is optional but it gives it a slightly tart taste. Dash of salt. Raita is also good for the summer. Instead of having a traditional salad you can make raita instead.',
      user_id=4
    )
    Lemouroudji = Recipe(
      name='Lemouroudji',
      description=None,
      instructions='Juice the lemons. Peel and grate the ginger. Place the grated ginger and a liberal dash of the cayenne pepper into a piece of cheesecloth, and tie it into a knot. Let soak in the water. After 15 minutes or so, add the sugar, and the lemon juice. Chill, and serve.',
      user_id=4
    )
    LochLomond = Recipe(
      name='Loch Lomond',
      description=None,
      instructions='In a mixing glass half-filled with ice cubes, combine the Scotch, Drambuie, and vermouth. Stir well. Strain into a cocktail glass. Garnish with the lemon twist.',
      user_id=3
    )
    LondonTown = Recipe(
      name='London Town',
      description=None,
      instructions='In a mixing glass half-filled with ice cubes, combine all of the ingredients. Stir well. Strain into a cocktail glass.',
      user_id=3
    )
    LassiMango = Recipe(
      name='Lassi - Mango',
      description=None,
      instructions='Put it all in a blender and pour over crushed ice. You can also use other fruits like strawberries and bananas.',
      user_id=3
    )
    LassiSweet = Recipe(
      name='Lassi - Sweet',
      description=None,
      instructions='Put all ingredients into a blender and blend until nice and frothy. Serve chilled.',
      user_id=2
    )
    LimonaCorona = Recipe(
      name='Limona Corona',
      description=None,
      instructions='Open the Corona. Fill the empty space in the neck in the bottle with the rum. The bottle should be filled to the top. Plug the bottle with your thumb or the palm of your hand. Turn the bottle upside-down so the rum and beer mix. Turn the bottle rightside-up, unplug, and drink.',
      user_id=2
    )
    LordAndLady = Recipe(
      name='Lord And Lady',
      description=None,
      instructions='Pour the rum and Tia Maria into an old-fashioned glass almost filled with ice cubes. Stir well.',
      user_id=4
    )
    LadyLoveFizz = Recipe(
      name='Lady Love Fizz',
      description=None,
      instructions='Shake all ingredients (except carbonated water) with ice and strain into a cocktail glass over two ice cubes. Fill with carbonated water, stir, and serve.',
      user_id=4
    )
    LongIslandTea = Recipe(
      name='Long Island Tea',
      description=None,
      instructions='Combine all ingredients (except cola) and pour over ice in a highball glass. Add the splash of cola for color. Decorate with a slice of lemon and serve.',
      user_id=1
    )
    LoneTreeCocktail = Recipe(
      name='Lone Tree Cocktail',
      description=None,
      instructions='Stir ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=3
    )
    LazyCoconutPaloma = Recipe(
      name='Lazy Coconut Paloma',
      description=None,
      instructions='Mix the coconut liqueur (preferably tequila) with the grapefruit juice and top with soda water. Garnish with a large grapefruit slice against the inside of the glass.',
      user_id=2
    )
    LongIslandIcedTea = Recipe(
      name='Long Island Iced Tea',
      description=None,
      instructions='Mix all contents in a highball glass and sitr gently. Add dash of Coca-Cola for the coloring and garnish with lemon or lime twist.',
      user_id=3
    )
    LemonElderflowerSpritzer = Recipe(
      name='Lemon Elderflower Spritzer',
      description=None,
      instructions='Pour all ingredients over ice, stir and enjoy!',
      user_id=4
    )
    LassiASouthIndianDrink = Recipe(
      name='Lassi - A South Indian Drink',
      description=None,
      instructions='Blend in a blender for 3 seconds. Lassi is one of the easiest things to make, and there are many ways of making it. Basically, it is buttermilk (yoghurt whisked with water), and you can choose almost any consistency that you like, from the thinnest to the thickest. Serve cold.',
      user_id=4
    )
    Mojito = Recipe(
      name='Mojito',
      description=None,
      instructions='Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.',
      user_id=4
    )
    Mimosa = Recipe(
      name='Mimosa',
      description=None,
      instructions='Ensure both ingredients are well chilled, then mix into the glass. Serve cold.',
      user_id=3
    )
    MaiTai = Recipe(
      name='Mai Tai',
      description=None,
      instructions='Shake all ingredients with ice. Strain into glass. Garnish and serve with straw.',
      user_id=3
    )
    Martini = Recipe(
      name='Martini',
      description=None,
      instructions='Straight: Pour all ingredients into mixing glass with ice cubes. Stir well. Strain in chilled martini cocktail glass. Squeeze oil from lemon peel onto the drink, or garnish with olive.',
      user_id=1
    )
    Michelada = Recipe(
      name='Michelada',
      description=None,
      instructions='Mix the beer with tomato juice, freshly squeezed lime juice, and Worcestershire sauce, teriyaki sauce, soy sauce, or hot sauce. Served In a chilled, salt-rimmed glass',
      user_id=3
    )
    Manhattan = Recipe(
      name='Manhattan',
      description=None,
      instructions='Stirred over ice, strained into a chilled glass, garnished, and served up.',
      user_id=4
    )
    Margarita = Recipe(
      name='Margarita',
      description=None,
      instructions='Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.',
      user_id=2
    )
    Mauresque = Recipe(
      name='Mauresque',
      description=None,
      instructions='1 - Pour the Ricard (or pastis) 2 - Pour the orgeat syrup 3 - Finally pour the water and add ice cubes at your convenience. Add the ice cubes at the end, otherwise the syrup and pastis do not mix well.',
      user_id=3
    )
    MintJulep = Recipe(
      name='Mint Julep',
      description=None,
      instructions='In a highball glass gently muddle the mint, sugar and water. Fill the glass with cracked ice, add Bourbon and stir well until the glass is well frosted. Garnish with a mint sprig.',
      user_id=2
    )
    Mudslinger = Recipe(
      name='Mudslinger',
      description=None,
      instructions='Add all contents to a large jug or punch bowl. Stir well!',
      user_id=4
    )
    Martinez2 = Recipe(
      name='Martinez 2',
      description=None,
      instructions='Add all ingredients to a mixing glass and fill with ice. Stir until chilled, and strain into a chilled coupe glass.',
      user_id=1
    )
    Moranguito = Recipe(
      name='Moranguito',
      description=None,
      instructions='first you put rhe absinthe, then put tequila, then put the Granadine syrup.',
      user_id=1
    )
    MiamiVice = Recipe(
      name='Miami Vice',
      description=None,
      instructions='First: Mix pina colada with 2.5 oz. of rum with ice(set aside). Second: Mix daiquiri with 2.5 oz. of rum with ice. Third: While frozen, add pina colda mix then daiquiri mix in glass (Making sure they do not get mixed together).',
      user_id=2
    )
    MoscowMule = Recipe(
      name='Moscow Mule',
      description=None,
      instructions='Combine vodka and ginger beer in a highball glass filled with ice. Add lime juice. Stir gently. Garnish.',
      user_id=3
    )
    MulledWine = Recipe(
      name='Mulled Wine',
      description=None,
      instructions='Simmer 3 cups water with, sugar, cloves, cinnamon sticks, and lemon peel in a stainless steel pot for 10 minutes. Add wine heat to a "coffee temperature" (DO NOT BOIL) then add the brandy.',
      user_id=3
    )
    MasalaChai = Recipe(
      name='Masala Chai',
      description=None,
      instructions='Bring 2 cups of water to boil. Add all the ingredients and boil again for about 15 seconds. Let stand for a minute. Warm milk in a pot. Filter tea into cups. Add milk and sugar. That\'s IT.',
      user_id=4
    )
    MunichMule = Recipe(
      name='Munich Mule',
      description=None,
      instructions='Fill glass with ice Pour Gin and Lime Juice Fill glass with Ginger Beer Garnish with Cucumer and Lime slice',
      user_id=2
    )
    MochaBerry = Recipe(
      name='Mocha-Berry',
      description=None,
      instructions='pour 6 oz. of coffee in a mug or Irish coffee cup. add coca mix and chambord, mix well and top off with whipped cream.',
      user_id=2
    )
    MangoMojito = Recipe(
      name='Mango Mojito',
      description=None,
      instructions='Squeeze the juice from 1½ limes and blend with the mango to give a smooth purée. Cut the rest of the limes into quarters, and then cut each wedge in half again. Put 2 pieces of lime in a highball glass for each person and add 1 teaspoon of caster sugar and 5-6 mint leaves to each glass. Squish everything together with a muddler or the end of a rolling pin to release all the flavours from the lime and mint. Divide the mango purée between the glasses and add 30ml white rum and a handful of crushed ice to each one, stirring well to mix everything together. Top up with soda water to serve and garnish with extra mint, if you like.',
      user_id=2
    )
    MojitoExtra = Recipe(
      name='Mojito Extra',
      description=None,
      instructions='Put mint with lemon juice in a glas, mash the mint with a spoon, ice, rum & fill up with club soda. Top it with Angostura.',
      user_id=3
    )
    MonkeyGland = Recipe(
      name='Monkey Gland',
      description=None,
      instructions='Shake well over ice cubes in a shaker, strain into a chilled cocktail glass.',
      user_id=4
    )
    MidnightMint = Recipe(
      name='Midnight Mint',
      description=None,
      instructions='If available, rim cocktail (Martini) glass with sugar syrup then dip into chocolate flakes or powder. Add ingredients into shaker with ice. Shake well then strain into cocktail glass.',
      user_id=1
    )
    MaryPickford = Recipe(
      name='Mary Pickford',
      description=None,
      instructions='Shake and strain into a chilled large cocktail glass',
      user_id=3
    )
    MonkeyWrench = Recipe(
      name='Monkey Wrench',
      description=None,
      instructions='Pour all of the ingredients into an old-fashioned glass almost filled with ice cubes. Stir well.',
      user_id=3
    )
    MothersMilk = Recipe(
      name='Mother\'s Milk',
      description=None,
      instructions='Shake over ice, strain. Serves two.',
      user_id=2
    )
    MidnightManx = Recipe(
      name='Midnight Manx',
      description=None,
      instructions='Fill a mixer with ice and add Baileys, Kahlua, Goldshlager, and cream. Shake for 5 seconds and Strain into a double rocks glass filled with ice. Add chilled coffee Stir and enjoy!',
      user_id=2
    )
    MalibuTwister = Recipe(
      name='Malibu Twister',
      description=None,
      instructions='Add rum & trister then, add cranberry jucie,stir',
      user_id=1
    )
    MidnightCowboy = Recipe(
      name='Midnight Cowboy',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine all of the ingredients. Shake well. Strain into a cocktail glass.',
      user_id=1
    )
    MountainBramble = Recipe(
      name='Mountain Bramble',
      description=None,
      instructions='Muddle the blackberries in a tumbler glass. Mix the Gin, lemon juice and sugar syrup in a shaker and strain over chopped ice. Top with Soda water and garnish with more blackberries and some mint',
      user_id=1
    )
    MartinezCocktail = Recipe(
      name='Martinez Cocktail',
      description=None,
      instructions='Stir all ingredients (except cherry) with ice and strain into a cocktail glass. Top with the cherry and serve.',
      user_id=1
    )
    MicrowaveHotCocoa = Recipe(
      name='Microwave Hot Cocoa',
      description=None,
      instructions='Combine sugar, cocoa, salt and hot water in 1-quart micro-proof measuring cup (or coffee mug). Microwave at HIGH (100%) for 1 to 1 1/2 minutes or until boiling. Add milk, sitr and microwave an additonal 1 1/2 to 2 minutes or until hot. Stir in vanilla, blend well.',
      user_id=1
    )
    MangoOrangeSmoothie = Recipe(
      name='Mango Orange Smoothie',
      description=None,
      instructions='Throw everything into a blender and liquify.',
      user_id=2
    )
    MississippiPlantersPunch = Recipe(
      name='Mississippi Planters Punch',
      description=None,
      instructions='Shake all ingredients (except carbonated water) with ice and strain into a collins glass over ice cubes. Fill with carbonated water, stir, and serve.',
      user_id=1
    )
    Negroni = Recipe(
      name='Negroni',
      description=None,
      instructions='Stir into glass over ice, garnish and serve.',
      user_id=1
    )
    NewYorkSour = Recipe(
      name='New York Sour',
      description=None,
      instructions='Shake blended whiskey, juice of lemon, and powdered sugar with ice and strain into a whiskey sour glass. Float claret on top. Decorate with the half-slice of lemon and the cherry and serve.',
      user_id=3
    )
    NuttyIrishman = Recipe(
      name='Nutty Irishman',
      description=None,
      instructions='Serve over ice',
      user_id=4
    )
    NationalAquarium = Recipe(
      name='National Aquarium',
      description=None,
      instructions='Pour all ingredients into a shaker of ice. Shake well. Serve on the rocks.',
      user_id=3
    )
    NewYorkLemonade = Recipe(
      name='New York Lemonade',
      description=None,
      instructions='Serve in a chilled cocktail glass. Lemon and sugar the rim. Stir and Strain.',
      user_id=2
    )
    NukedHotChocolate = Recipe(
      name='Nuked Hot Chocolate',
      description=None,
      instructions='Mix with a bit of milk (1 oz or so) in coffee mug. Nuke mug for about 30-50 seconds. Stir until the heated cocoa dissolves. Fill mug with milk. Nuke for 1-2 minutes, depending on wattage and preferences as to burnt mouth parts.',
      user_id=4
    )
    Orgasm = Recipe(
      name='Orgasm',
      description=None,
      instructions='Shake all ingredients with ice, strain into a chilled cocktail glass, and serve.',
      user_id=3
    )
    OldPal = Recipe(
      name='Old Pal',
      description=None,
      instructions='Chill cocktail glass. Add ingredients to a mixing glass, and fill 2/3 full with ice. Stir about 20 seconds. Empty cocktail glass and strain into the glass. Garnish with a twist of lemon peel.',
      user_id=3
    )
    OldCuban = Recipe(
      name='Old Cuban',
      description=None,
      instructions='Shake a handful of mint, 2oz white rum, 1oz of sugar syrup, 1oz lime juice and 2 dashes angostura bitters with ice. Double strain into a glass and top with 2oz of prosecco.',
      user_id=4
    )
    Orangeade = Recipe(
      name='Orangeade',
      description=None,
      instructions='Place some ice cubes in a large tumbler or highball glass, add lemon juice, orange juice, sugar syrup, and stir well. Top up with cold soda water, serve with a drinking straw.',
      user_id=4
    )
    OrangeWhip = Recipe(
      name='Orange Whip',
      description=None,
      instructions='Pour ingredients over ice and stir.',
      user_id=4
    )
    OrangeCrush = Recipe(
      name='Orange Crush',
      description=None,
      instructions='Add all ingredients to tumbler-Pour as shot',
      user_id=4
    )
    OrangeOasis = Recipe(
      name='Orange Oasis',
      description=None,
      instructions='Shake brandy, gin, and orange juice with ice and strain into a highball glass over ice cubes. Fill with ginger ale, stir, and serve.',
      user_id=3
    )
    OldFashioned = Recipe(
      name='Old Fashioned',
      description=None,
      instructions='Place sugar cube in old fashioned glass and saturate with bitters, add a dash of plain water. Muddle until dissolved. Fill the glass with ice cubes and add whiskey. Garnish with orange twist, and a cocktail cherry.',
      user_id=1
    )
    OreoMudslide = Recipe(
      name='Oreo Mudslide',
      description=None,
      instructions='Blend Vodka, Kahlua, Bailey\'s, ice-cream and the Oreo well in a blender. Pour into a large frosted glass. Garnish with whipped cream and a cherry.',
      user_id=1
    )
    OatmealCookie = Recipe(
      name='Oatmeal Cookie',
      description=None,
      instructions='Just mix it all together. It\'s meant to be a shot, but it works just fine as a proper adult-sized drink over lots of ice. Tastes like an oatmeal cookie.',
      user_id=1
    )
    OrangePushup = Recipe(
      name='Orange Push-up',
      description=None,
      instructions='Combine liquors in a blender. Add a half scoop of ice and blend. Garnish with an orange and cherry flag. So good it will melt in your mouth!!!',
      user_id=2
    )
    OrangeRosemaryCollins = Recipe(
      name='Orange Rosemary Collins',
      description=None,
      instructions='Add the spirits to the bottom of the glass and top equally with the mixer drinks. Garnish with orange slices inside the glass as well as some rosemary on top.',
      user_id=1
    )
    OrangeScentedHotChocolate = Recipe(
      name='Orange Scented Hot Chocolate',
      description=None,
      instructions='Combine all ingredients in heavy medium saucepan. Stir over low heat until chocolate melts. Increase heat and bring just to a boil, stirring often. Remove from heat and whisk untily frothy. Return to heat and bring to boil again. Remove from heat, whisk until frothy. Repeat heating and whisking once again. Discard orange peel. (Can be prepared 2 hours ahead. Let stand at room temperature. Before serving, bring just to boil, remove from heat and whisk until frothy.) Pour hot chocolate into coffee mugs. Makes 2 servings.',
      user_id=4
    )
    OwensGrandmothersRevenge = Recipe(
      name='Owen\'s Grandmother\'s Revenge',
      description=None,
      instructions='Add ingredients and mix in blender.',
      user_id=2
    )
    Paloma = Recipe(
      name='Paloma',
      description=None,
      instructions='Stir together and serve over ice.',
      user_id=3
    )
    Paradise = Recipe(
      name='Paradise',
      description=None,
      instructions='Shake together over ice. Strain into cocktail glass and serve chilled.',
      user_id=4
    )
    PinkGin = Recipe(
      name='Pink Gin',
      description=None,
      instructions='Pour the bitters into a wine glass. Swirl the glass to coat the inside with the bitters, shake out the excess. Pour the gin into the glass. Do not add ice.',
      user_id=2
    )
    PeguClub = Recipe(
      name='Pegu Club',
      description=None,
      instructions='Shake, strain, up, cocktail glass',
      user_id=3
    )
    PinkLady = Recipe(
      name='Pink Lady',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=4
    )
    PinkMoon = Recipe(
      name='Pink Moon',
      description=None,
      instructions='Slowly shake in a shaker with ice, strain into a square whiskey glass. Top with fresh ice. Add the blackberries to garnish. Add flowers and a green leaf for a special look!',
      user_id=4
    )
    Penicillin = Recipe(
      name='Penicillin',
      description=None,
      instructions='Shake blended Scotch, lemon juice, honey syrup and ginger syrup with ice. Strain over large ice in chilled rocks glass. Float smoky Scotch on top (be sure to use a smoky Scotch such as an Islay single malt). Garnish with candied ginger.',
      user_id=2
    )
    PiscoSour = Recipe(
      name='Pisco Sour',
      description=None,
      instructions='Vigorously shake and strain contents in a cocktail shaker with ice cubes, then pour into glass and garnish with bitters.',
      user_id=3
    )
    Portoflip = Recipe(
      name='Porto flip',
      description=None,
      instructions='Shake ingredients together in a mixer with ice. Strain into glass, garnish and serve.',
      user_id=4
    )
    PinaColada = Recipe(
      name='Pina Colada',
      description=None,
      instructions='Mix with crushed ice in blender until smooth. Pour into chilled glass, garnish and serve.',
      user_id=1
    )
    PinkPenocha = Recipe(
      name='Pink Penocha',
      description=None,
      instructions='mix all ingredients into bowl keep iced stir frequently',
      user_id=3
    )
    PurePassion = Recipe(
      name='Pure Passion',
      description=None,
      instructions='Mix up all ingredients with a cocktail stirrer and serve with crushed ice with mint and edible flour if available.',
      user_id=3
    )
    Poppedcherry = Recipe(
      name='Popped cherry',
      description=None,
      instructions='Served over ice in a tall glass with a popped cherry (can add more popped cherries if in the mood)!',
      user_id=4
    )
    PoppyCocktail = Recipe(
      name='Poppy Cocktail',
      description=None,
      instructions='Shake ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=4
    )
    PortWineFlip = Recipe(
      name='Port Wine Flip',
      description=None,
      instructions='Shake all ingredients (except nutmeg) with ice and strain into a whiskey sour glass. Sprinkle nutmeg on top and serve.',
      user_id=2
    )
    PlantersPunch = Recipe(
      name='Planter\'s Punch',
      description=None,
      instructions='Pour all ingredients, except the bitters, into shaker filled with ice. Shake well. Pour into large glass, filled with ice. Add Angostura bitters, "on top". Garnish with cocktail cherry and pineapple.',
      user_id=3
    )
    PineapplePaloma = Recipe(
      name='Pineapple Paloma',
      description=None,
      instructions='Rub the rim of each glass with lime slice and dip into salt. Add ice, tequila, grapefruit juice, lime juice and top with pineapple soda. Give it a quick stir. Garnish with fresh pineapple or lime.',
      user_id=3
    )
    PornstarMartini = Recipe(
      name='Pornstar Martini',
      description=None,
      instructions='Straight: Pour all ingredients into mixing glass with ice cubes. Shake well. Strain in chilled martini cocktail glass. Cut passion fruit in half and use as garnish. Pour prosecco into a chilled shot glass and serve alongside the martini.',
      user_id=2
    )
    PlantersPunch = Recipe(
      name='Planter\'s Punch',
      description=None,
      instructions='Squeeze an orange and strain the juice. Put all the ingredients in a shaker filled with ice and shake for at least 12 seconds. Strain into a highball glass and decorate with a pineapple wedge or fruit of your choice.',
      user_id=2
    )
    PortAndStarboard = Recipe(
      name='Port And Starboard',
      description=None,
      instructions='Pour carefully into a pousse-cafe glass, so that creme de menthe floats on grenadine. Serve without mixing.',
      user_id=1
    )
    PortWineCocktail = Recipe(
      name='Port Wine Cocktail',
      description=None,
      instructions='Stir ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=1
    )
    PyschVitaminLight = Recipe(
      name='Pysch Vitamin Light',
      description=None,
      instructions='Shake with ice.',
      user_id=3
    )
    PinkPantyPulldowns = Recipe(
      name='Pink Panty Pulldowns',
      description=None,
      instructions='Shake well',
      user_id=3
    )
    PassionFruitMartini = Recipe(
      name='Passion Fruit Martini',
      description=None,
      instructions='Pour all ingredients into a glass and stir. Garnish with half a passion fruit piece.',
      user_id=4
    )
    PineappleGingeraleSmoothie = Recipe(
      name='Pineapple Gingerale Smoothie',
      description=None,
      instructions='Throw everything into a blender and liquify.',
      user_id=3
    )
    Quentin = Recipe(
      name='Quentin',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the rum, Kahlua, and cream. Shake well. Strain into a cocktail glass and garnish with the nutmeg.',
      user_id=2
    )
    QueenBee = Recipe(
      name='Queen Bee',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=1
    )
    QuickFK = Recipe(
      name='Quick F**K',
      description=None,
      instructions='In a shot glass add 1/3 Kahlua first. Then 1/3 Miduri, topping it off with a 1/3 bailey\'s irish cream',
      user_id=3
    )
    Quicksand = Recipe(
      name='Quick-sand',
      description=None,
      instructions='Simply add the orange juice, quite a quick pour in order to mix the sambucca with the orange juice. The juice MUST have fruit pulp!',
      user_id=1
    )
    QueenCharlotte = Recipe(
      name='Queen Charlotte',
      description=None,
      instructions='Pour red wine and grenadine into a collins glass over ice cubes. Fill with lemon-lime soda, stir, and serve.',
      user_id=1
    )
    QueenElizabeth = Recipe(
      name='Queen Elizabeth',
      description=None,
      instructions='Stir all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=4
    )
    QuakersCocktail = Recipe(
      name='Quaker\'s Cocktail',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=2
    )
    QuarterDeckCocktail = Recipe(
      name='Quarter Deck Cocktail',
      description=None,
      instructions='Stir all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=1
    )
    Rose = Recipe(
      name='Rose',
      description=None,
      instructions='Shake together in a cocktail shaker, then strain into chilled glass. Garnish and serve.',
      user_id=2
    )
    Radler = Recipe(
      name='Radler',
      description=None,
      instructions='Pour beer into large mug, slowly add the 7-up (or Sprite).',
      user_id=3
    )
    RumSour = Recipe(
      name='Rum Sour',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the rum, lemon juice, and sugar. Shake well. Strain into a sour glass and garnish with the orange slice and the cherry.',
      user_id=2
    )
    RumPunch = Recipe(
      name='Rum Punch',
      description=None,
      instructions='Mix all ingredients in a punch bowl and serve.',
      user_id=4
    )
    RumToddy = Recipe(
      name='Rum Toddy',
      description=None,
      instructions='Dissolve powdered sugar in water in an old-fashioned glass. Add rum and one ice cube and stir. Add the twist of lemon peel and serve.',
      user_id=4
    )
    RoyalFizz = Recipe(
      name='Royal Fizz',
      description=None,
      instructions='Shake all ingredients (except cola) with ice and strain into a chilled collins glass. Fill with cola and serve.',
      user_id=2
    )
    RumCooler = Recipe(
      name='Rum Cooler',
      description=None,
      instructions='Pour the rum and soda into a collins glass almost filled with ice cubes. Stir well and garnish with the lemon wedge.',
      user_id=4
    )
    RumRunner = Recipe(
      name='Rum Runner',
      description=None,
      instructions='Mix all ingredients in glass & add ice.',
      user_id=2
    )
    RustyNail = Recipe(
      name='Rusty Nail',
      description=None,
      instructions='Pour the Scotch and Drambuie into an old-fashioned glass almost filled with ice cubes. Stir well. Garnish with the lemon twist.',
      user_id=4
    )
    RedSnapper = Recipe(
      name='Red Snapper',
      description=None,
      instructions='One shot each, shake n shoot',
      user_id=3
    )
    RoyalBitch = Recipe(
      name='Royal Bitch',
      description=None,
      instructions='Into a shot glass layer the Crown Royal on top of the Frangelico.',
      user_id=3
    )
    RoyalFlush = Recipe(
      name='Royal Flush',
      description=None,
      instructions='Pour all the ingredients into tumbler over ice. Strain into glass.',
      user_id=4
    )
    RumCobbler = Recipe(
      name='Rum Cobbler',
      description=None,
      instructions='In an old-fashioned glass, dissolve the sugar in the club soda. Add crushed ice until the glass is almost full. Add the rum. Stir well. Garnish with the cherry and the orange and lemon slices.',
      user_id=4
    )
    RubyTuesday = Recipe(
      name='Ruby Tuesday',
      description=None,
      instructions='Pour gin and cranberry into a highball filled with ice cubes. Add grenadine and stir.',
      user_id=4
    )
    RailSplitter = Recipe(
      name='Rail Splitter',
      description=None,
      instructions='Mix sugar syrup with lemon juice in a tall glass. Fill up with ginger ale.',
      user_id=2
    )
    RosemaryBlue = Recipe(
      name='Rosemary Blue',
      description=None,
      instructions='1) Add the Bombay Sapphire, Blue Curacao, rosemary sprig and gently squeezed lemon wedge to a balloon glass. Swirl well to combine. 2) Fill with cubed ice and top with the Fever-Tree Light Tonic Water. 3) Gently fold with a bar spoon to mix.',
      user_id=3
    )
    RamosGinFizz = Recipe(
      name='Ramos Gin Fizz',
      description=None,
      instructions='Prepare all the ingredients on the counter to be able to work well and quickly, especially the cream and egg white. Pour all the ingredients into a shaker. Shake vigorously for 1 minute: cream and egg white must be mixed perfectly, so don\'t rush. Now open the shaker and put some ice and shake for 1-2 minutes. It depends on how long you can resist! Pour into a highball glass, add a splash of soda and garnish to taste. Ramos Gin Fizz was once drunk as an invigorating drink or even as a breakfast, try it as an aperitif and after dinner and you will discover a little gem now lost.',
      user_id=3
    )
    RoyalGinFizz = Recipe(
      name='Royal Gin Fizz',
      description=None,
      instructions='Shake all ingredients (except carbonated water) with ice and strain into a highball glass over two ice cubes. Fill with carbonated water, stir, and serve.',
      user_id=3
    )
    RumMilkPunch = Recipe(
      name='Rum Milk Punch',
      description=None,
      instructions='Shake all ingredients (except nutmeg) with ice and strain into a collins glass. Sprinkle nutmeg on top and serve.',
      user_id=3
    )
    RaspberryJulep = Recipe(
      name='Raspberry Julep',
      description=None,
      instructions='Softly muddle the mint leaves and raspberry syrup in the bottom of the cup. Add crushed ice and Bourbon to the cup and then stir. Top with more ice, garnish with a mint sprig.',
      user_id=3
    )
    RumScrewdriver = Recipe(
      name='Rum Screwdriver',
      description=None,
      instructions='Pour rum into a highball glass over ice cubes. Add orange juice, stir, and serve.',
      user_id=4
    )
    RaspberryCooler = Recipe(
      name='Raspberry Cooler',
      description=None,
      instructions='Pour the raspberry vodka and soda into a highball glass almost filled with ice cubes. Stir well.',
      user_id=4
    )
    RumOldfashioned = Recipe(
      name='Rum Old-fashioned',
      description=None,
      instructions='Stir powdered sugar, water, and bitters in an old-fashioned glass. When sugar has dissolved add ice cubes and light rum. Add the twist of lime peel, float 151 proof rum on top, and serve.',
      user_id=1
    )
    RussianSpringPunch = Recipe(
      name='Russian Spring Punch',
      description=None,
      instructions='Pour the ingredients into an highball glass, top with Sparkling wine.',
      user_id=2
    )
    RadioactiveLongIslandIcedTea = Recipe(
      name='Radioactive Long Island Iced Tea',
      description=None,
      instructions='Pour all ingredients over ice in a very tall glass. Sip cautiously.',
      user_id=4
    )
    Smut = Recipe(
      name='Smut',
      description=None,
      instructions='Throw it all together and serve real cold.',
      user_id=1
    )
    Spritz = Recipe(
      name='Spritz',
      description=None,
      instructions='Build into glass over ice, garnish and serve.',
      user_id=3
    )
    Scooter = Recipe(
      name='Scooter',
      description=None,
      instructions='Shake all ingredients well with cracked ice, strain into a cocktail glass, and serve.',
      user_id=3
    )
    Sangria = Recipe(
      name='Sangria',
      description=None,
      instructions='Mix all together in a pitcher and refrigerate. Add cloves and cinnamon sticks to taste. Serve in wine glasses.',
      user_id=2
    )
    Stinger = Recipe(
      name='Stinger',
      description=None,
      instructions='Pour in a mixing glass with ice, stir and strain into a cocktail glass. May also be served on rocks in a rocks glass.',
      user_id=4
    )
    Sazerac = Recipe(
      name='Sazerac',
      description=None,
      instructions='Rinse a chilled old-fashioned glass with the absinthe, add crushed ice, and set it aside. Stir the remaining ingredients over ice and set it aside. Discard the ice and any excess absinthe from the prepared glass, and strain the drink into the glass. Add the lemon peel for garnish.',
      user_id=2
    )
    Sidecar = Recipe(
      name='Sidecar',
      description=None,
      instructions='Pour all ingredients into cocktail shaker filled with ice. Shake well and strain into cocktail glass.',
      user_id=2
    )
    Snowday = Recipe(
      name='Snowday',
      description=None,
      instructions='Stir all ingredients with ice. Strain into a chilled rocks glass over fresh ice. Express orange peel over drink and garnish.',
      user_id=4
    )
    Spice75 = Recipe(
      name='Spice 75',
      description=None,
      instructions='Gently warm 60g golden caster sugar in a pan with 30ml water and 1 tbsp allspice. Cook gently until the sugar has dissolved, then leave the mixture to cool. Strain through a sieve lined with a coffee filter (or a double layer of kitchen paper). Pour 60ml of the spiced syrup into a cocktail shaker along with 200ml rum and 90ml lime juice. Shake with ice and strain between six flute glasses. Top up with 600ml champagne and garnish each with an orange twist.',
      user_id=3
    )
    Snowball = Recipe(
      name='Snowball',
      description=None,
      instructions='Place one ice cube in the glass and add 1 1/2 oz of Advocaat. Fill up the glass with lemonade and decorate with a slice of lemon. Serve at once.',
      user_id=4
    )
    Shotgun = Recipe(
      name='Shot-gun',
      description=None,
      instructions='Pour one part Jack Daneils and one part Jim Beam into shot glass then float Wild Turkey on top.',
      user_id=3
    )
    SaltyDog = Recipe(
      name='Salty Dog',
      description=None,
      instructions='Pour all ingredients over ice cubes in a highball glass. Stir well and serve. (Vodka may be substituted for gin, if preferred.)',
      user_id=3
    )
    StoneSour = Recipe(
      name='Stone Sour',
      description=None,
      instructions='Shake all ingredients with ice, strain into a chilled whiskey sour glass, and serve.',
      user_id=4
    )
    Seabreeze = Recipe(
      name='Sea breeze',
      description=None,
      instructions='Build all ingredients in a highball glass filled with ice. Garnish with lime wedge.',
      user_id=3
    )
    ScotchSour = Recipe(
      name='Scotch Sour',
      description=None,
      instructions='Shake scotch, juice of lime, and powdered sugar with ice and strain into a whiskey sour glass. Decorate with 1/2 slice lemon, top with the cherry, and serve.',
      user_id=3
    )
    SweetTooth = Recipe(
      name='Sweet Tooth',
      description=None,
      instructions='Put 2 shots Godiva Liquour into a glass, add as much or as little milk as you would like.',
      user_id=2
    )
    Screwdriver = Recipe(
      name='Screwdriver',
      description=None,
      instructions='Mix in a highball glass with ice. Garnish and serve.',
      user_id=1
    )
    SherryFlip = Recipe(
      name='Sherry Flip',
      description=None,
      instructions='Shake all ingredients (except nutmeg) with ice and strain into a whiskey sour glass. Sprinkle nutmeg on top and serve.',
      user_id=2
    )
    SolYSombra = Recipe(
      name='Sol Y Sombra',
      description=None,
      instructions='Shake ingredients with ice, strain into a brandy snifter, and serve. (The English translation of the name of this drink is "Sun and Shade", and after sampling this drink, you\'ll understand why. Thanks, Kirby.)',
      user_id=4
    )
    SharkAttack = Recipe(
      name='Shark Attack',
      description=None,
      instructions='Mix lemonade and water according to instructions on back of can. If the instructions say to add 4 1/3 cans of water do so. Mix into pitcher. Add 1 1/2 cup of Vodka (Absolut). Mix well. Pour into glass of crushed ice. Excellent!',
      user_id=3
    )
    SanFrancisco = Recipe(
      name='San Francisco',
      description=None,
      instructions='Take a tall glass and put in a few ice cubes, fill the vodka over it and fill with juice then the "creme", to end fill in the grenadine but very carefully at the side of the glass so it will lay down in the bottom. garnish with orange and strawberry.',
      user_id=4
    )
    SpaceOdyssey = Recipe(
      name='Space Odyssey',
      description=None,
      instructions='Fill glass with ice and add shots of Bacardi and Malibu. Add splash of pineapple juice and top with orange juice. Add grenadine for color and garnish with cherries.',
      user_id=3
    )
    SherryEggnog = Recipe(
      name='Sherry Eggnog',
      description=None,
      instructions='Shake sherry, powdered sugar, and egg with ice and strain into a collins glass. Fill with milk and stir. Sprinkle nutmeg on top and serve.',
      user_id=1
    )
    SweetBananas = Recipe(
      name='Sweet Bananas',
      description=None,
      instructions='Place all ingredients in the blender jar - cover and whiz on medium speed until well blended. Pour in one tall, 2 medium or 3 small glasses and drink up.',
      user_id=3
    )
    SweetSangria = Recipe(
      name='Sweet Sangria',
      description=None,
      instructions='Dissolve the sugar in hot water and cool. Peel the citrus fruits and break into wedges. Mix the wine, sugar syrup, fruit, and Fresca in a pitcher and put in the fridge for a few hours. Serve in tall glasses with a straw.',
      user_id=3
    )
    ScotchCobbler = Recipe(
      name='Scotch Cobbler',
      description=None,
      instructions='Pour scotch, brandy, and curacao over ice in an old-fashioned glass. Add the orange slice, top with the mint sprig, and serve.',
      user_id=2
    )
    SwedishCoffee = Recipe(
      name='Swedish Coffee',
      description=None,
      instructions='Pour the coffee in an ordinary coffee cup. Add the aquavit. Add sugar by taste. Stir and have a nice evening (morning)',
      user_id=4
    )
    SingaporeSling = Recipe(
      name='Singapore Sling',
      description=None,
      instructions='Pour all ingredients into cocktail shaker filled with ice cubes. Shake well. Strain into highball glass. Garnish with pineapple and cocktail cherry.',
      user_id=4
    )
    SlipperyNipple = Recipe(
      name='Slippery Nipple',
      description=None,
      instructions='Pour the Sambuca into a shot glass, then pour the Irish Cream on top so that the two liquids do not mix.',
      user_id=2
    )
    SnakeBiteUK = Recipe(
      name='Snake Bite (UK)',
      description=None,
      instructions='Pour ingredients into a pint glass. Drink. Fall over.',
      user_id=2
    )
    ScreamingOrgasm = Recipe(
      name='Screaming Orgasm',
      description=None,
      instructions='Pour first vodka, then Bailey\'s, then Kahlua into a cocktail glass over crushed ice. Stir. Caution: use only high quality vodka. Cheap vodka can cause the Bailey\'s to curdle. Test your brand of vodka by mixing 1 Tsp each of vodka and Bailey\'s first.',
      user_id=3
    )
    SexontheBeach = Recipe(
      name='Sex on the Beach',
      description=None,
      instructions='Build all ingredients in a highball glass filled with ice. Garnish with orange slice.',
      user_id=1
    )
    SidecarCocktail = Recipe(
      name='Sidecar Cocktail',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=3
    )
    SpritzVeneziano = Recipe(
      name='Spritz Veneziano',
      description=None,
      instructions='Build into glass over ice, garnish and serve.',
      user_id=3
    )
    SloeGinCocktail = Recipe(
      name='Sloe Gin Cocktail',
      description=None,
      instructions='Stir all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=2
    )
    Spanishchocolate = Recipe(
      name='Spanish chocolate',
      description=None,
      instructions='Stir the milk with the chocolate and the cinnamon over low heat until the chocolate dissolves. Add the eggs and beat the mixture until it becomes thick, taking care not to boil. Serve in coffee mug.',
      user_id=1
    )
    SangriaTheBest = Recipe(
      name='Sangria The  Best',
      description=None,
      instructions='Mix wine, sugar and fruit, and let sit in the fridge for 18-24 hours. The mixture will have a somewhat syrupy consistency. Before serving stir in brandy and cut the mixture with soda water until it have a thinner, more wine like consistency. Serve from a pitcher in wine glasses.',
      user_id=1
    )
    ShanghaiCocktail = Recipe(
      name='Shanghai Cocktail',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=4
    )
    SpicedPeachPunch = Recipe(
      name='Spiced Peach Punch',
      description=None,
      instructions='Combine peach nectar, orange juice and brown sugar in a large saucepan. Tie cinnamon and cloves in a small cheesecloth bag. Drop into saucepan. Heat slowly, stirring constantly, until sugar dissolves. Simmer 10 minutes. Stir in lime juice. Serve in hot mugs.',
      user_id=1
    )
    StrawberryShivers = Recipe(
      name='Strawberry Shivers',
      description=None,
      instructions='Place all ingredients in the blender jar - cover and whiz on medium speed until well blended. Pour in one tall, 2 medium or 3 small glasses and drink up.',
      user_id=3
    )
    StrawberryDaiquiri = Recipe(
      name='Strawberry Daiquiri',
      description=None,
      instructions='Pour all ingredients into shaker with ice cubes. Shake well. Strain in chilled cocktail glass.',
      user_id=2
    )
    StrawberryLemonade = Recipe(
      name='Strawberry Lemonade',
      description=None,
      instructions='Throw everything into a blender and mix until fairly smooth. Serve over ice.',
      user_id=4
    )
    SnakebiteandBlack = Recipe(
      name='Snakebite and Black',
      description=None,
      instructions='Put blackcurrant squash in first up to about 1cm in glass. Then add the lager and cider one after another.',
      user_id=3
    )
    SunnyHolidayPunch = Recipe(
      name='Sunny Holiday Punch',
      description=None,
      instructions='Combine all ingredients in a punch bowl.',
      user_id=1
    )
    SurfCityLifesaver = Recipe(
      name='Surf City Lifesaver',
      description=None,
      instructions='Lots of ice and soda top up in tall glass with cherry and a grin.',
      user_id=3
    )
    StrawberryMargarita = Recipe(
      name='Strawberry Margarita',
      description=None,
      instructions='Rub rim of cocktail glass with lemon juice and dip rim in salt. Shake schnapps, tequila, triple sec, lemon juice, and strawberries with ice, strain into the salt-rimmed glass, and serve.',
      user_id=1
    )
    SaltedToffeeMartini = Recipe(
      name='Salted Toffee Martini',
      description=None,
      instructions='Add ice, toffee gin, chocolate liqueur and Amaretto to a cocktail shaker and shake vigorously. Pour the chocolate syrup into a saucer and dip the top of a martini glass into the sauce. Grate some of the Willie\'s sea salt chocolate into another saucer and dip the coated glass, so the flakes stick to the sauce, creating a chocolate rim! Pour the contents of the shaker into your chocolatey glass and sprinkle with more grated chocolate - enjoy!  ',
      user_id=2
    )
    ScottishHighlandLiqueur = Recipe(
      name='Scottish Highland Liqueur',
      description=None,
      instructions='Combine all ingreds in aging container. Cover tightly and shake gently several times during the first 24 hrs. After 24 hrs, remove the lemon zest. Cover again and let stand in a cool, dark place for 2 weeks, shaking gently every other day. Strain through a wire sieve to remove the angelica root and fennel. Return to aging container, cover and let stand undisturbed in a cool dark place for 6 months. Siphon or pour clear liqueur into a sterile bottle. The cloudy dregs may be saved for cooking.',
      user_id=3
    )
    SmashedWatermelonMargarita = Recipe(
      name='Smashed Watermelon Margarita',
      description=None,
      instructions='In a mason jar muddle the watermelon and 5 mint leaves together into a puree and strain. Next add the grapefruit juice, juice of half a lime and the tequila as well as some ice. Put a lid on the jar and shake. Pour into a glass and add more ice. Garnish with fresh mint and a small slice of watermelon.',
      user_id=2
    )
    Thriller = Recipe(
      name='Thriller',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine all of the ingredients. Shake well. Strain into a cocktail glass.',
      user_id=4
    )
    TheGalah = Recipe(
      name='The Galah',
      description=None,
      instructions='Mix together the alcoholic portions and top with Pineapple and Lime juice.',
      user_id=2
    )
    TiaMaria = Recipe(
      name='Tia-Maria',
      description=None,
      instructions='Boil water, sugar and coffe for 10 mins and let cool. Add rum and vanilla. Put in clean bottle(s) and leave for 1 week before using.',
      user_id=1
    )
    Tipperary = Recipe(
      name='Tipperary',
      description=None,
      instructions='Stir over ice. Strain into chilled glass. Cut a wide swath of orange peel, and express the orange oils over the drink. Discard orange twist.',
      user_id=3
    )
    Turkeyball = Recipe(
      name='Turkeyball',
      description=None,
      instructions='Shake with ice and strain into a shot glass.',
      user_id=1
    )
    TexasSling = Recipe(
      name='Texas Sling',
      description=None,
      instructions='Blend with Ice until smooth. Serve in a tulip glass, top with whip cream.',
      user_id=3
    )
    ThaiCoffee = Recipe(
      name='Thai Coffee',
      description=None,
      instructions='Place the coffee and spices in the filter cone of your coffee maker. Brew coffee as usual, let it cool. In a tall glass, dissolve 1 or 2 teaspoons of sugar in an ounce of the coffee (it\'s easier to dissolve than if you put it right over ice). Add 5-6 ice cubes and pour coffee to within about 1 inch of the top of the glass. Rest a spoon on top of the coffee and slowly pour whipping cream into the spoon. This will make the cream float on top of the coffee rather than dispersing into it right away.',
      user_id=3
    )
    TomCollins = Recipe(
      name='Tom Collins',
      description=None,
      instructions='In a shaker half-filled with ice cubes, combine the gin, lemon juice, and sugar. Shake well. Strain into a collins glass alomst filled with ice cubes. Add the club soda. Stir and garnish with the cherry and the orange slice.',
      user_id=1
    )
    TomatoTang = Recipe(
      name='Tomato Tang',
      description=None,
      instructions='Place all ingredients in the blender jar - cover and whiz on medium speed until well blended. Pour in one tall, 2 medium or 3 small glasses and drink up.',
      user_id=1
    )
    TalosCoffee = Recipe(
      name='Talos Coffee',
      description=None,
      instructions='Add your GM and then add your coffee.',
      user_id=2
    )
    TenneseeMud = Recipe(
      name='Tennesee Mud',
      description=None,
      instructions='Mix Coffee, Jack Daniels and Amaretto. Add Cream on top.',
      user_id=4
    )
    TequilaFizz = Recipe(
      name='Tequila Fizz',
      description=None,
      instructions='Shake all ingredients (except ginger ale) with ice and strain into a collins glass over ice cubes. Fill with ginger ale, stir, and serve.',
      user_id=1
    )
    TequilaSour = Recipe(
      name='Tequila Sour',
      description=None,
      instructions='Shake tequila, juice of lemon, and powdered sugar with ice and strain into a whiskey sour glass. Add the half-slice of lemon, top with the cherry, and serve.',
      user_id=3
    )
    ThaiIcedTea = Recipe(
      name='Thai Iced Tea',
      description=None,
      instructions='Combine Thai tea (i.e., the powder), boiling water, and sweetened condensed milk, stir until blended. Pour into 2 tall glasses filled with ice cubes. Garnish with mint leaves. Makes 2 servings.',
      user_id=4
    )
    TheLastWord = Recipe(
      name='The Last Word',
      description=None,
      instructions='Shake with ice and strain into a cocktail glass.',
      user_id=4
    )
    TurfCocktail = Recipe(
      name='Turf Cocktail',
      description=None,
      instructions='Stir all ingredients (except orange peel) with ice and strain into a cocktail glass. Add the twist of orange peel and serve.',
      user_id=4
    )
    TheLaverstoke = Recipe(
      name='The Laverstoke',
      description=None,
      instructions='1) Squeeze two lime wedges into a balloon glass then add the cordial, Bombay Sapphire and MARTINI Rosso Vermouth, swirl to mix. 2) Fully fill the glass with cubed ice and stir to chill. 3) Top with Fever-Tree Ginger Ale and gently stir again to combine. 4) Garnish with a snapped ginger slice and an awoken mint sprig.',
      user_id=3
    )
    TequilaSlammer = Recipe(
      name='Tequila Slammer',
      description=None,
      instructions='Mix carefully to avoid releasing the dissolved CO2.',
      user_id=2
    )
    TequilaSunrise = Recipe(
      name='Tequila Sunrise',
      description=None,
      instructions='Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.',
      user_id=4
    )
    ThePhilosopher = Recipe(
      name='The Philosopher',
      description=None,
      instructions='Add all the spirits in a shaker (best to use Hendricks gin) as well as the orange bitters and lemon juice. Strain into a Margarita glass, top with Prosecco.',
      user_id=1
    )
    TuxedoCocktail = Recipe(
      name='Tuxedo Cocktail',
      description=None,
      instructions='Stir all ingredients with ice and strain into a cocktail glass. Garnish with a cherry and a twist of lemon zest.',
      user_id=3
    )
    TequilaSurprise = Recipe(
      name='Tequila Surprise',
      description=None,
      instructions='Fill shot glass with Tequila. Add drops of Tobasco sauce.',
      user_id=3
    )
    ThaiIcedCoffee = Recipe(
      name='Thai Iced Coffee',
      description=None,
      instructions='Prepare a pot of coffee at a good European strength. In the ground coffee, add 2 or 3 freshly ground cardamom pods. Sweeten while hot, then cool quickly. Serve in highball glass over ice, with cream. To get the layered effect, place a spoon atop the coffee and pour the milk carefully into the spoon so that it floats on the top of the coffee.',
      user_id=4
    )
    TheJimmyConway = Recipe(
      name='The Jimmy Conway',
      description=None,
      instructions='Fill glass with ice Pour in The Irishman and Disaronno Fill to the top with Cranberry Juice Garnish with a slice of lemon...Enjoy!',
      user_id=2
    )
    TexasRattlesnake = Recipe(
      name='Texas Rattlesnake',
      description=None,
      instructions='Mix all ingredients and Shake well. Sweet at first, with a BITE at the end...',
      user_id=2
    )
    TommysMargarita = Recipe(
      name='Tommy\'s Margarita',
      description=None,
      instructions='Shake and strain into a chilled cocktail glass.',
      user_id=1
    )
    TheStrangeWeaver = Recipe(
      name='The Strange Weaver',
      description=None,
      instructions='Mix ingredients slowly in a glass with ice, garnish with orange slice',
      user_id=4
    )
    TheEvilBlueThing = Recipe(
      name='The Evil Blue Thing',
      description=None,
      instructions='Pour ingredients into glass, and drop in a blue whale! The blue whale isn\'t really necessary, but it makes the drink more "fun".',
      user_id=1
    )
    Vesper = Recipe(
      name='Vesper',
      description=None,
      instructions='Shake over ice until well chilled, then strain into a deep goblet and garnish with a thin slice of lemon peel.',
      user_id=4
    )
    Victor = Recipe(
      name='Victor',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=1
    )
    Vampiro = Recipe(
      name='Vampiro',
      description=None,
      instructions='Vampiros may be made in a tall glass or an old fashioned glass. Bartenders may first "rim" the glass with Kosher Salt, which is done by placing a layer of Kosher Salt on a chopping board, moistening the glass\' rim with lime juice or water, and then placing the upside down glass rim onto the Kosher Salt, so that the salt sticks to the moistened rim. The second step is to fill half the glass with ice and add one or two shooter glasses full of high quality Tequila. The next stage is to add the flavouring elements. This is done by squeezing a fresh lime into the glass, adding a few grains of salt, adding citrus-flavoured soda pop, until the glass is 4/5 full, and then adding spicy Viuda de Sanchez (or orange juice, lime juice and pico de gallo). The final step is to stir the ingredients so that the flavours are properly blended.',
      user_id=1
    )
    Vesuvio = Recipe(
      name='Vesuvio',
      description=None,
      instructions='Shake all ingredients with ice, strain into an old-fashioned glass over ice cubes, and serve.',
      user_id=4
    )
    Veteran = Recipe(
      name='Veteran',
      description=None,
      instructions='Pour the rum and cherry brandy into an old-fashioned glass almost filled with ice cubes. Stir well.',
      user_id=4
    )
    VanVleet = Recipe(
      name='Van Vleet',
      description=None,
      instructions='Shake all ingredients with ice, strain into an old-fashioned glass over ice cubes, and serve.',
      user_id=2
    )
    VodkaFizz = Recipe(
      name='Vodka Fizz',
      description=None,
      instructions='Blend all ingredients, save nutmeg. Pour into large white wine glass and sprinkle nutmeg on top.',
      user_id=2
    )
    VodkaLemon = Recipe(
      name='Vodka Lemon',
      description=None,
      instructions='The vodka lemon is prepared directly in a highball glass or in a large tumbler: put 6-7 ice cubes in the glass, pour the vodka, lemonade and mix with a bar spoon. Finally decorate with a slice of lemon and, if you prefer, add a few mint leaves. Your vodka lemon is ready to be served.',
      user_id=3
    )
    VodkaSlime = Recipe(
      name='Vodka Slime',
      description=None,
      instructions='Fill glass with ice. Add vodka, 7-up then finish with the lime juice.',
      user_id=4
    )
    VodkaTonic = Recipe(
      name='Vodka Tonic',
      description=None,
      instructions='Wash and cut 1 wedge and 1 slice of lime or lemon. Fill a tumbler with fresh ice. Pour the desired dose of vodka and top up with the tonic. Squeeze the lime wedge into the glass and decorate with the slice. That\'s all, very simple: it\'s just the recipe for happiness!',
      user_id=2
    )
    VodkaMartini = Recipe(
      name='Vodka Martini',
      description=None,
      instructions='Shake the vodka and vermouth together with a number of ice cubes, strain into a cocktail glass, add the olive and serve.',
      user_id=3
    )
    VodkaRussian = Recipe(
      name='Vodka Russian',
      description=None,
      instructions='Mix it as a ordinary drink .',
      user_id=1
    )
    VermouthCassis = Recipe(
      name='Vermouth Cassis',
      description=None,
      instructions='Stir vermouth and creme de cassis in a highball glass with ice cubes. Fill with carbonated water, stir again, and serve.',
      user_id=4
    )
    VictoryCollins = Recipe(
      name='Victory Collins',
      description=None,
      instructions='Shake all ingredients (except orange slice) with ice and strain into a collins glass over ice cubes. Add the slice of orange and serve.',
      user_id=4
    )
    VodkaAndTonic = Recipe(
      name='Vodka And Tonic',
      description=None,
      instructions='Pour vodka into a highball glass over ice cubes. Fill with tonic water, stir, and serve.',
      user_id=1
    )
    ValenciaCocktail = Recipe(
      name='Valencia Cocktail',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=2
    )
    WhiskyMac = Recipe(
      name='Whisky Mac',
      description=None,
      instructions='Pour both of the ingredients into a wine goblet with no ice.',
      user_id=3
    )
    WhiteLady = Recipe(
      name='White Lady',
      description=None,
      instructions='Add all ingredients into cocktail shaker filled with ice. Shake well and strain into large cocktail glass.',
      user_id=3
    )
    WinePunch = Recipe(
      name='Wine Punch',
      description=None,
      instructions='Combine all of the ingredients and pour over a block of ice.',
      user_id=2
    )
    WineCooler = Recipe(
      name='Wine Cooler',
      description=None,
      instructions='Mix wine and soft drink. Pour into glass. Add ice.',
      user_id=1
    )
    WinterRita = Recipe(
      name='Winter Rita',
      description=None,
      instructions='Salt rim. Combine all ingredients, shake with ice, and strain over fresh ice.',
      user_id=2
    )
    WhiskeySour = Recipe(
      name='Whiskey Sour',
      description=None,
      instructions='Shake with ice. Strain into chilled glass, garnish and serve. If served \'On the rocks\', strain ingredients into old-fashioned glass filled with ice.',
      user_id=4
    )
    WhiteRussian = Recipe(
      name='White Russian',
      description=None,
      instructions='Pour vodka and coffee liqueur over ice cubes in an old-fashioned glass. Fill with light cream and serve.',
      user_id=3
    )
    WinterPaloma = Recipe(
      name='Winter Paloma',
      description=None,
      instructions='Everyone\'s favourite Paloma gets a delicious Indian makeover. Tequila reposado infused with “Timur Pepper” which has citrusy & grapefruit notes and is grown at the foothills of Himalaya. It also produces a slightly numbing and tingling sensation on your lip when consumed. We have also spiced up the fresh grapefruit juice with the warming spice blend from Himalaya. The combination of all these interesting elements has allowed us to elevate your Paloma sipping experience.',
      user_id=2
    )
    WhiteWineSangria = Recipe(
      name='White Wine Sangria',
      description=None,
      instructions='Chop the Lemon, Lime and other fruits into large chunks. Fill the Pitcher with the white wine and mix in the Apple Brandy. Top to taste with soda water.',
      user_id=1
    )
    WhitecapMargarita = Recipe(
      name='Whitecap Margarita',
      description=None,
      instructions='Place all ingredients in a blender and blend until smooth. This makes one drink.',
      user_id=3
    )
    WaikikiBeachcomber = Recipe(
      name='Waikiki Beachcomber',
      description=None,
      instructions='Shake all ingredients with ice, strain into a cocktail glass, and serve.',
      user_id=1
    )
    YellowBird = Recipe(
      name='Yellow Bird',
      description=None,
      instructions='Shake and strain into a chilled cocktail glass',
      user_id=2
    )
    YoghurtCooler = Recipe(
      name='Yoghurt Cooler',
      description=None,
      instructions='Place all ingredients in the blender jar - cover and whiz on medium speed until well blended. Pour in one tall, 2 medium or 3 small glasses and drink up. Note: Use lots of ice in this one - great on hot days! To add ice: Remove the center of the cover while the blender is on - drop 3 or 4 ice cubs and blend until they\'re completely crushed.',
      user_id=4
    )
    Zorro = Recipe(
      name='Zorro',
      description=None,
      instructions='add all and pour black coffee and add whipped cream on top.',
      user_id=4
    )
    Zinger = Recipe(
      name='Zinger',
      description=None,
      instructions='Get a shot glass and pour in three shots of the schnapps. Do the same with the Surge Cola. Then down it like Scheetz would.',
      user_id=2
    )
    Zombie = Recipe(
      name='Zombie',
      description=None,
      instructions='Blend at high speed for no more than 5 seconds. Pour into a glass, add ice cubes to fill, then add the garnish. *Donn\'s mix: Bring 3 crushed cinnamon sticks, 1 cup of sugar and 1 cup of water to a boil, stirring until the sugar is dissolved. Simmer for 2 minutes, then remove from the heat and let sit for at least 2 hours before straining into a clean glass bottle. Then add 1 part of the syrup and 2 parts of fresh grapefruit juice together.',
      user_id=3
    )
    Zambeer = Recipe(
      name='Zambeer',
      description=None,
      instructions='Mix sambuca with rootbeer and stir. Add ice',
      user_id=4
    )
    Zorbatini = Recipe(
      name='Zorbatini',
      description=None,
      instructions='Prepare like a Martini. Garnish with a green olive.',
      user_id=4
    )
    Zenmeister = Recipe(
      name='Zenmeister',
      description=None,
      instructions='Mix together and enjoy',
      user_id=3
    )
    Zipperhead = Recipe(
      name='Zipperhead',
      description=None,
      instructions='Fill glass with rocks, add straw before putting in liquor. Then add the ingredients in order, trying to keep layered as much as possible (i.e. Chambord on bottom, then Vodka, Then soda on top).',
      user_id=3
    )
    ZimaBlaster = Recipe(
      name='Zima Blaster',
      description=None,
      instructions='Fill glass with ice. Pour in Chambord, then fill with Zima. Mix and enjoy.',
      user_id=2
    )
    ZiziCoincoin = Recipe(
      name='Zizi Coin-coin',
      description=None,
      instructions='Pour 5cl of Cointreau on ice, add 2cl of fresh lemon (or lime) juice, stir gently, and finally add slices of lemon/lime in glass.',
      user_id=1
    )
    ZimadoriZinger = Recipe(
      name='Zimadori Zinger',
      description=None,
      instructions='Pour Zima in a collins glass over ice and then pour the shot of Midori. Don\'t stir. Garnish with a cherry.',
      user_id=3
    )
    ZippysRevenge = Recipe(
      name='Zippy\'s Revenge',
      description=None,
      instructions='Mix Kool-Aid to taste then add Rum and ammaretto. shake well to disolve the sugar in the Kool-Aid... serve cold',
      user_id=4
    )
    ZiemesMartiniApfelsaft = Recipe(
      name='Ziemes Martini Apfelsaft',
      description=None,
      instructions='Serve without ice. At least the juice shold have room temperature.',
      user_id=4
    )

    db.session.add(Aone)
    db.session.add(Abc)
    db.session.add(Ace)
    db.session.add(Acid)
    db.session.add(Adam)
    db.session.add(Att)
    db.session.add(Aj)
    db.session.add(Affair)
    db.session.add(Apello)
    db.session.add(Avalon)
    db.session.add(Abilene)
    db.session.add(Addison)
    db.session.add(Almeria)
    db.session.add(Acapulco)
    db.session.add(Affinity)
    db.session.add(Applecar)
    db.session.add(Aviation)
    db.session.add(AdamBomb)
    db.session.add(Addington)
    db.session.add(Aftersex)
    db.session.add(Afterglow)
    db.session.add(Afternoon)
    db.session.add(Alexander)
    db.session.add(Algonquin)
    db.session.add(Allegheny)
    db.session.add(Americano)
    db.session.add(Applejack)
    db.session.add(Artillery)
    db.session.add(Autodaf)
    db.session.add(Avalanche)
    db.session.add(AdamEve)
    db.session.add(AfterFive)
    db.session.add(AlmondJoy)
    db.session.add(AngelFace)
    db.session.add(Aquamarine)
    db.session.add(Archbishop)
    db.session.add(Absinthe2)
    db.session.add(AbsolutSex)
    db.session.add(ArcticFish)
    db.session.add(AztecPunch)
    db.session.add(AdamSunrise)
    db.session.add(AmarettoTea)
    db.session.add(AppleGrande)
    db.session.add(AppleKarate)
    db.session.add(ApricotLady)
    db.session.add(Armyspecial)
    db.session.add(AtlanticSun)
    db.session.add(AbbeyMartini)
    db.session.add(Amarettofizz)
    db.session.add(AmarettoMist)
    db.session.add(AmarettoRose)
    db.session.add(AmarettoSour)
    db.session.add(AperolSpritz)
    db.session.add(AppleSlammer)
    db.session.add(Apricotpunch)
    db.session.add(AriseMyLove)
    db.session.add(AtomicLokade)
    db.session.add(APieceofAss)
    db.session.add(AbbeyCocktail)
    db.session.add(AlfieCocktail)
    db.session.add(AliceCocktail)
    db.session.add(AmarettoShake)
    db.session.add(AppleHighball)
    db.session.add(AddisonSpecial)
    db.session.add(AdonisCocktail)
    db.session.add(AlabamaSlammer)
    db.session.add(AlaskaCocktail)
    db.session.add(AlliesCocktail)
    db.session.add(AmarettoSunset)
    db.session.add(ArizonaTwister)
    db.session.add(ArthurTompkins)
    db.session.add(ArtilleryPunch)
    db.session.add(ASplashofNash)
    db.session.add(AmarettoLiqueur)
    db.session.add(AmarettoStinger)
    db.session.add(AmarettoSunrise)
    db.session.add(AngelicaLiqueur)
    db.session.add(ArcticMouthwash)
    db.session.add(ArizonaStingers)
    db.session.add(AutumnGaribaldi)
    db.session.add(AbsolutEvergreen)
    db.session.add(Absolutlimousine)
    db.session.add(AbsolutStress2)
    db.session.add(AlohaFruitpunch)
    db.session.add(AppleCiderPunch)
    db.session.add(AuburnHeadbanger)
    db.session.add(ADayattheBeach)
    db.session.add(AFurlongTooLate)
    db.session.add(AbsolutSummertime)
    db.session.add(AmarettoAndCream)
    db.session.add(ArizonaAntifreeze)
    db.session.add(AGilligansIsland)
    db.session.add(AbsolutelyFabulous)
    db.session.add(AliceinWonderland)
    db.session.add(AmarettoStoneSour)
    db.session.add(ATrueAmarettoSour)
    db.session.add(AbsolutlyScrewedUp)
    db.session.add(AppleBerrySmoothie)
    db.session.add(AdiosAmigosCocktail)
    db.session.add(AfterDinnerCocktail)
    db.session.add(AfterSupperCocktail)
    db.session.add(AmarettoSweetSour)
    db.session.add(Amidsummernightdream)
    db.session.add(ApplePiewithACrust)
    db.session.add(ANightInOldMandalay)
    db.session.add(AlmondChocolateCoffee)
    db.session.add(ADMAfterDinnerMint)
    db.session.add(AbsolutelyCranberrySmash)
    db.session.add(AmarettoStoneSourAlternative)
    db.session.add(bfiftytwo)
    db.session.add(bfiftythree)
    db.session.add(Bijou)
    db.session.add(Boxcar)
    db.session.add(BigRed)
    db.session.add(Bellini)
    db.session.add(Bramble)
    db.session.add(Balmoral)
    db.session.add(Bluebird)
    db.session.add(Brooklyn)
    db.session.add(BoraBora)
    db.session.add(Boomerang)
    db.session.add(Barracuda)
    db.session.add(Brigadier)
    db.session.add(Broadside)
    db.session.add(Buccaneer)
    db.session.add(BrainFart)
    db.session.add(Blackthorn)
    db.session.add(BobMarley)
    db.session.add(BibleBelt)
    db.session.add(BubbleGum)
    db.session.add(BumbleBee)
    db.session.add(BabyEskimo)
    db.session.add(BostonSour)
    db.session.add(BahamaMama)
    db.session.add(Brainteaser)
    db.session.add(BloodyMary)
    db.session.add(BlackTan)
    db.session.add(BlueLagoon)
    db.session.add(BeesKnees)
    db.session.add(BrandyFlip)
    db.session.add(BrandySour)
    db.session.add(ButterBaby)
    db.session.add(Boulevardier)
    db.session.add(BourbonSour)
    db.session.add(BrucesPuce)
    db.session.add(BelgianBlue)
    db.session.add(BloodyPunch)
    db.session.add(BerryDeadly)
    db.session.add(BloodyMaria)
    db.session.add(BlindRussian)
    db.session.add(BlueMountain)
    db.session.add(BountyHunter)
    db.session.add(BombayCassis)
    db.session.add(BourbonSling)
    db.session.add(BruisedHeart)
    db.session.add(BlackRussian)
    db.session.add(BabyGuinness)
    db.session.add(BrandyCobbler)
    db.session.add(BlueHurricane)
    db.session.add(BostonSidecar)
    db.session.add(BlueMargarita)
    db.session.add(BananaCreamPi)
    db.session.add(BananaDaiquiri)
    db.session.add(BelliniMartini)
    db.session.add(BlackandBrown)
    db.session.add(BrandyAlexander)
    db.session.add(BacardiCocktail)
    db.session.add(BleedingSurgeon)
    db.session.add(BlueberryMojito)
    db.session.add(BermudaHighball)
    db.session.add(ButterflyEffect)
    db.session.add(BananaMilkShake)
    db.session.add(BraveBullShooter)
    db.session.add(BlackForestShake)
    db.session.add(BetweenTheSheets)
    db.session.add(BaileysDreamShake)
    db.session.add(BobbyBurnsCocktail)
    db.session.add(BananaStrawberryShake)
    db.session.add(BoozySnickersMilkshake)
    db.session.add(BananaCantaloupeSmoothie)
    db.session.add(BrandonandWillsCokeFloat)
    db.session.add(BananaStrawberryShakeDaiquiri)
    db.session.add(Casino)
    db.session.add(CafeSavoy)
    db.session.add(Caipirinha)
    db.session.add(CreamSoda)
    db.session.add(CubaLibra)
    db.session.add(CherryRum)
    db.session.add(CubaLibre)
    db.session.add(CornnOil)
    db.session.add(CitrusCoke)
    db.session.add(CasaBlanca)
    db.session.add(CloverClub)
    db.session.add(Caipirissima)
    db.session.add(CitySlicker)
    db.session.add(CampariBeer)
    db.session.add(ChicagoFizz)
    db.session.add(Cosmopolitan)
    db.session.add(CoffeeVodka)
    db.session.add(CasinoRoyale)
    db.session.add(CorpseReviver)
    db.session.add(ChocolateMilk)
    db.session.add(CloveCocktail)
    db.session.add(CoffeeLiqueur)
    db.session.add(CokeandDrops)
    db.session.add(ChocolateDrink)
    db.session.add(CranberryPunch)
    db.session.add(CremedeMenthe)
    db.session.add(ChocolateMonkey)
    db.session.add(CranberryCordial)
    db.session.add(ChocolateBeverage)
    db.session.add(ChampagneCocktail)
    db.session.add(CaliforniaLemonade)
    db.session.add(CaliforniaRootBeer)
    db.session.add(CaptainKiddsPunch)
    db.session.add(CosmopolitanMartini)
    db.session.add(CaribbeanBoilermaker)
    db.session.add(ClassicOldFashioned)
    db.session.add(ChocolateBlackRussian)
    db.session.add(CocktailHorsesNeck)
    db.session.add(CaribbeanOrangeLiqueur)
    db.session.add(CastillianHotChocolate)
    db.session.add(CherryElectricLemonade)
    db.session.add(Derby)
    db.session.add(Diesel)
    db.session.add(Daiquiri)
    db.session.add(Danbooka)
    db.session.add(Downshift)
    db.session.add(Dragonfly)
    db.session.add(DryMartini)
    db.session.add(DryRobRoy)
    db.session.add(DirtyNipple)
    db.session.add(DirtyMartini)
    db.session.add(DarkwoodSling)
    db.session.add(DarkandStormy)
    db.session.add(DarkCaipirinha)
    db.session.add(DuchampsPunch)
    db.session.add(Damnedifyoudo)
    db.session.add(DubonnetCocktail)
    db.session.add(DrinkingChocolate)
    db.session.add(DeathintheAfternoon)
    db.session.add(EggCream)
    db.session.add(EggNog4)
    db.session.add(EnglishHighball)
    db.session.add(EspressoMartini)
    db.session.add(EspressoRumtini)
    db.session.add(EggNogHealthy)
    db.session.add(EnglishRoseCocktail)
    db.session.add(ElderflowerCaipirinha)
    db.session.add(EggNogClassicCooked)
    db.session.add(EmpellnCocinasFatWashedMezcal)
    db.session.add(Fros)
    db.session.add(Frapp)
    db.session.add(FoxyLady)
    db.session.add(French75)
    db.session.add(FiggyThyme)
    db.session.add(FriscoSour)
    db.session.add(FruitShake)
    db.session.add(FruitCooler)
    db.session.add(FreddyKruger)
    db.session.add(FunkandSoul)
    db.session.add(FuzzyAsshole)
    db.session.add(FrenchMartini)
    db.session.add(FrenchNegroni)
    db.session.add(Fahrenheit5000)
    db.session.add(FlyingDutchman)
    db.session.add(FrozenDaiquiri)
    db.session.add(FruitFlipFlop)
    db.session.add(FlyingScotchman)
    db.session.add(FrenchConnection)
    db.session.add(FlamingDrPepper)
    db.session.add(FlamingLamborghini)
    db.session.add(FlandersFlakeOut)
    db.session.add(FrozenMintDaiquiri)
    db.session.add(FrozenPineappleDaiquiri)
    db.session.add(GG)
    db.session.add(Gimlet)
    db.session.add(Godchild)
    db.session.add(GinFizz)
    db.session.add(GinSour)
    db.session.add(Gagliardo)
    db.session.add(Godmother)
    db.session.add(Godfather)
    db.session.add(Gluehwein)
    db.session.add(GinTonic)
    db.session.add(GinToddy)
    db.session.add(GinSmash)
    db.session.add(GinDaisy)
    db.session.add(GinLemon)
    db.session.add(GinSling)
    db.session.add(Greyhound)
    db.session.add(GinRickey)
    db.session.add(GinSquirt)
    db.session.add(GrandBlue)
    db.session.add(GinCooler)
    db.session.add(GinSwizzle)
    db.session.add(GrassSkirt)
    db.session.add(Grasshopper)
    db.session.add(GrimReaper)
    db.session.add(GinandSoda)
    db.session.add(Goldendream)
    db.session.add(GreenGoblin)
    db.session.add(GrizzlyBear)
    db.session.add(GinAndTonic)
    db.session.add(GinBasilSmash)
    db.session.add(GentlemansClub)
    db.session.add(GirlFromIpanema)
    db.session.add(GaribaldiNegroni)
    db.session.add(GideonsGreenDinosaur)
    db.session.add(GrapelemonpineappleSmoothie)
    db.session.add(Hd)
    db.session.add(HoneyBee)
    db.session.add(HotToddy)
    db.session.add(Herbalflame)
    db.session.add(HorsesNeck)
    db.session.add(HappySkipper)
    db.session.add(HuntersMoon)
    db.session.add(HalloweenPunch)
    db.session.add(HavanaCocktail)
    db.session.add(HolloweenPunch)
    db.session.add(HomemadeKahlua)
    db.session.add(HotCreamyBush)
    db.session.add(HarveyWallbanger)
    db.session.add(HawaiianCocktail)
    db.session.add(HemingwaySpecial)
    db.session.add(HighlandFlingCocktail)
    db.session.add(HotChocolatetoDiefor)
    db.session.add(Ipamena)
    db.session.add(IcePick)
    db.session.add(IcedCoffee)
    db.session.add(IrishCream)
    db.session.add(IrishCoffee)
    db.session.add(IrishSpring)
    db.session.add(ImperialFizz)
    db.session.add(IrishRussian)
    db.session.add(ImperialCocktail)
    db.session.add(IcedCoffeeFillip)
    db.session.add(IrishCurdlingCow)
    db.session.add(JamDonut)
    db.session.add(Jitterbug)
    db.session.add(Jackhammer)
    db.session.add(JellyBean)
    db.session.add(Jelloshots)
    db.session.add(JamaicaKiss)
    db.session.add(JohnCollins)
    db.session.add(JapaneseFizz)
    db.session.add(JamaicanCoffee)
    db.session.add(JustaMoonmint)
    db.session.add(JewelOfTheNile)
    db.session.add(JackRoseCocktail)
    db.session.add(JacksVanillaCoke)
    db.session.add(Kir)
    db.session.add(Karsk)
    db.session.add(Kamikaze)
    db.session.add(KirRoyale)
    db.session.add(KiwiLemon)
    db.session.add(KurantTea)
    db.session.add(KiokiCoffee)
    db.session.add(KiwiMartini)
    db.session.add(KissmeQuick)
    db.session.add(KoolAidShot)
    db.session.add(KoolFirstAid)
    db.session.add(KentuckyBAndB)
    db.session.add(KentuckyColonel)
    db.session.add(KoolAidSlammer)
    db.session.add(KiwiPapayaSmoothie)
    db.session.add(KillthecoldSmoothie)
    db.session.add(Limeade)
    db.session.add(LunchBox)
    db.session.add(LemonDrop)
    db.session.add(LemonShot)
    db.session.add(Longvodka)
    db.session.add(LassiKhara)
    db.session.add(LassiRaita)
    db.session.add(Lemouroudji)
    db.session.add(LochLomond)
    db.session.add(LondonTown)
    db.session.add(LassiMango)
    db.session.add(LassiSweet)
    db.session.add(LimonaCorona)
    db.session.add(LordAndLady)
    db.session.add(LadyLoveFizz)
    db.session.add(LongIslandTea)
    db.session.add(LoneTreeCooler)
    db.session.add(LoneTreeCocktail)
    db.session.add(LazyCoconutPaloma)
    db.session.add(LongIslandIcedTea)
    db.session.add(LemonElderflowerSpritzer)
    db.session.add(LassiASouthIndianDrink)
    db.session.add(Melya)
    db.session.add(Mojito)
    db.session.add(Mimosa)
    db.session.add(MaiTai)
    db.session.add(Martini)
    db.session.add(Michelada)
    db.session.add(Manhattan)
    db.session.add(Margarita)
    db.session.add(Mauresque)
    db.session.add(MintJulep)
    db.session.add(Mudslinger)
    db.session.add(Martinez2)
    db.session.add(Moranguito)
    db.session.add(MiamiVice)
    db.session.add(MoscowMule)
    db.session.add(MulledWine)
    db.session.add(MasalaChai)
    db.session.add(MunichMule)
    db.session.add(MochaBerry)
    db.session.add(MangoMojito)
    db.session.add(MojitoExtra)
    db.session.add(MonkeyGland)
    db.session.add(MidnightMint)
    db.session.add(MaryPickford)
    db.session.add(MonkeyWrench)
    db.session.add(MothersMilk)
    db.session.add(MidnightManx)
    db.session.add(MalibuTwister)
    db.session.add(MidnightCowboy)
    db.session.add(MountainBramble)
    db.session.add(MartinezCocktail)
    db.session.add(MicrowaveHotCocoa)
    db.session.add(MangoOrangeSmoothie)
    db.session.add(MississippiPlantersPunch)
    db.session.add(Negroni)
    db.session.add(NewYorkSour)
    db.session.add(NuttyIrishman)
    db.session.add(NationalAquarium)
    db.session.add(NewYorkLemonade)
    db.session.add(NukedHotChocolate)
    db.session.add(Orgasm)
    db.session.add(OldPal)
    db.session.add(OldCuban)
    db.session.add(Orangeade)
    db.session.add(OrangeWhip)
    db.session.add(OrangeCrush)
    db.session.add(OrangeOasis)
    db.session.add(OldFashioned)
    db.session.add(OreoMudslide)
    db.session.add(OatmealCookie)
    db.session.add(OrangePushup)
    db.session.add(OrangeRosemaryCollins)
    db.session.add(OrangeScentedHotChocolate)
    db.session.add(OwensGrandmothersRevenge)
    db.session.add(Paloma)
    db.session.add(Paradise)
    db.session.add(PinkGin)
    db.session.add(PeguClub)
    db.session.add(PinkLady)
    db.session.add(PinkMoon)
    db.session.add(Penicillin)
    db.session.add(PiscoSour)
    db.session.add(Portoflip)
    db.session.add(PinaColada)
    db.session.add(PinkPenocha)
    db.session.add(PurePassion)
    db.session.add(Poppedcherry)
    db.session.add(PoppyCocktail)
    db.session.add(PortWineFlip)
    db.session.add(PlantersPunch)
    db.session.add(PineapplePaloma)
    db.session.add(PornstarMartini)
    db.session.add(PlantersPunch)
    db.session.add(PortAndStarboard)
    db.session.add(PortWineCocktail)
    db.session.add(PyschVitaminLight)
    db.session.add(PinkPantyPulldowns)
    db.session.add(PassionFruitMartini)
    db.session.add(PineappleGingeraleSmoothie)
    db.session.add(Quentin)
    db.session.add(QueenBee)
    db.session.add(QuickFK)
    db.session.add(Quicksand)
    db.session.add(QueenCharlotte)
    db.session.add(QueenElizabeth)
    db.session.add(QuakersCocktail)
    db.session.add(QuarterDeckCocktail)
    db.session.add(Rose)
    db.session.add(Radler)
    db.session.add(RumSour)
    db.session.add(RumPunch)
    db.session.add(RumToddy)
    db.session.add(RoyalFizz)
    db.session.add(RumCooler)
    db.session.add(RumRunner)
    db.session.add(RustyNail)
    db.session.add(RedSnapper)
    db.session.add(RoyalBitch)
    db.session.add(RoyalFlush)
    db.session.add(RumCobbler)
    db.session.add(RubyTuesday)
    db.session.add(RailSplitter)
    db.session.add(RosemaryBlue)
    db.session.add(RamosGinFizz)
    db.session.add(RoyalGinFizz)
    db.session.add(RumMilkPunch)
    db.session.add(RaspberryJulep)
    db.session.add(RumScrewdriver)
    db.session.add(RaspberryCooler)
    db.session.add(RumOldfashioned)
    db.session.add(RussianSpringPunch)
    db.session.add(RadioactiveLongIslandIcedTea)
    db.session.add(Smut)
    db.session.add(Spritz)
    db.session.add(Scooter)
    db.session.add(Sangria)
    db.session.add(Stinger)
    db.session.add(Sazerac)
    db.session.add(Sidecar)
    db.session.add(Snowday)
    db.session.add(Spice75)
    db.session.add(Snowball)
    db.session.add(Shotgun)
    db.session.add(SaltyDog)
    db.session.add(StoneSour)
    db.session.add(Seabreeze)
    db.session.add(ScotchSour)
    db.session.add(SweetTooth)
    db.session.add(Screwdriver)
    db.session.add(SherryFlip)
    db.session.add(SolYSombra)
    db.session.add(SharkAttack)
    db.session.add(SanFrancisco)
    db.session.add(SpaceOdyssey)
    db.session.add(SherryEggnog)
    db.session.add(SweetBananas)
    db.session.add(SweetSangria)
    db.session.add(ScotchCobbler)
    db.session.add(Spikingcoffee)
    db.session.add(SwedishCoffee)
    db.session.add(SingaporeSling)
    db.session.add(SlipperyNipple)
    db.session.add(SnakeBiteUK)
    db.session.add(ScreamingOrgasm)
    db.session.add(SexontheBeach)
    db.session.add(SidecarCocktail)
    db.session.add(SpritzVeneziano)
    db.session.add(SloeGinCocktail)
    db.session.add(Spanishchocolate)
    db.session.add(SangriaTheBest)
    db.session.add(ShanghaiCocktail)
    db.session.add(SpicedPeachPunch)
    db.session.add(StrawberryShivers)
    db.session.add(StrawberryDaiquiri)
    db.session.add(StrawberryLemonade)
    db.session.add(SnakebiteandBlack)
    db.session.add(SunnyHolidayPunch)
    db.session.add(SurfCityLifesaver)
    db.session.add(StrawberryMargarita)
    db.session.add(SaltedToffeeMartini)
    db.session.add(ScottishHighlandLiqueur)
    db.session.add(SmashedWatermelonMargarita)
    db.session.add(Thriller)
    db.session.add(TheGalah)
    db.session.add(TiaMaria)
    db.session.add(Tipperary)
    db.session.add(Turkeyball)
    db.session.add(TexasSling)
    db.session.add(ThaiCoffee)
    db.session.add(TomCollins)
    db.session.add(TomatoTang)
    db.session.add(TalosCoffee)
    db.session.add(TenneseeMud)
    db.session.add(TequilaFizz)
    db.session.add(TequilaSour)
    db.session.add(ThaiIcedTea)
    db.session.add(TheLastWord)
    db.session.add(TurfCocktail)
    db.session.add(TheLaverstoke)
    db.session.add(TequilaSlammer)
    db.session.add(TequilaSunrise)
    db.session.add(ThePhilosopher)
    db.session.add(TuxedoCocktail)
    db.session.add(TequilaSurprise)
    db.session.add(ThaiIcedCoffee)
    db.session.add(TheJimmyConway)
    db.session.add(TexasRattlesnake)
    db.session.add(TommysMargarita)
    db.session.add(TheStrangeWeaver)
    db.session.add(TheEvilBlueThing)
    db.session.add(Vesper)
    db.session.add(Victor)
    db.session.add(Vampiro)
    db.session.add(Vesuvio)
    db.session.add(Veteran)
    db.session.add(VanVleet)
    db.session.add(VodkaFizz)
    db.session.add(VodkaLemon)
    db.session.add(VodkaSlime)
    db.session.add(VodkaTonic)
    db.session.add(VodkaMartini)
    db.session.add(VodkaRussian)
    db.session.add(VermouthCassis)
    db.session.add(VictoryCollins)
    db.session.add(VodkaAndTonic)
    db.session.add(ValenciaCocktail)
    db.session.add(WhiskyMac)
    db.session.add(WhiteLady)
    db.session.add(WinePunch)
    db.session.add(WineCooler)
    db.session.add(WinterRita)
    db.session.add(WhiskeySour)
    db.session.add(WhiteRussian)
    db.session.add(WinterPaloma)
    db.session.add(WhiteWineSangria)
    db.session.add(WhitecapMargarita)
    db.session.add(WaikikiBeachcomber)
    db.session.add(YellowBird)
    db.session.add(YoghurtCooler)
    db.session.add(Zorro)
    db.session.add(Zinger)
    db.session.add(Zoksel)
    db.session.add(Zombie)
    db.session.add(Zambeer)
    db.session.add(Zorbatini)
    db.session.add(Zenmeister)
    db.session.add(Zipperhead)
    db.session.add(ZimaBlaster)
    db.session.add(ZiziCoincoin)
    db.session.add(ZimadoriZinger)
    db.session.add(ZippysRevenge)
    db.session.add(ZiemesMartiniApfelsaft)
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
