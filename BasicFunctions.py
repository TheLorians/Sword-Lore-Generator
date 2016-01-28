'''
This is a module with useful tools for creating generators
'''
# M V S E V M:

# from random import random

# This is the line of code that used to import the randint function from the random module.
# Those were dark days indeed.

# def randint(lower, upper, startseed):

# This was the opening line of the code.
# It is similar to the current opening line but with a startseed.
# This was from the days before seed was a global variable. *shivers*

# def randint(lower, upper, startseed=None):

# This is a later version of the opening line of the code.
# It still takes a startseed for the few lines that still try to give it one,
# but actually does nothing with the startseed and doesn't require one to run.
# Other core functions such as the ooses held this archaic holdover


# Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random
import re

# Variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

seeded = False

# Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def seed(newSeed):
    '''Changes the seed to a set amount'''
    random.seed(newSeed)
    global seeded
    seeded = True


def randint(lower, upper):
    '''Selects a random interger between the upper and lower values'''
    # the backbone of the entire code

    # sanity checks
    global seeded
    if not seeded:
        raise RuntimeError("Call to randint before seed has been set")
    if lower > upper:
        lower, upper = upper, lower

    return random.randint(lower, upper)


# def relist(array, freqlist):
#  This creates a new list based upon an array and freqlist
#  This is used in in the woose function to create weightedness
# newarray = []
# for index in array:
# for x in range(0, freqlist[index]):
# newarray.append(index)
# return newarray


# Below are the ooses.
# These functions are versions of the original choose function.
# They each have a specific task but all take and array and return some of the elements
# Choose is currently the only one that returns multiple elements
# (and perhaps will always be)

def choose(array, times=1):
    '''Chooses a number of elements from an array'''
    result = []
    virtual = array[::]
    for x in range(0, times):
        temp = virtual[randint(0, len(virtual) - 1)]
        result.append(temp)
        virtual.remove(temp)

    return result if len(result) > 1 else result[0]


def woose(freqdict, array=None):
    '''Weighted version of choose'''
    if array is None:
        array = freqdict.keys()
    major_sum = sum(map(lambda x: freqdict.get(x, 0), array))
    selection = randint(0, major_sum - 1)
    for item in array:
        selection -= freqdict.get(item, 0)
        if selection < 0:
            return item
    else:
        print 'Something has gone horribly wrong (in woose).'
        print 'Inputs:'
        print array
        print freqdict


def boose(array):
    '''Either chooses or returns an empty string'''
    # (I cannot remember why I called it boose)
    # Declare a default value
    dfault = None
    typeset = set([type(x) for x in array])
    if typeset == set([str]):
        dfault = ''
    elif typeset == set([bool]):
        dfault = False
    return choose([choose(array), dfault])


def capitalize(word):
    '''Similar to .capitalize except it leaves all the rest of the word in the same case it was'''
    # Example:
    # fOo BaR.capitalize() = Foo bar
    # fOo BaR.capitalize() = FOo BaR
    return word[0].upper() + word[1:]


def plural(string):
    '''makes a word plural'''
    key_list = {
        'human': 'humans', 'ox': 'oxen', 'goose': 'geese', 'moose': 'moose', 'deer': 'deer', 'cyclops': 'cyclopes'
    }
    if string.lower() in key_list:
        return key_list[string.lower()]
    elif string.lower()[-3:] == 'man':
        return string[:-2] + 'en'
    elif string.lower()[-2:] in ['lf', 'rf']:
        return string[:-1] + 'ves'
    elif string.lower()[-3:] in ['ife', 'oof']:
        return string[:-2] + 'ves'
    elif string.lower()[-1:] in ['s', 'x']:
        return string + 'es'
    else:
        return string + 's'


def precep(word):
    '''Adds the correct version of either a or an before the input'''
    # because I was doing this individually before and it was a pain in the butt
    # (I don't remember why I called it preceps but the name is stuck now)
    if word[0].lower() in 'aeiou':
        return 'an ' + word
    else:
        return 'a ' + word


def addaned(word):
    # Adds the ed to the end of a word in accordance with english grammar
    special_cases = {'ear': 'eared', 'tail' : 'tailed'}
    if word in special_cases:
        return special_cases[word]
    if re.search('e$', word):
        return word + 'd'
    if re.search('y$', word):
        return re.sub('y$','ied',word)
    if re.search('[aeiou][^aeiou]$', word):
        return word + word[-1] + 'ed'
    return word + 'ed'

def read_list(array, oxford=True):
    '''Translates list objects into writen lists'''
    if isinstance(array, basestring):
        return array
    while '' in array:
        array.remove('')
    if len(array) == 2:
        oxford = False
    if len(array) == 1:
        return array[0]
    elif len(array) == 0:
        return ''
    return ', '.join(array[:-1]) + ',' * int(oxford) + ' and ' + array[-1]

# Body~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    seed(82914372)
    for x in range(0,40):
        print word('Hello world')
