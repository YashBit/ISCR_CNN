#!/bin/bash

# Define the alphabet
alphabet="abcdefghijklmnopqrstuvwxyz"

# Iterate over each letter and call the Python script
for letter in $(echo $alphabet | grep -o .); do
    python trace_generator.py --letter $letter
done
