#!/bin/bash

fonts=("mathptmx" "helvet" "courier" "mathpazo" "charter")

for letter in {a..z}
do
    for font in "${fonts[@]}"
    do
        python trace_generator.py --letter $letter --fonts $font
        python letter_generator.py --letter $letter --fonts $font 
    done
done
