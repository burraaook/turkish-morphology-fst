import pywrapfst as fst
import word_fsts

# words: {şehir, yemek, portre, robot, metin, tahmin, ders, süre, bina, kedi}

fst_var, symbols = word_fsts.create_fst()
word_set_01 = ["şehir", "şehirler", "şehrim", "şehrin", "şehri", "şehrimiz", "şehriniz", "şehirlerim",
               "şehirlerin", "şehirlerimiz", "şehirleriniz", "şehirleri", "şehrimizler", "şehirden", "şehrimizde", "şehr"]

word_set_02 = ["yemek", "yemekler", "yemeğim", "yemeğin", "yemeği", "yemeğimiz", "yemeğiniz", "yemeklerim",
               "yemeklerin", "yemeklerimiz", "yemekleriniz", "yemekleri", "yemeğimler", "yemekten", "yemeğimde", "yemeğ"]

word_set_03 = ["portre", "portreler", "portrem", "portren", "portresi", "portremiz", "portreniz", "portrelerim",
                "portrelerin", "portrelerimiz", "portreleriniz", "portreleri", "portremizler", "portreden", "portremde"]

word_set_04 = ["robot", "robotlar", "robotum", "robotun", "robotu", "robotumuz", "robotunuz", "robotlarım",
                "robotların", "robotlarımız", "robotlarınız", "robotları", "robotumuzlar", "robottan", "robotumda"]

word_set_05 = ["metin", "metinler", "metnim", "metnin", "metni", "metnimiz", "metniniz", "metinlerim",
                "metinlerin", "metinlerimiz", "metinleriniz", "metinleri", "metnimizler", "metinden", "metnimde"]

word_set_06 = ["tahmin", "tahminler", "tahminim", "tahminin", "tahmini", "tahminimiz", "tahmininiz", "tahminlerim",
                "tahminlerin", "tahminlerimiz", "tahminleriniz", "tahminleri", "tahminimizler", "tahminden", "tahminimde"]

word_set_07 = ["ders", "dersler", "dersim", "dersin", "dersi", "dersimiz", "dersiniz", "derslerim",
                "derslerin", "derslerimiz", "dersleriniz", "dersleri", "dersimizler", "dersten", "dersimde"]

word_set_08 = ["süre", "süreler", "sürem", "süren", "süresi", "süremiz", "süreniz", "sürelerim",
                "sürelerin", "sürelerimiz", "süreleriniz", "süreleri", "süremizler", "süreden", "süremde"]

word_set_09 = ["bina", "binalar", "binam", "binan", "binası", "binamız", "binanız", "binalarım",
                "binaların", "binalarımız", "binalarınız", "binaları", "binamızlar", "binadan", "binamda"]

word_set_10 = ["kedi", "kediler", "kedim", "kedin", "kedisi", "kedimiz", "kediniz", "kedilerim",
                "kedilerin", "kedilerimiz", "kedileriniz", "kedileri", "kedimizler", "kediden", "kedimde"]

all_words = word_set_01 + word_set_02 + word_set_03 + word_set_04 + word_set_05 + word_set_06 + word_set_07 + word_set_08 + word_set_09 + word_set_10

for word in all_words:
    word_fsts.test_fst(word, fst_var, symbols)