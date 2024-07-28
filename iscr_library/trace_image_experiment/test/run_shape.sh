#!/bin/bash


# ONLY TESTING 200 FONTS WITH a! 


letters=(a)
# fonts=("spectral" "cuprum" "accanthis" "Alegreya" "algolrevived" "almendra"
#        "anttor" "antpolt" "gfsartemisia" "gfsartemisia-euler" "baskervald"
#        "bera" "berenis" "LibreBodoni" "tgbonum"
#        "librecaslon" "CharisSIL" "cochineal" "concmath" "DejaVuSerif" "gfsdidot"
#        "electrum" "ETbb" "ibarra"
#        "imfellEnglish" "aesupp" "mlmodern" "venturis2" "fbb" "noto"
#        "CormorantGaramond" "bookman" "kerkis" "Arvo" "bitter"
#        "electrum" "drm" "chancery" "fourier" "stix2" "scholax" "lxfonts" "kpfonts"
#        "tgchorus" "aurical" "palatino"  "charter" "mathptmx" "mathpazo" "arev" "kurier"
# typefaces=("normal" "italic" "bold" "bolditalic" "smallcaps" "slanted")

# 200 Fonts * 5 Typefaces = 1000 per class (Trace, Normal Each) = 52k total
# 65 (inclusive of blackletter) FONTS -> NEED TO GET TO 200


fonts=("ocr")
typefaces=("normal")
sizes=(10 20 30 40)  # Define your desired sizes here

for letter in "${letters[@]}"
do
    for font in "${fonts[@]}"
    do
        for typeface in "${typefaces[@]}"
        do
            for size in "${sizes[@]}"
            do
                python letter_generator.py --letter $letter --font $font --typeface $typeface --size $size
            done
        done
    done
done