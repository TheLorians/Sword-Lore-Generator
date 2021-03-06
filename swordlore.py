# coding=utf-8
# Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re
from BasicFunctions import *
from Language import *

# Classes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Animal Classes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Animal(object):
    def __init__(self, names, bodyparts, covering):
        self.names = names
        self.bodyparts = bodyparts
        self.covering = covering

class Bodypart(object):
    def __init__(self, name, texture, count, shape):
        self.name = name
        self.texture = texture
        self.count = count
        self.shape = shape
    def bodmod(self):
        text_groups = {
            'furry' : ['fire', 'straight', 'flame', 'stripe', 'curved', 'fluffy',
                       'boney', 'soft', 'furry', 'bright', 'dark', color()],
            'feathery' : ['fire', 'straight', 'flame', 'stripe', 'spot', 'curved',
                          'round', 'boney', 'plume', 'bright', 'dark','boney', color()],
            'scaly' : ['fire', 'straight', 'flame', 'wet','stripe','spot','rough', color()],
            'organ' : ['fire', 'straight', 'flame', 'wet', color()],
            'bone' : ['fire', 'straight', 'flame', 'stripe', 'curved', 'sharp',
                      'boney', 'soft', 'hard', color()]
        }
        shape_groups = {
        #I know these shape names are not descriptive (Its really hard) so I've added examples above each one
            # legs, necks and arms
            'connector' : ['long', 'short', 'wide', 'thin', 'thick', 'slender'],
            # heads, feet, hands
            'end' : ['hammer', 'round', 'big', 'small','flat','smooth'],
            # belly and back
            'big' : ['armor','plate'],
            # eyes, tongue and teeth
            'small' : ['round', 'large', 'small', 'big', 'long', 'short']
        }
        return choose(text_groups[self.texture] + shape_groups[self.shape])

# Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def animal(animal_class):
    # Makes animals from an animal class
    # I'll move this later on
    defadj = ['aboreal', 'agile', 'alpine', 'barn', 'baron', 'bold', 'boreal', 'bowl', 'bronze', 'brook', 'burrowing', 'canyon', 'cave', 'cellar', 'chorus', 'cloud', 'cobweb', 'coffin', 'common', 'crested', 'desert', 'desert', 'domestic', 'dusky', 'dwarf', 'ebony', 'elegant', 'false', 'fire', 'flower', 'garden', 'garden', 'giant', 'goldenrod', 'goliath', 'grass', 'horned', 'house', 'huntsman', 'hybrid', 'imperial', 'ivory', 'king', 'labyrinth', 'lattice', 'marbled', 'marsh', 'midwife', 'mountain', 'orchard', 'ornamental', 'painted', 'pike', 'pool', 'pygmy', 'queen', 'regal', 'river', 'robber', 'rose', 'royal', 'skeleton', 'slender', 'smooth', 'spectal', 'spined', 'spotted', 'spring', 'steppe', 'stream', 'trapdoor', 'tree', 'wandering', 'water', pattern(), color()]
    bodypart = choose(animal_class.bodyparts)
    return choose([
        bodypart.bodmod() + ' ' + addaned(bodypart.name),
        choose(defadj),
        choose([word('Discov')+ '\'s', land('demonym')])
    ]) + ' ' + choose(animal_class.names)

def color():
    # this makes colors
    def ish(color):
        if color[-1] == 'e':
            return color[:-1] + 'ish'
        else:
            return color + 'ish'

    color = ['orange', 'red', 'crimson', 'purple', 'blue', 'green', 'yellow', 'black', 'white', 'grey', 'brown', 'gold']
    return choose([boose(['bright ', 'dark ', 'pale ']) + choose(color), choose(color), ish(choose(color))])


def element():
    # makes the name of an element 
    suffix = ['ite', 'ium', 'alt', 'sten', 'thril', 'yx', 'muth']
    return word('met') + choose(suffix)


def normalmetal():
    # returns an existing metal from a list
    return choose(['iron', 'steel', 'brass', 'bronze', 'silver', 'gold', 'pewter', 'tungsten', 'cast iron', 'pig iron',
                   'titanium', 'copper', 'lodestone', 'bismuth', 'nickel', 'duralumin', 'billon', 'tombac', 'ormolu',
                   'electrum', 'hepatizon', 'sterling silver', 'mithril'])


def specificmetal():
    # makes the name of a new metal 
    adjective = ['blood', 'ancient', 'red', 'black', 'white', 'astral', 'meteoric', 'rose', 'crucible',
                 word('Name') + "'s", 'cursed', 'spectral', 'solar', 'raw']
    metal = ['iron', 'steel', 'silver', 'metal', 'brass', 'bronze']
    return choose(adjective) + ' ' + choose(metal)


def loredmetal():
    # makes metal with lore
    # room for improvement
    return choose([specificmetal(), normalmetal()]) + ' mined from ' + boose(['beneath ', 'under ']) + mountain()


def alloy():
    #makes an alloy of two metals
    metal1 = choose([element(), normalmetal(), specificmetal(), loredmetal()])
    metal2 = choose([element(), normalmetal(), specificmetal(), loredmetal()])
    return 'an alloy of ' + metal1 + ' and ' + metal2


def metal():
    #This combines the above functions into one function
    return choose([element(), normalmetal(), specificmetal(), loredmetal(), alloy()])


def professional(profession, plurality=None, dobject='none'):
    # This makes a worker of a certain profession
    if plurality is None:
        plurality = choose(['singular','plural'])
    basic_synonym = [
        [
            'gaffer',
            'glassmith',
            'glassblower'
        ],
        [
            'craftsman'
        ],
        [
            'smith',
            'blacksmith',
            'goldsmith',
            'pewtersmith',
            'coppersmith',
            'silversmith',
            dobject + 'smith'
        ],
        [
            'wizard',
            wizardtype()
        ],
        [
            'hunter',
            dobject + ' hunter'
        ]
    ]
    if any(profession not in group for group in basic_synonym):
        basic_synonym.append([profession])
    profession_class = choose(choose([group for group in basic_synonym if profession in group]))
    if randint(0,1) == 0:
        profession_class = 'master ' + profession_class
    name = word(capitalize(profession))
    # RIP Akteerg the painter
    epithettype = 'maker'
    if profession == 'wizard':
        epithettype = 'wizard'
    singular = choose([
        profession_class + ' ' + name,
        name + ' the ' + profession_class,
        name + ', '+ epithet(epithettype)
    ])
    # TODO add aprenticeships
    if plurality == 'singular':
        return singular
    template = choose([
        'the # & of @',
        'the & of @',
        'the last great & of @',
        'the first great & of @',
        '# & from @',
        '& from @',
        'the ' + choose([
            'disciples',
            'followers',
            'apprentices'
        ]) + ' of ' + singular
    ])
    professional_class = choose([
        choose(['dwarf', 'elf', 'man', 'gnome']),
        choose(['dwarven', 'elven', 'human', 'gnomish']) + ' ' + profession_class
    ])
    temp = template.replace('#', str(randint(2, 9)))
    temp = temp.replace('&', plural(professional_class))
    temp = temp.replace('@', capitalize(word('place')))
    return temp


def mountain():
    # creates the name of a mountain


    # TODO: Move this out of the function
    adjectives = ['lonely', 'icy', 'misty', 'red', 'golden', 'silver', 'frozen', 'ancient', 'cold', 'windy', 'cloudy',
                  'north', 'south', 'east', 'west', 'crying', 'burning', 'walking', 'wandering', 'howling', 'windswept',
                  'white', 'silver', 'sleepy', 'sleeping']
    return choose(
        ['The ' + capitalize(choose(adjectives)) + ' Mountains', 'Mount ' + capitalize(word('mount'))])


def location(feature):
    # This makes a natural location
    # TODO: Move this out of the function
    adjectives = ['lonely', 'icy', 'misty', 'red', 'golden', 'silver', 'frozen', 'ancient', 'cold', 'windy', 'cloudy',
                  'north', 'south', 'east', 'west', 'crying', 'burning', 'walking', 'wandering', 'howling', 'windswept',
                  'white', 'silver', 'sleepy', 'sleeping']
    return choose(['the ' + capitalize(choose(adjectives)), word('Plaq')]) + ' ' + capitalize(feature)


def forge(dobject='none'):
    # room for improvement
    # templates = ['Halls of &', 'fires of &', 'flames of &', 'forges of &', 'Hearth of &', 'embers of &', '& caves',
    # '& caverns']
    # return choose(templates).replace('&', word('Forge', startseed))
    return choose([
        'the ' + choose([
            'forges ',
            'forge ',
            'hearth '
        ]) + choose([
            # make separate guild function
            'of ' + choose([
                choose([
                    professional('blacksmith', 'singular', dobject),
                    'the ' + professional('blacksmith', 'plural', dobject)
                ]),
                land()
            ]),
            choose([
                'under ',
                'beneath '
            ]) + mountain()
        ])

    ])


def land(type='country'):
    # makes a country or a demonym 
    root = word('Land')
    while root[-1] in list('aeiou') and len(root) > 1:
        root = root[:-1]
    root += choose(['ia', 'land'])
    if type == 'country':
        return root
    else:
        if root[-2:] == 'ia':
            return root + 'n'
        elif root[-4:] == 'land':
            return choose([root + 'ic', root[:-4] + 'ish'])


def cavespawn():
    # the cavespawn are a collection of ancient races that inhabit the darkest corners of the earth
    # they are generally rather passive and appear in small groups
    # they are mute but have elaborate writing systems and social orders
    # kings have waged war with them over millennia but they still remain
    lingtype = ['eye', 'ear', 'ghost', 'rock', 'bone', 'stone', 'wood', 'husk']
    mantype = ['slug', 'snail', 'snake', 'bird', 'moth', 'worm', 'pig', 'wolf', 'bear', 'fish', 'pig', 'husk', 'lava',
               'magma', 'rock', 'mail', 'olm', 'frog', 'lizard', 'leopard', 'dog']
    return choose([choose(lingtype) + 'ling', choose(mantype) + 'man'])


def wizardtype():
    # this makes wizard types
    # this is not really a generator because it chooses from a predetermined list and doesn't mix up the parts
    # there is room for improvement here
    return choose(['wizard', 'sorcerer', 'mage', 'alchemist', 'warlock', choose(['necro', 'pyro', 'litho']) + 'mancer'])


def epithet(dobject, gender='male'):
    # gives epithets to various things to add flavour
    if gender == 'male':
        genpronoun = 'son'
    else:
        genpronoun = 'daughter'
    if dobject == 'beast':
        simple_descriptor = choose([
            'ghastly',
            'undying',
            'unspeakable',
            'unseen',
            'unheard',
            'silent',
            'ancient',
            'relentless',
            'hellish',
            'hundred-eyed',
            'thousand-eyed',
            'immortal',
            'unholy',
            'howling',
            'undead',
            'festering',
            'abominable',
            'formidable',
            'wretched',
            'grusome',
            'blind',
            'dreadful',
            'great'
        ]) + ' '
        dominion = choose([
            'orc',
            'goblin',
            'skeleton',
            'skeletal warrior',
            'demon',
            'man',
            'hobgoblin',
            'demon',
            'cyclops',
            'giant',
            'troll',
            'knight',
            'undead',
            'ice giant',
            'ghost',
            cavespawn()
        ])
        epithet_name = choose([
            choose([
                'reaper',
                'eater',
                'harvester',
                'swallower',
                'corrupter',
                'defiler',
                'reckoner',
                'render',
                'digester'
            ]) + ' of ' + choose([
                'souls',
                'minds',
                'flesh',
                'bone',
                'the damned',
                'blood'
            ]),
            'the ' + simple_descriptor + choose([
                'mind',
                'overmind',
                'beast',
                'horror',
                'terror',
                'monster',
                'evil',
                'abomination',
                'seer',
                'overseer',
                'priest',
                'gatekeeper'
            ]),
            choose([
                choose([
                    'keeper',
                    'king',
                    'god',
                    'ruler',
                    'prince',
                    'master'
                ]) + ' of ' + choose([
                    'worms',
                    'maggots',
                    'the dead',
                    'the undead',
                    'bones',
                    'blood',
                    'souls',
                    'minds',
                    'snakes',
                    'fire',
                    'darkness',
                    'gold'
                ]), 'the ' + boose([
                    simple_descriptor
                ]) + choose([
                    'worm',
                    'maggot',
                    'snake',
                    'soul'
                ]) + ' ' + choose([
                    'keeper',
                    'eater',
                    'lord',
                    'god'
                ]),
                choose([
                    'king',
                    'god',
                    'ruler',
                    'prince',
                    'master'
                ]) + ' of the ' + plural(dominion).replace('undeads', 'undead'),  # TODO: plural function here
                'the ' + boose([
                    simple_descriptor
                ]) + dominion + ' ' + choose([
                    'king',
                    'god',
                    'ruler',
                    'prince',
                    'master'
                ])
            ])
        ]).replace('  ', ' ')
    elif dobject == 'hero':
        # room for improvement
        epithet_name = choose([
            'the ' + choose([
                'brave', 'strong', 'great', 'stoic', 'elder', 'younger', 'tall', 'short', 'powerful', 'adored', 'ox',
                'boar', 'bull', 'mountain', 'rock', 'stoic', 'wise', 'peaceful', 'calm', 'fast', 'bear', 'wolf', 
                'fox','lion', 'thirsty', 'hungry', 'tired', 'gentle', 'giant', 'last', 'holy', 'divine', 'fearless', 
                'steadfast','enlightened', 'exalted'
            ]),
            choose([
                'lion', 'bear', 'wolf', 'kind', 'soft'
            ]) + '-hearted',genpronoun + ' of ' + word('Father'),
            choose([
                'ogre', 'undead', 'ghast', 'skeleton', 'serpent', cavespawn(), 'demon', 'bear', 'beast', 'lion', 
                'wyvern', 'goblin', 'orc', 'man', 'troll', 'giant', 'hobgoblin', 'lindworm', 'knight', 'worm', 
                'frost giant', 'dragon', 'cyclops', 'skeletal warrior', 'wolf', 'minotaur', choose(['the ', '']) + 
                dragon()
                ]) + ' ' + choose(['slayer', 'killer']),
            'bane of '+plural(choose([
                'ogre', 'undead', 'ghast', 'skeleton', 'serpent', cavespawn(), 'demon', 'bear', 'beast', 'lion', 'wyvern', 'goblin', 'orc', 'man', 'troll', 'giant', 'hobgoblin', 'lindworm', 'knight', 'worm', 'frost giant', 'dragon', 'cyclops', 'skeletal warrior', 'wolf', 'minotaur', 'arthropod'
            ]))
        ])
    elif dobject == 'noble':
        # room for improvement
        romannumeral = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        epithet_name = choose([', the ' + choose(
            ['fair', 'kind', 'noble', 'just', 'wise', 'great', 'cruel', 'terrible', 'horrible', 'rotten', 'foolish']),
                               ', ' + genpronoun + ' of ' + land(), ' ' + choose(romannumeral)])
    elif dobject == 'maker':
        # room for improvement
        epithet_name = choose(['the steady handed', 'the steady of hand', 'the craftsman', 'the fireproof',
                               'the iron ' + choose(['thumbed', 'fingered', 'skinned']), 'the careful',
                               'the sharp-eyed', 'fire bellied', 'the bloodless', 'the dirty', 'the soot covered'])
    elif dobject == 'game':
        # this generates epithets for use in the legendry_game function
        # room for improvement
        epithet_name = ' of ' + location(choose(['valley', 'plain', 'forest', 'woods', 'mountain']))
    elif dobject == 'wizard':
        # room for improvement
        epithet_name = choose([' the ' + color(), ' the ' + wizardtype() + ' of ' + location(choose(
            ['valley', 'mountains', 'hills', 'caves', 'caverns', 'plains', 'plateau', 'island', 'desert', 'lake',
             'swamp', 'forest', 'canyon', 'ravine', 'chasm', 'hollow']))])
    else:
        # in case I made a mistake
        epithet_name = 'the forsaken'
    return epithet_name


def legendary_game():
    # creates the name of a legendary game animal
    coloration = choose(['white', 'silver', 'black', 'golden'])
    genus = choose(['elk', 'stag', 'ram', 'bison'])
    return 'the ' + boose(['great ']) + coloration + ' ' + genus + ' ' + epithet('game')


def dragon():
    # this makes the name for a type of dragon
    # Not a specific dragon
    # there is plenty room for improvement here
    return choose(
        ['lind', 'grind', 'lode', 'blood', 'flesh', 'gore', 'grist', 'grit', 'stench', 'fester', 'bone', 'old', 'book',
         'stone', 'husk']) + choose(['worm', 'wurm', 'wyrm'])


def worm():
    # creates the name of a worm
    classification = choose(
        ['blood', 'book', 'bone', 'flesh', 'mind', 'earth', 'stone', 'night', 'fire', 'lung', 'gut', 'mud', 'moss',
         'wood', 'sludge', 'husk', 'book'])
    basis = choose(['worm', 'maggot', 'crawler'])
    return choose(['giant ', '']) + classification + basis


def beast():
    # creates the name of an evil beast or creature
    class_type = choose(
        ['dragon', 'minotaur', 'cyclops', 'ogre', 'ghast', 'beast', 'serpent', 'wolf', 'lion', 'bear', 'wyvern', 'worm',
         'lindworm', 'frost giant', dragon()])
    # TODO this was copy pasted from line 395, move outside functions
    origin = location(choose(
        ['valley', 'mountains', 'hills', 'caves', 'caverns', 'plains', 'plateau', 'island', 'desert', 'lake', 'swamp',
         'forest', 'canyon', 'ravine', 'chasm', 'hollow']))
    name = capitalize(word('beast'))
    Epithet = epithet('beast')
    return choose([choose(['', name + ', ']) + 'the ' + class_type + ' of ' + origin, name + ', ' + Epithet])


def horde():
    return choose([
        'a horde of', 'an army of', choose([
            'one thousand', 'ten thousand', 'five hundred', 'one hundred', 'fifty', 'forty', 'thirty'
        ])
    ]) + ' ' + boose([
        'angry', 'unholy', 'demonic', 'ravenous', 'ghastly'
    ]) + ' ' + plural(choose([
        'ogre', 'undead', 'ghast', 'skeleton', 'serpent', cavespawn(), 'demon', 'bear', 'beast', 'lion', 'wyvern', 
        'goblin', 'orc', 'man', 'troll', 'giant', 'hobgoblin', 'lindworm', 'knight', 'worm', 'frost giant', 'dragon',
        'cyclops', 'skeletal warrior', 'wolf', 'minotaur'
    ]))


def hero():
    # creates the name and title of a mythical hero
    name = word('Hero')
    epithet_name = epithet('hero')
    return name + ', ' + epithet_name


def royalty():
    # creates the name and title of a royal
    name = word('King')
    title = choose(
        ['King', 'Queen', 'Duke', 'Duchess', 'Grand Duke', 'Archduke', 'Lord', 'Lady', 'Prince', 'Princess', 'Marquess',
         'Earl', 'Count', 'Countess', 'Baron', 'Baroness', 'Viscount', 'Viscountess']).lower()
    if title in ['queen', 'duchess', 'lady', 'princess', 'countess', 'baroness', 'viscountess']:
        gender = 'female'
    else:
        gender = 'male'
    epithet_name = epithet('noble', gender)
    return choose([capitalize(title) + ' ' + name + epithet_name, 'the ' + title + ' of ' + land()])


def spirit():
    # please comment this
    class_type = choose(['nymph', 'spirit', 'lady'])
    origin = location(choose(['lake', 'pond', 'forest']))
    return 'the ' + class_type + ' of ' + origin


def coral():
    # makes coral
    affix = ['fire', 'cloak', 'cactus', 'brain', 'ghost', 'cloud', 'rock', 'stone', color() + ' crust',
             choose(['elk', 'bison', 'bull', 'deer', 'moose', 'stag']) + 'horn', land('demonym')]
    return choose(affix) + ' coral'


def bone():
    # makes bone
    bsource = choose(['goblin', 'orc', 'human', 'dwarf', 'giant', 'troll', 'fish', 'deer', 'cow', cavespawn()])
    classification = choose(['rib', 'bone', 'tooth', 'spine', 'jaw'])
    lbsource = choose([beast()])
    return choose([bsource + ' ' + classification, 'the ' + classification + ' of ' + lbsource + ','])


def wood():
    # makes wood
    wsource = choose(
        ['oak', 'spruce', 'cedar', 'birch', 'pine', 'fir', 'hemlock', 'ash', 'chestnut', 'beech', 'elm', 'mahogany',
         'hickory', 'maple', 'stone'])
    return wsource + ' wood'


def ivory():
    # makes ivory
    i_source = boose(['mammoth', 'walrus', 'whale', land('demonym')])
    return i_source + ' ivory'


def biomaterial(size='small'):
    # makes biological materials
    # bone:
    bsource = bone()
    # wood:
    wsource = wood()
    # ivory:
    isource = ivory()
    # coral:
    csource = coral()
    if size == 'small':
        return choose([bsource, wsource, isource, csource])
    else:
        return choose([wsource, isource, csource])


def strange_biomaterial():
    # makes strange or unconventional biological materials
    # there is room for improvement here
    # crustacean based
    reflist = {'': 954, 'blue ': 50, 'yellow ': 5, 'white ': 1}
    coloration = woose(reflist)
    crust = coloration + choose(['crab', 'lobster']) + ' ' + choose(['shell', 'chitin'])
    # I can't think of anymore right now I'll add some later
    return choose([crust])


def material(size='small'):
    # makes materials
    # mainly used for sword blades and hilts
    biomat = biomaterial(size)
    strangemat = strange_biomaterial()
    inertmat = choose(['petrified', 'calcified', 'fossilized']) + ' ' + biomat
    return choose([biomat, inertmat, strangemat])


def script():
    # creates the name for a form of writing or alphabet
    preprefix = choose([land('demonym') + ' ', choose(
        ['proto-', 'elvish ', 'goblin ', 'dwarven ', 'gnomish', 'demonic', cavespawn() + ' ', 'rudimentary ', 'ancient '])])
    prefix = choose(['rune', 'glyph', 'old', 'stone', 'bone', 'dark', 'death', 'cipher ', 'cryptic ', 'sand'])
    suffix = choose(['script', 'rune', 'glyph', 'scratch', 'form'])
    if prefix == suffix:
        prefix = choose(['old', 'stone', 'bone', 'dark', 'death', 'cipher ', 'cryptic '])
    if prefix == 'cryptic ':
        return prefix + boose([preprefix]) + suffix
    return choose([preprefix, '']) + prefix + suffix


def council():
    # creates the name of a council
    variety = ['council', 'aldermen', 'senate', 'congress']
    place_of_origin = land()
    return 'the' + boose([' high', ' grand']) + ' ' + choose(variety) + ' of ' + place_of_origin


def age():
    # creates the name of an age or era
    var = choose(['age', 'era'])
    time = choose([
        choose([
            'golden',
            'silver',
            'dark',
            'bronze',
            'brass',
            'stone',
            'ancient',
            'ice',
            choose([
                'dwarven',
                'elven',
                'goblin',
                'woadic'
            ])
        ]) + ' ' + var,
        var + ' of ' + choose([
            'fire',
            'iron',
            'steel',
            'kings',
            'lords',
            'gods',
            'darkness',
            'the shadows',
            'blood',
            'filth',
            'the ancients',
            'monsters',
            'conquest',
            'empires',
            'beasts',
            'birds',
            'magic',
            'wizards',
            'war',
            'sand',
            word('Ruler'),
            plural(choose([
                'orc',
                'woad',
                'goblin',
                'troll',
                'giant',
                'cyclops',
                'man',
                'elf',
                'dwarf',
                'demon',
                cavespawn()
            ]))
        ]),
        choose([
            'early',
            'mid',
            'late'
        ]) + ' ' + choose([ #TODO make this a function
            '1st',
            '2nd',
            '3rd',
            '4th',
            '5th',
            '6th',
            '7th',
            '8th',
            '9th',
            '10th',
            '11th',
            '12th',
            '13th',
            '14th',
            '15th',
            '16th'
        ]) + ' century'
    ])
    return time.title()


def moonphase():
    # a generator for special phases of the moon
    # It does't really create new phases just picks from a list of existing ones
    phase = choose(['full', 'new', 'blood', 'blue', 'harvest', 'hunter\'s' + ' moon'])
    return phase


def moss():
    # A generator for types of mosses
    # https://en.wikipedia.org/wiki/List_of_the_mosses_of_Britain_and_Ireland
    attribute = choose(
        ['soft', 'long', 'wide', 'smooth', 'fine', 'bent', 'thin', 'short', 'tiny', 'slender', 'round', 'many', 'thick',
         color()]) + '-' + choose(['tufted', 'leafed', 'capped', 'stalked', 'fruited', 'tipped', 'capped'])

    primary_adjective = [choose(
        ['calcareous', 'flagellate', 'bimous', 'sessile', 'glaucous', 'alpine', 'silvergreen', 'western', 'northern',
         'eastern', 'southern', 'swamp', 'creeping', 'crawling', 'icy', 'pendulous', 'dark', 'bright', 'hanging',
         'slender', 'arctic', 'spreading', 'bog', 'rusty', 'velvet', 'robust', 'ambiguous', 'bordered', 'spinose',
         'mountain', 'sand', 'river', 'wall', 'pale', 'saltmarsh', 'twisting', 'cernuous', 'giant', 'fountain',
         'smaller', 'tendril', 'compact', 'silky', 'field', 'common', 'dusky', 'spiral', 'ribbed', 'fringed', 'fuzzy',
         'chalk', 'felted', 'shady', 'cordate', 'blunt', 'pretty', 'clustered', 'thin', 'hooded', 'starry', 'whorled',
         'elegant', 'striated', 'fatfoot', 'tiny', 'curled', 'petty', 'dappled', 'dingy', 'polar', 'soft', 'snow',
         'sparkling', 'feathery', 'snowy', 'woolly', 'bristly', 'tall']), word('Lord') + '\'s',
        color(), land('demonym'), attribute]

    secondary_adjective = ['pygmy', 'dwarf', 'hump', 'feather', 'yoke', 'fork', 'wood', 'beard', 'beardless', 'rock',
                           'thread', 'silver', 'earth', 'carrion', 'groove', 'apple', 'shield', 'spear', 'bow',
                           'rabbit', 'lattice', 'tree', 'helmet', 'hook', 'comb', 'cave', 'forklet', 'nut', 'flag',
                           'fox', 'extinguisher', 'cord', 'pocket', 'water', 'tufa', 'hoar', 'screw', 'brook', 'plait',
                           'silk', 'thatch', 'copper', 'thyme', 'flood', 'spur', 'bristle', 'fen', 'crisp', 'scorpion',
                           'fringe', 'streak', 'rose', 'ghost', 'turf', 'shaggy', 'dew', 'bark', 'club', 'ganite',
                           'umbrella', 'dung']

    variety = woose({'moss': 8, 'peatmoss': 1, 'smoothcap': 1, 'bryum': 1, 'ditrichum': 1, 'grimmia': 1, 'pottia': 1,
                     'pincusion': 1, 'redshank': 1, 'quillwort': 1})

    moss_name = (boose(primary_adjective) + ' ' + variety).replace(' moss', ' ' + boose(secondary_adjective) + '-moss')
    moss_name = moss_name.replace(' -', ' ')
    if not (not (moss_name[0] == ' ') or '-' in list(moss_name)):  # DeMorgan's law
        moss_name = choose(primary_adjective) + moss_name
    elif moss_name[0] == ' ':
        moss_name = moss_name[1:]
    return moss_name


def pattern():
    # This makes body patterns for animals (and maybe other things
    # this is a pretty good function further implementation could benefit the program
    modifier = ['long', 'short', 'wide', 'thin', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
    base = ['band', 'spot', 'stripe']
    return choose([choose(modifier), color()]) + ' ' + choose(base)


def spider():
    # makes spiders
    # https://en.wikipedia.org/wiki/List_of_spider_common_names

    def weaver():
        shape = ['orb', 'hammock', 'tent', 'dome', 'rob', 'net', 'tower', 'maze', 'labyrinth']
        return choose(shape) + 'weaver'

    # TODO Do something with the variables below

    bodymodifier = ['long', 'feather', 'star', 'greater', 'tuft', 'fire', 'straight', 'flame', 'stripe', 'curved',
                    'hammer', 'thick', 'thin', 'slender', 'round']
    bodypart = ['horned', 'legged', 'headed', 'bellied', 'kneed', 'toed', 'footed', 'jawed', 'backed', 'mouth',
                'shouldered']
    subvar = choose(
        ['cloud', 'crab', 'garden', 'cave', 'ornamental', 'house', 'wolf', 'bat', 'spotted', 'zebra', 'barn', 'baboon',
         'canyon', 'marbled', 'lynx', 'cellar', 'cobweb', 'giant', 'rose', 'common', 'mahogany', 'slender', 'false',
         'bowl', 'huntsman', 'desert', 'goliath', 'skeleton', 'domestic', 'baron', 'king', 'lattice', 'leafflitter',
         'goldenrod', 'dewdrop', 'sand', 'bottle', 'diving', 'flower', 'humpbacked', 'ivory', 'borrowing', 'bold',
         'water', 'bronze', 'spined', 'wall', 'ebony', 'trapdoor', 'ghost', 'pike', 'labyrinth', 'robber', 'coffin',
         'grass', 'elegant', 'orchard'])
    var = ['orbweaver', 'tarantula', 'meshweaver', 'jumper', 'birdeater', 'widow', weaver()]
    subvar = choose([subvar, pattern()])
    tempor = choose(['$', '%', '&', '$ %', '$ &', '% &', '$ % &']) + ' ' + choose([choose(var), 'spider'])
    return tempor.replace('$', color()).replace('%', land('demonym')).replace('&', subvar)


def normalgem():
    # A generator for real gemstones
    # https://www.wikiwand.com/en/List_of_gemstone_species
    # http://www.gemselect.com/other-info/gemstone-list.php
    gem = ['alexandrite', 'andalusite', 'axinite', 'benitoite', 'beryl', 'aquamarine', 'bixbite', 'emerald',
           'morganite', 'blood stone', 'cassiterite', 'celestite', 'chrysoberyl', "cat's eye", 'chrysocolla',
           'clinohumite', 'cordierite', 'corundum', 'ruby', 'saphire', 'danburite', 'diamond', 'diopside', 'dioptase',
           'dumortierite', 'feldspar', 'amazonite', 'labradorite', 'moonstone', 'sunstone', 'fluorite', 'garnet',
           'hessonite', 'hambergite', 'hematitejade', 'jadeite', 'nephrite', 'jasper', 'kornerupine', 'kunzite',
           'malachite', 'peridot', 'prehnite', 'pyrite', 'quartz', 'amethystcitrine', 'smokey quartz', "tiger's-eye",
           'chalcedony', 'agate', 'aventurine', 'onyx', 'rhodochrosite', 'serandite', 'spinel', 'sugilite', 'topaz',
           'turquoise', 'tourmaline', 'variscite', 'vesuviante', 'xenotime', 'zeolite', 'thomsonite', 'zircon',
           'zoisite', 'tanzanite', 'thulite', 'amber', 'ammolite', 'copal', 'coral', 'pearl', 'lapis-lazuliobsidian',
           'maw-sit-sit', 'unakite', 'ametrine', 'apatite', 'carnelian', 'diaspore', 'scapolite', 'opal', 'calcite',
           'charoite', 'chrysoprase', 'clinohumite', 'enstatite', 'gaspeite', 'goshenite', 'hackmanite', 
           'hemimorphite','hiddenite', 'howlite', 'idocrase', 'iolite', 'kunzite', 'kyanite', 'larimar', 
           'lepidolite', 'melanite', 'andradite', 'moldavite', 'tektite', 'chrysolite', 'morganite', 'nuummite', 
           'orthoclase', 'pietersite', 'rhodonite', 'scapolite', 'serphinite', 'clinochlores', 'serpentine', 
           'smithsonite', 'sodalite', 'sphalerite', 'sphene', 'tanzanite', 'verdite']
    return choose(gem)


def specificgem():
    # This makes a gem that may or may not exist
    adjective = ['mystic', 'cat\'s eye', 'andesine', 'color-change', 'dendritic', 'fire', 'star', 'pyrope', 'rainbow',
                 'rutile', 'rose', 'tashmarine', 'chrome', color()]
    return choose(adjective) + ' ' + normalgem()


def gem():
    # makes gems from the above functions
    return choose([normalgem(), specificgem(), element()])


def normalglass():
    # a generator for real types of glasses
    # https://en.wikipedia.org/wiki/Category:Glass_types
    # http://www.cmog.org/article/types-glass
    # https://en.wikipedia.org/wiki/Category:Glass_compositions
    glass = ['glass', 'beveled glass', 'plate glass', 'carnival glass', 'crown glass', 'depression glass',
             'favrile glass', 'flat glass', 'float glass', 'vitrum flextile', 'flexible glass', 'frosted glass',
             'fumed silica', 'pyrogenic silica', 'fused quartz', 'glass of antimony', 'goofus glass', 'ground glass',
             'moss agate glass', 'rippled glass', 'sitall', 'starfire glass', 'tiffany glass', 'toughened glass',
             'reinforced glass', 'tempered glass', 'photochromic glass', 'soda-lime glass', 'lead glass',
             'cobalt glass', 'cranberry glass', 'dichroic glass', 'flint glass', 'jadeite', 'leaded glass',
             'milk glass', 'opaline glass', 'reagent bottle', 'uranium glass', color() + ' glass',
             color() + ' plate glass']
    return choose(glass)


def specificglass():
    # makes the name of a non-real type of glass
    # room for improvement
    return color() + ' glass'

def glass():
    # makes glass from the above functions
    return choose([normalglass(),specificglass()])

def dog():
    # makes the name for a type of dog
    adjective = ['alpine', 'great', 'king', 'lowland', 'highland', color()]
    prey = ['fox', 'rabbit', 'sheep', 'deer', 'wolf', 'seal']
    base = ['hound', 'shepherd', 'malamute', 'akita', 'mountain dog', 'bloodhound', 'setter', 'greyhound', 'sleddog',
            'mastiff', choose(prey) + choose(['hound', 'dog'])]
    return choose(adjective) + ' ' + choose(base)


def book():
    # makes the title for a fictional book
    # room for improvement

    def epic():
        # TODO Improve this, use people sometime
        people = ['bard', 'king', 'knight', 'jester', 'man']
        title = choose(['the tale of ' + word('Epic'), 'the fall of ' + word('Epic'),
                        'the epic of ' + word('Epic'), 'the myth of ' + word('Epic'),
                        word('Epic')])
        return title

    def contemporary():
        first_person = ['The Old Man', 'A Man', 'The King', 'The Prince']
        second_person = ['the Sea', 'His Dog', 'The Moon']
        return choose(first_person) + ' and ' + choose(second_person)

    return choose([epic(), contemporary()])


def academicbook():
    # makes a non-fiction book title
    academic = ['Physicist', 'Mathematician', 'Chemist', 'Alchemist', 'Scientist', 'Herpetologist', 'Herbologist',
                'Entomologist', 'Philosopher', 'Logician', 'Economist', 'Engineer', 'Botanist', 'Zoologist',
                'Pharmacologist', 'Geologist', 'Astronomer', 'Psychologist']
    field = ['Physics', 'Mathematics', 'Chemistry', 'Alchemy', 'Science', 'Herpetology', 'Herbology', 'Entomology',
             'Philosophy', 'Logic', 'Economics', 'Engineering', 'Botany', 'Zoology', 'Pharmacology', 'Geology',
             'Astronomy', 'Psychology']
    fieldadjective = ['Physical', 'Mathematical', 'Chemi cal', 'Alchemical', 'Scientific', 'Herpetologic', 'Herbologic',
                      'Entomological', 'Philosophic', 'Logical', 'Economic', 'Engineering', 'Botanical', 'Zoologic',
                      'Pharmacological', 'Geologic', 'Astronomic', 'Psychological']

    # TODO use these some day
    place = ['Plains', 'Savanna', 'Arctic', 'Tropics']
    organism = ['Insects', 'Plants', 'Fungi', 'Birds', 'Fish', 'Reptiles', 'Mammals', 'Amphibians', 'Arachnids',
                'Beetles']
    title = ['Principles of ' + choose(field), precep(choose(academic)) + '\'s ' + choose(['Handbook', 'Guidebook']),
             'A Guide to ' + choose(fieldadjective) + ' Principles', 'Mastering ' + choose(field),
             'A ' + boose(['Brief ', 'Comprehensive ']) + 'History of ' + choose(field)]
    return choose(title)


def enscript():
    # Eamon's function
    return '\t' + choose(['All that is gold does not glitter', 'Not all those who wander are lost',
                          'The old that is strong does not wither', 'Deep roots are not reached by the frost',
                          'From the ashes a fire shall be woken', 'A light from the shadows shall spring',
                          'Renewed shall be blade that was broken', 'The crownless again shall be king',
                          'All that is gold does not glitter,\nNot all those who wander are lost;\n'
                          'Deep roots are not reached by the frost.\nFrom the ashes a fire shall be woken,\n'
                          'A light from the shadows shall spring;\nRenewed shall be blade that was broken,\n'
                          'The crownless again shall be king',
                          'Three Rings for the Elven-kings under the sky,\n'
                          'Seven for the Dwarf-lords in their halls of stone,\nNine for Mortal Men doomed to die,\n'
                          'One for the Dark Lord on his dark throne\nIn the Land of Mordor where the Shadows lie.\n'
                          'One Ring to rule them all, One Ring to find them,\n'
                          'One Ring to bring them all and in the darkness bind them\n'
                          'In the Land of Mordor where the Shadows lie.',
                          'One Ring to rule them all, One Ring to find them,\n'
                          'One Ring to bring them all and in the darkness bind them',
                          'Do not go gently into that good night', 'Where is your god now', 'I hurt people']).replace(
        '\n', '\n\t') + '\n'


def war():
    state = random.getstate()
    participant1 = land('demonym')
    random.setstate(state)
    participant1l = land()
    participant2 = participant1
    participant2l = participant1l
    while participant1 == participant2:
        state = random.getstate()
        participant1 = land('demonym')
        random.setstate(state)
        participant1l = land()
    return 'the ' + choose([
        boose(['first', 'second', 'third']) + ' ' + participant1 + '-' + participant2 + ' war',
        participant1 + ' civil war',
        participant1 + choose([' invasion', ' conquest']) + ' of ' + participant2l
    ])


def amphibian(genus=None):
    # makes amphibians
    # https://en.wikipedia.org/wiki/List_of_amphibians_of_Europe
    # http://www.californiaherps.com/allsalamanders.
    # http://www.californiaherps.com/allfrogs.html
    if genus is None:
        genus = choose(['frog', 'salamander', 'toad', 'newt', 'spadefoot', 'bullfrog', 'eft', 'olm', 'axolotl',
                         'treefrog'])
    bodymodifier = ['long', 'feather', 'star', 'greater', 'fire', 'straight', 'flame', 'stripe', 'curved', 'hammer',
                    'thick', 'thin', 'slender', 'round']
    bodypart = ['legged', 'headed', 'bellied', 'kneed', 'toed', 'footed', 'backed', 'mouth', 'shouldered']
    subvar = choose(
        ['cloud', 'common', 'water', 'crested', 'painted', 'tree', 'widwife', 'brook', 'alpine', 'stream', 'agile',
         'fire', 'marbled', 'pool', 'hybrid', 'imperial', 'wood', 'smooth', 'ribbed', 'marsh', 'regal', 'royal',
         'tiger', 'cloud', 'aboreal', 'wandering', 'mountain', 'garden', 'alpine', 'desert', 'river', 'brook', 'spring',
         'dusky', 'pygmy', 'giant', 'slimy', 'boreal', 'spectal', 'king', 'queen', 'leopard', 'chorus', 'clawed'])
    genera = ['frog', 'salamander', 'toad', 'newt', 'spadefoot', 'bullfrog', 'eft', 'olm', 'axolotl', 'treefrog']
    subvar = choose([subvar, pattern()])
    tempor = choose(['$', '%', '&', '$ %', '$ &', '% &', '$ % &']) + ' ' + genus
    return tempor.replace('$', color()).replace('%', land('demonym')).replace('&', subvar)


def carving(epithets=True):
    prey = choose(['fox', 'bear', 'moose', 'deer', 'stag', 'rabbit'])
    royal = royalty()
    if not epithets:
        royal = royal.split(',')[0]
    picture = choose([
        boose([hero() + ' leading troops in ']) + battle(),
        hero() + ', ' + choose([
            'fighting',
            'slaying',
            'defeating',
            'vanquishing'
        ]) + ' ' + choose([
            beast(),
            horde()
        ]),
        choose([
            'hunters',
            'huntsmen',
            'hounds',
            'dogs',
            plural(dog()),
            'a ' + dog(),
            professional('hunter', prey)
        ]) + ' ' + choose([
            'hunting',
            'chasing'
        ]) + ' ' + choose([
            'a ' + boose([
                'wild '
            ]) + prey,
            plural(prey),
            legendary_game()
        ]),
        'a scene from ' + book(),
        royal + '\'s ' + dog() + ' ' + word('Dog')
    ])
    return 'a depiction of ' + picture


def stringthing():
    # makes literal strings.
    # like for bows and such.
    mamsource = ['elk', 'deer', 'bison', 'moose', 'pig', 'cow']
    return choose([choose(mamsource) + ' ' + choose(['sinew']), spider() + ' silk'])


def wool():
    # This makes types of wool
    # Possibly room for improvement
    return (boose(['sheep', 'alpaca', 'llama', 'churro']) + ' ' + choose(['wool', 'cashmere'])).strip(' ')


def velvet():
    # makes velvets & velveteen
    materials_master_list = ['silk', 'cotton', 'chiffon', 'rayon', wool()]
    materials = choose([
        choose(materials_master_list),
        read_list(choose(materials_master_list,randint(2,3)))
    ])
    return materials + ' ' + choose(['velvet', 'velveteen', 'velveret'])


def dye(coloration=None):
    # this creates a natural dye mixture for a given color
    # add black, brown, grey, and white
    # http://pioneerthinking.com/crafts/natural-dyes
    # https://en.wikipedia.org/wiki/Natural_dye#Greys_and_blacks
    if coloration == None:
        coloration = choose(['red','orange','yellow','green','blue','purple','brown'])
    color_sources = {
            'purple': [
                'murex',
                'mulberries',
                'elderberries',
                'red cedar roots',
                'black berries'
                ],
            'orange': [
                'alder bark',
                'madder',
                'juniper',
                'king bolete',
                'chicken mushroom',
                'chicken of the woods',
                'sulphur shelf',
                'barberry',
                'bloodroot',
                'butternut tree bark',
                'carrot',
                'eucalyptus',
                'giant coreopsis',
                'lichen',
                'lilac',
                'onion',
                'tumeric',
                'dyer\'s polypore cooked with ammonia'
                ],
            'red': [
                'fermented prickly pears',
                'sumac',
                'cochineal',
                'lobster mushroom',
                'giant puffball',
                'sycamore bark',
                'bedstraw root'
                'pokeweed berries',
                'dyer\'s madder',
                'dyer\'s polypore cooked with ammonia in an iron pot'
            ],
            'blue': [
                'indigo',
                'woad',
                'dogwood bark',
                'dyer\'s knotweed'
            ],
            'green': [
                'algae',
                'lichen',
                'horse mushroom',
                'meadow mushroom',
                'shaggy mane',
                'oyster mushroom',
                'blewit',
                'green foxglove',
                'red pine needles',
                'dyer\'s polypore cooked with ammonia in a copper pot'
            ],
            'yellow': [
                'alfalfa seeds',
                'chanterelle',
                'saffron',
                'weld',
                'pomegranate rind',
                'turmeric',
                'safflower',
                'quercitron',
                'waxen woad',
                'larkspur',
                'old fustic',
                'young fustic',
                'maitake',
                'dyer\'s mulberry',
                'dyer\'s greenweed',
                'dyer\'s broom',
                'dyer\'s whin',
                'dyer\'s polypore cooked with salt water'
            ],
            'brown': [
                'artist\'s conk',
                'reishi mushroom',
                'boiled acorn',
                'beetroot',
                'birch bark',
                'broom bark',
                'broom sedge',
                'coffee grinds',
                'coneflower',
                'goldenrod shoots',
                'oak bark',
                'walnut'
            ],
            'black': [
                'ink',
                'iris',
                'oak galls'
            ]
        }
    color_chart = {
        'purple': [
            [
                'red',
                'blue'
            ]
        ],
        'orange': [
            [
                'red',
                'yellow'
            ]
        ],
        'green' : [
            [
                'blue',
                'yellow'
            ]
        ],
        'brown' : [
            [
                'orange',
                'black'
            ],
            [
                'yellow',
                'red',
                'black'
            ]
        ]
    }
    if coloration in color_chart:
        color_mix = choose(color_chart[coloration])
    else:
        color_mix = [coloration]
    ingredients = map(lambda x: choose(color_sources[x]), color_mix)
    return read_list(ingredients)

def clothlore():
    # provides short lore for cloth
    coloration = choose(['red','orange','yellow','green','blue','purple','brown'])
    lore = ''
    lore += choose([
        'woven',
        'spun'
    ]) + ' from ' + choose([
        spider() + ' silk',
        'hemp',
        'straw',
        'grass',
        'sisal',
        'cotton',
        wool(),
        'qiviut',
        'silk',
        metal()
    ]) + boose([
            ' by ' + professional('weaver')
        ]) + boose([
            ' and dyed ' + coloration + ' with ' + dye(coloration)
        ])
    return lore


def fabric():
    return choose([
        choose([
            'raw hide',
            choose([
                'cow',
                'goat',
                'deer',
                'elk',
                'caribou',
                'reindeer',
                'ox',
                'bison',
                'buffalo'
            ]) + ' hide',
            'cloth',
            color() + ' cloth',
            color() + ' ' + wool(),
            color() + ' silk',
            'fabric',
            velvet(),
            'silk',
            'chiffon',
            'leather',
            'black leather',
            'brown leather',
            'red leather',
            'bat leather',
            'fish leather',
            'deerskin',
            'human skin',
            'goblin skin',
            'snakeskin',
            'lizard skin',
            'dragon skin'
        ]),
        boose([
            color() + ' '
        ]) + choose([
            'cloth',
            'fabric'
        ]) + ' ' + clothlore()
    ])


def bird():
    # this makes bird names
    """Makes Birds"""
    # birds are made here
    genera_count = 0
    def bird_genus():
        # this makes formulaic bird genera names
        prefixes = ['ant', 'eas', 'sun', 'humming', 'snow', 'wes', 'bell', 'bower', 'fairy', 'black', 'mocking',
                    'cuckoo', 'grass', 'jungle', 'puff', 'love', 'gold', 'wren', 'rifle', 'bush', 'tropic', 'bit',
                    'king', 'frigate', 'shrike-', 'cat', 'mouse', 'blue', 'guinea', 'bristle', 'pea', 'scrub', 'cow',
                    'dollar', 'fern', 'magpie-', 'hoopoe-', 'lyre', 'oven', 'satin', 'meadow', 'gnat', 'rose',
                    'mistletoe', 'sky', 'sugar', 'wood', 'fig', 'mallee', 'haw', 'song', 'fire', 'tailor', 'bull',
                    'spur', 'pilot', 'parrot', 'laughing', 'friar', 'apostle', 'widow', 'chaf', 'sunbit', 'shel',
                    'wattle', 'spinifex', 'cicada', 'umbrella', 'whip', 'helmet', 'leaf', 'stitch', 'butcher', 'moor',
                    'pepper', 'oil', 'water', 'go-away-', 'tinker', 'nun', 'swamp', 'green', 'secretary', 'quail-',
                    'tree', 'fish', 'cloud', 'humming']
        suffixes = ['tern', 'bird', 'hen', 'duck', 'lark', 'tit', 'fowl', 'shrike', 'finch', 'thrush', 'wren',
                    'warbler', 'dove']
        return choose(prefixes) + choose(suffixes)

    # TODO wat @ next line
    voriabel = bird_genus()
    common_genera = ['sparrow', 'owl', 'woodpecker', 'flycatcher', 'warbler', 'eagle', 'parrot', 'goose', 'oriole',
                     'penguin', 'duck', 'kingfisher', 'hawk', 'pigeon', 'finch', 'cuckoo', 'petrel', 'robin', 'dove',
                     'vulture', 'thrush', 'gull', 'plover', 'heron', 'quetzal']
    uncommon_genera = ['sunbird', 'tern', 'hornbill', 'parakeet', 'jay', 'tanager', 'starling', 'swallow',
                       'hummingbird', 'wren', 'tinamou', 'weaver', 'bird-of-paradise', 'barbet', 'tyrant', 'honeyeater',
                       'macaw', 'crane', 'tit', 'snowfinch', 'kite', 'gnatcatcher', 'white-eye', 'swift', 'nightjar',
                       'grebe', 'antbird', 'pheasant', 'vanga', 'babbler', 'crow', 'buzzard', 'pitta', 'magpie',
                       'turaco', 'falcon', 'lark', 'grosbeak', 'albatross', 'pipit', 'bee-eater', 'stork', 'cormorant',
                       'bustard', 'swan', 'harrier', 'ibis', 'shearwater', 'lorikeet', 'roller', 'skua', 'broadbill',
                       'quail', 'bowerbird', 'monarch', 'rail', 'lapwing', 'pelican', 'partridge', 'flamingo',
                       'bellbird', 'woodcreeper', 'cockatoo', 'trogon', 'toucan', 'fairywren', 'bulbul', 'manakin',
                       'bunting', 'redstart', 'myna', 'kestrel', 'antshrike', 'jacamar', 'amazon', 'piculet',
                       'toucanet', 'puffbird', 'tragopan', 'thrasher', 'raven', 'mockingbird', 'junglefowl', 'hermit',
                       'cuckooshrike', 'cotinga', 'grouse', 'miner', 'booby', 'aracari', 'sandgrouse', 'guan',
                       'petronia', 'chough', 'motmot', 'blackbird', 'shrike', 'goshawk', 'vireo', 'martin']
    rare_genera = ['flicker', 'curlew', 'condor', 'bittern', 'waxwing', 'cisticola', 'godwit', 'guillemot',
                   'oystercatcher', 'topaz', 'teal', 'honeycreeper', 'spoonbill', 'owlet', 'frigatebird', 'lovebird',
                   'waxbill', 'nightingale', 'sapsucker', 'parrotbill', 'treecreeper', 'foliage-gleaner', 'tapaculo',
                   'catbird', 'turkey', 'crake', 'flameback', 'stone-curlew', 'pratincole', 'riflebird', 'wagtail',
                   'finfoot', 'prion', 'nuthatch', 'egret', 'shag', 'parrotlet', 'caracara', 'coucal', 'ptarmigan',
                   'sparrowhawk', 'bristlebird', 'kingbird', 'hoopoe', 'grassbird', 'stilt', 'fantail', 'thornbill',
                   'chickadee', 'dipper', 'gannet', 'guineafowl', 'tropicbird', 'cardinal', 'antwren', 'quail-dove',
                   'tody', 'wheatear', 'jacana', 'peafowl', 'minivet', 'eagle-owl', 'minla', 'whistler', 'hawk-owl',
                   'screamer', 'swiftlet', 'needletail', 'mousebird', 'accentor', 'kiwi', 'avocet', 'cowbird', 'chat',
                   'sandpiper', 'hawk-eagle', 'antpitta', 'nutcracker', 'goldfinch', 'bluebird', 'fiscal', 'coquette',
                   'snipe', 'whydah', 'dollarbird', 'shoebill', 'gadwall', 'poorwill', 'razorbill', 'scimitarbill',
                   'redpoll', 'kittiwake', 'silvereye', 'smew', 'chicken', 'veery', 'yellowhammer', 'titmouse',
                   'rosella', 'eider', 'merlin', 'lory', 'pochard', 'dickcissel', 'auk', 'tody-flycatcher', 'grenadier',
                   'shrike-thrush', 'whiteface', 'go-away-bird', 'berrypecker', 'grassquit', 'camaroptera', 'hawfinch',
                   'oxpecker', 'bushchat', 'umbrellabird', 'chiffchaff', 'woodnymph', 'songlark', 'apostlebird',
                   'auklet', 'kinglet', 'fernwren', 'helmetshrike', 'firefinch', 'merganser', 'shoveler', 'iora',
                   'nighthawk', 'frogmouth', 'peacock-pheasant', 'openbill', 'bare-eye', 'gallito', 'seedeater',
                   'siskin', 'spinetail', 'tattler', 'nunbird', 'brolga', 'besra', 'rockjumper', 'tailorbird', 'brant',
                   'pytilia', 'sungrebe', 'phalarope', 'nene', 'chlorophonia', 'hoatzin', 'tyrannulet', 'yellowlegs',
                   'reedling', 'anhinga', 'peppershrike', 'sicklebill', 'argus', 'puffin', 'butcherbird', 'cicadabird',
                   'gnateater', 'monal', 'roadrunner', 'hypocolius', 'mesite', 'logrunner', 'bernieria', 'oropendola',
                   'cachalote', 'meadowlark', 'jabiru', 'mesia', 'fulvetta', 'flowerpecker', 'grasswren', 'eremomela',
                   'astrapia', 'scythebill', 'buttonquail', 'harrier-hawk', 'antthrush', 'bateleur', 'bluebill',
                   'forktail', 'bleeding-heart', 'painted-snipe', 'sora', 'sheathbill', 'red-headed', 'osprey',
                   'racquet-tail', 'rook', 'shrike-tit', 'verdin', 'ibisbill', 'towhee', 'wattlebird', 'brilliant',
                   'phoebe', 'woodlark', 'redshank', 'whitethroat', 'shortwing', 'winp', 'conebill', 'quail-thrush',
                   'chaffinch', 'hornero', 'seriema', 'jackdaw', 'yuhina', 'owlet-nightjar', 'waterthrush', 'winter',
                   'curassow', 'fulmar', 'gallinule', 'killdeer', 'inca', 'friarbird', 'cinclodes', 'gnatwren',
                   'bristlebill', 'firewood-gatherer', 'magpie-goose', 'honeyguide', 'bronzewing', 'boatbill', 'alethe',
                   'scrubwren', 'goldcrest', 'trembler', 'whipbird', 'wattle-eye', 'bluebonnet', 'crombec', 'canastero',
                   'maleo', 'cahow', 'coua', 'triller', 'mallard', 'sittella', 'picathartes', 'bananaquit',
                   'mistletoebird', 'wallcreeper', 'sugarbird', 'tchagra', 'saddleback', 'hobby', 'hawk-cuckoo',
                   'blackeye', 'wrenthrush', 'whimbrel', 'dunlin', 'ruff', 'spinifexbird', 'knot', 'emerald', 'wigeon',
                   'courser', 'fieldfare', 'monjita', 'scoter', 'bullfinch', 'pewee', 'kakapo', 'puffleg', 'quelea',
                   'oilbird', 'junco', 'donacobius', 'goldeneye', 'fruiteater', 'iiwi', 'cuckoo-roller', 'parrotfinch',
                   'chachalaca', 'spinebill', 'pintail', 'quail-plover', 'trumpeter', 'sunbittern', 'boobook',
                   'longspur', 'xenops', 'secretarybird', 'drongo', 'bristlefront', 'scaup', 'snowcock', 'plantcutter',
                   'pardalote', 'swamphen', 'plovercrest', 'pauraque', 'rayadito', 'kookaburra', 'dowitcher',
                   'whip-poor-will', 'illadopsis', 'widowbird', 'noddy', 'niltava', 'magpie-robin', 'potoo', 'corella',
                   'linnet', 'bobwhite', 'budgerigar', 'ovenbird', 'parula', 'stitchbird', 'silktail', 'munia',
                   'twinspot', 'hoopoe-lark', 'yellownape', 'capercaillie', 'sabrewing', 'elaenia', 'koel', 'kiskadee',
                   'grackle', 'scrubbird', 'hillstar', 'bushshrike', 'tinkerbird', 'bristlehead', 'hammerkop', 'apalis',
                   'piapiac', 'cockatiel', 'sharpbill', 'saltator', 'gerygone', 'leafbird', 'malleefowl', 'limpkin',
                   'sylph', 'stonechat', 'skimmer', 'kagu', 'greenbul', 'bobolink', 'wrentit', 'spurfowl', 'moorhen',
                   'skylark', 'schiffornis', 'streamertail', 'longbill', 'bokmakierie', 'weebill', 'figbird',
                   'euphonia', 'sunbird-asity', 'bluethroat', 'asity', 'cacique', 'blackcap', 'laughingthrush',
                   'prinia', 'ani', 'creeper', 'dunnock', 'shelduck', 'coot', 'brambling', 'satinbird', 'lyrebird',
                   'seedsnipe', 'currawong', 'korhaan', 'pilotbird', 'galah', 'woodcock', 'nunlet', 'sage-grouse',
                   'wryneck', 'greenfinch', 'ouzel', 'rosefinch', 'woodswallow', 'magpie-lark', 'sibia', 'crossbill',
                   'gyrfalcon', 'trainbearer', 'spadebill', 'batis', 'yellowthroat', 'wrybill', 'longclaw', 'bushtit',
                   'cochoa', 'adjutant']
    body_adjective = ['long', 'rufous', 'swallow', 'gros', 'wax', 'broad', 'lap', 'pin', 'racquet', 'short', 'spur',
                      'double', 'wag', 'bar', 'thick', 'burro', 'fin', 'bristle', 'needle', 'spoon', 'fan', 'parrot',
                      'spine', 'plain', 'flame', 'bare', 'groove', 'boat', 'thorn', 'golden', 'golden', 'hoary', 'gold',
                      'parrot', 'sickle', 'cross', 'shoe', 'band', 'open', 'boat', 'razor', 'long', 'sabre', 'wee',
                      'frog', 'silver', 'standard', 'streamer', 'wry', 'fork', 'reddish', 'scissor', 'straw', 'channel',
                      'gull', 'streak', 'three', 'hook', 'silk', 'logger', 'pheasant', 'plum', 'erect', 'saddle',
                      'spot', 'fiery', 'dusky', 'olive', 'cone', 'plover', 'pin', 'keel', 'slaty', 'streamer', 'sharp',
                      'sheath', 'wire', 'spade', 'thorn', 'wedge', 'sulphur', 'rusty', 'large', 'scimitar', 'azure',
                      'silky', 'saddle', 'fire', 'wattle', 'zone', 'curve', 'ibis', 'scythe', 'dark', 'bronze', 'pale',
                      'ribbon', 'short', 'plate', 'fan', 'spoon', 'rose', 'mistle', 'sword', 'stork', 'puff', 'silver',
                      'chestnut']
    body_part = ['beaked', 'crowned', 'billed', 'winged', 'crested', 'tufted', 'breasted', 'kneed', 'toed', 'footed',
                 'tailed', 'backed', 'headed', 'eyed', 'feathered']
    prefix = ['common', 'northern', 'great', 'crested', 'greater', 'spotted', 'golden', 'southern', 'little', 'eastern',
              'pygmy', 'cape', 'pied', 'rufous', 'wood', 'masked', 'ground', 'superb', 'paradise', 'mountain',
              'western', 'white', 'barred', 'new', 'king', 'rock', 'storm', 'scarlet', 'collared', 'chestnut', 'water',
              'striated', 'crimson', 'lesser', 'house', 'crowned', 'horned', 'giant', 'bush', 'speckled', 'alpine',
              'sooty', 'scops', 'varied', 'fruit', 'royal', 'ferruginous', 'spectacled', 'laughing', 'bearded', 'noisy',
              'imperial', 'snowy', 'snow', 'cuban', 'magellanic', 'reed', 'socotra', 'tufted', 'elegant', 'sea',
              'cattle', 'musk', 'bronze', 'desert', 'black-and-white', 'canyon', 'sage', 'sedge', 'tropical', 'tiger',
              'plain', 'song', 'pine', 'rhinoceros', 'planalto', 'burrowing', 'vulturine', 'roseate', 'abyssinian',
              'helmeted', 'tawny', 'slaty', 'olivaceous', 'fairy', 'fish', 'blue-and-white', 'hill', 'ruddy',
              'mourning', 'brush', 'arctic', 'cinereous', 'cliff', 'grasshopper', 'flightless', 'tree', 'glossy',
              'wandering', 'ringed', 'rainbow', 'painted', 'barn', 'whistling', 'buffalo', 'sarus', 'fox', 'vermilion',
              'hanging', 'thicket', 'ruffed', 'toco', 'greylag', 'loggerhead', 'jack', 'socorro', 'gray', 'cackling',
              'whooping', 'large', 'carrion', 'sand', 'adelie', 'kordofan', 'rockhopper', 'spinifex', 'orinoco',
              'prairie', 'cactus', 'scrub', 'abd', 'acadian', 'chimney', 'eclectus', 'blackburnian', 'hairy', 'wattled',
              'okinawa', 'izu', 'mew', 'key', 'bicoloured', 'houbara', 'sultan', 'manx', 'screech', 'lanner', 'mistle',
              'calandra', 'cinnamon', 'subdesert', 'chanting', 'malachite', 'elf', 'shining', 'herring', 'harlequin',
              'west', 'barnacle', 'monk', 'sociable', 'crab', 'lovely', 'rosy', 'hyacinth', 'diamond', 'squirrel',
              'tundra', 'kelp', 'marbled', 'ruby', 'eared', 'gila', 'lizard', 'clapper', 'wild', 'frilled', 'vernal',
              'restless', 'sombre', 'savanna', 'paddyfield', 'serpent', 'lapland', 'squamate', 'harpy', 'honey',
              'spruce', 'violet', 'pink', 'helmet', 'austral', 'peregrine', 'sind', 'macaroni', 'sacred', 'saxaul',
              'beach', 'necklaced', 'gentoo', 'bald', 'pinyon', 'iago', 'blood', 'scalloped', 'nicobar', 'splendid',
              'orchard', 'campo', 'snail', 'banded', 'coal', 'jungle', 'flame', 'cedar', 'nubian', 'mute',
              'versicoloured', 'steamer', 'prothonotary', 'fishing', 'silver', 'scimitar', 'striped', 'humboldt',
              'solitary', 'willow', 'regent', 'satyr', 'chinstrap', 'marsh', 'fig', 'carmine', 'griffon', 'belted',
              'evening', 'virginia', 'dark', 'lineated', 'jacobin', 'snake', 'unicoloured', 'downy', 'ring', 'croller',
              'chipping', 'sandhill', 'turtle', 'parasitic', 'dead', 'plumbeous', 'martial', 'palm', 'zebra', 'diving',
              'icterine', 'brent', 'jewel', 'velvet', 'penduline', 'namaqua', 'meadow', 'red-and-green', 'ceylon',
              'marabou', 'whooper', 'willie', 'welcome', 'sokoke', 'corn', 'night', 'small', 'vasa', 'acorn', 'saffron',
              'blue-and-yellow', 'resplendent', 'muscovy', 'pere', 'pallid', 'squacco', 'waterfall', 'ashy',
              'blacksmith', 'emperor', 'south', 'mulga', 'warbling', 'satin', 'coppersmith', 'goliath', 'topknot',
              'laysan', 'guira', 'chapada', 'jacky', 'raggiana', 'zitting', 'inland', 'bee', 'cerulean', 'russet',
              'mimic', 'ivory', 'paulo', 'wompoo', 'luzon', 'graceful', 'chukar', 'narina', 'brahminy', 'hooded',
              'zapata', 'antenna', 'java', 'cave', 'polar', 'variegated', 'kori', 'rufescent', 'hazel', 'victoria',
              'ocellated', 'variable', 'leaf', 'red-and-yellow', 'guanay', 'moustached', 'cloud', 'ghost', 'steppe',
              'tricolored']
    return choose([choose(prefix), choose([color(), choose(body_adjective)]) + choose(body_part), color(),
                   word('Bird') + '\'s', land('demonym')]) + ' ' + choose(
        [choose(common_genera), choose(uncommon_genera), choose(rare_genera), bird_genus()])


def blood():
    # makes blood
    reflist = {'': 15, 'coagulated ': 1}
    return woose(reflist) + boose(
        ['orc', 'woad', 'goblin', 'hobgoblin', 'kobold', 'gnome', 'troll', 'giant', 'cyclops', 'minotaur',
         cavespawn()]) + ' blood'


def ant():
    # makes the names of types of ants
    # http://www.antstuff.net/html/species_of_ants.html
    # http://www.myrmecos.net/north-american-ants/
    bodymodifier = ['long', 'feather', 'star', 'greater', 'tuft', 'fire', 'straight', 'flame', 'stripe', 'curved',
                    'hammer', 'thick', 'thin', 'slender', 'round']
    bodypart = ['horned', 'legged', 'headed', 'bellied', 'kneed', 'toed', 'footed', 'jawed', 'backed', 'mouth',
                'shouldered']
    adject = ['cloud', 'army', 'fighting', 'bull', 'carpenter', 'fire', 'glider', 'honey', 'honey pot', 'jumping',
              'leaf cutter', 'lemon', 'pharaoh', 'king', 'theif', 'weaver', 'silk', 'crab', 'garden', 'cave',
              'ornamental', 'house', 'wolf', 'bat', 'spotted', 'zebra', 'barn', 'baboon', 'canyon', 'marbled', 'lynx',
              'cellar', 'cobweb', 'giant', 'rose', 'common', 'mahogany', 'slender', 'false', 'bowl', 'huntsman',
              'huntress', 'desert', 'goliath', 'skeleton', 'domestic', 'baron', 'lattice', 'leafflitter', 'goldenrod',
              'dewdrop', 'sand', 'bottle', 'diving', 'flower', 'humpbacked', 'ivory', 'borrowing', 'bold', 'water',
              'bronze', 'spined', 'ebony', 'trapdoor', 'ghost', 'pike', 'labyrinth', 'robber', 'coffin', 'grass',
              'elegant', 'orchard', 'rover', 'needle', 'turtle', 'acrobat', 'fungus-growing', 'cone', 'field', 'guest',
              'tree', 'tiger', 'harvester', 'winter', 'acorn']
    return boose([land('demonym') + ' ', color() + ' ',
                  choose([choose(bodymodifier), color()]) + ' ' + choose(bodypart) + ' ']) + choose(adject) + ' ant'


def antlore():
    # A generator for the descriptions of ant species
    # I have no plans of implementation I just noticed that the descriptions on this website
    # (http://www.antstuff.net/html/species_of_ants.html) looked very formulaic so I decided to emulate them
    antname = ant()
    family = ['Monomorium minimum', 'Monomorium pharaonis', 'Formicidae', 'Myrmecia', 'Nothomyrmecia',
              'Pheidole megacephala', 'Solenopsis invicta']
    antvar = ['stinging ant', 'indoor pest ant']
    nestplace = ['soil under rocks', 'logs', 'walls', 'very fine soil', 'open areas of soil in lawns', 'open areas',
                 'damp locations']
    nestplaces = choose(nestplace, len(nestplace))
    food = ['young plants', 'seeds', 'nectar', 'bruised fruits', 'fungus']
    foods = choose(food, len(food))
    nesttype = ['large mounds', 'small craters', 'complex tunnels']
    bodypart = ['head', 'legs', 'jaws', 'thorax', 'abdomen']
    antrole = ['worker', 'drone', 'queen', 'soldier']
    size = randint(0, 8)
    if size > 3:
        relsize = 'large'
    else:
        relsize = 'small'

    template1 = 'Belonging to the ' + choose(family) + ' family. A ' + boose(['very ']) + choose(
        ['small', 'large']) + ', ' + color() + ' ant closely related to the ' + ant() + ' (' + precep(
        choose(antvar)) + '). It nests in ' + nestplaces[0] + ', ' + nestplaces[1] + ' or ' + nestplaces[
                    2] + '. It also builds nests in ' + nestplaces[3] + '. The nests in the ground are ' + choose(
        nesttype) + ' of very fine soil. '

    template2 = 'Belonging to the ' + choose(family) + ' family, ' + plural(antname) + ' are ' + plural(
        choose(antvar)) + ' of which there are over ' + str(
        randint(1, 40)) + '0 species worldwide. A typical ' + antname + ' colony produces ' + choose(
        nesttype) + ' in ' + nestplaces[0] + ', and feeds mostly on ' + foods[0] + ' and ' + foods[1] + '. ' + plural(
        antname.capitalize()) + ' often attack small animals and can kill them. '

    tempant = ant()
    template3 = 'The ' + antname + ' is one of about a dozen species of ' + \
                plural(tempant) + ' in the family ' + choose(family) + \
                ', found from ' + land() + ' to ' + land() + \
                '. This species is one of the ' + choose(['largest', 'smallest']) + ' ' + \
                tempant + ' species, and can be recognized by the smooth and shining ' + choose(bodypart) + \
                ' of the ' + choose(['largest', 'smallest']) + ' ' + \
                choose([choose(antrole), plural(choose(antrole))]) + \
                ' in a colony. '

    temprole = choose(antrole)
    extra1 = capitalize(plural(antname)) + ' have two sizes of ' + plural(temprole) + ' -- major ' + plural(
        temprole) + ' and minor ' + plural(temprole) + '. ' + choose(['Major', 'Minor']) + ' ' + plural(
        temprole) + ' have a ' + boose(['very ']) + 'large ' + choose(bodypart) + ' in proportion to their bodies.'

    extra2 = capitalize(plural(antname)) + ' are social insects found in warmer regions of ' + land() + '. '

    extra3 = ' These ants are ' + relsize + ', ranging from ' + str(size) + ' mm to ' + str(
        size) + '.5 mm in length. The ' + plural(choose(antrole)) + ' are ' + color() + ' to ' + color(
    ) + ', while the winged reproductives are ' + color() + '.'

    return choose([template1, template2, template3]) + boose([extra1, extra2, extra3])


def battle():
    # makes a battle or seige
    # room for improvement
    return 'the ' + choose(['battle', 'seige']) + ' of ' + choose([word('Batel'), location(choose(
        ['valley', 'mountains', 'hills', 'caves', 'caverns', 'plains', 'plateu', 'island', 'desert', 'lake', 'swamp',
         'forest', 'canyon', 'ravine', 'chasm', 'hollow']))])


def seige():
    # this makes only seiges
    # in case you need a seige but no a battle
    return 'the seige of ' + word('Seig')


def gramcheck(string):
    # Checks for common errors/basic grammar
    local_string = string
    local_string = local_string.replace('  ', ' ').replace('the the', 'the')
    local_string = re.sub('[ ,\.][,.]','.',local_string)
    for letter in list('abcdefghijklmnopqrstuvwxyz'):
        local_string = local_string.replace('. ' + letter, '. ' + letter.upper())
    for letter in list('aeiou'):
        local_string = local_string.replace(' a ' + letter, ' an ' + letter)
        local_string = local_string.replace(' a ' + letter.upper(), ' an ' + letter.upper())
    return local_string


def ghost():
    # this makes the name of a ghost
    return 'the ' + choose(['ghost', 'spirit']) + ' of ' + choose(
        [royalty(), hero(), professional('wizard', 'singular')])


def paintinglore():
    # this makes the lore of a painting

    def commission():
        # this makes the starting description for commissioned paintings
        # I stole and modified this code from swordlore
        # this should probably be made a separate function if I ever use it again
        royal1, royal2 = royalty(), royalty()
        while royal1 == royal2:
            # In the unlikely event that the royals are the same 
            # (It has happened)
            # try again
            royal1 = royalty()
        tlore = choose([
            choose([
                'It was ',
                'It is one of ' + str(randint(2, 11)) + ' paintings '
            ]),
            choose([
                'Commissioned',
                'One of ' + str(randint(2, 11)) + ' paintings commissioned'
            ]) + ' by ' + choose([
                royalty(),
                council()
            ]) + ', it was ',
            'A painting gifted from ' + royal1 + ' to ' + royal2 + boose([' as a peace offering']) + ', it was '
        ])
        return tlore

    year_of_creation = randint(1, 1500)

    return gramcheck(
        choose([
            'Painted by ' + professional('painter') + boose([
                ' for ' + royalty(),
                ' during the ' + age()
            ]) + ', ',
            'One of ' + professional('painter') + '\'s lesser known works, ',
            commission() + 'painted by ' + professional('painter') + boose([
                choose([
                    ' during',
                    ' in'
                ]) + ' the ' + age(),
                choose([
                    ' during',
                    ' in'
                ]) + ' the year ' + str(year_of_creation),
                ' under a ' + moonphase() + ' moon'
            ]) + '. '
        ]) + choose([
            'it is ' + carving(False),
            carving(False).replace('a depiction of', 'it depicts'),
            'it is a landscape painting' + boose(
                [' of ' + location(choose(['valley', 'plain', 'forest', 'woods', 'mountain']))])
        ]) + '. ' + boose([
            'It was ' + choose([
                'lost',
                'stolen'
            ]) + choose([
                choose([
                    ' during',
                    ' in'
                ]) + ' the ' + age(),
                choose([
                    ' during',
                    ' in'
                ]) + ' the year ' + str(randint(year_of_creation, 1501)),
                ' during ' + seige(),
                ' during ' + war()
            ]) + '. ',
            'It was ' + choose([
                'thought to be',
                'presumed',
                'believed to have been'
            ]) + ' ' + choose([
                'lost',
                'stolen',
                'destroyed'
            ]) + boose([
                choose([
                    ' during',
                    ' in'
                ]) + ' the ' + age(),
                choose([
                    ' during',
                    ' in'
                ]) + ' the year ' + str(randint(year_of_creation, 1501)),
                ' during ' + seige(),
                ' during ' + war()
            ]) + '. '
        ])
    )


def potterylore():
    # This makes pottery lore
    material = choose(['clay', 'ceramic', 'porcelain'])
    archetype = choose(['pot', 'vase', 'bowl'])
    return 'a '+boose([material + ' ']) + archetype + ' made by ' + professional('potter',dobject=material)


def musiclore():
    # This makes the lore for a piece of music
    mood = choose(['somber', 'joyful', 'forboding', 'eerie'])
    instrument = choose(['piano', 'organ', 'harpsicord', 'harp', 'flute', 'violin', 'viola', 'xylophone'])
    composer = professional('composer')
    return 'It is ' + boose([
        precep(mood)+' '
    ]) + 'piece' + boose([
        ' composed by ' + composer
    ]) + '. ' + boose([
        'It is intended to be played on ' + precep(instrument) + '. '
    ]) + boose([
        'It is one of ' + composer + '\'s ' + choose([
            'best',
            'better',
            'later',
            'last',
            'earlier',
            'earliest',
            'better known'
            'best known',
            'lesser known',
            'least known'
        ]) + choose([
            ' works',
            ' pieces',
            ' compositions'
        ]) + '. '
    ])


def music():
    # This makes the name of a piece of music
    pass


def scuplpturelore():
    # This makes the lore for a sculpture
    pass


def sauce():
    # This makes sauces to go on food
    # https://en.wikipedia.org/wiki/Gravy
    meat = ['pork', 'beef', 'chicken', 'fish', 'venison', 'veal', 'mutton', 'escargot', 'rabbit', 'duck', choose(['crab', 'lobster', 'shrimp']), amphibian(), bird(), dog()]
    gravy = choose(meat + ['mushroom', 'vegetable']) + ' gravy'
    # TODO make fruit function
    fruits = ['apple', 'cranberry', fruit()]
    defaults = ['duck sauce','tomato sauce', 'mushroom sauce', choose(fruits)+' sauce']
    return choose([gravy, choose(defaults)])


def tavern():
    # Makes the names of taverns
    def tavern_synonym():
        descriptor = ['tap', 'grog', 'mead', 'ale', 'lager', 'stout', 'malt']
        place = ['room', 'house', 'shop', 'hall']
        return choose(descriptor) + choose(place)
    person_adj = ['drunken', 'sleeping', 'wandering', 'lost', 'crying', 'greedy', 'jolly', 'cheerful', 'happy', 'sly', 'old', 'charming', 'lazy', 'hungry', 'thirsty', 'laughing', 'dancing', 'singing', 'friendly', 'poor', 'rich', 'one-eyed', 'three-eyed', 'blind']
    person = ['fool', 'king', 'priest', 'monk', 'maiden', 'barmaid', 'bartender', 'barkeep', 'robber', 'thief', 'minister', 'angel', 'traveler', 'trader', 'scribe', 'bard', 'dwarf', 'elf', 'gnome', 'goblin', 'woad', 'leprechaun', 'sheperd', 'ghost', 'hermit', 'companion', 'wizard', cavespawn()]
    tavern_synonyms = ['tavern', 'pub', 'bar', 'meadhall', 'inn', 'barroom', 'alehouse']
    thing_adj = ['golden', 'brass', 'glass', 'ivory', 'iron', 'seeing', 'cursed', 'shaking', 'burning', 'poisoned', 'magic', 'fiery', 'rotten', 'lucky', color()]
    thing = ['hand', 'foot', 'toad', 'frog', 'mushroom', 'toadstool', 'bone', 'salamander', 'apple', 'eye', 'barstool', 'mug', 'cross', str(choose(range(1,16)+['cue']))+'-ball']
    building_adj = ['golden', 'brass', 'glass', 'ivory', 'iron', 'crooked', 'crumbling', 'shady', 'burning', 'old', color()]
    building = ['tower', 'wall', 'castle', 'church', 'well', tavern_synonym()]
    return choose([
        'the ' + choose(person_adj) + ' ' + choose(person),
        'the ' + choose(person) + '\'s ' + choose([
            choose(tavern_synonyms),
            tavern_synonym()
        ]),
        'the ' + choose([
            choose(thing_adj),
            choose(person) + '\'s'
        ]) + ' ' + choose(thing),
        'the ' + choose([
            choose(building_adj),
            choose(person)+'\'s'
        ]) + ' ' + choose(building),
        'the ' + choose([
            choose(tavern_synonyms),
            tavern_synonym()
        ]) + choose([
            ' on ' + location('hill'),
            ' over ' + location(choose(['river', 'ravine', 'canyon'])),
            ' in ' + location(choose(['valley', 'forest', 'woods']))
        ])
    ])


def fruit(archetype=None):
    # makes the name of a fruit
    # room for improvement
    if archetype is None:
        archetype =  choose(['apple', 'fruit', 'peach', 'berry'])
    if archetype == 'orange':
        archetype = choose(['orange', 'clementine', 'tangerine', 'mandarin'])
    flavor = ['sour', 'sweet', 'tangy', 'tart']
    descriptor = ['crab', 'cloud', 'blood', 'rock', 'stone', 'pine', 'oak', 'frost', 'elder', 'wood', 'bone', 'jewel', 'box', 'star', 'dragon', 'ghost', color(), choose(flavor), land('demonnym'), word('fruit')]
    return choose(descriptor) + ' ' + archetype



def foodlore():
    # This makes a description of a dish
    # https://en.wikipedia.org/wiki/List_of_cooking_techniques
    # encorporate legendary game
    cooking_meth = ['fried', 'sauteed', 'boiled', 'roasted', 'grilled', 'baked', 'smoked', 'pickeled', 'dried', 'stuffed', 'broiled', 'carmelized', 'charbroiled']
    seasoning = ['pepper', 'garlic', 'paprika', 'salt', 'seasalt', 'allspice', 'arrowroot', 'curry', 'bayleaf', 'carraway'+boose(['seeds']), 'cayene', 'chili peppers', 'red pepper flakes', 'chives', 'cilantro', 'cinamon', 'cloves', 'cumin', 'dill', 'peppercorn', 'ginger', 'juniper berries', 'mustard', 'nutmeg', 'onion', 'oregano', 'parsley', 'rosemary', 'saffron', 'thyme', 'vanilla']
    vegetable = ['potato', 'yam', 'aparagus', 'rice', 'celery', 'radish', 'pumpkin', 'onion', 'mushroom', fruit(), fruit(choose(['lemon', 'orange']))]
    # TODO make crustacean generator
    meat = ['egg', 'pork', 'beef', 'chicken', 'fish', 'venison', 'veal', 'mutton', 'escargot', 'rabbit', 'duck', choose(['crab', 'lobster', 'shrimp']), amphibian(), bird(), bird()+' egg', dog()]
    extra_sentances = [
        boose([
            ' seasoned with ' + choose([
                read_list(choose(seasoning,randint(2,3))),
                choose(seasoning)
                ])
            ]),
        boose([
            ' served with ' + boose(cooking_meth) + ' ' + choose(vegetable)
        ]),
        boose([
            ' covered in ' + sauce()
        ])
    ]
    extra_sentances = filter(lambda x: x != '', extra_sentances)
    return gramcheck(choose(cooking_meth) + ' ' + choose(meat) + read_list(extra_sentances))

def enscript(dobject):
    enscription = ' ' + choose([
               'the %s is enscribed with ' + choose([
                   'a' + choose([
                       'n ancient',
                       ' mysterious'
                   ]) + ' script',
                   choose([
                       'ancient',
                       'mysterious'
                   ]) + ' ' + choose([
                       'runes',
                       'glyphs',
                       'hieroglyphics'
                   ]),
                   script()
               ]),
               'the %s is engraved with ' + carving(),
               'there is ' + precep(choose([
                   'crudely',
                   'unskillfully'
               ])) + ' scratched ' + script() + ' enscription on the %s',
               'the %s is engraved with a ' + choose([
                   'geometric',
                   'floral'
               ]) + ' pattern',
               'the %s is engraved with ' + choose([
                   'an unknown',
                   'the ' + land('demonym'),
                   'the ' + word('Famil') + ' family'
               ]) + ' coat of arms'
           ]) + '. '
    return enscription %dobject

def swordlore():
    # This is the heart and soul of this program
    # This makes the lore for a particular sword
    # I will comment this better in the future
    known = True
    lore = ''

    def giftsword():
        tlore = 'It was '
        tlore += choose(['given to ', 'gifted to ', 'presented to '])
        tlore += hero()
        tlore += ', by ' + choose([spirit(), royalty() + ','])
        if randint(0, 1) == 1:
            tlore += ' for his ' + choose(['victory at ' + battle(),
                                           choose(['defeating', 'killing', 'slaying', 'vanquishing']) + ' ' + beast(),
                                           choose(
                                               ['valor', 'honesty', 'bravery', 'kindness', 'skill', 'fairness',
                                                'gentle spirit'])])
        tlore += '. '
        if lore[-3:] == ',. ':
            tlore = lore[:-3] + '. '
        return tlore
    def unknownsword():
        tlore = 'The sword is of '
        tlore += choose([
            choose([
                'dwarven',
                'elvish',
                'goblin',
                cavespawn()
            ]),
            'unknown',
            land('demonym')
        ])
        tlore += ' origin. '
        return choose([
            'The sword is ' + choose([
                land('demonym'),
                'made in the style of ' + land('demonym') + ' swords from the ' + age()
            ]) + '. ',
            tlore
        ])
    def strangesword():
        tlore = ''
        tlore += 'The sword ' + choose(['seems like it is', 'seems to be', 'is']) + ' made of ' + material('Large')
        tlore += '. '
        return tlore
    lore += choose([
        giftsword(),
        unknownsword(),
        strangesword()
    ])
    if lore[:3] == 'The':
        known = False
    if randint(0, 2) == 0 and known:
        lore += choose(['Wielded by ', 'In the hands of ', 'Held by ']) + choose(
            [hero().split(',')[0], hero()]) + ', it ' + choose(['once ']) + choose(
            ['slew ', 'defeated ', 'killed ', 'vanquished ', 'struck down']) + choose([horde(), beast()]) + '.'
    elif randint(0, 1) == 0 and known:
        lore += 'It was ' + choose(['wielded by ', 'held by ']) + choose(
            [hero().split(',')[0], hero() + ',']) + choose([' in ', ' during ']) + battle() + ' ' + choose(
            ['', ' where it ' + choose(['slew', 'killed']) + ' ' + choose([hero(), royalty()])]) + '.'
    else:
        lore += strangelore()
    return gramcheck(lore)


def print_as_sentences(lore):
    sentences = re.split(r' *[\.\?!][\'"\)\]]* +', lore)

    for sentence in sentences:
        if sentence[-1] != '.':
            sentence += '.'

        print sentence

# ASCII art~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

           █▀
      ▄███ █▐█▄   ▄█      █▄   ▄██████▄   ▄██████▄  ████████▄        ▄█  ▄██████▄     ▄██████▄     ▄███████▄
     ▐███ ▐█▐█▪█  ▀▀▀     ███ ███    ▀▀▀ ███    ███ ▀▀▀   ▀███      ███ ▀▀▀▀  ▀███   ███▀   ▀▀▀   ▀██▀   ▀███
 ▄   ▐███▄▀▀ ▀▀ ▄███▌████ ███ ███ ██████ ███▐██▌███ ███▌██ ███ ████ ███ ██████ ███ █ ███ ██████▐▐█▄▄▄     ▐██
▐████▌▀████████▄▐████▄▄▄▄ ███ ███ ▄▄▄▄▄ ▄███▄▄▄▄███ ▄▄▄▄▄▄ ███ ▄▄▄▄ ███ ▄▄▄▄▄▄ ███ ▄ ███ ▄▄▄████▐███████▀ ▐██
 ▀        ▄▄▀███ █▐▐█████ ███ ███ █▐▐█ ▀▀███▀▀▀▀▀▀▀ ██████ ███ ████ ███ ██▌███ ███ █ ███ ██████████▀▀▀   ▄██▀
          ▐█ ▐██▌ ▄▄▄     ███ ███    ▄▄▀█████████▄  ▄▄▄    ███      ███ ▄▄▄    ███  ▄███▄▄▄▄▄▄    ▄▄██████▀
     ▄▄███ █ ███  ███ ▄█▄ ███ ███    ███ ███   ▀███ ███   ▄███      ███ ███▄  ▄███ ▀▀███▀▀▀▀▀     ███▄     ▄█
   ▄███▀▀▀ █▄ ▀    ▀███▀███▀   ▀██████▀   ███   ███ ████████▀       ███  ▀██████▀  ▀████████▄▄     ▀███████▀
   ███                                   ███     ██▄                ████▄▄▄▄▄▄▄▄▄█   ███  ▀▀███
   ███▄  ▄█                              ▀█       ▀▀▀              ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    ▀██  ▄███
    ▀▀███▀▀                                                                           ▀▀   ▀██
                                                                                              ▀
'''

# Body~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    seed(142811)
    part = WeaponHandle('grip','main')
    print part.lore()
    print
    print swordlore()
