# coding=utf-8
'''
This is a language module.  It is used in language based computations.  It can translate to a variety of languages
'''
#Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from BasicFunctions import *
import re

#Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def polish(word):
    # Fixes any errors that might exist with the raw output of the word() function
    #TODO: rewrite with regex
    #Fix q:
    word = word.replace('q','qu')
    word = word.replace('quy','qui')
    #Add multi-character letters:
    word = word.replace('$','sh')
    word = word.replace('%','th')
    word = word.replace('^','ch')
    word = word.replace('&',choose(letters['8']))
    #Fix hh:
    word = word.replace('hh','h')
    #Fix double multi:
    word = word.replace('thth','th')
    word = word.replace('shsh','sh')
    #Enhance double vowel:
    for vowel in list('aiu'):
        word = word.replace(2*vowel,vowel+"'"+vowel)
    #Fix misc.:
    word = word.replace('iy','ey')
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
        syllable = ''
        syllable_skeleton = woose(frequencies,syllables)
        for letter in syllable_skeleton:
            syllable += woose(frequencies,letters[letter])
        # Fixe 'yy'
        if 'y' == syllable[0]:
            syllable = syllable.replace('yy','yi')
        else:
            syllable = syllable.replace('yy','ey')
        # Fix iw:
        syllable = syllable.replace('iw','ew')
        # Fix (letter)l:
        for letter in ['d','t','r','$','%']:
            syllable = syllable.replace(letter+'l',letter+woose(frequencies, letters['3'])+'l')
        # Fix lr:
        syllable = syllable.replace('lr','l'+woose(frequencies, letters['3'])+'r')
        # Fix wl:
        if syllable[:2] == 'wl':
            syllable = 'wr' + syllable[2:]
        # Fix duplicate liquid:
        syllable = syllable.replace('rr','r')
        syllable = syllable.replace('ll','l')
        # commit the syllable to word
        word += syllable
        skeleton += syllable_skeleton
    word = polish(word)
    if oldword[0] == oldword[0].upper():
        word = capitalize(word)
    return word


def translate(string,conjugated=False):
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
    conjugated = True
    language = raw_input('Language seed: ')
    seed(hash(language.lower()))
    text = raw_input('Text: ')
    print(translate(text,conjugated))