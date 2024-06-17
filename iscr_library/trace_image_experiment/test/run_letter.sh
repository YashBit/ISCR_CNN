#!/bin/bash


# ONLY TESTING 200 FONTS WITH a! 


letters=(a)
# fonts=("spectral" "cuprum" "accanthis" "Alegreya" "algolrevived" "almendra"
#        "anttor" "antpolt" "gfsartemisia" "gfsartemisia-euler" "baskervald"
#        "bera" "berenis" "LibreBodoni" "tgbonum" "bookman"
#        "librecaslon" "CharisSIL" "cochineal" "concmath" "DejaVuSerif" "gfsdidot"
#        "electrum" "ETbb" "ibarra"
#        "imfellEnglish" "aesupp" "mlmodern" "venturis2" "fbb"
#        "CormorantGaramond" "bookman" "kerkis" "algolrevived" "Arvo" "bitter" "concmath"
#        "electrum" "drm" "chancery"
#        "tgchorus" "aurical")
# typefaces=("normal" "italic" "bold" "bolditalic" "smallcaps" "slanted")

# 39 FONTS -> NEED TO GET TO 200
fonts=()
typefaces=("normal")


for letter in "${letters[@]}"
do
    for font in "${fonts[@]}"
    do
        for typeface in "${typefaces[@]}"
        do
            python letter_generator.py --letter $letter --font $font --typeface $typeface
        done
    done
done
