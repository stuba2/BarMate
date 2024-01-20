from app.models import db, environment, SCHEMA, Recipe, RecipeImage
from sqlalchemy.sql import text


# Adds a demo user, you can add other recipe_images here if you want
def seed_recipe_images():
    vodka_red_bull_pic = RecipeImage(
        recipe_id=1,
        url='https://images.pexels.com/photos/16444383/pexels-photo-16444383/free-photo-of-glass-of-red-bull.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
    gin_apple_cider_pic = RecipeImage(
        recipe_id=2,
        url='https://images.rawpixel.com/image_600/cHJpdmF0ZS9zdGF0aWMvaW1hZ2Uvd2Vic2l0ZS8yMDIyLTA0L2xyL3NrODA0LWltYWdlLWt3dnVrMWZtLmpwZw.jpg')
    kentucky_mule_pic = RecipeImage(
        recipe_id=3,
        url='https://live.staticflickr.com/7255/7560780984_6e2a5f066e_c.jpg')
    malort_highball_pic = RecipeImage(
        recipe_id=4,
        url='https://negativespace.co/wp-content/uploads/2019/06/negative-space-red-summer-cocktail-473x708.jpg')

    db.session.add(vodka_red_bull_pic)
    db.session.add(gin_apple_cider_pic)
    db.session.add(kentucky_mule_pic)
    db.session.add(malort_highball_pic)

    ir0 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'A1').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/2x8thr1504816928.jpg'
        )
    ir1 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'ABC').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tqpvqp1472668328.jpg'
        )
    ir2 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Ace').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/l3cd7f1504818306.jpg'
        )
    ir3 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'ACID').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xuxpxt1479209317.jpg'
        )
    ir4 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Adam').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/v0at4i1582478473.jpg'
        )
    ir5 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'AT&T').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rhhwmp1493067619.jpg'
        )
    ir6 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'A. J.').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/l74qo91582480316.jpg'
        )
    ir7 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Affair').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/h5za6y1582477994.jpg'
        )
    ir8 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Apello').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uptxtv1468876415.jpg'
        )
    ir9 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Avalon').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/3k9qic1493068931.jpg'
        )
    ir10 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Abilene').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/smb2oe1582479072.jpg'
        )
    ir11 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Addison').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yzva7x1504820300.jpg'
        )
    ir12 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Almeria').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rwsyyu1483388181.jpg'
        )
    ir13 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Acapulco').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/il9e0r1582478841.jpg'
        )
    ir14 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Affinity').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wzdtnn1582477684.jpg'
        )
    ir15 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Applecar').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sbffau1504389764.jpg'
        )
    ir16 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Aviation').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/trbplb1606855233.jpg'
        )
    ir17 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Adam Bomb').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tpxurs1454513016.jpg'
        )
    ir18 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Addington').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ib0b7g1504818925.jpg'
        )
    ir19 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'After sex').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xrl66i1493068702.jpg'
        )
    ir20 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Afterglow').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vuquyv1468876052.jpg'
        )
    ir21 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Afternoon').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vyrurp1472667777.jpg'
        )
    ir22 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Alexander').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/0clus51606772388.jpg'
        )
    ir23 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Algonquin').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uwryxx1483387873.jpg'
        )
    ir24 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Allegheny').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uwvyts1483387934.jpg'
        )
    ir25 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Americano').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/709s6m1613655124.jpg'
        )
    ir26 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Applejack').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sutyqp1479209062.jpg'
        )
    ir27 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Artillery').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/g1vnbe1493067747.jpg'
        )
    ir28 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Autodafé').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7dkf0i1487602928.jpg'
        )
    ir29 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Avalanche').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uppqty1472720165.jpg'
        )
    ir30 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Adam & Eve').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vfeumw1504819077.jpg'
        )
    ir32 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Almond Joy').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xutuqs1483388296.jpg'
        )
    ir33 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Angel Face').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vaukir1606772580.jpg'
        )
    ir34 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Aquamarine').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/zvsre31572902738.jpg'
        )
    ir35 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Archbishop').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/4g6xds1582579703.jpg'
        )
    ir36 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Absinthe #2').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uxxtrt1472667197.jpg'
        )
    ir37 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Sex').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xtrvtx1472668436.jpg'
        )
    ir38 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Fish').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ttsvwy1472668781.jpg'
        )
    ir39 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Aztec Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uqwuyp1454514591.jpg'
        )
    ir40 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Adam Sunrise').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vtuyvu1472812112.jpg'
        )
    ir41 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Tea').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/b7qzo21493070167.jpg'
        )
    ir42 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Apple Grande').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wqrptx1472668622.jpg'
        )
    ir43 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Apple Karate').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/syusvw1468876634.jpg'
        )
    ir44 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Apricot Lady').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7ityp11582579598.jpg'
        )
    ir45 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Army special').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/55muhh1493068062.jpg'
        )
    ir46 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Atlantic Sun').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/doyxqb1493067556.jpg'
        )
    ir47 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/2mcozt1504817403.jpg'
        )
    ir48 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto fizz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/92h3jz1582474310.jpg'
        )
    ir49 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Mist').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/utpxxq1483388370.jpg'
        )
    ir50 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Rose').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/3jm41q1493069578.jpg'
        )
    ir51 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xnzc541493070211.jpg'
        )
    ir52 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Aperol Spritz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/iloasq1587661955.jpg'
        )
    ir53 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Apple Slammer').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/09yd5f1493069852.jpg'
        )
    ir54 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Apricot punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tuxxtp1472668667.jpg'
        )
    ir55 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Arise My Love').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wyrrwv1441207432.jpg'
        )
    ir56 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Atomic Lokade').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/n3zfrh1493067412.jpg'
        )
    ir57 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'A Piece of Ass').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tqxyxx1472719737.jpg'
        )
    ir58 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Abbey Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mr30ob1582479875.jpg'
        )
    ir59 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Alfie Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ypxsqy1483387829.jpg'
        )
    ir60 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Alice Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qyqtpv1468876144.jpg'
        )
    ir61 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Shake').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xk79al1493069655.jpg'
        )
    ir62 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Apple Highball').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/66mt9b1619695719.jpg'
        )
    ir63 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Addison Special').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/4vo5651493068493.jpg'
        )
    ir64 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Adonis Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xrvruq1472812030.jpg'
        )
    ir65 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Alabama Slammer').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jntghf1606771886.jpg'
        )
    ir66 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Alaska Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wsyryt1483387720.jpg'
        )
    ir67 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Allies Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qvprvp1483388104.jpg'
        )
    ir68 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunset').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/apictz1493069760.jpg'
        )
    ir69 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Twister').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ido1j01493068134.jpg'
        )
    ir70 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Arthur Tompkins').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7onfhz1493067921.jpg'
        )
    ir71 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Artillery Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/9a4vqb1493067692.jpg'
        )
    ir72 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'A Splash of Nash').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rsvtrr1472668201.jpg'
        )
    ir73 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Liqueur').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/swqxuv1472719649.jpg'
        )
    ir74 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stinger').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vvop4w1493069934.jpg'
        )
    ir75 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Sunrise').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/akcpsh1493070267.jpg'
        )
    ir76 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Angelica Liqueur').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yuurps1472667672.jpg'
        )
    ir77 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Arctic Mouthwash').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wqstwv1478963735.jpg'
        )
    ir78 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Stingers').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/y7w0721493068255.jpg'
        )
    ir79 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Autumn Garibaldi').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ne7re71604179012.jpg'
        )
    ir80 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Evergreen').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wrxrxp1472812609.jpg'
        )
    ir81 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Absolut limousine').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ssqpyw1472719844.jpg'
        )
    ir82 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Stress #2').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xuyqrw1472811825.jpg'
        )
    ir83 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Aloha Fruit punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wsyvrt1468876267.jpg'
        )
    ir84 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Apple Cider Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xrqxuv1454513218.jpg'
        )
    ir85 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Auburn Headbanger').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vw7iv91493067320.jpg'
        )
    ir86 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'A Day at the Beach').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/trptts1454514474.jpg'
        )
    ir87 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'A Furlong Too Late').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ssxvww1472669166.jpg'
        )
    ir88 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Absolut Summertime').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/trpxxs1472669662.jpg'
        )
    ir89 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto And Cream').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/dj8n0r1504375018.jpg'
        )
    ir90 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Arizona Antifreeze').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/dbtylp1493067262.jpg'
        )
    ir91 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'A Gilligan\'s Island').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wysqut1461867176.jpg'
        )
    ir92 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Fabulous').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/abcpwr1504817734.jpg'
        )
    ir93 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Alice in Wonderland').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/g12lj41493069391.jpg'
        )
    ir94 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xwryyx1472719921.jpg'
        )
    ir95 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'A True Amaretto Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rptuxy1472669372.jpg'
        )
    ir96 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Absolutly Screwed Up').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yvxrwv1472669728.jpg'
        )
    ir97 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Apple Berry Smoothie').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xwqvur1468876473.jpg'
        )
    ir98 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Adios Amigos Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/8nk2mp1504819893.jpg'
        )
    ir99 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'After Dinner Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vtytxq1483387578.jpg'
        )
    ir100 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'After Supper Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/quyxwu1483387610.jpg'
        )
    ir102 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'A midsummernight dream').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ysqvqp1461867292.jpg'
        )
    ir103 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Apple Pie with A Crust').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qspqxt1472720078.jpg'
        )
    ir104 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'A Night In Old Mandalay').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vyrvxt1461919380.jpg'
        )
    ir105 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Almond Chocolate Coffee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jls02c1493069441.jpg'
        )
    ir106 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'A.D.M. (After Dinner Mint)').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ruxuvp1472669600.jpg'
        )
    ir107 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Absolutely Cranberry Smash').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vqwstv1472811884.jpg'
        )
    ir108 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Amaretto Stone Sour Alternative').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wutxqr1472720012.jpg'
        )
    ir109 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'B-52').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/5a3vg61504372070.jpg'
        )
    ir110 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'B-53').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rwqxrv1461866023.jpg'
        )
    ir111 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bijou').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rysb3r1513706985.jpg'
        )
    ir112 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Boxcar').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/pwgtpa1504366376.jpg'
        )
    ir113 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Big Red').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yqwuwu1441248116.jpg'
        )
    ir114 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bellini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/eaag491504367543.jpg'
        )
    ir115 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bramble').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/twtbh51630406392.jpg'
        )
    ir116 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Balmoral').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vysuyq1441206297.jpg'
        )
    ir117 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bluebird').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/5jhyd01582579843.jpg'
        )
    ir118 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Brooklyn').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ojsezf1582477277.jpg'
        )
    ir119 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bora Bora').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xwuqvw1473201811.jpg'
        )
    ir120 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Boomerang').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/3m6yz81504389551.jpg'
        )
    ir121 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Barracuda').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jwmr1x1504372337.jpg'
        )
    ir122 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Brigadier').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/nl89tf1518947401.jpg'
        )
    ir123 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Broadside').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/l2o6xu1582476870.jpg'
        )
    ir124 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Buccaneer').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/upvtyt1441249023.jpg'
        )
    ir125 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Brain Fart').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rz5aun1504389701.jpg'
        )
    ir126 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Blackthorn').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/dgj92f1616098672.jpg'
        )
    ir127 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bob Marley').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rrqrst1477140664.jpg'
        )
    ir128 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bible Belt').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/6bec6v1503563675.jpg'
        )
    ir129 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bubble Gum').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/spuurv1468878783.jpg'
        )
    ir130 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bumble Bee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uwqpvv1461866378.jpg'
        )
    ir131 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Baby Eskimo').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wywrtw1472720227.jpg'
        )
    ir132 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/kxlgbi1504366100.jpg'
        )
    ir133 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bahama Mama').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tyb4a41515793339.jpg'
        )
    ir134 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Brainteaser').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ruywtq1461866066.jpg'
        )
    ir135 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Mary').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/t6caa21582485702.jpg'
        )
    ir136 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Black & Tan').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rwpswp1454511017.jpg'
        )
    ir137 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Blue Lagoon').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/5wm4zo1582579154.jpg'
        )
    ir138 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bee\'s Knees').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tx8ne41582475326.jpg'
        )
    ir139 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Flip').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/6ty09d1504366461.jpg'
        )
    ir140 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/b1bxgq1582484872.jpg'
        )
    ir141 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Butter Baby').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/1xhjk91504783763.jpg'
        )
    ir142 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Boulevardier').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/km84qi1513705868.jpg'
        )
    ir143 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/dms3io1504366318.jpg'
        )
    ir145 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Belgian Blue').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jylbrq1582580066.jpg'
        )
    ir146 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/5yhd3n1571687385.jpg'
        )
    ir147 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Berry Deadly').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/zk74k21593351065.jpg'
        )
    ir148 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bloody Maria').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yz0j6z1504389461.jpg'
        )
    ir149 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Blind Russian').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wxuqvr1472720408.jpg'
        )
    ir150 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Blue Mountain').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/bih7ln1582485506.jpg'
        )
    ir151 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bounty Hunter').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/t8bgxl1596018175.jpg'
        )
    ir152 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bombay Cassis').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/h1e0e51510136907.jpg'
        )
    ir153 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bourbon Sling').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/3s36ql1504366260.jpg'
        )
    ir154 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bruised Heart').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7if5kq1503564209.jpg'
        )
    ir155 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Black Russian').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/8oxlqf1606772765.jpg'
        )
    ir156 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Baby Guinness').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rvyvxs1473482359.jpg'
        )
    ir157 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Cobbler').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/5xgu591582580586.jpg'
        )
    ir158 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Blue Hurricane').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/nwx02s1515795822.jpg'
        )
    ir159 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Boston Sidecar').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qzs5d11504365962.jpg'
        )
    ir160 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Blue Margarita').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/bry4qh1582751040.jpg'
        )
    ir161 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cream Pi').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/m5p67n1582474609.jpg'
        )
    ir162 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Banana Daiquiri').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/k1xatq1504389300.jpg'
        )
    ir163 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bellini Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/3h9wv51504389379.jpg'
        )
    ir164 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Black and Brown').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wwuvxv1472668899.jpg'
        )
    ir165 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Brandy Alexander').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mlyk1i1606772340.jpg'
        )
    ir166 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bacardi Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/n433t21504348259.jpg'
        )
    ir167 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bleeding Surgeon').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/usuvvr1472719118.jpg'
        )
    ir168 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Blueberry Mojito').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/07iep51598719977.jpg'
        )
    ir169 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bermuda Highball').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qrvtww1441206528.jpg'
        )
    ir170 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Butterfly Effect').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ht3hnk1619704289.jpg'
        )
    ir171 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Banana Milk Shake').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rtwwsx1472720307.jpg'
        )
    ir172 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Brave Bull Shooter').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yrtypx1473344625.jpg'
        )
    ir173 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Black Forest Shake').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xxtxsu1472720505.jpg'
        )
    ir174 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Between The Sheets').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/of1rj41504348346.jpg'
        )
    ir175 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bailey\'s Dream Shake').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qxrvqw1472718959.jpg'
        )
    ir176 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Bobby Burns Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/km6se51484411608.jpg'
        )
    ir177 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vqquwx1472720634.jpg'
        )
    ir178 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Boozy Snickers Milkshake').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/861tzm1504784164.jpg'
        )
    ir179 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Banana Cantaloupe Smoothie').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uqxqsy1468876703.jpg'
        )
    ir180 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Brandon and Will\'s Coke Float').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xspxyr1472719185.jpg'
        )
    ir181 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Banana Strawberry Shake Daiquiri').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uvypss1472720581.jpg'
        )
    ir182 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Casino').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/1mvjxg1504348579.jpg'
        )
    ir184 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Caipirinha').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jgvn7p1582484435.jpg'
        )
    ir185 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Cream Soda').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yqstxr1479209367.jpg'
        )
    ir186 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libra').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ck6d0p1504388696.jpg'
        )
    ir187 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Rum').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/twsuvr1441554424.jpg'
        )
    ir188 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Cuba Libre').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wmkbfj1606853905.jpg'
        )
    ir189 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Corn n Oil').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/pk6dwi1592767243.jpg'
        )
    ir190 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Citrus Coke').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uyrvut1479473214.jpg'
        )
    ir191 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Casa Blanca').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/usspxq1441553762.jpg'
        )
    ir192 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Clover Club').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/t0aja61504348715.jpg'
        )
    ir193 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Caipirissima').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yd47111503565515.jpg'
        )
    ir194 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'City Slicker').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/dazdlg1504366949.jpg'
        )
    ir195 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Campari Beer').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xsqrup1441249130.jpg'
        )
    ir196 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Chicago Fizz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qwvwqr1441207763.jpg'
        )
    ir197 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/kpsajh1504368362.jpg'
        )
    ir198 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Coffee-Vodka').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qvrrvu1472667494.jpg'
        )
    ir199 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Casino Royale').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/3qpv121504366699.jpg'
        )
    ir200 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Corpse Reviver').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/gifgao1513704334.jpg'
        )
    ir201 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Milk').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/j6q35t1504889399.jpg'
        )
    ir202 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Clove Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qxvtst1461867579.jpg'
        )
    ir203 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Coffee Liqueur').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ryvtsu1441253851.jpg'
        )
    ir204 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Coke and Drops').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yrtxxp1472719367.jpg'
        )
    ir205 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Drink').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/q7w4xu1487603180.jpg'
        )
    ir206 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mzgaqu1504389248.jpg'
        )
    ir207 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Creme de Menthe').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yxswtp1441253918.jpg'
        )
    ir208 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Monkey').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tyvpxt1468875212.jpg'
        )
    ir209 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Cranberry Cordial').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qtspsx1472667392.jpg'
        )
    ir210 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Beverage').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jbqrhv1487603186.jpg'
        )
    ir211 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Champagne Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/t5pv461606773026.jpg'
        )
    ir212 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'California Lemonade').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/q5z4841582484168.jpg'
        )
    ir213 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'California Root Beer').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rsxuyr1472719526.jpg'
        )
    ir214 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Captain Kidd\'s Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/d83spj1596017390.jpg'
        )
    ir215 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Cosmopolitan Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/upxxpq1439907580.jpg'
        )
    ir216 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Boilermaker').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/svsxsv1454511666.jpg'
        )
    ir217 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Classic Old-Fashioned').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/w8cxqv1582485254.jpg'
        )
    ir218 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Chocolate Black Russian').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yyvywx1472720879.jpg'
        )
    ir219 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Cocktail Horse\'s Neck').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/4vobt21643844913.jpg'
        )
    ir220 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Caribbean Orange Liqueur').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qwxuwy1472667570.jpg'
        )
    ir221 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Castillian Hot Chocolate').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/3nbu4a1487603196.jpg'
        )
    ir222 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Cherry Electric Lemonade').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tquyyt1451299548.jpg'
        )
    ir223 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Derby').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/52weey1606772672.jpg'
        )
    ir224 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Diesel').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sxrrqq1454512852.jpg'
        )
    ir225 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Daiquiri').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mrz9091589574515.jpg'
        )
    ir226 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Danbooka').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vurrxr1441246074.jpg'
        )
    ir227 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Downshift').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/y36z8c1503563911.jpg'
        )
    ir228 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Dragonfly').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uc63bh1582483589.jpg'
        )
    ir229 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Dry Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/6ck9yi1589574317.jpg'
        )
    ir230 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Dry Rob Roy').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/typuyq1439456976.jpg'
        )
    ir232 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Dirty Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vcyvpq1485083300.jpg'
        )
    ir233 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Darkwood Sling').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sxxsyq1472719303.jpg'
        )
    ir234 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Dark and Stormy').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/t1tn0s1504374905.jpg'
        )
    ir235 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Dark Caipirinha').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uwstrx1472406058.jpg'
        )
    ir236 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Duchamp\'s Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/g51naw1485084685.jpg'
        )
    ir237 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Damned if you do').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ql7bmx1503565106.jpg'
        )
    ir238 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Dubonnet Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/pfz3hz1582483111.jpg'
        )
    ir239 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Drinking Chocolate').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/u6jrdf1487603173.jpg'
        )
    ir240 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Death in the Afternoon').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/y7s3rh1598719574.jpg'
        )
    ir241 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Egg Cream').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mvis731484430445.jpg'
        )
    ir242 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog #4').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wpspsy1468875747.jpg'
        )
    ir243 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'English Highball').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/dhvr7d1504519752.jpg'
        )
    ir244 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/n0sx531504372951.jpg'
        )
    ir245 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Espresso Rumtini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/acvf171561574403.jpg'
        )
    ir246 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Egg Nog - Healthy').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qxuppv1468875308.jpg'
        )
    ir247 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'English Rose Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yxwrpp1441208697.jpg'
        )
    ir248 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Elderflower Caipirinha').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/dif7a31614006331.jpg'
        )
    ir249 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Egg-Nog - Classic Cooked').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/quxsvt1468875505.jpg'
        )
    ir250 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Empellón Cocina\'s Fat-Washed Mezcal').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/osgvxt1513595509.jpg'
        )
    ir251 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Frosé').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/b4cadp1619695347.jpg'
        )
    ir252 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Frappé').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vqwryq1441245927.jpg'
        )
    ir253 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Foxy Lady').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/r9cz3q1504519844.jpg'
        )
    ir254 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'French 75').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/hrxfbl1606773109.jpg'
        )
    ir255 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Figgy Thyme').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/pbw4e51606766578.jpg'
        )
    ir256 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Frisco Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/acuvjz1582482022.jpg'
        )
    ir257 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Shake').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/q0fg2m1484430704.jpg'
        )
    ir258 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Cooler').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/i3tfn31484430499.jpg'
        )
    ir259 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Freddy Kruger').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tuppuq1461866798.jpg'
        )
    ir260 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Funk and Soul').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qtv83q1596015790.jpg'
        )
    ir261 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Fuzzy Asshole').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wrvpuu1472667898.jpg'
        )
    ir262 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'French Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/clth721504373134.jpg'
        )
    ir263 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'French Negroni').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/x8lhp41513703167.jpg'
        )
    ir264 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Fahrenheit 5000').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tysssx1473344692.jpg'
        )
    ir265 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Flying Dutchman').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mwko4q1582482903.jpg'
        )
    ir266 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Daiquiri').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7oyrj91504884412.jpg'
        )
    ir267 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Fruit Flip-Flop').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/nfdx6p1484430633.jpg'
        )
    ir268 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Flying Scotchman').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/q53l911582482518.jpg'
        )
    ir269 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'French Connection').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/zaqa381504368758.jpg'
        )
    ir270 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Dr. Pepper').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/d30z931503565384.jpg'
        )
    ir271 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Flaming Lamborghini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yywpss1461866587.jpg'
        )
    ir272 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Flander\'s Flake-Out').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sqvqrx1461866705.jpg'
        )
    ir273 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Mint Daiquiri').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jrhn1q1504884469.jpg'
        )
    ir274 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Frozen Pineapple Daiquiri').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/k3aecd1582481679.jpg'
        )
    ir275 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'GG').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vyxwut1468875960.jpg'
        )
    ir276 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gimlet').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/3xgldt1513707271.jpg'
        )
    ir277 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Godchild').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/m5nhtr1504820829.jpg'
        )
    ir278 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Fizz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/drtihp1606768397.jpg'
        )
    ir279 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/noxp7e1606769224.jpg'
        )
    ir280 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gagliardo').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/lyloe91487602877.jpg'
        )
    ir281 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Godmother').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/quksqg1582582597.jpg'
        )
    ir282 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Godfather').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/e5zgao1582582378.jpg'
        )
    ir283 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gluehwein').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vuxwvt1468875418.jpg'
        )
    ir284 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Tonic').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qcgz0t1643821443.jpg'
        )
    ir285 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Toddy').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jxstwf1582582101.jpg'
        )
    ir286 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Smash').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/iprva61606768774.jpg'
        )
    ir287 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Daisy').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/z6e22f1582581155.jpg'
        )
    ir288 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Lemon').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/6gdohq1681212476.jpg'
        )
    ir289 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Sling').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/8cl9sm1582581761.jpg'
        )
    ir290 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Greyhound').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/g5upn41513706732.jpg'
        )
    ir291 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Rickey').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/s00d6f1504883945.jpg'
        )
    ir292 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Squirt').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xrbhz61504883702.jpg'
        )
    ir293 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Grand Blue').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vsrsqu1472761749.jpg'
        )
    ir294 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Cooler').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/678xt11582481163.jpg'
        )
    ir295 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Swizzle').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sybce31504884026.jpg'
        )
    ir296 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Grass Skirt').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qyvprp1473891585.jpg'
        )
    ir297 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Grasshopper').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/aqm9el1504369613.jpg'
        )
    ir298 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Grim Reaper').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/kztu161504883192.jpg'
        )
    ir299 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin and Soda').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/nzlyc81605905755.jpg'
        )
    ir300 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Golden dream').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qrot6j1504369425.jpg'
        )
    ir301 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Green Goblin').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qxprxr1454511520.jpg'
        )
    ir302 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Grizzly Bear').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/k6v97f1487602550.jpg'
        )
    ir303 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin And Tonic').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/k0508k1668422436.jpg'
        )
    ir304 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gin Basil Smash').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jqh2141572807327.jpg'
        )
    ir305 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gentleman\'s Club').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/k2r7wv1582481454.jpg'
        )
    ir306 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Girl From Ipanema').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xypspq1469090633.jpg'
        )
    ir307 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Garibaldi Negroni').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/kb4bjg1604179771.jpg'
        )
    ir308 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Gideon\'s Green Dinosaur').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/p5r0tr1503564636.jpg'
        )
    ir309 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Grape lemon pineapple Smoothie').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/54z5h71487603583.jpg'
        )
    ir310 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'H.D.').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/upusyu1472667977.jpg'
        )
    ir311 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Honey Bee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vu8l7t1582475673.jpg'
        )
    ir312 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Hot Toddy').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ggx0lv1613942306.jpg'
        )
    ir313 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Herbal flame').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rrstxv1441246184.jpg'
        )
    ir314 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Horse\'s Neck').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/006k4e1504370092.jpg'
        )
    ir315 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Happy Skipper').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/42w2g41487602448.jpg'
        )
    ir316 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Hunter\'s Moon').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/t0iugg1509556712.jpg'
        )
    ir317 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Halloween Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7hcgyj1571687671.jpg'
        )
    ir318 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Havana Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/59splc1504882899.jpg'
        )
    ir320 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Homemade Kahlua').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uwtsst1441254025.jpg'
        )
    ir321 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Hot Creamy Bush').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/spvrtp1472668037.jpg'
        )
    ir322 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Harvey Wallbanger').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7os4gs1606854357.jpg'
        )
    ir323 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Hawaiian Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ujoh9x1504882987.jpg'
        )
    ir324 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Hemingway Special').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jfcvps1504369888.jpg'
        )
    ir325 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Highland Fling Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/0bkwca1492975553.jpg'
        )
    ir326 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Hot Chocolate to Die for').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/0lrmjp1487603166.jpg'
        )
    ir327 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Ipamena').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yswuwp1469090992.jpg'
        )
    ir328 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Ice Pick').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ypsrqp1469091726.jpg'
        )
    ir329 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ytprxy1454513855.jpg'
        )
    ir330 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Irish Cream').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/90etyl1504884699.jpg'
        )
    ir331 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Irish Coffee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sywsqw1439906999.jpg'
        )
    ir332 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Irish Spring').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sot8v41504884783.jpg'
        )
    ir333 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Fizz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/zj1usl1504884548.jpg'
        )
    ir334 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Irish Russian').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/swqurw1454512730.jpg'
        )
    ir335 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Imperial Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/bcsj2e1487603625.jpg'
        )
    ir336 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Iced Coffee Fillip').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sxtxrp1454514223.jpg'
        )
    ir337 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Irish Curdling Cow').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yrhutv1503563730.jpg'
        )
    ir338 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Jam Donut').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uuytrp1474039804.jpg'
        )
    ir339 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Jitterbug').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wwqvrq1441245318.jpg'
        )
    ir340 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Jackhammer').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/9von5j1504388896.jpg'
        )
    ir341 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Jelly Bean').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/bglc6y1504388797.jpg'
        )
    ir342 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Jello shots').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/l0smzo1504884904.jpg'
        )
    ir343 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Jamaica Kiss').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/urpvvv1441249549.jpg'
        )
    ir344 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'John Collins').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/0t4bv71606854479.jpg'
        )
    ir345 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Japanese Fizz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/37vzv11504884831.jpg'
        )
    ir346 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Jamaican Coffee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xqptps1441247257.jpg'
        )
    ir347 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Just a Moonmint').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/znald61487604035.jpg'
        )
    ir348 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Jewel Of The Nile').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/hx4nrb1504884947.jpg'
        )
    ir349 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Jack Rose Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uuqqrv1439907068.jpg'
        )
    ir350 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Jack\'s Vanilla Coke').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/kjnt7z1504793319.jpg'
        )
    ir351 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kir').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/apneom1504370294.jpg'
        )
    ir352 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Karsk').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/808mxk1487602471.jpg'
        )
    ir353 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kamikaze').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/d7ff7u1606855412.jpg'
        )
    ir354 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kir Royale').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yt9i7n1504370388.jpg'
        )
    ir355 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Lemon').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tpupvr1478251697.jpg'
        )
    ir356 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kurant Tea').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xrsrpr1441247464.jpg'
        )
    ir357 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kioki Coffee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uppqty1441247374.jpg'
        )
    ir358 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/bmxmyq1630407098.jpg'
        )
    ir359 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kiss me Quick').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/m7iaxu1504885119.jpg'
        )
    ir360 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Shot').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/fegm621503564966.jpg'
        )
    ir361 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kool First Aid').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/hfp6sv1503564824.jpg'
        )
    ir362 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky B And B').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sqxsxp1478820236.jpg'
        )
    ir363 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kentucky Colonel').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/utqwpu1478820348.jpg'
        )
    ir364 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kool-Aid Slammer').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/kugu2m1504735473.jpg'
        )
    ir365 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kiwi Papaya Smoothie').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jogv4w1487603571.jpg'
        )
    ir366 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Kill the cold Smoothie').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7j1z2e1487603414.jpg'
        )
    ir367 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Limeade').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/5jdp5r1487603680.jpg'
        )
    ir368 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lunch Box').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qywpvt1454512546.jpg'
        )
    ir369 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Drop').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mtpxgk1504373297.jpg'
        )
    ir370 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Shot').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mx31hv1487602979.jpg'
        )
    ir371 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Long vodka').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/9179i01503565212.jpg'
        )
    ir372 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Khara').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/m1suzm1487603970.jpg'
        )
    ir373 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lassi Raita').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/s4x0qj1487603933.jpg'
        )
    ir374 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lemouroudji').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/eirmo71487603745.jpg'
        )
    ir375 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Loch Lomond').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rpvtpr1468923881.jpg'
        )
    ir376 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'London Town').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rpsrqv1468923507.jpg'
        )
    ir377 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Mango').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/1bw6sd1487603816.jpg'
        )
    ir378 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - Sweet').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/9jeifz1487603885.jpg'
        )
    ir379 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Limona Corona').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wwqrsw1441248662.jpg'
        )
    ir380 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lord And Lady').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/quwrys1468923219.jpg'
        )
    ir381 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lady Love Fizz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/20d63k1504885263.jpg'
        )
    ir382 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Tea').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/nkwr4c1606770558.jpg'
        )
    ir384 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lone Tree Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tsxpty1468923417.jpg'
        )
    ir385 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lazy Coconut Paloma').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rytuex1598719770.jpg'
        )
    ir386 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Long Island Iced Tea').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wx7hsg1504370510.jpg'
        )
    ir387 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lemon Elderflower Spritzer').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/125w0o1630407389.jpg'
        )
    ir388 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Lassi - A South Indian Drink').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/iq6scx1487603980.jpg'
        )
    ir390 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mojito').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/metwgh1606770327.jpg'
        )
    ir391 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mimosa').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/juhcuu1504370685.jpg'
        )
    ir392 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mai Tai').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/twyrrp1439907470.jpg'
        )
    ir393 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/71t8581504353095.jpg'
        )
    ir394 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Michelada').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/u736bd1605907086.jpg'
        )
    ir395 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Manhattan').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yk70e31606771240.jpg'
        )
    ir396 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Margarita').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg'
        )
    ir397 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mauresque').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/duwfa11686236556.jpg'
        )
    ir398 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mint Julep').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/squyyq1439907312.jpg'
        )
    ir399 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mudslinger').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/hepk6h1504885554.jpg'
        )
    ir400 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Martinez 2').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/fs6kiq1513708455.jpg'
        )
    ir401 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Moranguito').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/urpsyq1475667335.jpg'
        )
    ir402 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Miami Vice').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qvuyqw1441208955.jpg'
        )
    ir403 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Moscow Mule').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/3pylqc1504370988.jpg'
        )
    ir404 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mulled Wine').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/iuwi6h1504735724.jpg'
        )
    ir405 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Masala Chai').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uyrpww1441246384.jpg'
        )
    ir406 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Munich Mule').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rj55pl1582476101.jpg'
        )
    ir407 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mocha-Berry').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vtwyyx1441246448.jpg'
        )
    ir408 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mango Mojito').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wfqmgm1630406820.jpg'
        )
    ir409 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mojito Extra').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vwxrsw1478251483.jpg'
        )
    ir410 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Gland').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/94psp81504350690.jpg'
        )
    ir411 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Mint').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/svuvrq1441208310.jpg'
        )
    ir412 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mary Pickford').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/f9erqb1504350557.jpg'
        )
    ir413 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Monkey Wrench').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/bw2noj1582473243.jpg'
        )
    ir414 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mother\'s Milk').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7stuuh1504885399.jpg'
        )
    ir415 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Manx').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uqqurp1441208231.jpg'
        )
    ir416 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Malibu Twister').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/2dwae41504885321.jpg'
        )
    ir417 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Midnight Cowboy').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vsxxwy1441208133.jpg'
        )
    ir418 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mountain Bramble').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/stwiva1619704025.jpg'
        )
    ir419 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Martinez Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wwxwvr1439906452.jpg'
        )
    ir420 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Microwave Hot Cocoa').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/8y4x5f1487603151.jpg'
        )
    ir421 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mango Orange Smoothie').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vdp2do1487603520.jpg'
        )
    ir422 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Mississippi Planters Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/urpyqs1439907531.jpg'
        )
    ir423 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Negroni').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qgdu971561574065.jpg'
        )
    ir424 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'New York Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/61wgch1504882795.jpg'
        )
    ir425 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Nutty Irishman').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xspupx1441248014.jpg'
        )
    ir426 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'National Aquarium').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/dlw0om1503565021.jpg'
        )
    ir427 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'New York Lemonade').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/b3n0ge1503565473.jpg'
        )
    ir428 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Nuked Hot Chocolate').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xcu6nb1487603142.jpg'
        )
    ir429 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Orgasm').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vr6kle1504886114.jpg'
        )
    ir430 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Old Pal').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/x03td31521761009.jpg'
        )
    ir431 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Old Cuban').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/eo8gfx1699022995.jpg'
        )
    ir432 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Orangeade').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ytsxxw1441167732.jpg'
        )
    ir433 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Orange Whip').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ttyrxr1454514759.jpg'
        )
    ir434 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Orange Crush').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/zvoics1504885926.jpg'
        )
    ir435 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Orange Oasis').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/su1olx1582473812.jpg'
        )
    ir436 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Old Fashioned').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vrwquq1478252802.jpg'
        )
    ir437 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Oreo Mudslide').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tpwwut1468925017.jpg'
        )
    ir438 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Oatmeal Cookie').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/bsvmlg1515792693.jpg'
        )
    ir439 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Orange Push-up').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mgf0y91503565781.jpg'
        )
    ir440 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Orange Rosemary Collins').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mokcas1604179977.jpg'
        )
    ir441 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Orange Scented Hot Chocolate').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/hdzwrh1487603131.jpg'
        )
    ir442 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Owen\'s Grandmother\'s Revenge').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/0wt4uo1503565321.jpg'
        )
    ir443 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Paloma').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/samm5j1513706393.jpg'
        )
    ir444 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Paradise').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ejozd71504351060.jpg'
        )
    ir445 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pink Gin').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qyr51e1504888618.jpg'
        )
    ir446 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pegu Club').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jfkemm1513703902.jpg'
        )
    ir447 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pink Lady').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/5ia6j21504887829.jpg'
        )
    ir448 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pink Moon').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/lnjoc81619696191.jpg'
        )
    ir449 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Penicillin').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/hc9b1a1521853096.jpg'
        )
    ir450 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pisco Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tsssur1439907622.jpg'
        )
    ir451 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Porto flip').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/64x5j41504351518.jpg'
        )
    ir452 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pina Colada').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/upgsue1668419912.jpg'
        )
    ir453 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pink Penocha').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/6vigjx1503564007.jpg'
        )
    ir454 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pure Passion').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/4tymma1604179273.jpg'
        )
    ir455 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Popped cherry').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sxvrwv1473344825.jpg'
        )
    ir456 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Poppy Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/cslw1w1504389915.jpg'
        )
    ir457 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Flip').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vrprxu1441553844.jpg'
        )
    ir458 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/fdk8a31606854815.jpg'
        )
    ir459 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Paloma').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/pg8iw31593351601.jpg'
        )
    ir460 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pornstar Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xjhjdf1630406071.jpg'
        )
    ir461 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Planter\'s Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jn6o251643844541.jpg'
        )
    ir462 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Port And Starboard').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wxvupx1441553911.jpg'
        )
    ir463 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Port Wine Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qruprq1441553976.jpg'
        )
    ir464 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pysch Vitamin Light').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xsqsxw1441553580.jpg'
        )
    ir465 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pink Panty Pulldowns').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/squsuy1468926657.jpg'
        )
    ir466 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Passion Fruit Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/6trfve1582473527.jpg'
        )
    ir467 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Pineapple Gingerale Smoothie').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/eg9i1d1487603469.jpg'
        )
    ir468 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Quentin').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/spxtqp1478963398.jpg'
        )
    ir469 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Queen Bee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rvvpxu1478963194.jpg'
        )
    ir470 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Quick F**K').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wvtwpp1478963454.jpg'
        )
    ir471 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Quick-sand').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vprxqv1478963533.jpg'
        )
    ir472 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Queen Charlotte').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vqruyt1478963249.jpg'
        )
    ir473 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Queen Elizabeth').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vpqspv1478963339.jpg'
        )
    ir474 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Quaker\'s Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yrqppx1478962314.jpg'
        )
    ir475 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Quarter Deck Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qrwvps1478963017.jpg'
        )
    ir476 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rose').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/8kxbvq1504371462.jpg'
        )
    ir477 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Radler').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xz8igv1504888995.jpg'
        )
    ir478 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rum Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/bylfi21504886323.jpg'
        )
    ir479 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rum Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wyrsxu1441554538.jpg'
        )
    ir480 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rum Toddy').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/athdk71504886286.jpg'
        )
    ir481 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Royal Fizz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wrh44j1504390609.jpg'
        )
    ir482 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cooler').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/2hgwsb1504888674.jpg'
        )
    ir483 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rum Runner').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vqws6t1504888857.jpg'
        )
    ir484 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rusty Nail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yqsvtw1478252982.jpg'
        )
    ir485 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Red Snapper').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7p607y1504735343.jpg'
        )
    ir486 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Royal Bitch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qupuyr1441210090.jpg'
        )
    ir487 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Royal Flush').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7rnm8u1504888527.jpg'
        )
    ir488 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rum Cobbler').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/5vh9ld1504390683.jpg'
        )
    ir489 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Ruby Tuesday').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qsyqqq1441553437.jpg'
        )
    ir490 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rail Splitter').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/stsuqq1441207660.jpg'
        )
    ir491 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rosemary Blue').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qwc5f91512406543.jpg'
        )
    ir492 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Ramos Gin Fizz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/967t911643844053.jpg'
        )
    ir493 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Royal Gin Fizz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/pe1x1c1504735672.jpg'
        )
    ir494 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rum Milk Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/w64lqm1504888810.jpg'
        )
    ir495 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Julep').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/hyztmx1598719265.jpg'
        )
    ir496 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rum Screwdriver').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/4c85zq1511782093.jpg'
        )
    ir497 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Raspberry Cooler').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/suqyyx1441254346.jpg'
        )
    ir498 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Rum Old-fashioned').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/otn2011504820649.jpg'
        )
    ir499 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Russian Spring Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ctt20s1504373488.jpg'
        )
    ir500 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Radioactive Long Island Iced Tea').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rdvqmh1503563512.jpg'
        )
    ir501 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Smut').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rx8k8e1504365812.jpg'
        )
    ir502 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Spritz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/j9evx11504373665.jpg'
        )
    ir503 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Scooter').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/twuptu1483388307.jpg'
        )
    ir504 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sangria').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xrvxpp1441249280.jpg'
        )
    ir505 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Stinger').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/2ahv791504352433.jpg'
        )
    ir506 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sazerac').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vvpxwy1439907208.jpg'
        )
    ir507 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/x72sik1606854964.jpg'
        )
    ir508 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Snowday').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/4n1ipk1614009624.jpg'
        )
    ir509 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Spice 75').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/0108c41576797064.jpg'
        )
    ir510 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Snowball').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7ibfs61504735416.jpg'
        )
    ir511 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Shot-gun').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/2j1m881503563583.jpg'
        )
    ir512 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Salty Dog').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/4vfge01504890216.jpg'
        )
    ir513 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Stone Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vruvtp1472719895.jpg'
        )
    ir514 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sea breeze').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7rfuks1504371562.jpg'
        )
    ir515 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/0dnb6k1504890436.jpg'
        )
    ir516 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Tooth').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/j6rq6h1503563821.jpg'
        )
    ir517 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Screwdriver').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/8xnyke1504352207.jpg'
        )
    ir518 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Flip').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qrryvq1478820428.jpg'
        )
    ir519 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sol Y Sombra').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/3gz2vw1503425983.jpg'
        )
    ir520 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Shark Attack').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uv96zr1504793256.jpg'
        )
    ir521 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'San Francisco').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/szmj2d1504889961.jpg'
        )
    ir522 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Space Odyssey').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vxtjbx1504817842.jpg'
        )
    ir523 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sherry Eggnog').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xwrpsv1478820541.jpg'
        )
    ir524 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Bananas').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sxpcj71487603345.jpg'
        )
    ir525 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sweet Sangria').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/uqqvsp1468924228.jpg'
        )
    ir526 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Scotch Cobbler').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/1q7coh1504736227.jpg'
        )
    ir528 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Swedish Coffee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ywtrvt1441246783.jpg'
        )
    ir529 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Singapore Sling').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7dozeg1582578095.jpg'
        )
    ir530 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Slippery Nipple').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/l9tgru1551439725.jpg'
        )
    ir531 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Snake Bite (UK)').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xuwpyu1441248734.jpg'
        )
    ir532 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Screaming Orgasm').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/x894cs1504388670.jpg'
        )
    ir533 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sex on the Beach').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/fi67641668420787.jpg'
        )
    ir534 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sidecar Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ewjxui1504820428.jpg'
        )
    ir535 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Spritz Veneziano').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/51ezka1551456113.jpg'
        )
    ir536 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sloe Gin Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/d7mo481504889531.jpg'
        )
    ir537 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Spanish chocolate').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/pra8vt1487603054.jpg'
        )
    ir538 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sangria The  Best').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vysywu1468924264.jpg'
        )
    ir539 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Shanghai Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ttyrxr1478820678.jpg'
        )
    ir540 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Spiced Peach Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qxvypq1468924331.jpg'
        )
    ir541 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Shivers').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/9h1vvt1487603404.jpg'
        )
    ir542 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Daiquiri').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/deu59m1504736135.jpg'
        )
    ir543 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Lemonade').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/spvvxp1468924425.jpg'
        )
    ir544 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Snakebite and Black').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rssvwv1441248863.jpg'
        )
    ir545 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Sunny Holiday Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rywtwy1468924758.jpg'
        )
    ir546 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Surf City Lifesaver').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/2rzfer1487602699.jpg'
        )
    ir547 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Strawberry Margarita').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tqyrpw1439905311.jpg'
        )
    ir548 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Salted Toffee Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/3s6mlr1509551211.jpg'
        )
    ir549 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Scottish Highland Liqueur').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/upqvvp1441253441.jpg'
        )
    ir550 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Smashed Watermelon Margarita').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/dztcv51598717861.jpg'
        )
    ir551 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Thriller').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rvuswq1461867714.jpg'
        )
    ir552 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'The Galah').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sy7y6r1614775067.jpg'
        )
    ir553 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tia-Maria').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sih81u1504367097.jpg'
        )
    ir554 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tipperary').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/b522ek1521761610.jpg'
        )
    ir555 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Turkeyball').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rxurpr1441554292.jpg'
        )
    ir556 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Texas Sling').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ypl13s1504890158.jpg'
        )
    ir557 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Thai Coffee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wquwxs1441247025.jpg'
        )
    ir558 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tom Collins').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/7cll921606854636.jpg'
        )
    ir559 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tomato Tang').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/869qr81487603278.jpg'
        )
    ir560 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Talos Coffee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rswqpy1441246518.jpg'
        )
    ir561 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tennesee Mud').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/txruqv1441245770.jpg'
        )
    ir562 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Fizz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/2bcase1504889637.jpg'
        )
    ir563 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ek0mlq1504820601.jpg'
        )
    ir564 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Tea').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/trvwpu1441245568.jpg'
        )
    ir565 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'The Last Word').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/91oule1513702624.jpg'
        )
    ir566 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Turf Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/utypqq1441554367.jpg'
        )
    ir567 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'The Laverstoke').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/6xfj5t1517748412.jpg'
        )
    ir568 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Slammer').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/43uhr51551451311.jpg'
        )
    ir569 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Sunrise').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg'
        )
    ir570 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'The Philosopher').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/sp8hkp1596017787.jpg'
        )
    ir571 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tuxedo Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/4u0nbl1504352551.jpg'
        )
    ir572 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tequila Surprise').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/8189p51504735581.jpg'
        )
    ir573 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Thai Iced Coffee').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rqpypv1441245650.jpg'
        )
    ir574 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'The Jimmy Conway').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wbcvyo1535794478.jpg'
        )
    ir575 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Texas Rattlesnake').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rtohqp1504889750.jpg'
        )
    ir576 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Tommy\'s Margarita').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/loezxn1504373874.jpg'
        )
    ir577 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'The Strange Weaver').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/opxjzh1604179528.jpg'
        )
    ir578 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'The Evil Blue Thing').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ojnpz71504793059.jpg'
        )
    ir579 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Vesper').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mtdxpa1504374514.jpg'
        )
    ir580 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Victor').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/voapgc1492976416.jpg'
        )
    ir581 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Vampiro').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yfhn371504374246.jpg'
        )
    ir582 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Vesuvio').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/26cq601492976203.jpg'
        )
    ir583 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Veteran').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/iwml9t1492976255.jpg'
        )
    ir584 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Van Vleet').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/fgq2bl1492975771.jpg'
        )
    ir585 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Fizz').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xwxyux1441254243.jpg'
        )
    ir586 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Lemon').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/mql55h1643820632.jpg'
        )
    ir587 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Slime').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/apex461643588115.jpg'
        )
    ir588 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Tonic').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/9koz3f1643821062.jpg'
        )
    ir589 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Martini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qyxrqw1439906528.jpg'
        )
    ir590 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Vodka Russian').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/rpttur1454515129.jpg'
        )
    ir591 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Vermouth Cassis').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/tswpxx1441554674.jpg'
        )
    ir592 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Victory Collins').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/lx0lvs1492976619.jpg'
        )
    ir593 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Vodka And Tonic').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/lmj2yt1504820500.jpg'
        )
    ir594 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Valencia Cocktail').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/9myuc11492975640.jpg'
        )
    ir595 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Whisky Mac').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yvvwys1461867858.jpg'
        )
    ir596 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'White Lady').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/jofsaz1504352991.jpg'
        )
    ir597 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Wine Punch').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/txustu1473344310.jpg'
        )
    ir598 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Wine Cooler').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/yutxtv1473344210.jpg'
        )
    ir599 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Winter Rita').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/fwpd0v1614006733.jpg'
        )
    ir600 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Whiskey Sour').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/hbkfsh1589574990.jpg'
        )
    ir601 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'White Russian').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/vsrupw1472405732.jpg'
        )
    ir602 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Winter Paloma').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/u5f0pz1614007748.jpg'
        )
    ir603 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'White Wine Sangria').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/hnuod91587851576.jpg'
        )
    ir604 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Whitecap Margarita').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/srpxxp1441209622.jpg'
        )
    ir605 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Waikiki Beachcomber').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/ysuqus1441208583.jpg'
        )
    ir606 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Yellow Bird').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/2t9r6w1504374811.jpg'
        )
    ir607 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Yoghurt Cooler').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/trttrv1441254466.jpg'
        )
    ir608 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Zorro').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/kvvd4z1485621283.jpg'
        )
    ir609 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Zinger').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/iixv4l1485620014.jpg'
        )
    ir611 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Zombie').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/2en3jk1509557725.jpg'
        )
    ir612 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Zambeer').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/bje5401485619578.jpg'
        )
    ir613 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Zorbatini').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/wtkqgb1485621155.jpg'
        )
    ir614 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Zenmeister').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/qyuvsu1479209462.jpg'
        )
    ir615 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Zipperhead').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/r2qzhu1485620235.jpg'
        )
    ir616 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Zima Blaster').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/1wifuv1485619797.jpg'
        )
    ir617 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Zizi Coin-coin').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/0fbo2t1485620752.jpg'
        )
    ir618 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Zimadori Zinger').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/bw8gzx1485619920.jpg'
        )
    ir619 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Zippy\'s Revenge').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/1sqm7n1485620312.jpg'
        )
    ir620 = RecipeImage(
        recipe_id=Recipe.query.filter(Recipe.name == 'Ziemes Martini Apfelsaft').first().id,
        url='https://www.thecocktaildb.com/images/media/drink/xnzr2p1485619687.jpg'
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
    db.session.add(ir263)
    db.session.add(ir264)
    db.session.add(ir265)
    db.session.add(ir266)
    db.session.add(ir267)
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
    db.session.add(ir285)
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
    db.session.add(ir372)
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
    db.session.add(ir384)
    db.session.add(ir385)
    db.session.add(ir386)
    db.session.add(ir387)
    db.session.add(ir388)
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
    db.session.add(ir496)
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
    db.session.add(ir528)
    db.session.add(ir529)
    db.session.add(ir530)
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
    db.session.add(ir553)
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

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the recipe_images table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_recipe_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipe_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM recipe_images"))

    db.session.commit()
