"""
Pigs latin-ator, this code will take any input you give it and convert it to
Pig Latin
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  pigs_latin.py

import sys

def pig_latin(word):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxzy'
    
    if ((len(word) > 1) & (word[0] != 'y') & ("y" in word[1:].lower()) & (word[1:] not in consonants) & (word[0] not in vowels)):
        y_index = [ i for i in range(len(word)) if word[i].lower() == 'y'] 
        first_vowel = [ i for i in range(len(word)) if word[i].lower() not in consonants]
        if (y_index[0] < first_vowel[0]):
            return pig_y(word.lower(),y_index[0])
        else:
            return pig_cons(word.lower(),first_vowel[0])
    elif ((len(word) > 1) & (word[0] != 'y') & ("y" in word[1:].lower()) & (word[0] not in vowels)):
        y_index = [ i for i in range(len(word)) if word[i].lower() == 'y']
        return pig_y(word.lower(),y_index[0])
    else:
        first_vowel = [ i for i in range(len(word)) if word[i].lower() not in consonants] 
        if (first_vowel[0] == 0):
            return pig_vow(word.lower())
        elif (first_vowel[0] > 0):
            return pig_cons(word,first_vowel[0])
                
def pig_y(word,i):
    return word[i:]+"-"+word[0:i]+"ay"

def pig_cons(word,i):
    return word[i:]+"-"+word[0:i]+"ay"

def pig_vow(word):
    return word+"-"+"yay"

def main():
    """ Pseudocode
    
    """
    print("This code will write a phrase of your choice in Pig Latin\n")
    user_phrase = raw_input("Please enter your phrase: ")

    phrase_list = user_phrase.split()
    output = []

    [output.append(pig_latin(phrase_list[i])) for i in range(len(phrase_list))]
    final_phrase = " ".join(output)
    print(final_phrase)

    return 0

if __name__ == '__main__':
    main()
