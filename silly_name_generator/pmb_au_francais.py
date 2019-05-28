#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Uses the googletrans API to translate your input phrase into French and
then perform the poor man's barchart algorithm on it.
In French, there are 26 letters in the alphabet now
This code only adds the extra letters+accent appearing upon translation.
"""

#TODO pylint and pydocstyle these files.

import pprint
import string
from collections import defaultdict
from googletrans import Translator


def remove_punctuation(value):
    result = ""
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    return result

def translate_phrase(user_phrase):
    translator = Translator()
    translation = translator.translate(text=user_phrase,dest='fr')
    print("Your phrase in French is:",translation.origin, ' -> ', translation.text)
    return translation.text


def pmb_dict(letter_list):
    # use the alphabet to make all the keys, letters on the alphabet.
    alphabet = string.ascii_lowercase
    letter_count = defaultdict(list)
    for letter in alphabet:
        # makes a key for every letter in alphabet
        letter_count[letter]
    for letter in letter_list:
        letter_count[letter].append(letter)
    return letter_count


def request_input():
    user_phrase = input('Please enter your phrase: ')
    return user_phrase


def split_and_strip(user_phrase):
    user_phrase = remove_punctuation(user_phrase)
    word_list = user_phrase.lower().replace(" ", "")
    return word_list


def main():
    user_phrase = request_input()
    user_phrase = translate_phrase(user_phrase)
    letter_list = split_and_strip(user_phrase)
    pp = pprint.PrettyPrinter(indent=1, width=120)
    pp.pprint(pmb_dict(letter_list))
    return 0


if __name__ == '__main__':
    main()