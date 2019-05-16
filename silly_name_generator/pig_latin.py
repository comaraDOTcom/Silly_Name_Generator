"""Will take any input you give it and convert it to Pig-Latin."""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  pigs_latin.py


def pig_latin(word):
    """Receives word, pig-latinates it and returns the outcome."""
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxzy'
    if ((len(word) > 1) & (word[0] != 'y') & ("y" in word[1:].lower()) &
            (word[1:] not in consonants) & (word[0] not in vowels)):
        y_index = [i for i in range(len(word)) if word[i].lower() == 'y']
        first_vowel = [i for i in range(len(word)) if word[i].lower()
                       not in consonants]
        if y_index[0] < first_vowel[0]:
            final = pig_y(word.lower(), y_index[0])
        else:
            final = pig_cons(word.lower(), first_vowel[0])
    elif ((len(word) > 1) & (word[0] != 'y') & ("y" in word[1:].lower())
          & (word[0] not in vowels)):
        y_index = [i for i in range(len(word)) if word[i].lower() == 'y']
        final = pig_y(word.lower(), y_index[0])
    else:
        first_vowel = [i for i in range(len(word)) if word[i].lower()
                       not in consonants]
        if first_vowel[0] == 0:
            final = pig_vow(word.lower())
        elif first_vowel[0] > 0:
            final = pig_cons(word, first_vowel[0])
    return final
def pig_y(word, i):
    """Pig-latinates for character y at position i, given i>0."""
    return word[i:]+"-"+word[0:i]+"ay"

def pig_cons(word, i):
    """Pig-latinates word for consonant at position i."""
    return word[i:]+"-"+word[0:i]+"ay"

def pig_vow(word):
    """Pig-latinates for word beginning with vowel."""
    return word+"-"+"yay"
def main():
    """Convert string from user input to pig-latin."""
    print("This code will write a phrase of your choice in Pig Latin\n")
    user_phrase = input("Please enter your phrase: ")
    phrase_list = user_phrase.split()
    output = []
    # pylint suggested enumerate instead of range(len(list))
    for i, _ in enumerate(phrase_list):
        output.append(pig_latin(phrase_list[i]))
    final_phrase = " ".join(output)
    print(final_phrase)

    return 0

if __name__ == '__main__':
    main()
