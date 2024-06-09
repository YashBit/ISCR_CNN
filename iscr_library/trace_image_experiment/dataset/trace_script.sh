#!/bin/bash


# ONLY LOOK AT COMMANDS WHICH
# \usepackage
fonts=(
"spectral",
"cuprum",
"accanthis",
"Alegreya",
"algolrevived",
"almendra",
"antiqua",
"anttor",
"antpolt",
"gfsartemisia",
"gfsartemisia-euler",
"baskervald",
"QTBengal",
"bera",
"berenis",
"LibreBodoni",
"boisik",
"tgbonum",
"bookman",
"QTBookmann",
"librecaslon",
"CharisSIL",
"cochineal",
"concmath",
"covfonts",
"DejaVuSerif",
"gfsdidot",
"droidserif",
"electrum",
"ETbb",
"gandhi",
"QTGaromand",
"QTGraphLite",
"ibarra",
"imfellEnglish",
"aesupp",
"mlmodern",
"roboto",
"venturis2",
"Asana-Math",
"fbb",
"CormorantGaramond",
"bookman",
"kerkis",
"algolrevived",
"Arvo",
"bitter",
"concmath",
"electrum",
"drm",
"egothic",
"yfonts",
"pgothic",
"auncial",
"carolmin",
"huncial",
"inslrmaj",
"humanist",
"rotunda",
"emerald",
"aurical",
"pbsi",
"calligra",
"chancery",
"tgchorus",
"wedn",
"aurical",
"wesu",
"weva",
"oesch",
"AnonymousPro",
"ascii",
"beramono",
"cascadia-code",
"courier",
"courierten",
"GoMono",
"luximono",
"pandora"
)



for letter in {a..z}
do
    for font in "${fonts[@]}"
    do
        python trace_generator.py --letter $letter --font $font
        python letter_generator.py --letter $letter --font $font 
    done
done

blackletter_fonts=(
"QTBeckman",
"QTCloisteredMonk",
"egothic",
"QTHeidelbergType",
"QTLinoscroll",
"Missaali-Regular.otf",
"QTLondonScroll",
"QTDublinIrish",
"QTArtiston",
"QTBlackForest",
"QTBoulevard",
"QTBrushStroke",
"QTCaligulatype",
"QTCascadetype",
"QTChanceryType",
)
for letter in {a..z}
do
    for font in "${blackletter_fonts[@]}"
    do
        python blackletter_normal.py --letter $letter --font $font
        python blackletter_trace.py --letter $letter --font $font 
    done
done
