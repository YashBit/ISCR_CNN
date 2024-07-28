#!/bin/bash


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
"QTChanceryType")

for letter in {a..z}
do
    for font in "${blackletter_fonts[@]}"
    do
        python blackletter_trace.py --letter $letter --font $font 
    done
done
