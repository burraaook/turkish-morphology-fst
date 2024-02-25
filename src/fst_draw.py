import pywrapfst as fst
import word_fsts
import os

# words: {şehir, yemek, portre, robot, metin, tahmin, ders, süre, bina, kedi}
# add symbols
fst_final, symbols = word_fsts.create_fst()

# draw all fsts
fst_01 = word_fsts.create_fst_01(symbols)
fst_01.minimize()
fst_01.draw('fst_sehir.dot', isymbols=symbols, osymbols=symbols, portrait=True)

fst_02 = word_fsts.create_fst_02(symbols)
fst_02.minimize()
fst_02.draw('fst_yemek.dot', isymbols=symbols, osymbols=symbols, portrait=True)

fst_03 = word_fsts.create_fst_03(symbols)
fst_03.minimize()
fst_03.draw('fst_portre.dot', isymbols=symbols, osymbols=symbols, portrait=True)

fst_04 = word_fsts.create_fst_04(symbols)
fst_04.minimize()
fst_04.draw('fst_robot.dot', isymbols=symbols, osymbols=symbols, portrait=True)

fst_05 = word_fsts.create_fst_05(symbols)
fst_05.minimize()
fst_05.draw('fst_metin.dot', isymbols=symbols, osymbols=symbols, portrait=True)

fst_06 = word_fsts.create_fst_06(symbols)
fst_06.minimize()
fst_06.draw('fst_tahmin.dot', isymbols=symbols, osymbols=symbols, portrait=True)

fst_07 = word_fsts.create_fst_07(symbols)
fst_07.minimize()
fst_07.draw('fst_ders.dot', isymbols=symbols, osymbols=symbols, portrait=True)

fst_08 = word_fsts.create_fst_08(symbols)
fst_08.minimize()
fst_08.draw('fst_süre.dot', isymbols=symbols, osymbols=symbols, portrait=True)

fst_09 = word_fsts.create_fst_09(symbols)
fst_09.minimize()
fst_09.draw('fst_bina.dot', isymbols=symbols, osymbols=symbols, portrait=True)

fst_10 = word_fsts.create_fst_10(symbols)
fst_10.minimize()
fst_10.draw('fst_kedi.dot', isymbols=symbols, osymbols=symbols, portrait=True)

fst_final.minimize()
fst_final.draw('fst_final.dot', isymbols=symbols, osymbols=symbols, portrait=True)

# execute dot -Tpng -o fst_x.png fst_x.dot for each fst
# remove .dot files
array_str = ["sehir", "yemek", "portre", "robot", "metin", "tahmin", "ders", "süre", "bina", "kedi", "final"]
for i in range(11):
    command = "dot -Tpng -o fst_" + array_str[i] + ".png fst_" + array_str[i] + ".dot"
    os.system(command)
    command = "rm fst_" + array_str[i] + ".dot"
    os.system(command)