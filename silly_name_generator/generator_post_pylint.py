"""
The Silly Name Generator.

Author: Conor O'Mara
Date: 16/04/2019
Header: This code uses two lists, first and last to randomly create
        silly nicknames


Code for building a silly name generator. This docstring is so the C0111 error
won't be thrown on Pylint.

Had to change the settings in Geany to indent with spaces (4)
instead of tabs for Pylint.

To follow pep8 guidelines run the following I overwrote the pylint default line
length of 100 to pep8's fixed 79. I'm content with other default settings.

Command for mac was
pylint --max-line-length=79 --generate-rcfile > ~/.pylintrc

This code gets 10/10 from pylint and no issues from pydocstyle.

"""

#!/usr/bin/env python
# coding: utf-8

import sys
import random

def main():
    """
    Will generate silly names out of two lists.

    Returns: String of two words separated by one space
    To exit: press "N" or "n" followed by any key. Otherwise program will
    continue to generate more random names
    """
    print("Welcome to the Silly Name Generator, created by COMARA CORP\n")
    print("I hope you are ready to have some fun")

    first = (
        'Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
        "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
        'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
        'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
        'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
        'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
        'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
        'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
        '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
        'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
        'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'",
        'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
        'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
        'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms'
    )

    last = (
        'Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks'
    )

    while True:
        firstname = random.choice(first)
        # random.choice allows you to randomly select from a list
        lastname = random.choice(last)
        print("\n\n")
        print("{} {}".format(firstname, lastname), file=sys.stderr)
        print("\n\n")
        try_again = input("Try again? (Press Enter else n to quit)")
        if try_again.lower() == "n":
            break
        input("\n Press Enter to exit.")

if __name__ == "__main__":
    main()
