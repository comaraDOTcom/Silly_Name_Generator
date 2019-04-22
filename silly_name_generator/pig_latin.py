"""
Pigs latin-ator, this code will take any input you give it and convert it to
Pig Latin
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  pigs_latin.py

import sys

def main(args):
    print("This code will write a phrase of your choice in Pig Latin\n")
    user_phrase = input("Please enter your phrase")

    phrase_list = user_phrase.split()
    
    dict_vowel = {'vowels':['a','e','i','o','u']}
    
    for i in len(phrase_list):
        
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
