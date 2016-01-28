# coding=utf-8
'''
This is a language module.  It is used in language based computations.  It can translate to a variety of languages
'''
#Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from BasicFunctions import *
import re
import json

#Files~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

f = open('markov.txt')
markov_bank = json.loads(f.read())
f.close()

# Variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

letters = {
    '1': list('bcdfgjkprstvwz$%'),
    '2': list('lr'),
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

#Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    # Fixes any errors that might exist with the raw output of the word() function
    #TODO: rewrite with regex
    #Fix q:
    word = re.sub('q', 'qu', word)
    word = re.sub('quy', 'qui', word)
    #Add multi-character letters:
    word = re.sub('<', 'sh', word)
    word = re.sub('%', 'th', word)
    word = re.sub('>', 'ch', word)
    word = re.sub('&', choose(letters['8']), word)
    #Fix hh:
    word = re.sub('hh', 'h', word)
    #Fix double multi:
    word = re.sub('thth', 'th', word)
    word = re.sub('shsh', 'sh', word)
    #Enhance double vowel:
    for vowel in list('aiu'):
        word = re.sub(2*vowel, vowel+"'"+vowel, word)
    #Fix misc.:
    word = re.sub('iy', 'ey', word)
    # Fix excessive liquid:
    word = re.sub('r{3,4}', 'rr', word)
    word = re.sub('l{3,4}', 'll', word)
    return word


def word(word):
    # Makes words
    #returns blank requests to prevent it from being junked up
    if word == '':
        return word
    #&& bypasses translation
    if word[-2:] == '&&':
        return word[:-2]
    # reseeds
    seed(hash(word.lower()) + hash(randint(0,9999999999)))
    # sets syllable number
    number = approxsyllables(word) + randint(-1,1)
    if number < 1:
        number = 1
    # prepares for the construction of a word
    skeleton = ''
    oldword = word
    word = ''
    
    for x in range(0,number):
        syllable = '^'
        syllable_skeleton = woose(frequencies,syllables)
        for letter in syllable_skeleton:
            syllable += woose(markov_bank[syllable[-1]],letters[letter])
        # Fixe 'yy'
        syllable = re.sub('yy$', 'yi$', syllable)
        syllable = re.sub('yy', 'ey', syllable)
        # Fix iw:
        syllable = syllable.replace('iw','ew')
        # Fix (letter)l:
        for letter in ['d','t','r','\$','%']:
            syllable = re.sub(letter+'l', letter+woose(frequencies, letters['3'])+'l', syllable)
        # Fix lr:
        syllable = re.sub('lr', 'l'+woose(frequencies, letters['3'])+'r', syllable)
        # Fix wl:
        syllable = re.sub('^wl' , '^wr', syllable)
        # commit the syllable to word
        word += syllable
        skeleton += syllable_skeleton
    word = polish(word.replace('^',''))
    if oldword[0] == oldword[0].upper():
        word = capitalize(word)
    return word


def translate(string, conjugated=False):
    origin_state = random.getstate()
    work = string
    for forbiddenchar in '.,:;?!':
        work = work.replace(forbiddenchar,'')
    work = work.replace('-',' ')
    array = work.split(' ')
    array.sort(key=len, reverse=True)
    for x, item in enumerate(array):
        string = string.replace(item,str(x))
    random.setstate(origin_state)
    if conjugated:
        f = lambda item: conjugatedword(item)
    else:
        f = lambda item: word(item)
    transarray = map(f, array)
    for x, item in enumerate(array):
        y = len(array)-x-1
        string = string.replace(str(y),transarray[y])
    return string


def compute(number):
    if number in '12345678':
        return choose(letters[number])
    else:
        if number == '9':
            return choose([choose(letters['6']),choose(letters['1'])+choose(letters['2'])])
        if number == 'A':
            return choose([choose(letters['7']),choose(letters['4'])+choose(letters['5'])])


def ending(piece):
    if piece == '':
        return ''
    #make seed
    seed(hash(piece.lower()) + hash(randint(0,9999999999)))
    #select a template
    template = choose(['393A','3A'])
    #fill in template
    output =  ''
    for component in template:
        output += compute(component)
    #preliminary custom polish
    output = output.replace('wl','w')
    #return
    return polish(output)


def conjugatedword(worde):
    if worde == '':
        return ''
    origin_state = random.getstate()
    # parse into two pieces
    splite = worde.split('|')
    # reseed here
    seed(hash(splite[0].lower()) + hash(randint(0,9999999999)))
    # render body
    body = word(splite[0])
    # render ending
    random.setstate(origin_state)
    seed(hash(splite[1].lower()) + hash(randint(0,9999999999)))
    suffix = ending(splite[1])
    # combine
    return body+suffix

#Body~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    conjugated = False
    language = raw_input('Language seed: ')
    seed(hash(language.lower()))
    text = raw_input('Text: ')
    print(translate(text))