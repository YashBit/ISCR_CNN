#!/bin/bash


#!/bin/bash


# ONLY TESTING 200 FONTS WITH a! 


letters=(a)
fonts=("lmodern" "spectral" "cuprum" "accanthis" "Alegreya" "algolrevived" "almendra"
       "antiqua" "anttor" "antpolt" "gfsartemisia" "gfsartemisia-euler" "baskervald"
       "QTBengal" "bera" "berenis" "LibreBodoni" "boisik" "tgbonum" "bookman" "QTBookmann"
       "librecaslon" "CharisSIL" "cochineal" "concmath" "covfonts" "DejaVuSerif" "gfsdidot"
       "droidserif" "electrum" "ETbb" "gandhi" "QTGaromand" "QTGraphLite" "ibarra"
       "imfellEnglish" "aesupp" "mlmodern" "roboto" "venturis2" "Asana-Math" "fbb"
       "CormorantGaramond" "bookman" "kerkis" "algolrevived" "Arvo" "bitter" "concmath"
       "electrum" "drm" "egothic" "yfonts" "pgothic" "auncial" "carolmin" "huncial"
       "inslrmaj" "humanist" "rotunda" "emerald" "aurical" "pbsi" "calligra" "chancery"
       "tgchorus" "wedn" "aurical" "wesu" "weva" "oesch" "AnonymousPro" "ascii" "beramono"
       "cascadia-code" "courier" "courierten" "GoMono" "luximono" "pandora")
# typefaces=("normal" "italic" "bold" "bolditalic" "smallcaps" "slanted")
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
