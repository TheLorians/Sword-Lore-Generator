# M V S E V M:

#from random import randint

#This is the line of code that used to import the random module.
#Those were dark days indeed.

#def randint(lower,upper,startseed):

#This was the opening line of the code.
#It is similar to the current opening line but with a startseed.
#This was from the days before seed was a global variable. *shivers*

#def randint(lower,upper,startseed = None):

#This is a later version of the opening line of the code.
#It still takes a startseed for the few lines that still try to give it one,
#but actually does nothing with the startseed and doesn't require one to run.
#Other core functions such as the ooses held this archaic holdover

seed = 0

def randint(lower,upper):
    #the random integer function
    #the backbone of the entire code
    
    #this allows us to edit the seed so when we call this function agian it yields a different result
    global seed
    #this checks if I was an idiot and put the number in backwards and fixes them if I was.
    if lower > upper:
        temp = upper
        upper = lower
        lower = temp
    #this makes seed a really big and essentially random number
    #the random ness comes from the two really big numbers which are both primes
    #it changes the seed globally so that when we call this function again it will yeild a different result
    seed += (seed)**2%(982451653*961748941)
    #this portion takes the really big number and puts it between the bounds
    return lower+(seed%(upper-lower+1))
def relist(array,freqlist):
    #This creates a new list based upon an array and freqlist
    #This is used in in the woose function to create weightedness
    newarray = []
    for index in array:
        for x in range(0,freqlist[index]):
            newarray.append(index)
    return newarray

#Below are the ooses.
#These functions are versions of the original choose function.
#They each have a specific task but all take and array and return some of the elements
#Choose is currently the only one that returns multiple elements
#(and perhaps will always be)
def choose(array,times = 1):
    #Chooses a number of elements from an array
    result = []
    virtula = array
    for x in range(0,times):
        temp = virtula[randint(0,len(virtula)-1)]
        result.append(temp)
        virtula.remove(temp)
    if len(result) == 1:
        return result[0]
    else:
        return result
def woose(array,freqlist):
    #weighted version of choose
    return choose(relist(array,freqlist))
def boose(array):
    #Either chooses or does not
    #(I cannot remember why I called it boose)
    return choose([choose(array),''])

def numbify(string):
    #turns a string into a number for seeding purposes
    try:
        int(string)
        return int(string)
    except ValueError:
        total = 0
        alphabet = {}
        for x in range(0,36):
            alphabet.update({list('abcdefghijklmnopqrstuvwxyz0123456789')[x]:x})
        for letter in range(0,len(string)):
            total += alphabet[string.lower()[letter]]*(36**letter)
        return total
def capitalize(word):
    #similar to .capitalize except it leaves all the rest of the word in the same case it was
    #Example:
    #fOo BaR.capitalize() = Foo bar
    #fOo BaR.capitalize() = FOo BaR
    return word[0].upper()+word[1:]
def plural(string):
    #makes a word plural
    keylist = {'human':'humans','ox':'oxen','goose':'geese','moose':'moose','deer':'deer'}
    if string.lower() in ['human','ox','goose','moose','deer']:
        return keylist[string.lower()]
    elif string.lower()[-3:] == 'man':
        return string[:-2]+'en'
    elif string.lower()[-2:] in ['lf','rf']:
        return string[:-1]+'ves'
    elif  string.lower()[-3:] in ['ife','oof']:
        return string[:-2]+'ves'
    elif string.lower()[-1:] in ['s','x']:
        return string+'es'
    else:
        return string+'s'
def precep(word):
    #adds the correct version pf either a or an before the input
    #because I was doing this individually before and it was a pain in the butt
    #(I don't remember why I called it preceps but the name is stuck now)
    if word[0].lower() in 'aeiou':
        return 'an '+word
    else:
        return 'a '+word
def approxsyllables(string):
    #approximates the number of syllables based on the number of vowels
    total = 0
    for letter in list(string):
        if letter in list('aeiou'):
            total += 1
    if total < 1:
        total = 1
    return total
#here is a list of letters split up into categories
letters = {
    '1':list('bcdfgjkprstvwz$%'),
    '2':list('lrj'),
    '3':list('aeiouy&'),
    '4':list('lr'),
    '5':list('bcdfgjklmnprstvxz$%^'),
    '6':list('bcdfghjklpqrstvwxyz$%^'),
    '7':list('bcdfghjklprstvwxyz$%^'),
    '8':['ae','ai','ao','au','ea','ee','ei','ie','oe','oi','ou','ue']
    }
frequencies = {
    'a':82,
    'b':15,
    'c':28,
    'd':43,
    'e':127,
    'f':22,
    'g':20,
    'h':61,
    'i':70,
    'j':2,
    'k':8,
    'l':40,
    'm':24,
    'n':67,
    'o':75,
    'p':19,
    'q':1,
    'r':60,
    's':63,
    't':91,
    'u':28,
    'v':10,
    'w':24,
    'wh':24,
    'x':2,
    'y':20,
    'z':1,
    '$':33,
    '%':33,
    '&':80,
    '^':33,
    '3':9,
    '63':30,
    '37':30,
    '123':1,
    '637':90,
    '345':1,
    '1237':10,
    '6345':13,
    '12345':1
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
def polish(word):
    global seed
    #<polish word:
    #<Fix q:
    word = word.replace('q','qu')
    word = word.replace('quy','qui')
    #>q fixed
    #<Add multi-character letters:
    word = word.replace('$','sh')
    word = word.replace('%','th')
    word = word.replace('^','ch')
    word = word.replace('&',choose(['ae','ai','ao','au','ea','ee','ei','ie','oe','oi','ou','ue']))
    #>Multi-character letters added
    #<Fix hh:
    word = word.replace('hh','h')
    #>hh fixed
    #<Fix double multi:
    word = word.replace('thth','th')
    word = word.replace('shsh','sh')
    #>double multi fixed
    #<Enhance double vowel:
    for vowel in list('aiu'):
        word = word.replace(2*vowel,vowel+'\''+vowel)
    #>Double vowel enhanced
    #<Fix misc.:
    word = word.replace('iy','ey')
    word = word.replace('ih','eh')
    word = word.replace('yh','eh')
    #>Fixed
    #>word polished
    return word
def word(word,startseed):
    #returns blank requests to prevent it from being junked up
    if word == '':
        return word
    #&& bypasses translation
    if word[-2:] == '&&':
        return word[:-2]
    global seed
    seed = numbify(word)+startseed
    number = approxsyllables(word)+randint(-1,1)
    if number < 1:
        number = 1
    skeleton = ''
    oldword = word
    word = ''
    for x in range(0,number):
        syllable = ''
        syllable_skeleton = woose(syllables,frequencies)
        for letter in syllable_skeleton:
            syllable += woose(letters[letter],frequencies)
        #<polish syllable:
        #<Fix yy:
        if 'y' == syllable[0]:
            syllable = syllable.replace('yy','yi')
        else:
            syllable = syllable.replace('yy','ey')
        #>yy fixed
        #<Fix iw:
        syllable = syllable.replace('iw','ew')
        #>iw fixed
        #<Fix (letter)l:
        for letter in ['d','t','r','$','%']:
            syllable = syllable.replace(letter+'l',letter+choose(relist(letters['3'],frequencies))+'l')
        #>(letter)l fixed
        #<Fix lr:
        syllable = syllable.replace('lr','l'+choose(relist(letters['3'],frequencies))+'r')
        #>lr fixed
        #<Fix duplicate liquid:
        syllable = syllable.replace('rr','r')
        syllable = syllable.replace('ll','l')
        syllable = syllable.replace('jj','j')
        #>Duplicate liquids fixed
        #>syllable polished
        word += syllable
        skeleton += syllable_skeleton
    word = polish(word)
    if oldword[0] == oldword[0].upper():
        word = capitalize(word)
    return word