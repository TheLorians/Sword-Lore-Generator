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

letters = {
    '1': list('bcdfgjkprstvwz$%'),
    '2': list('lrj'),
    '3': list('aeiouy&'),
    '4': list('lr'),
    '5': list('bcdfgjklmnprstvxz$%^'),
    '6': list('bcdfghjklpqrstvwxyz$%^'),
    '7': list('bcdfghjklprstvwxyz$%^'),
    '8': ['ae', 'ai', 'ao', 'au', 'ea', 'ee', 'ei', 'ie', 'oe', 'oi', 'ou', 'ue']
}
frequencies = {
    'a': 82,
    'b': 15,
    'c': 28,
    'd': 43,
    'e': 127,
    'f': 22,
    'g': 20,
    'h': 61,
    'i': 70,
    'j': 2,
    'k': 8,
    'l': 40,
    'm': 24,
    'n': 67,
    'o': 75,
    'p': 19,
    'q': 1,
    'r': 60,
    's': 63,
    't': 91,
    'u': 28,
    'v': 10,
    'w': 24,
    'wh': 24,
    'x': 2,
    'y': 20,
    'z': 1,
    '$': 33,
    '%': 33,
    '&': 80,
    '^': 33,
    '3': 9,
    '63': 30,
    '37': 30,
    '123': 1,
    '637': 90,
    '345': 1,
    '1237': 10,
    '6345': 13,
    '12345': 1
}
syllables = [
    '3',
    '63',
    '37',
    '123',
    '637',
    '345',
    '1237',
    '6345',
    '12345'
]

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


def approxsyllables(string):
    '''approximates the number of syllables based on the number of vowels'''
    total = 0
    for letter in list(string):
        if letter in list('aeiou'):
            total += 1
    if total < 1:
        total = 1
    return total


def polish(word):
    '''Fixes issues that might arise with word generation'''
    # <polish word:
    # <Fix q:
    word = word.replace('q', 'qu')
    word = word.replace('quy', 'qui')
    # >q fixed
    # <Add multi-character letters:
    word = word.replace('<', 'sh')
    word = word.replace('%', 'th')
    word = word.replace('>', 'ch')
    word = word.replace('&', choose(['ae', 'ai', 'ao', 'au', 'ea', 'ee', 'ei', 'ie', 'oe', 'oi', 'ou', 'ue']))
    # >Multi-character letters added
    # <Fix hh:
    word = word.replace('hh', 'h')
    # >hh fixed
    # <Fix double multi:
    word = word.replace('thth', 'th')
    word = word.replace('shsh', 'sh')
    # >double multi fixed
    # <Enhance double vowel:
    for vowel in list('aiu'):
        word = word.replace(2 * vowel, vowel + '\'' + vowel)
    # >Double vowel enhanced
    # <Fix misc.:
    word = word.replace('iy', 'ey')
    word = word.replace('ih', 'eh')
    word = word.replace('yh', 'eh')
    # >Fixed
    # >word polished
    return word


def word(word):
    '''
    This is the word generation function
    # It translates words into seed based languages by the power of 
    # '*.~MATHS~.*'
    '''
    #TODO json or xml
    markov = {'%': {'a': 157, 'c': 3, 'b': 8, 'e': 916, 'd': 11, 'f': 38, 'i': 402, 'h': 4, 'm': 34, 'l': 48, 'o': 326, 'n': 18, 'q': 2, 'p': 12, 's': 230, 'r': 290, 'u': 95, 't': 3, 'w': 36, 'y': 108, '%': 2}, '<': {'a': 448, 'c': 8, 'b': 28, 'e': 893, 'd': 4, 'g': 6, 'f': 11, 'i': 722, 'h': 3, 'k': 12, 'm': 59, 'l': 81, 'o': 410, 'n': 53, 'p': 14, 'r': 145, 'u': 79, 't': 19, 'w': 15, 'v': 2, 'y': 44}, '>': {'%': 6, '<': 2, 'a': 793, 'c': 6, 'b': 23, 'e': 1231, 'd': 10, 'g': 6, 'f': 12, 'i': 915, 'h': 10, 'k': 4, 'm': 66, 'l': 84, 'o': 376, 'n': 44, 'p': 4, 's': 64, 'r': 117, 'u': 181, 't': 29, 'w': 14, 'y': 89, 'z': 3}, '^': {'%': 681, '<': 1105, '>': 1436, 'a': 6557, 'c': 8949, 'b': 6848, 'e': 4364, 'd': 6436, 'g': 3950, 'f': 4937, 'i': 4013, 'h': 4080, 'k': 1312, 'j': 1106, 'm': 6270, 'l': 3710, 'o': 3978, 'n': 2208, 'q': 568, 'p': 8693, 's': 11486, 'r': 7141, 'u': 2934, 't': 5270, 'w': 2927, 'v': 1932, 'y': 438, 'x': 82, 'z': 398}, 'a': {'%': 434, '<': 449, '>': 487, 'a': 59, 'c': 3360, 'b': 2656, 'e': 598, 'd': 2790, 'g': 2377, 'f': 661, 'i': 2315, 'h': 354, 'k': 845, 'j': 80, 'm': 2939, 'l': 7701, 'o': 71, 'n': 8434, 'q': 75, 'p': 2466, 's': 4740, 'r': 8012, 'u': 1411, 't': 9164, 'w': 861, 'v': 1234, 'y': 1103, 'x': 380, 'z': 469}, 'c': {'%': 2, '>': 19, 'a': 4807, 'c': 537, 'b': 4, 'e': 3504, 'd': 11, 'i': 2612, 'k': 2640, 'm': 8, 'l': 1462, 'o': 5667, 'n': 15, 'q': 56, 'p': 2, 's': 406, 'r': 1951, 'u': 1857, 't': 2156, 'w': 2, 'y': 478, 'z': 17}, 'b': {'<': 6, '>': 4, 'a': 2493, 'c': 61, 'b': 768, 'e': 2900, 'd': 80, 'g': 12, 'f': 36, 'i': 2120, 'h': 48, 'k': 8, 'j': 55, 'm': 36, 'l': 2750, 'o': 2246, 'n': 45, 'p': 25, 's': 517, 'r': 1488, 'u': 1492, 't': 135, 'w': 28, 'v': 37, 'y': 197, 'z': 2}, 'e': {'%': 266, '<': 208, '>': 236, 'a': 4486, 'c': 2786, 'b': 756, 'e': 2743, 'd': 12297, 'g': 1231, 'f': 1233, 'i': 1094, 'h': 338, 'k': 242, 'j': 112, 'm': 2539, 'l': 4837, 'o': 693, 'n': 8991, 'q': 224, 'p': 1768, 's': 21145, 'r': 19103, 'u': 548, 't': 3909, 'w': 876, 'v': 1082, 'y': 710, 'x': 1351, 'z': 146}, 'd': {'%': 21, '<': 37, '>': 15, 'a': 1756, 'c': 62, 'b': 139, 'e': 6197, 'd': 754, 'g': 437, 'f': 94, 'i': 4782, 'h': 135, 'k': 6, 'j': 81, 'm': 182, 'l': 885, 'o': 1881, 'n': 202, 'q': 8, 'p': 77, 's': 1842, 'r': 1116, 'u': 1051, 't': 18, 'w': 183, 'v': 86, 'y': 389, 'z': 13}, 'g': {'%': 22, '<': 20, 'a': 2086, 'c': 10, 'b': 74, 'e': 3412, 'd': 36, 'g': 913, 'f': 41, 'i': 1971, 'h': 1043, 'k': 6, 'j': 4, 'm': 162, 'l': 1275, 'o': 1225, 'n': 660, 'p': 20, 's': 1163, 'r': 1812, 'u': 1066, 't': 32, 'w': 63, 'v': 2, 'y': 353, 'z': 4}, 'f': {'%': 7, '<': 3, 'a': 1237, 'c': 6, 'b': 18, 'e': 1555, 'd': 10, 'g': 4, 'f': 1180, 'i': 2342, 'h': 11, 'j': 4, 'm': 2, 'l': 1404, 'o': 1536, 'n': 12, 'p': 6, 's': 244, 'r': 888, 'u': 1191, 't': 445, 'w': 8, 'y': 331}, 'i': {'%': 277, '<': 1046, '>': 146, 'a': 2846, 'c': 5341, 'b': 1042, 'e': 6861, 'd': 2887, 'g': 2075, 'f': 1485, 'i': 38, 'h': 67, 'k': 570, 'j': 32, 'm': 2413, 'l': 4395, 'o': 4378, 'n': 21173, 'q': 157, 'p': 1491, 's': 6556, 'r': 2231, 'u': 343, 't': 5227, 'w': 34, 'v': 1721, 'y': 17, 'x': 263, 'z': 1741}, 'h': {'%': 38, '>': 3, 'a': 1912, 'c': 2, 'b': 27, 'e': 1796, 'd': 10, 'f': 2, 'i': 1105, 'h': 5, 'k': 1, 'j': 8, 'm': 23, 'l': 51, 'o': 1902, 'n': 35, 'p': 5, 's': 238, 'r': 72, 'u': 498, 't': 584, 'w': 5, 'y': 500, 'z': 3}, 'k': {'%': 2, '<': 40, 'a': 591, 'c': 10, 'b': 77, 'e': 2732, 'd': 23, 'g': 10, 'f': 61, 'i': 1771, 'h': 93, 'k': 35, 'j': 4, 'm': 72, 'l': 450, 'o': 240, 'n': 299, 'p': 36, 's': 1108, 'r': 115, 'u': 120, 't': 54, 'w': 84, 'v': 15, 'y': 269}, 'j': {'a': 410, 'e': 361, 'd': 2, 'i': 173, 'k': 1, 'j': 5, 'o': 365, 'n': 4, 's': 2, 'u': 450}, 'm': {'%': 2, '<': 19, '>': 2, 'a': 4101, 'c': 21, 'b': 1324, 'e': 4414, 'd': 9, 'g': 4, 'f': 70, 'i': 4372, 'h': 18, 'k': 10, 'j': 3, 'm': 988, 'l': 124, 'o': 2578, 'n': 201, 'q': 4, 'p': 2046, 's': 1352, 'r': 34, 'u': 1145, 't': 27, 'w': 18, 'v': 15, 'y': 355, 'z': 4}, 'l': {'%': 54, '<': 19, '>': 59, 'a': 5975, 'c': 217, 'b': 171, 'e': 9394, 'd': 782, 'g': 180, 'f': 290, 'i': 8037, 'h': 57, 'k': 363, 'j': 4, 'm': 305, 'l': 4439, 'o': 4148, 'n': 180, 'q': 6, 'p': 291, 's': 2004, 'r': 59, 'u': 1888, 't': 920, 'w': 65, 'v': 297, 'y': 3489, 'x': 2, 'z': 12}, 'o': {'%': 323, '<': 89, '>': 174, 'a': 1097, 'c': 1617, 'b': 1039, 'e': 662, 'd': 1690, 'g': 1706, 'f': 577, 'i': 1399, 'h': 150, 'k': 611, 'j': 40, 'm': 2840, 'l': 3838, 'o': 2724, 'n': 9327, 'q': 67, 'p': 2148, 's': 3069, 'r': 6695, 'u': 4883, 't': 2406, 'w': 1815, 'v': 1697, 'y': 404, 'x': 433, 'z': 211}, 'n': {'%': 243, '<': 120, '>': 492, 'a': 3418, 'c': 2598, 'b': 228, 'e': 7175, 'd': 3725, 'g': 12871, 'f': 723, 'i': 4498, 'h': 253, 'k': 913, 'j': 113, 'm': 194, 'l': 391, 'o': 2459, 'n': 1101, 'q': 113, 'p': 231, 's': 5524, 'r': 243, 'u': 871, 't': 6057, 'w': 214, 'v': 440, 'y': 386, 'x': 35, 'z': 95}, 'q': {'a': 475, 'e': 479, 'i': 592, 'o': 67, 'r': 4, 'u': 4, 'y': 9, '<': 2}, 'p': {'%': 12, '<': 30, '>': 4, 'a': 2977, 'c': 46, 'b': 64, 'e': 4414, 'd': 35, 'g': 33, 'f': 46, 'i': 2848, 'h': 1460, 'k': 22, 'j': 10, 'm': 47, 'l': 2035, 'o': 2799, 'n': 74, 'p': 1333, 's': 1160, 'r': 3212, 'u': 1188, 't': 839, 'w': 62, 'y': 322}, 's': {'%': 83, '<': 14, '>': 197, 'a': 2307, 'c': 1940, 'b': 151, 'e': 6878, 'd': 69, 'g': 61, 'f': 135, 'i': 4026, 'k': 736, 'j': 28, 'm': 1358, 'l': 1106, 'o': 2170, 'n': 759, 'q': 290, 'p': 2163, 's': 4873, 'r': 80, 'u': 2190, 't': 9247, 'w': 541, 'v': 24, 'y': 540, 'z': 2}, 'r': {'%': 243, '<': 118, '>': 365, 'a': 7910, 'c': 725, 'b': 752, 'e': 12368, 'd': 1607, 'g': 875, 'f': 356, 'i': 8262, 'h': 294, 'k': 766, 'j': 40, 'm': 1318, 'l': 758, 'o': 5695, 'n': 1187, 'q': 45, 'p': 640, 's': 6327, 'r': 1531, 'u': 1917, 't': 1980, 'w': 166, 'v': 422, 'y': 1298, 'z': 31}, 'u': {'%': 194, '<': 272, '>': 198, 'a': 551, 'c': 1058, 'b': 1166, 'e': 679, 'd': 934, 'g': 875, 'f': 384, 'i': 588, 'h': 15, 'k': 149, 'j': 24, 'm': 2261, 'l': 3160, 'o': 183, 'n': 4517, 'q': 6, 'p': 1388, 's': 3489, 'r': 3901, 'u': 15, 't': 2996, 'w': 6, 'v': 117, 'y': 32, 'x': 112, 'z': 124}, 't': {'%': 23, '<': 32, '>': 524, 'a': 4768, 'c': 110, 'b': 218, 'e': 11396, 'd': 76, 'g': 93, 'f': 246, 'i': 11162, 'k': 16, 'j': 20, 'm': 189, 'l': 1066, 'o': 3784, 'n': 214, 'q': 6, 'p': 128, 's': 4029, 'r': 4103, 'u': 1836, 't': 2029, 'w': 400, 'v': 21, 'y': 1306, 'z': 146}, 'w': {'%': 20, '<': 16, '>': 4, 'a': 1820, 'c': 16, 'b': 94, 'e': 1336, 'd': 117, 'g': 10, 'f': 47, 'i': 1400, 'h': 557, 'k': 73, 'm': 36, 'l': 279, 'o': 1051, 'n': 425, 'p': 39, 's': 426, 'r': 279, 'u': 15, 't': 38, 'w': 10, 'y': 52, 'z': 9}, 'v': {'a': 1404, 'e': 4781, 'd': 2, 'g': 3, 'i': 1962, 'k': 3, 'o': 782, 'n': 6, 's': 9, 'r': 23, 'u': 130, 'v': 22, 'y': 46, 'z': 2}, 'y': {'%': 62, '<': 3, '>': 58, 'a': 480, 'c': 222, 'b': 111, 'e': 665, 'd': 145, 'g': 112, 'f': 38, 'i': 637, 'h': 35, 'k': 24, 'j': 5, 'm': 386, 'l': 526, 'o': 321, 'n': 325, 'p': 470, 's': 866, 'r': 320, 'u': 42, 't': 161, 'w': 81, 'v': 12, 'y': 2, 'x': 42, 'z': 58}, 'x': {'%': 5, '>': 6, 'a': 205, 'c': 143, 'b': 10, 'e': 483, 'g': 2, 'f': 11, 'i': 527, 'h': 65, 'm': 6, 'l': 19, 'o': 126, 'n': 2, 'q': 1, 'p': 283, 's': 24, 'u': 74, 't': 292, 'w': 15, 'v': 2, 'y': 105}, 'z': {'a': 456, 'c': 4, 'b': 2, 'e': 1571, 'g': 2, 'i': 727, 'h': 4, 'k': 2, 'j': 2, 'm': 8, 'l': 137, 'o': 361, 'n': 2, 'q': 4, 'p': 10, 's': 4, 'u': 29, 'w': 6, 'v': 6, 'y': 101, 'z': 260}}
    # The commenting here could be improved
    # (Also perhaps import the larger language module)
    # returns blank requests to prevent it from being junked up
    if word == '':
        return word
    # && bypasses translation
    if word[-2:] == '&&':
        return word[:-2]
    number = approxsyllables(word) + randint(-1, 1)
    if number < 1:
        number = 1
    skeleton = ''
    oldword = word
    word = ''
    for x in range(0, number):
        syllable = '^'
        syllable_skeleton = woose(frequencies, syllables)
        for letter in list(syllable_skeleton):
            syllable += woose(markov[syllable[-1]], letters[letter])
        # <polish syllable:
        # <Fix yy:
        if 'y' == syllable[0]:
            syllable = syllable.replace('yy', 'yi')
        else:
            syllable = syllable.replace('yy', 'ey')
        # >yy fixed
        # <Fix iw:
        syllable = syllable.replace('iw', 'ew')
        # >iw fixed
        # <Fix (letter)l:
        for letter in ['d', 't', 'r', '$', '%']:
            syllable = syllable.replace(letter + 'l', letter + woose(frequencies, letters['3']) + 'l')
        # >(letter)l fixed
        # <Fix lr:
        syllable = syllable.replace('lr', 'l' + woose(frequencies, letters['3']) + 'r')
        # >lr fixed
        # <Fix duplicate liquid:
        syllable = syllable.replace('rr', 'r')
        syllable = syllable.replace('ll', 'l')
        syllable = syllable.replace('jj', 'j')
        # >Duplicate liquids fixed
        # >syllable polished
        word += syllable
        skeleton += syllable_skeleton
    word = polish(word.replace('^',''))
    if oldword[0] == oldword[0].upper():
        word = capitalize(word)
    return word

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
