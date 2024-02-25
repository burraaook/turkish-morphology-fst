import pywrapfst as fst

# word: "şehir"
def create_fst_01(symbol_table):
    fst_var = fst.Fst()

    # add 16 states
    s0 = fst_var.add_state()
    s1 = fst_var.add_state()
    s2 = fst_var.add_state()
    s3 = fst_var.add_state()
    s4 = fst_var.add_state()
    s5 = fst_var.add_state()
    s6 = fst_var.add_state()
    s7 = fst_var.add_state()
    s8 = fst_var.add_state()
    s9 = fst_var.add_state()
    s10 = fst_var.add_state()
    s11 = fst_var.add_state()
    s12 = fst_var.add_state()
    s13 = fst_var.add_state()
    s14 = fst_var.add_state()
    s15 = fst_var.add_state()
    s16 = fst_var.add_state()

    symbol_table.add_symbol("r + <N>")
    symbol_table.add_symbol("ir + <N>")

    # add arcs
    
    # Noun arcs
    fst_var.add_arc(s0, fst.Arc(symbol_table.find("ş"), symbol_table.find("ş"), fst.Weight.One(fst_var.weight_type()), s1))
    fst_var.add_arc(s1, fst.Arc(symbol_table.find("e"), symbol_table.find("e"), fst.Weight.One(fst_var.weight_type()), s2))
    fst_var.add_arc(s2, fst.Arc(symbol_table.find("h"), symbol_table.find("h"), fst.Weight.One(fst_var.weight_type()), s3))
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("i"), symbol_table.find("i"), fst.Weight.One(fst_var.weight_type()), s4))
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("r"), symbol_table.find("r + <N>"), fst.Weight.One(fst_var.weight_type()), s5)) # + <N> for noun


    # Plural arc
    fst_var.add_arc(s5, fst.Arc(symbol_table.find("l"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s6))
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("e"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s7))
    fst_var.add_arc(s7, fst.Arc(symbol_table.find("r"), symbol_table.find(" + <Pl>"), fst.Weight.One(fst_var.weight_type()), s8)) # + <Pl> for plural

    # Possessive arcs
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("r"), symbol_table.find("ir + <N>"), fst.Weight.One(fst_var.weight_type()), s9))
    fst_var.add_arc(s9, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s10)) # ir + <N> for possessive noun
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s11)) # + <p1s> for possessive 1st person singular
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s12)) # + <p2s> for possessive 2nd person singular
    fst_var.add_arc(s11, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s13))
    fst_var.add_arc(s12, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s14))
    fst_var.add_arc(s13, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p1p>"), fst.Weight.One(fst_var.weight_type()), s15)) # + <p1p> for possessive 1st person plural
    fst_var.add_arc(s14, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p2p>"), fst.Weight.One(fst_var.weight_type()), s16)) # + <p2p> for possessive 2nd person plural


    # Plural + Possessive arcs
    fst_var.add_arc(s8, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s10))

    # final states
    fst_var.set_final(s5)
    fst_var.set_final(s8)
    fst_var.set_final(s10)
    fst_var.set_final(s11)
    fst_var.set_final(s12)
    fst_var.set_final(s15)
    fst_var.set_final(s16)

    # set start state
    fst_var.set_start(s0)

    return fst_var

# word: "yemek"
def create_fst_02(symbol_table):
    fst_var = fst.Fst()

    # add states
    s0 = fst_var.add_state()
    s1 = fst_var.add_state()
    s2 = fst_var.add_state()
    s3 = fst_var.add_state()
    s4 = fst_var.add_state()
    s5 = fst_var.add_state()
    s6 = fst_var.add_state()
    s7 = fst_var.add_state()
    s8 = fst_var.add_state()
    s9 = fst_var.add_state()
    s10 = fst_var.add_state()
    s11 = fst_var.add_state()
    s12 = fst_var.add_state()
    s13 = fst_var.add_state()
    s14 = fst_var.add_state()
    s15 = fst_var.add_state()
    s16 = fst_var.add_state()

    symbol_table.add_symbol("k + <N>")
    

    # add arcs
    
    # Noun arcs
    fst_var.add_arc(s0, fst.Arc(symbol_table.find("y"), symbol_table.find("y"), fst.Weight.One(fst_var.weight_type()), s1))
    fst_var.add_arc(s1, fst.Arc(symbol_table.find("e"), symbol_table.find("e"), fst.Weight.One(fst_var.weight_type()), s2))
    fst_var.add_arc(s2, fst.Arc(symbol_table.find("m"), symbol_table.find("m"), fst.Weight.One(fst_var.weight_type()), s3))
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("e"), symbol_table.find("e"), fst.Weight.One(fst_var.weight_type()), s4))
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("k"), symbol_table.find("k + <N>"), fst.Weight.One(fst_var.weight_type()), s5)) # + <N> for noun

    # plural arc
    fst_var.add_arc(s5, fst.Arc(symbol_table.find("l"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s6))
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("e"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s7))
    fst_var.add_arc(s7, fst.Arc(symbol_table.find("r"), symbol_table.find(" + <Pl>"), fst.Weight.One(fst_var.weight_type()), s8)) # + <Pl> for plural

    # possessive arcs
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("ğ"), symbol_table.find("k + <N>"), fst.Weight.One(fst_var.weight_type()), s9))
    fst_var.add_arc(s9, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s10)) # k + <N> for possessive noun
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s11)) # + <p1s> for possessive 1st person singular
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s12)) # + <p2s> for possessive 2nd person singular
    fst_var.add_arc(s11, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s13))
    fst_var.add_arc(s12, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s14))
    fst_var.add_arc(s13, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p1p>"), fst.Weight.One(fst_var.weight_type()), s15)) # + <p1p> for possessive 1st person plural
    fst_var.add_arc(s14, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p2p>"), fst.Weight.One(fst_var.weight_type()), s16)) # + <p2p> for possessive 2nd person plural

    # plural + possessive arcs
    fst_var.add_arc(s8, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s10))

    # final and start states
    fst_var.set_start(s0)
    fst_var.set_final(s5)
    fst_var.set_final(s8)
    fst_var.set_final(s10)
    fst_var.set_final(s11)
    fst_var.set_final(s12)
    fst_var.set_final(s15)
    fst_var.set_final(s16)

    return fst_var

# word: "portre"
def create_fst_03(symbol_table):
    fst_var = fst.Fst()

    # add states
    s0 = fst_var.add_state()
    s1 = fst_var.add_state()
    s2 = fst_var.add_state()
    s3 = fst_var.add_state()
    s4 = fst_var.add_state()
    s5 = fst_var.add_state()
    s6 = fst_var.add_state()
    s7 = fst_var.add_state()
    s8 = fst_var.add_state()
    s9 = fst_var.add_state()
    s10 = fst_var.add_state()
    s11 = fst_var.add_state()
    s12 = fst_var.add_state()
    s13 = fst_var.add_state()
    s14 = fst_var.add_state()
    s15 = fst_var.add_state()
    s16 = fst_var.add_state()
    s17 = fst_var.add_state()
    s18 = fst_var.add_state()

    symbol_table.add_symbol("e + <N>")

    # add arcs
    
    # Noun arcs
    fst_var.add_arc(s0, fst.Arc(symbol_table.find("p"), symbol_table.find("p"), fst.Weight.One(fst_var.weight_type()), s1))
    fst_var.add_arc(s1, fst.Arc(symbol_table.find("o"), symbol_table.find("o"), fst.Weight.One(fst_var.weight_type()), s2))
    fst_var.add_arc(s2, fst.Arc(symbol_table.find("r"), symbol_table.find("r"), fst.Weight.One(fst_var.weight_type()), s3))
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("t"), symbol_table.find("t"), fst.Weight.One(fst_var.weight_type()), s4))
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("r"), symbol_table.find("r"), fst.Weight.One(fst_var.weight_type()), s5))
    fst_var.add_arc(s5, fst.Arc(symbol_table.find("e"), symbol_table.find("e + <N>"), fst.Weight.One(fst_var.weight_type()), s6)) # + <N> for noun

    # plural arc
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("l"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s7))
    fst_var.add_arc(s7, fst.Arc(symbol_table.find("e"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s8))
    fst_var.add_arc(s8, fst.Arc(symbol_table.find("r"), symbol_table.find(" + <Pl>"), fst.Weight.One(fst_var.weight_type()), s9)) # + <Pl> for plural

    # possessive arcs
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s10)) # + <p1s> for possessive 1st person singular
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s11)) # + <p2s> for possessive 2nd person singular
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("s"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s12))
    fst_var.add_arc(s12, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s13)) # possessive 3rd person singular/plural
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s14))
    fst_var.add_arc(s11, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s15))
    fst_var.add_arc(s14, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p1p>"), fst.Weight.One(fst_var.weight_type()), s16)) # + <p1p> for possessive 1st person plural
    fst_var.add_arc(s15, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p2p>"), fst.Weight.One(fst_var.weight_type()), s17)) # + <p2p> for possessive 2nd person plural

    # plural + possessive arcs
    fst_var.add_arc(s9, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s18)) # possessive 3rd person singular/plural
    fst_var.add_arc(s18, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s10)) # + <p1p> for possessive 1st person singular
    fst_var.add_arc(s18, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s11)) # + <p2p> for possessive 2nd person singular

    # final and start states
    fst_var.set_start(s0)
    fst_var.set_final(s6)
    fst_var.set_final(s9)
    fst_var.set_final(s10)
    fst_var.set_final(s11)
    fst_var.set_final(s13)
    fst_var.set_final(s16)
    fst_var.set_final(s17)
    fst_var.set_final(s18)

    return fst_var

# word: "robot"
def create_fst_04(symbol_table):
    fst_var = fst.Fst()

    # add states
    s0 = fst_var.add_state()
    s1 = fst_var.add_state()
    s2 = fst_var.add_state()
    s3 = fst_var.add_state()
    s4 = fst_var.add_state()
    s5 = fst_var.add_state()
    s6 = fst_var.add_state()
    s7 = fst_var.add_state()
    s8 = fst_var.add_state()
    s9 = fst_var.add_state()
    s10 = fst_var.add_state()
    s11 = fst_var.add_state()
    s12 = fst_var.add_state()
    s13 = fst_var.add_state()
    s14 = fst_var.add_state()
    s15 = fst_var.add_state()
    s16 = fst_var.add_state()
    s17 = fst_var.add_state()
    s18 = fst_var.add_state()
    s19 = fst_var.add_state()
    s20 = fst_var.add_state()
    s21 = fst_var.add_state()
    s22 = fst_var.add_state()

    symbol_table.add_symbol("t + <N>")

    # add arcs
    fst_var.add_arc(s0, fst.Arc(symbol_table.find("r"), symbol_table.find("r"), fst.Weight.One(fst_var.weight_type()), s1))
    fst_var.add_arc(s1, fst.Arc(symbol_table.find("o"), symbol_table.find("o"), fst.Weight.One(fst_var.weight_type()), s2))
    fst_var.add_arc(s2, fst.Arc(symbol_table.find("b"), symbol_table.find("b"), fst.Weight.One(fst_var.weight_type()), s3))
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("o"), symbol_table.find("o"), fst.Weight.One(fst_var.weight_type()), s4))
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("t"), symbol_table.find("t + <N>"), fst.Weight.One(fst_var.weight_type()), s5)) # + <N> for noun

    # plural arc
    fst_var.add_arc(s5, fst.Arc(symbol_table.find("l"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s6))
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("a"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s7))
    fst_var.add_arc(s7, fst.Arc(symbol_table.find("r"), symbol_table.find(" + <Pl>"), fst.Weight.One(fst_var.weight_type()), s8)) # + <Pl> for plural

    # possessive arcs
    fst_var.add_arc(s5, fst.Arc(symbol_table.find("u"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s9)) # possessive 3rd person singular/plural
    fst_var.add_arc(s9, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s10)) # + <p1s> for possessive 1st person singular
    fst_var.add_arc(s9, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s11)) # + <p2s> for possessive 2nd person singular
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("u"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s12))
    fst_var.add_arc(s11, fst.Arc(symbol_table.find("u"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s13))
    fst_var.add_arc(s12, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p1p>"), fst.Weight.One(fst_var.weight_type()), s14)) # + <p1p> for possessive 1st person plural
    fst_var.add_arc(s13, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p2p>"), fst.Weight.One(fst_var.weight_type()), s15)) # + <p2p> for possessive 2nd person plural

    # plural + possessive arcs
    fst_var.add_arc(s8, fst.Arc(symbol_table.find("ı"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s16)) # possessive 3rd person singular/plural
    fst_var.add_arc(s16, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s17)) # + <p1p> for possessive 1st person singular
    fst_var.add_arc(s16, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s18)) # + <p2p> for possessive 2nd person singular
    fst_var.add_arc(s17, fst.Arc(symbol_table.find("ı"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s19))
    fst_var.add_arc(s18, fst.Arc(symbol_table.find("ı"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s20))
    fst_var.add_arc(s19, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p1p>"), fst.Weight.One(fst_var.weight_type()), s21)) # + <p1p> for possessive 1st person plural
    fst_var.add_arc(s20, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p2p>"), fst.Weight.One(fst_var.weight_type()), s22)) # + <p2p> for possessive 2nd person plural

    # final and start states
    fst_var.set_start(s0)
    fst_var.set_final(s5)
    fst_var.set_final(s8)
    fst_var.set_final(s9)
    fst_var.set_final(s10)
    fst_var.set_final(s11)
    fst_var.set_final(s14)
    fst_var.set_final(s15)
    fst_var.set_final(s16)
    fst_var.set_final(s17)
    fst_var.set_final(s18)
    fst_var.set_final(s21)
    fst_var.set_final(s22)

    return fst_var

# word: "metin"
def create_fst_05(symbol_table):
    fst_var = fst.Fst()

    # add states
    s0 = fst_var.add_state()
    s1 = fst_var.add_state()
    s2 = fst_var.add_state()
    s3 = fst_var.add_state()
    s4 = fst_var.add_state()
    s5 = fst_var.add_state()
    s6 = fst_var.add_state()
    s7 = fst_var.add_state()
    s8 = fst_var.add_state()
    s9 = fst_var.add_state()
    s10 = fst_var.add_state()
    s11 = fst_var.add_state()
    s12 = fst_var.add_state()
    s13 = fst_var.add_state()
    s14 = fst_var.add_state()
    s15 = fst_var.add_state()
    s16 = fst_var.add_state()

    symbol_table.add_symbol("n + <N>")
    symbol_table.add_symbol("in + <N>")

    # add arcs
    fst_var.add_arc(s0, fst.Arc(symbol_table.find("m"), symbol_table.find("m"), fst.Weight.One(fst_var.weight_type()), s1))
    fst_var.add_arc(s1, fst.Arc(symbol_table.find("e"), symbol_table.find("e"), fst.Weight.One(fst_var.weight_type()), s2))
    fst_var.add_arc(s2, fst.Arc(symbol_table.find("t"), symbol_table.find("t"), fst.Weight.One(fst_var.weight_type()), s3))
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("i"), symbol_table.find("i"), fst.Weight.One(fst_var.weight_type()), s4))
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("n"), symbol_table.find("n + <N>"), fst.Weight.One(fst_var.weight_type()), s5)) # + <N> for noun

    # plural arc
    fst_var.add_arc(s5, fst.Arc(symbol_table.find("l"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s6))
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("e"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s7))
    fst_var.add_arc(s7, fst.Arc(symbol_table.find("r"), symbol_table.find(" + <Pl>"), fst.Weight.One(fst_var.weight_type()), s8)) # + <Pl> for plural

    # possessive arcs
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("n"), symbol_table.find("in + <N>"), fst.Weight.One(fst_var.weight_type()), s9))
    fst_var.add_arc(s9, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s10)) # in + <N> for possessive noun
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s11)) # + <p1s> for possessive 1st person singular
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s12)) # + <p2s> for possessive 2nd person singular
    fst_var.add_arc(s11, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s13))
    fst_var.add_arc(s12, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s14))
    fst_var.add_arc(s13, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p1p>"), fst.Weight.One(fst_var.weight_type()), s15)) # + <p1p> for possessive 1st person plural
    fst_var.add_arc(s14, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p2p>"), fst.Weight.One(fst_var.weight_type()), s16)) # + <p2p> for possessive 2nd person plural

    # plural + possessive arcs
    fst_var.add_arc(s8, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s10))

    # final and start states
    fst_var.set_start(s0)
    fst_var.set_final(s5)
    fst_var.set_final(s8)
    fst_var.set_final(s10)
    fst_var.set_final(s11)
    fst_var.set_final(s12)
    fst_var.set_final(s15)
    fst_var.set_final(s16)

    return fst_var

# word: "tahmin"
def create_fst_06(symbol_table):
    fst_var = fst.Fst()

    # add states
    s0 = fst_var.add_state()
    s1 = fst_var.add_state()
    s2 = fst_var.add_state()
    s3 = fst_var.add_state()
    s4 = fst_var.add_state()
    s5 = fst_var.add_state()
    s6 = fst_var.add_state()
    s7 = fst_var.add_state()
    s8 = fst_var.add_state()
    s9 = fst_var.add_state()
    s10 = fst_var.add_state()
    s11 = fst_var.add_state()
    s12 = fst_var.add_state()
    s13 = fst_var.add_state()
    s14 = fst_var.add_state()
    s15 = fst_var.add_state()
    s16 = fst_var.add_state()

    symbol_table.add_symbol("n + <N>")
    
    # add arcs
    fst_var.add_arc(s0, fst.Arc(symbol_table.find("t"), symbol_table.find("t"), fst.Weight.One(fst_var.weight_type()), s1))
    fst_var.add_arc(s1, fst.Arc(symbol_table.find("a"), symbol_table.find("a"), fst.Weight.One(fst_var.weight_type()), s2))
    fst_var.add_arc(s2, fst.Arc(symbol_table.find("h"), symbol_table.find("h"), fst.Weight.One(fst_var.weight_type()), s3))
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("m"), symbol_table.find("m"), fst.Weight.One(fst_var.weight_type()), s4))
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("i"), symbol_table.find("i"), fst.Weight.One(fst_var.weight_type()), s5))
    fst_var.add_arc(s5, fst.Arc(symbol_table.find("n"), symbol_table.find("n + <N>"), fst.Weight.One(fst_var.weight_type()), s6)) # + <N> for noun

    # plural arc
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("l"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s7))
    fst_var.add_arc(s7, fst.Arc(symbol_table.find("e"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s8))
    fst_var.add_arc(s8, fst.Arc(symbol_table.find("r"), symbol_table.find(" + <Pl>"), fst.Weight.One(fst_var.weight_type()), s9)) # + <Pl> for plural

    # possessive arcs
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s10)) # possessive 3rd person singular/plural
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s11)) # + <p1s> for possessive 1st person singular
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s12)) # + <p2s> for possessive 2nd person singular
    fst_var.add_arc(s11, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s13))
    fst_var.add_arc(s12, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s14))
    fst_var.add_arc(s13, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p1p>"), fst.Weight.One(fst_var.weight_type()), s15)) # + <p1p> for possessive 1st person plural
    fst_var.add_arc(s14, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p2p>"), fst.Weight.One(fst_var.weight_type()), s16)) # + <p2p> for possessive 2nd person plural

    # plural + possessive arcs
    fst_var.add_arc(s9, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s10)) # possessive 3rd person singular/plural

    # final and start states
    fst_var.set_start(s0)
    fst_var.set_final(s6)
    fst_var.set_final(s9)
    fst_var.set_final(s10)
    fst_var.set_final(s11)
    fst_var.set_final(s12)
    fst_var.set_final(s15)
    fst_var.set_final(s16)

    return fst_var

# word: "ders"
def create_fst_07(symbol_table):
    fst_var = fst.Fst()

    # add states
    s0 = fst_var.add_state()
    s1 = fst_var.add_state()
    s2 = fst_var.add_state()
    s3 = fst_var.add_state()
    s4 = fst_var.add_state()
    s5 = fst_var.add_state()
    s6 = fst_var.add_state()
    s7 = fst_var.add_state()
    s8 = fst_var.add_state()
    s9 = fst_var.add_state()
    s10 = fst_var.add_state()
    s11 = fst_var.add_state()
    s12 = fst_var.add_state()
    s13 = fst_var.add_state()
    s14 = fst_var.add_state()

    symbol_table.add_symbol("s + <N>")

    # add arcs
    fst_var.add_arc(s0, fst.Arc(symbol_table.find("d"), symbol_table.find("d"), fst.Weight.One(fst_var.weight_type()), s1))
    fst_var.add_arc(s1, fst.Arc(symbol_table.find("e"), symbol_table.find("e"), fst.Weight.One(fst_var.weight_type()), s2))
    fst_var.add_arc(s2, fst.Arc(symbol_table.find("r"), symbol_table.find("r"), fst.Weight.One(fst_var.weight_type()), s3))
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("s"), symbol_table.find("s + <N>"), fst.Weight.One(fst_var.weight_type()), s4)) # + <N> for noun

    # plural arc
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("l"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s5))
    fst_var.add_arc(s5, fst.Arc(symbol_table.find("e"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s6))
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("r"), symbol_table.find(" + <Pl>"), fst.Weight.One(fst_var.weight_type()), s7)) # + <Pl> for plural

    # possessive arcs
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s8)) # possessive 3rd person singular/plural
    fst_var.add_arc(s8, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s9)) # + <p1s> for possessive 1st person singular
    fst_var.add_arc(s8, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s10)) # + <p2s> for possessive 2nd person singular
    fst_var.add_arc(s9, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s11))
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s12))
    fst_var.add_arc(s11, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p1p>"), fst.Weight.One(fst_var.weight_type()), s13)) # + <p1p> for possessive 1st person plural
    fst_var.add_arc(s12, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p2p>"), fst.Weight.One(fst_var.weight_type()), s14)) # + <p2p> for possessive 2nd person plural

    # plural + possessive arcs
    fst_var.add_arc(s7, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s8)) # possessive 3rd person singular/plural

    # final and start states
    fst_var.set_start(s0)
    fst_var.set_final(s4)
    fst_var.set_final(s7)
    fst_var.set_final(s8)
    fst_var.set_final(s9)
    fst_var.set_final(s10)
    fst_var.set_final(s13)
    fst_var.set_final(s14)

    return fst_var

# word: "süre"
def create_fst_08(symbol_table):
    fst_var = fst.Fst()

    # add states
    s0 = fst_var.add_state()
    s1 = fst_var.add_state()
    s2 = fst_var.add_state()
    s3 = fst_var.add_state()
    s4 = fst_var.add_state()
    s5 = fst_var.add_state()
    s6 = fst_var.add_state()
    s7 = fst_var.add_state()
    s8 = fst_var.add_state()
    s9 = fst_var.add_state()
    s10 = fst_var.add_state()
    s11 = fst_var.add_state()
    s12 = fst_var.add_state()
    s13 = fst_var.add_state()
    s14 = fst_var.add_state()
    s15 = fst_var.add_state()
    s16 = fst_var.add_state()

    symbol_table.add_symbol("e + <N>")
    
    # add arcs
    fst_var.add_arc(s0, fst.Arc(symbol_table.find("s"), symbol_table.find("s"), fst.Weight.One(fst_var.weight_type()), s1))
    fst_var.add_arc(s1, fst.Arc(symbol_table.find("ü"), symbol_table.find("ü"), fst.Weight.One(fst_var.weight_type()), s2))
    fst_var.add_arc(s2, fst.Arc(symbol_table.find("r"), symbol_table.find("r"), fst.Weight.One(fst_var.weight_type()), s3))
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("e"), symbol_table.find("e + <N>"), fst.Weight.One(fst_var.weight_type()), s4)) # + <N> for noun

    # plural arc
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("l"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s5))
    fst_var.add_arc(s5, fst.Arc(symbol_table.find("e"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s6))
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("r"), symbol_table.find(" + <Pl>"), fst.Weight.One(fst_var.weight_type()), s7)) # + <Pl> for plural

    # possessive arcs
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s8)) # + <p1s> for possessive 1st person singular
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s9)) # + <p2s> for possessive 2nd person singular
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("s"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s10))
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s11)) # possessive 3rd person singular/plural
    fst_var.add_arc(s8, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s12))
    fst_var.add_arc(s9, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s13))
    fst_var.add_arc(s12, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p1p>"), fst.Weight.One(fst_var.weight_type()), s14)) # + <p1p> for possessive 1st person plural
    fst_var.add_arc(s13, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p2p>"), fst.Weight.One(fst_var.weight_type()), s15)) # + <p2p> for possessive 2nd person plural

    # plural + possessive arcs
    fst_var.add_arc(s7, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s16)) # possessive 3rd person singular/plural
    fst_var.add_arc(s16, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s8)) # + <p1p> for possessive 1st person singular
    fst_var.add_arc(s16, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s9)) # + <p2p> for possessive 2nd person singular

    # final and start states
    fst_var.set_start(s0)
    fst_var.set_final(s4)
    fst_var.set_final(s7)
    fst_var.set_final(s8)
    fst_var.set_final(s9)
    fst_var.set_final(s11)
    fst_var.set_final(s14)
    fst_var.set_final(s15)
    fst_var.set_final(s16)

    return fst_var

# word: "bina"
def create_fst_09(symbol_table):
    fst_var = fst.Fst()

    # add states
    s0 = fst_var.add_state()
    s1 = fst_var.add_state()
    s2 = fst_var.add_state()
    s3 = fst_var.add_state()
    s4 = fst_var.add_state()
    s5 = fst_var.add_state()
    s6 = fst_var.add_state()
    s7 = fst_var.add_state()
    s8 = fst_var.add_state()
    s9 = fst_var.add_state()
    s10 = fst_var.add_state()
    s11 = fst_var.add_state()
    s12 = fst_var.add_state()
    s13 = fst_var.add_state()
    s14 = fst_var.add_state()
    s15 = fst_var.add_state()

    symbol_table.add_symbol("a + <N>")
    
    # add arcs
    fst_var.add_arc(s0, fst.Arc(symbol_table.find("b"), symbol_table.find("b"), fst.Weight.One(fst_var.weight_type()), s1))
    fst_var.add_arc(s1, fst.Arc(symbol_table.find("i"), symbol_table.find("i"), fst.Weight.One(fst_var.weight_type()), s2))
    fst_var.add_arc(s2, fst.Arc(symbol_table.find("n"), symbol_table.find("n"), fst.Weight.One(fst_var.weight_type()), s3))
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("a"), symbol_table.find("a + <N>"), fst.Weight.One(fst_var.weight_type()), s4)) # + <N> for noun

    # plural arc
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("l"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s5))
    fst_var.add_arc(s5, fst.Arc(symbol_table.find("a"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s6))
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("r"), symbol_table.find(" + <Pl>"), fst.Weight.One(fst_var.weight_type()), s7)) # + <Pl> for plural

    # possessive arcs
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s8)) # + <p1s> for possessive 1st person singular
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s9)) # + <p2s> for possessive 2nd person singular
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("s"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s10))
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("ı"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s11)) # possessive 3rd person singular/plural
    fst_var.add_arc(s8, fst.Arc(symbol_table.find("ı"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s12))
    fst_var.add_arc(s9, fst.Arc(symbol_table.find("ı"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s13))
    fst_var.add_arc(s12, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p1p>"), fst.Weight.One(fst_var.weight_type()), s14)) # + <p1p> for possessive 1st person plural
    fst_var.add_arc(s13, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p2p>"), fst.Weight.One(fst_var.weight_type()), s14)) # + <p2p> for possessive 2nd person plural

    # plural + possessive arcs
    fst_var.add_arc(s7, fst.Arc(symbol_table.find("ı"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s15)) # possessive 3rd person singular/plural
    fst_var.add_arc(s15, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s8)) # + <p1p> for possessive 1st person singular
    fst_var.add_arc(s15, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s9)) # + <p2p> for possessive 2nd person singular

    # final and start states
    fst_var.set_start(s0)
    fst_var.set_final(s4)
    fst_var.set_final(s7)
    fst_var.set_final(s8)
    fst_var.set_final(s9)
    fst_var.set_final(s11)
    fst_var.set_final(s14)
    fst_var.set_final(s15)

    return fst_var

# word: "kedi"
def create_fst_10(symbol_table):
    fst_var = fst.Fst()

    # add states
    s0 = fst_var.add_state()
    s1 = fst_var.add_state()
    s2 = fst_var.add_state()
    s3 = fst_var.add_state()
    s4 = fst_var.add_state()
    s5 = fst_var.add_state()
    s6 = fst_var.add_state()
    s7 = fst_var.add_state()
    s8 = fst_var.add_state()
    s9 = fst_var.add_state()
    s10 = fst_var.add_state()
    s11 = fst_var.add_state()
    s12 = fst_var.add_state()
    s13 = fst_var.add_state()
    s14 = fst_var.add_state()
    s15 = fst_var.add_state()
    s16 = fst_var.add_state()

    symbol_table.add_symbol("i + <N>")
    
    # add arcs
    fst_var.add_arc(s0, fst.Arc(symbol_table.find("k"), symbol_table.find("k"), fst.Weight.One(fst_var.weight_type()), s1))
    fst_var.add_arc(s1, fst.Arc(symbol_table.find("e"), symbol_table.find("e"), fst.Weight.One(fst_var.weight_type()), s2))
    fst_var.add_arc(s2, fst.Arc(symbol_table.find("d"), symbol_table.find("d"), fst.Weight.One(fst_var.weight_type()), s3))
    fst_var.add_arc(s3, fst.Arc(symbol_table.find("i"), symbol_table.find("i + <N>"), fst.Weight.One(fst_var.weight_type()), s4)) # + <N> for noun

    # plural arc
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("l"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s5))
    fst_var.add_arc(s5, fst.Arc(symbol_table.find("e"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s6))
    fst_var.add_arc(s6, fst.Arc(symbol_table.find("r"), symbol_table.find(" + <Pl>"), fst.Weight.One(fst_var.weight_type()), s7)) # + <Pl> for plural

    # possessive arcs
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("s"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s8))
    fst_var.add_arc(s8, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s9)) # possessive 3rd person singular/plural
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s10)) # + <p1s> for possessive 1st person singular
    fst_var.add_arc(s4, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s11)) # + <p2s> for possessive 2nd person singular
    fst_var.add_arc(s10, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s12))
    fst_var.add_arc(s11, fst.Arc(symbol_table.find("i"), symbol_table.find("<eps>"), fst.Weight.One(fst_var.weight_type()), s13))
    fst_var.add_arc(s12, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p1p>"), fst.Weight.One(fst_var.weight_type()), s14)) # + <p1p> for possessive 1st person plural
    fst_var.add_arc(s13, fst.Arc(symbol_table.find("z"), symbol_table.find(" + <p2p>"), fst.Weight.One(fst_var.weight_type()), s15)) # + <p2p> for possessive 2nd person plural

    # plural + possessive arcs
    fst_var.add_arc(s7, fst.Arc(symbol_table.find("i"), symbol_table.find(" + <p3s>/<p3p>"), fst.Weight.One(fst_var.weight_type()), s16)) # possessive 3rd person singular/plural
    fst_var.add_arc(s16, fst.Arc(symbol_table.find("m"), symbol_table.find(" + <p1s>"), fst.Weight.One(fst_var.weight_type()), s10)) # + <p1p> for possessive 1st person singular
    fst_var.add_arc(s16, fst.Arc(symbol_table.find("n"), symbol_table.find(" + <p2s>"), fst.Weight.One(fst_var.weight_type()), s11)) # + <p2p> for possessive 2nd person singular

    # final and start states
    fst_var.set_start(s0)
    fst_var.set_final(s4)
    fst_var.set_final(s7)
    fst_var.set_final(s9)
    fst_var.set_final(s10)
    fst_var.set_final(s11)
    fst_var.set_final(s14)
    fst_var.set_final(s15)
    fst_var.set_final(s16)

    return fst_var


def create_fst():

    # add symbols
    symbols = fst.SymbolTable()
    
    symbols.add_symbol("<eps>")
    symbols.add_symbol("<err>")

    # add turkish alphabet
    for letter in "abcçdefgğhıijklmnoöprsştuüvyz":
        symbols.add_symbol(letter)

    symbols.add_symbol(" + <N>")
    symbols.add_symbol(" + <Pl>")
    symbols.add_symbol(" + <p1s>")
    symbols.add_symbol(" + <p2s>")
    symbols.add_symbol(" + <p3s>")
    symbols.add_symbol(" + <p1p>")
    symbols.add_symbol(" + <p2p>")
    symbols.add_symbol(" + <p3p>")
    symbols.add_symbol(" + <p3s>/<p3p>")
    
    # one big fst for all words
    fst_var = fst.Fst()
    
    fst_01 = create_fst_01(symbols)

    fst_var = fst_01.union(create_fst_02(symbols))
    fst_var = fst_var.union(create_fst_03(symbols))
    fst_var = fst_var.union(create_fst_04(symbols))
    fst_var = fst_var.union(create_fst_05(symbols))
    fst_var = fst_var.union(create_fst_06(symbols))
    fst_var = fst_var.union(create_fst_07(symbols))
    fst_var = fst_var.union(create_fst_08(symbols))
    fst_var = fst_var.union(create_fst_09(symbols))
    fst_var = fst_var.union(create_fst_10(symbols))

    fst_var = fst.determinize(fst_var)

    return fst_var, symbols

def test_fst(word, fst_var, symbols):
    state = fst_var.start()
    buffer = []
    i = 0

    while i < len(word):
        letter = word[i]
        arc_found = False

        # first, check for non-epsilon transitions
        for arc in fst_var.arcs(state):
            if symbols.find(letter) == arc.ilabel:
                state = arc.nextstate
                if arc.olabel != symbols.find("<eps>"):
                    label_str = symbols.find(arc.olabel).decode('utf-8')
                    if not (label_str.startswith(" + <p") and letter != word[-1]):
                        buffer.append(arc.olabel)
                arc_found = True
                i += 1
                break

        # if no non-epsilon transition is found, check for epsilon transitions
        if not arc_found:
            for arc in fst_var.arcs(state):
                if symbols.find(arc.ilabel).decode('utf-8') == '<eps>':
                    state = arc.nextstate
                    if arc.olabel != symbols.find("<eps>"):
                        buffer.append(arc.olabel)
                    arc_found = True
                    break

        # if no transition is found, exit the loop
        if not arc_found:
            print(f"'{word}' -> invalid")
            return

    # check if the final state is valid
    if fst_var.final(state) != fst.Weight.Zero(fst_var.weight_type()):
        buffer_output = [symbols.find(s).decode('utf-8') for s in buffer]
        print(f"'{word}' -> {''.join(buffer_output)}")
    else:
        print(f"'{word}' -> invalid")