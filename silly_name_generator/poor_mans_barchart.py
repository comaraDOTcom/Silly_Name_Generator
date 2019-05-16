#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pprint
import string
from collections import defaultdict

def remove_punctuation(value):
    result = ""
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    return result


def pmb_dict(letter_list):
    letter_count = defaultdict(list)
    for letter in letter_list:
        letter_count[letter].append(letter)
    return letter_count

def request_input():
    user_phrase = input('Please enter your phrase: ')
    return user_phrase

def split_and_strip(user_phrase ):
    user_phrase  = remove_punctuation(user_phrase)
    word_list = user_phrase.lower().replace(" ", "")
    return word_list
    

def main():
    user_phrase = request_input()
    letter_list = split_and_strip(user_phrase)
    pp = pprint.PrettyPrinter(indent=1,width=120)
    pp.pprint(pmb_dict(letter_list))
    return 0

if __name__ == '__main__':
    main()
