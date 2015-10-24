# coding=utf-8
from BasicFunctions import *


def color(startseed):
    # this makes colors
    global seed
    seed = startseed

    def ish(color):
        if color[-1] == 'e':
            return color[:-1] + 'ish'
        else:
            return color + 'ish'

    color = ['orange', 'red', 'crimson', 'purple', 'blue', 'green', 'yellow', 'black', 'white', 'grey', 'brown', 'gold']
    return choose([boose(['bright ', 'dark ', 'pale ']) + choose(color), choose(color), ish(choose(color))])


def element(startseed):
    # makes the name of an element 
    global seed
    seed = startseed
    suffix = ['ite', 'ium', 'alt', 'sten', 'thril', 'yx', 'muth']
    return word('met', startseed) + choose(suffix)


def normalmetal(startseed):
    # returns an existing metal from a list
    global seed
    seed = startseed
    return choose(['iron', 'steel', 'brass', 'bronze', 'silver', 'gold', 'pewter', 'tungsten', 'cast iron', 'pig iron',
                   'titanium', 'copper', 'lodestone', 'bismuth', 'nickel', 'duralumin', 'billon', 'tombac', 'ormolu',
                   'electrum', 'hepatizon', 'sterling silver', 'mithril'])


def specificmetal(startseed):
    # makes the name of a new metal 
    global seed
    seed = startseed
    adjective = ['blood', 'ancient', 'red', 'black', 'white', 'astral', 'meteoric', 'rose', 'crucible',
                 word('Name', startseed) + "'s", 'cursed', 'spectral', 'solar', 'raw']
    metal = ['iron', 'steel', 'silver', 'metal', 'brass', 'bronze']
    return choose(adjective) + ' ' + choose(metal)

def loredmetal(startseed):
    # makes metal with lore
    global seed
    seed = startseed
    return choose([specificmetal(startseed), normalmetal(startseed)]) + ' mined from ' + boose(['beneath ','under ']) + mountain(seed)

def blacksmith(startseed, dobject):
    # fossil function see professional
    return professional(startseed, 'blacksmith', 'singular', dobject)


def blacksmiths(startseed, dobject):
    # fossil function see professional
    return professional(startseed, 'blacksmith', 'plural', dobject)


def craftsman(startseed):
    # fossil function see professional
    return professional(startseed, 'craftsman', 'singular')


def craftsmen(startseed):
    # fossil function see professional
    return professional(startseed, 'craftsman', 'plural')


def glassmith(startseed):
    # fossil function see professional
    return professional(startseed, 'glassmith', 'singular')


def glassmiths(startseed):
    # fossil function see professional
    return professional(startseed, 'glassmith', 'plural')


def professional(startseed, profession, plurality=choose(['singular', 'plural']), dobject='none'):
    # a combination of the old professsional functions (fossilized above).
    # It takes a type of profession and creates the name and title of a person of that profession.
    global seed
    seed = startseed
    synonyms = {'bowyer': ['bowyer'], 'glassmith': ['gaffer', 'glassmith', 'glassblower'], 'craftsman': ['craftsman'],
                'blacksmith': ['smith', 'blacksmith', 'goldsmith', 'pewtersmith', 'coppersmith', 'silversmith',
                               dobject + 'smith'], 'wizard': [wizardtype(startseed)]}
    professional_class = ''
    def single():
        #This is a function created so I can create apprentices without creating the potential for infinite or long loops
        #E.G. Sam the master swordsmith while apprenticed to dave the iron smith while apprenticed to Garett the blacksmith
        #basically allow you to call it only twice
        global professional_class
        if profession not in synonyms:
            synonyms.update({profession: [profession]})
        professional_class = choose(synonyms[profession])
        if randint(0, 1) == 1:
            professional_class = 'master ' + professional_class
        name = word(capitalize(profession), startseed)
        # RIP Akteerg the painter
        epithettype = 'maker'
        if profession == 'wizard': epithettype = 'wizard'
        singlular = choose([professional_class + ' ' + name, name + ' the ' + professional_class, name + ', '
                         + epithet(startseed, epithettype)])
        return singlular
    singlular = single()
    if randint(0,1) == 0:
        # when guilds are complete add to this
        seed += randint(12,3677)  # without this line of code the last entry is never selected
                                  # fix this eventually please
        singlular += boose([' while apprenticed to '+single(),' while he was an apprentice',' while he was working to join a guild'])
    if plurality == 'singular':
        return singlular
    else:
        template = choose(
            ['the # & of @', 'the & of @', 'the last great & of @', 'the first great & of @', '# & from @', '& from @',
             'the ' + choose(['disciples', 'followers', 'aprentices']) + ' of ' + singlular])
        professional_class = choose([
            choose(['dwarf', 'elf', 'man', 'gnome'] + synonyms[profession]),
            choose(['dwarven', 'elven', 'human', 'gnomish']) + ' ' + professional_class
        ])
        if professional_class.split(' ')[0] not in ['dwarf', 'elf', 'man', 'gnome',
                                                    'dwarven', 'elven', 'human', 'gnomish'] and randint(0, 1) == 1:
            professional_class = 'master ' + professional_class
        temp = template.replace('#', str(randint(2, 9)))
        temp = temp.replace('&', plural(professional_class))
        temp = temp.replace('@', capitalize(word('place', startseed)))
        return temp


def mountain(startseed):
    # creates the name of a mountain
    global seed
    seed = startseed
    adjectives = ['lonely', 'icey', 'misty', 'red', 'golden', 'silver', 'frozen', 'ancient', 'cold', 'windy', 'cloudy',
                  'north', 'south', 'east', 'west', 'crying', 'burning', 'walking', 'wandering', 'howling', 'windswept',
                  'white', 'silver']
    return choose(
        ['The ' + capitalize(choose(adjectives)) + ' Mountains', 'Mount ' + capitalize(word('mount', startseed))])


def location(startseed, feature):
    global seed
    seed = startseed
    adjectives = ['lonely', 'icey', 'misty', 'red', 'golden', 'silver', 'frozen', 'ancient', 'cold', 'windy', 'cloudy',
                  'north', 'south', 'east', 'west', 'crying', 'burning', 'walking', 'wandering', 'howling', 'windswept',
                  'sleepy', 'sleeping', 'silver']
    return choose(['the ' + capitalize(choose(adjectives)), word('Plaq', startseed)]) + ' ' + capitalize(feature)


def forge(startseed, dobject='none'):
    # room for improvement
    global seed
    seed = startseed
    #templates = ['Halls of &', 'fires of &', 'flames of &', 'forges of &', 'Hearth of &', 'embers of &', '& caves',
                 #'& caverns']
    #return choose(templates).replace('&', word('Forge', startseed))
    return choose([
        'the ' + choose([
            'forges ',
            'forge ',
            'hearth '
        ]) + choose([
            # make separate guild function
            'of ' + choose([
                choose([
                    professional(seed, 'blacksmith', 'singular', dobject),
                    'the ' + professional(seed, 'blacksmith', 'plural', dobject)
                ]),
                land(seed)
            ]),
            choose([
                'under ',
                'beneath '
            ]) + mountain(seed)
        ])
        
    ])


def land(startseed, type='country'):
    # makes a country or a demonym 
    global seed
    seed = startseed
    root = word('Land', startseed)
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


def cavespawn(startseed):
    # the cavespawn are a collection of ancient races that inhabit the darkest corners of the earth
    # they are gnerally rather passive and appear in small groups
    # they are mute but have elaborate writing systems and social orders
    # kings have waged war with them over millenia but they still remain
    global seed
    seed = startseed
    lingtype = ['eye', 'ear', 'ghost', 'rock', 'bone', 'stone', 'wood', 'husk']
    mantype = ['slug', 'snail', 'snake', 'bird', 'moth', 'worm', 'pig', 'wolf', 'bear', 'fish', 'pig', 'husk', 'lava',
               'magma', 'rock', 'mail', 'olm', 'frog', 'lizard', 'leopard', 'dog']
    return choose([choose(lingtype) + 'ling', choose(mantype) + 'man'])


def wizardtype(startseed):
    # this makes wizard types
    # this is not really a generator because it chooses from a predetermined list and doesn't mix up the parts
    # there is room for improvement here
    global seed
    seed = startseed
    return choose(['wizard', 'sorcerer', 'mage', 'alchemist', 'warlock', choose(['necro', 'pyro', 'litho']) + 'mancer'])


def epithet(startseed, dobject, gender='male'):
    # gives epithets to various things to add flavour
    global seed
    seed = startseed
    if gender == 'male':
        genpronoun = 'son'
    else:
        genpronoun = 'daughter'
    if dobject == 'beast':
        simple_descriptor = choose(
            ['ghastly', 'undying', 'unspeakable', 'unseen', 'unheard', 'silent', 'ancient', 'relentless', 'hellish',
             'hundred-eyed', 'thousand-eyed', 'immortal', 'unholy', 'howling', 'undead', 'festering', 'abominable',
             'formidable', 'wretched', 'grusome', 'blind', 'dreadful', 'great']) + ' '
        dominion = choose(
            ['orc', 'goblin', 'skelton', 'skeletal warrior', 'demon', 'man', 'hobgoblin', 'demon', 'cyclops', 'giant',
             'troll', 'knight', 'undead', 'ice giant', 'ghost', cavespawn(startseed)])
        Epithet = choose([
            choose(['reaper', 'eater', 'harvester', 'swallower', 'corrupter', 'defiler', 'reckoner', 'render',
                    'digester']) + ' of ' + choose(['souls', 'minds', 'flesh', 'bone', 'the damned', 'blood']),

            'the ' + simple_descriptor + choose(
                ['mind', 'overmind', 'beast', 'horror', 'terror', 'monster', 'evil', 'abomination', 'seer', 'overseer',
                 'priest', 'gatekeeper']),

            choose([
                choose(['keeper', 'king', 'god', 'ruler', 'prince', 'master']) + ' of ' + choose(
                    ['worms', 'maggots', 'the dead', 'the undead', 'bones', 'blood', 'souls', 'minds', 'snakes', 'fire',
                     'darkness', 'gold']),

                'the ' + boose([simple_descriptor]) + choose(['worm', 'maggot', 'snake', 'soul']) + ' ' + choose(
                    ['keeper', 'eater', 'lord', 'god']),

                choose(['king', 'god', 'ruler', 'prince', 'master']) + ' of the ' + plural(dominion).replace('undeads',
                                                                                                             'undead'),

                'the ' + boose([simple_descriptor]) + dominion + ' ' + choose(
                    ['king', 'god', 'ruler', 'prince', 'master'])
            ])
        ]).replace('  ', ' ')
    elif dobject == 'hero':
        # room for improvement
        Epithet = choose(['the ' + choose(
            ['brave', 'strong', 'great', 'stoic', 'elder', 'younger', 'tall', 'short', 'powerful', 'adored', 'ox',
             'boar', 'bull', 'mountain', 'rock', 'stoic', 'wise', 'peaceful', 'calm', 'fast', 'bear', 'wolf', 'fox',
             'lion', 'thirsty', 'hungry', 'tired', 'gentle', 'giant', 'last', 'holy', 'divine', 'fearless', 'steadfast',
             'enlightened', 'exhalted']), choose(['lion', 'bear', 'wolf', 'kind', 'soft']) + '-hearted',
                          genpronoun + ' of ' + word('Father', startseed), choose(
                ['dragon', 'minotaur', 'cyclops', 'ogre', 'ghast', 'beast', 'serpent', 'wolf', 'lion', 'bear', 'wyvern',
                 'worm', 'lindworm', cavespawn(seed), choose(['the ', '']) + dragon(startseed)]) + ' ' + choose(
                ['slayer', 'killer'])])
    elif dobject == 'noble':
        # room for improvement
        romannumeral = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        Epithet = choose([', the ' + choose(
            ['fair', 'kind', 'noble', 'just', 'wise', 'great', 'cruel', 'terrible', 'horrible', 'rotten', 'foolish']),
                          ', ' + genpronoun + ' of ' + land(startseed), ' ' + choose(romannumeral)])
    elif dobject == 'maker':
        # room for improvement
        Epithet = choose(['the steady handed', 'the steady of hand', 'the craftsman', 'the fireproof',
                          'the iron ' + choose(['thumbed', 'fingered', 'skinned']), 'the careful', 'the sharp-eyed',
                          'fire bellied', 'the bloodless', 'the dirty', 'the soot covered'])
    elif dobject == 'game':
        # this generates epithets for use in the legendry_game function
        # room for improvement
        Epithet = ' of ' + location(seed, choose(['valley', 'plain', 'forest', 'woods', 'mountain']))
    elif dobject == 'wizard':
        # room for improvement
        Epithet = choose([' the ' + color(seed), ' the ' + wizardtype(startseed) + ' of ' + location(seed, choose(
            ['valley', 'mountains', 'hills', 'caves', 'caverns', 'plains', 'plateu', 'island', 'desert', 'lake',
             'swamp', 'forest', 'canyon', 'ravine', 'chasm', 'hollow']))])
    else:
        # in case I made a mistake
        Epithet = 'the forsaken'
    return Epithet


def legendry_game(startseed):
    # creates the name of a legendary game animal
    global seed
    seed = startseed
    color = choose(['white', 'silver', 'black', 'golden'])
    genus = choose(['elk', 'stag', 'ram', 'bison'])
    return 'the ' + boose(['great ']) + color + ' ' + genus + ' ' + epithet(startseed, 'game')


def dragon(startseed):
    # this makes the name for a type of dragon
    # Not a specific dragon
    # there is plenty room for improvement here
    global seed
    seed = startseed
    return choose(
        ['lind', 'grind', 'lode', 'blood', 'flesh', 'gore', 'grist', 'grit', 'stench', 'fester', 'bone', 'old', 'book',
         'stone', 'husk']) + choose(['worm', 'wurm', 'wyrm'])


def worm(startseed):
    # creates the name of a worm
    global seed
    seed = startseed
    classification = choose(
        ['blood', 'book', 'bone', 'flesh', 'mind', 'earth', 'stone', 'night', 'fire', 'lung', 'gut', 'mud', 'moss',
         'wood', 'sludge', 'husk', 'book'])
    basis = choose(['worm', 'maggot', 'crawler'])
    return choose(['giant ', '']) + classification + basis


def beast(startseed):
    # creates the name of an evil beast or creature
    global seed
    seed = startseed
    Class = choose(
        ['dragon', 'minotaur', 'cyclops', 'ogre', 'ghast', 'beast', 'serpent', 'wolf', 'lion', 'bear', 'wyvern', 'worm',
         'lindworm', 'frost giant', dragon(startseed)])
    origin = location(startseed, choose(
        ['valley', 'mountains', 'hills', 'caves', 'caverns', 'plains', 'plateu', 'island', 'desert', 'lake', 'swamp',
         'forest', 'canyon', 'ravine', 'chasm', 'hollow']))
    name = capitalize(word('beast', startseed))
    Epithet = epithet(startseed, 'beast')
    return choose([choose(['', name + ', ']) + 'the ' + Class + ' of ' + origin, name + ', ' + Epithet])


def horde(startseed):
    global seed
    seed = startseed
    return choose(['a horde of', 'an army of', choose(
        ['one thousand', 'ten thousand', 'five hundred', 'one hundred', 'fifty', 'forty', 'thirty'])]) + ' ' + boose(
        ['angry', 'unholy', 'demonic', 'ravenous', 'ghastly']) + ' ' + choose(
        ['orcs', 'goblins', 'skeltons', 'skeletal warriors', 'demons', 'men', 'hobgoblins', 'demons', 'cyclopses',
         'giants', 'trolls', 'knights', 'undead', 'frost giants', plural(cavespawn(startseed))])


def hero(startseed):
    # creates the name and title of a mythical hero
    global seed
    seed = startseed
    name = word('Hero', startseed)
    Epithet = epithet(startseed, 'hero')
    return name + ', ' + Epithet


def royalty(startseed):
    # creates the name and title of a royal
    global seed
    seed = startseed
    name = word('King', startseed)
    title = choose(
        ['King', 'Queen', 'Duke', 'Duchess', 'Grand Duke', 'Archduke', 'Lord', 'Lady', 'Prince', 'Princess', 'Marquess',
         'Earl', 'Count', 'Countess', 'Baron', 'Baroness', 'Viscount', 'Viscountess']).lower()
    if title in ['queen', 'duchess', 'lady', 'princess', 'countess', 'baroness', 'viscountess']:
        gender = 'female'
    else:
        gender = 'male'
    Epithet = epithet(startseed, 'noble', gender)
    return choose([capitalize(title) + ' ' + name + Epithet, 'the ' + title + ' of ' + land(seed)])


def spirit(startseed):
    global seed
    seed = startseed
    Class = choose(['nymph', 'spirit', 'lady'])
    origin = location(startseed, choose(['lake', 'pond', 'forest']))
    return 'the ' + Class + ' of ' + origin


def coral(startseed):
    # makes coral
    global seed
    seed = startseed
    affix = ['fire', 'cloak', 'cactus', 'brain', 'ghost', 'cloud', 'rock', 'stone', color(seed) + ' crust',
             choose(['elk', 'bison', 'bull', 'deer', 'moose', 'stag']) + 'horn', land(seed, 'demonym')]
    return choose(affix) + ' coral'


def bone(startseed):
    # makes bone
    global seed
    seed = startseed
    bsource = choose(['goblin', 'orc', 'human', 'dwarf', 'giant', 'troll', 'fish', 'deer', 'cow', cavespawn(seed)])
    classification = choose(['rib', 'bone', 'tooth', 'spine', 'jaw'])
    lbsource = choose([beast(seed)])
    return choose([bsource + ' ' + classification, 'the ' + classification + ' of ' + lbsource + ','])


def wood(startseed):
    # makes wood
    global seed
    seed = startseed
    wsource = choose(
        ['oak', 'spruce', 'cedar', 'birch', 'pine', 'fir', 'hemlock', 'ash', 'chestnut', 'beech', 'elm', 'mahogany',
         'hickory', 'maple', 'stone'])
    return wsource + ' wood'


def ivory(startseed):
    # makes ivory
    global seed
    seed = startseed
    isource = boose(['mammoth', 'walrus', 'whale', land(seed, 'demonym')])
    return isource + ' ivory'


def biomaterial(startseed, size='small'):
    # makes biological materials
    global seed
    seed = startseed
    # bone:
    bsource = bone(startseed)
    # wood:
    wsource = wood(startseed)
    # ivory:
    isource = ivory(startseed)
    # coral:
    csource = coral(startseed)
    if size == 'small':
        return choose([bsource, wsource, isource, csource])
    else:
        return choose([wsource, isource, csource])


def strange_biomaterial(startseed):
    # makes strange or unconventional biological materials
    # there is room for improvement here
    global seed
    seed = startseed
    # crustacesan based
    reflist = {'': 954, 'blue ': 50, 'yellow ': 5, 'white ': 1}
    color = woose(reflist)
    crust = color + choose(['crab', 'lobster']) + ' ' + choose(['shell', 'chitin'])
    # I can't think of anymore right now I'll add some later
    return choose([crust])


def material(startseed, size='small'):
    # makes materials
    # mainly used for sword blades and hilts
    global seed
    seed = startseed
    biomat = biomaterial(startseed, size)
    strangemat = strange_biomaterial(startseed)
    inertmat = choose(['petrified', 'calcified', 'fossilized']) + ' ' + biomat
    return choose([biomat, inertmat, strangemat])


def script(startseed):
    # creates the name for a form of writing or alphabet
    global seed
    seed = startseed
    preprefix = choose([land(startseed, 'detonym') + ' ', choose(
        ['proto-', 'elvish ', 'goblin ', 'dwarven ', cavespawn(startseed) + ' ', 'rudimentry ', 'ancient '])])
    prefix = choose(['rune', 'glyph', 'old', 'stone', 'bone', 'dark', 'death', 'cipher ', 'cryptic ', 'sand'])
    suffix = choose(['script', 'rune', 'glyph', 'scratch', 'form'])
    if prefix == suffix:
        prefix = choose(['old', 'stone', 'bone', 'dark', 'death', 'cipher ', 'cryptic '])
    if prefix == 'cryptic ':
        return prefix + boose([preprefix]) + suffix
    return choose([preprefix, '']) + prefix + suffix


def council(startseed):
    # creates the name of a council
    global seed
    seed = startseed
    variety = ['council', 'aldermen', 'senate', 'congress']
    location = land(startseed)
    return 'the' + choose([' high', ' grand', '']) + ' ' + choose(variety) + ' of ' + location


def age(startseed):
    # creates the name of an age or era
    global seed
    seed = startseed
    var = choose(['age', 'era'])
    time = choose([
        choose(['golden', 'silver', 'dark', 'bronze', 'brass', 'stone', 'ancient']) + ' ' + var,
        var + ' of ' + choose(
            ['fire', 'iron', 'steel', 'kings', 'lords', 'gods', 'darkness', 'the shadows', 'blood', 'filth',
             'the ancients', 'monsters', 'conquest', 'empires', 'elves', 'beasts', 'birds', 'magic', 'wizards',
             word('Ruler', startseed), plural(choose(
                ['orc', 'woad', 'goblin', 'troll', 'giant', 'cyclops', 'man', 'elf', 'dwarf', cavespawn(startseed)]))])
    ])
    return time.title()


def moonphase(startseed):
    # a generator for special phases of the moon
    # It does't really create new phases just picks from a list of existing ones
    global seed
    seed = startseed
    phase = choose(['full', 'new', 'blood', 'blue', 'harvest', 'hunter\'s' + ' moon'])
    return phase


def moss(startseed):
    # A generator for types of mosses
    # https://en.wikipedia.org/wiki/List_of_the_mosses_of_Britain_and_Ireland
    global seed
    seed = startseed
    atribute = choose(
        ['soft', 'long', 'wide', 'smooth', 'fine', 'bent', 'thin', 'short', 'tiny', 'slender', 'round', 'many', 'thick',
         color(startseed)]) + '-' + choose(['tufted', 'leafed', 'capped', 'stalked', 'fruited', 'tipped', 'capped'])

    primaryadjective = [choose(
        ['calcareous', 'flagellate', 'bimous', 'sessile', 'glaucous', 'alpine', 'silvergreen', 'western', 'northern',
         'eastern', 'southern', 'swamp', 'creeping', 'crawling', 'icy', 'pendulous', 'dark', 'bright', 'hanging',
         'slender', 'arctic', 'spreading', 'bog', 'rusty', 'velvet', 'robust', 'ambiguous', 'bordered', 'spinose',
         'mountain', 'sand', 'river', 'wall', 'pale', 'saltmarsh', 'twisting', 'cernuous', 'giant', 'fountain',
         'smaller', 'tendril', 'compact', 'silky', 'field', 'common', 'dusky', 'spiral', 'ribbed', 'fringed', 'fuzzy',
         'chalk', 'felted', 'shady', 'cordate', 'blunt', 'pretty', 'clustered', 'thin', 'hooded', 'starry', 'whorled',
         'elegant', 'striated', 'fatfoot', 'tiny', 'curled', 'petty', 'dappled', 'dingy', 'polar', 'soft', 'snow',
         'sparkling', 'feathery', 'snowy', 'woolly', 'bristly', 'tall']), word('Lord', startseed) + '\'s',
        color(startseed), land(startseed, 'demonym'), atribute]

    secondaryadjective = ['pygmy', 'dwarf', 'hump', 'feather', 'yoke', 'fork', 'wood', 'beard', 'beardless', 'rock',
                          'thread', 'silver', 'earth', 'carrion', 'groove', 'apple', 'shield', 'spear', 'bow', 'rabbit',
                          'lattice', 'tree', 'helmet', 'hook', 'comb', 'cave', 'forklet', 'nut', 'flag', 'fox',
                          'extinguisher', 'cord', 'pocket', 'water', 'tufa', 'hoar', 'screw', 'brook', 'plait', 'silk',
                          'thatch', 'copper', 'thyme', 'flood', 'spur', 'bristle', 'fen', 'crisp', 'scorpion', 'fringe',
                          'streak', 'rose', 'ghost', 'turf', 'shaggy', 'dew', 'bark', 'club', 'ganite', 'umbrella',
                          'dung']

    variety = woose({'moss': 8, 'peatmoss': 1, 'smoothcap': 1, 'bryum': 1, 'ditrichum': 1, 'grimmia': 1, 'pottia': 1,
                        'pincusion': 1, 'redshank': 1, 'quillwort': 1})

    moss = (boose(primaryadjective) + ' ' + variety).replace(' moss', ' ' + boose(secondaryadjective) + '-moss')
    moss = moss.replace(' -', ' ')
    if moss[0] == ' ' and not '-' in list(moss):
        moss = choose(primaryadjective) + moss
    elif moss[0] == ' ':
        moss = moss[1:]
    return moss


def pattern(startseed):
    global seed
    seed = startseed
    modifier = ['long', 'short', 'wide', 'thin', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
    base = ['band', 'spot', 'stripe']
    return choose([choose(modifier), color(seed)]) + choose(base)


def spider(startseed):
    # makes spiders
    # https://en.wikipedia.org/wiki/List_of_spider_common_names
    global seed
    seed = startseed

    def weaver(startseed):
        global seed
        seed = startseed
        shape = ['orb', 'hammock', 'tent', 'dome', 'rob', 'net', 'tower', 'maze', 'labyrinth']
        return choose(shape) + 'weaver'

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
    var = ['orbweaver', 'tarantula', 'meshweaver', 'jumper', 'birdeater', 'widow', weaver(startseed)]
    subvar = choose([subvar, pattern(startseed)])
    tempor = choose(['$', '%', '&', '$ %', '$ &', '% &', '$ % &']) + ' ' + choose([choose(var), 'spider'])
    return tempor.replace('$', color(seed)).replace('%', land(seed, 'demonym')).replace('&', subvar)


def normalgem(startseed):
    # A generator for real gemstones
    # https://www.wikiwand.com/en/List_of_gemstone_species
    # http://www.gemselect.com/other-info/gemstone-list.php
    global seed
    seed = startseed
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
           'charoite', 'chrysoprase', 'clinohumite', 'enstatite', 'gaspeite', 'goshenite', 'hackmanite', 'hemimorphite',
           'hiddenite', 'howlite', 'idocrase', 'iolite', 'kunzite', 'kyanite', 'larimar', 'lepidolite', 'melanite',
           'andradite', 'moldavite', 'tektite', 'chrysolite', 'morganite', 'nuummite', 'orthoclase', 'pietersite',
           'rhodonite', 'scapolite', 'serphinite', 'clinochlores', 'serpentine', 'smithsonite', 'sodalite',
           'sphalerite', 'sphene', 'tanzanite', 'verdite']
    return choose(gem)


def specificgem(startseed):
    global seed
    seed = startseed
    adjective = ['mystic', 'cat\'s eye', 'andesine', 'color-change', 'dendritic', 'fire', 'star', 'pyrope', 'rainbow',
                 'rutile', 'rose', 'tashmarine', 'chrome', color(startseed)]
    return choose(adjective) + ' ' + normalgem(startseed)


def glass(startseed):
    # a generator for real types of glasses
    # https://en.wikipedia.org/wiki/Category:Glass_types
    # http://www.cmog.org/article/types-glass
    # https://en.wikipedia.org/wiki/Category:Glass_compositions
    global seed
    seed = startseed
    glass = ['glass', 'beveled glass', 'plate glass', 'carnival glass', 'crown glass', 'depression glass',
             'favrile glass', 'flat glass', 'float glass', 'vitrum flextile', 'flexible glass', 'frosted glass',
             'fumed silica', 'pyrogenic silica', 'fused quartz', 'glass of antimony', 'goofus glass', 'ground glass',
             'moss agate glass', 'rippled glass', 'sitall', 'starfire glass', 'tiffany glass', 'toughened glass',
             'reinforced glass', 'tempered glass', 'photochromic glass', 'soda-lime glass', 'lead glass',
             'cobalt glass', 'cranberry glass', 'dichroic glass', 'flint glass', 'jadeite', 'leaded glass',
             'milk glass', 'opaline glass', 'reagent bottle', 'uranium glass', color(startseed) + ' glass',
             color(startseed) + ' plate glass']
    return choose(glass)


def specificglass(startseed):
    # makes the name of a non-real type of glass
    # room for progress
    global seed
    seed = startseed
    return color(startseed) + ' glass'


def dog(startseed):
    # makes the name for a type of dog
    global seed
    seed = startseed
    adjective = ['alpine', 'great', 'king', 'lowland', 'highland', color(startseed)]
    prey = ['fox', 'rabbit', 'sheep', 'deer', 'wolf', 'seal']
    base = ['hound', 'shepherd', 'malamute', 'akita', 'mountain dog', 'bloodhound', 'setter', 'greyhound', 'sleddog',
            'mastiff', choose(prey) + choose(['hound', 'dog'])]
    return choose(adjective) + ' ' + choose(base)


def book(startseed):
    # makes the title for a fictional book
    # room for improvement
    global seed
    seed = startseed

    def epic():
        people = ['bard', 'king', 'knight', 'jester', 'man']
        title = choose(['the tale of ' + word('Epic', startseed), 'the fall of ' + word('Epic', startseed),
                        'the epic of ' + word('Epic', startseed), 'the myth of ' + word('Epic', startseed),
                        word('Epic', startseed)])
        return title

    def contemporary():
        firstperson = ['The Old Man', 'A Man', 'The King', 'The Prince']
        secondperson = ['the Sea', 'His Dog', 'The Moon']
        return choose(firstperson) + ' and ' + choose(secondperson)

    return choose([epic(), contemporary()])


def academicbook(startseed):
    # makes a non-fiction book title
    global seed
    seed = startseed
    academic = ['Physicist', 'Mathematician', 'Chemist', 'Alchemist', 'Scientist', 'Herpetologist', 'Herbologist',
                'Entemologist', 'Philosopher', 'Logician', 'Economist', 'Engineer', 'Botanist', 'Zoologist',
                'Pharmacologist', 'Geologist', 'Astronomer', 'Psychologist']
    field = ['Physics', 'Mathematics', 'Chemistry', 'Alchemy', 'Science', 'Herpetology', 'Herbology', 'Entemology',
             'Philosophy', 'Logic', 'Economics', 'Engineering', 'Botany', 'Zoology', 'Pharmacology', 'Geology',
             'Astronomy', 'Psychology']
    fieldadjective = ['Physical', 'Mathematical', 'Chemi cal', 'Alchemical', 'Scientific', 'Herpetologic', 'Herbologic',
                      'Entemologic', 'Philosophic', 'Logical', 'Economic', 'Engineering', 'Botanical', 'Zoologic',
                      'Pharmacologic', 'Geologic', 'Astronomic', 'Psychologic']
    place = ['Plains', 'Savana', 'Arctic', 'Tropics']
    organism = ['Insects', 'Plants', 'Fungi', 'Birds', 'Fish', 'Reptiles', 'Mammals', 'Amphibians', 'Arachnids',
                'Beetles']
    title = ['Principles of ' + choose(field), precep(choose(academic)) + '\'s ' + choose(['Handbook', 'Guidebook']),
             'A Guide to ' + choose(fieldadjective) + ' Principles', 'Mastering ' + choose(field),
             'A ' + boose(['Brief ', 'Comprehensive ']) + 'History of ' + choose(field)]
    return choose(title)


def enscript(startseed):
    # Eamon's function
    global seed
    seed = startseed
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


def war(startseed):
    global seed
    seed = startseed
    tempseed = seed
    participant1 = land(tempseed, 'demonym')
    paritcipant1l = land(tempseed)
    participant2 = land(startseed, 'demonym')
    participant2l = land(startseed)
    while participant1 == participant2:
        tempseed = seed
        participant1 = land(tempseed, 'demonym')
        participant1l = land(tempseed)
        seed += 1
    return 'the ' + choose([
        boose(['first', 'second', 'third']) + ' ' + participant1 + '-' + participant2 + ' war',
        participant1 + ' civil war',
        participant1 + choose([' invasion', ' conquest']) + ' of ' + participant2l
    ])


def salamander(startseed):
    # makes salamanders
    # http://www.californiaherps.com/allsalamanders.html
    # THIS GENERATOR IS NOW OBSOLETE
    # (no longer in use not actually obsolete)
    # See amphibian instead
    global seed
    seed = startseed
    bodyadject = ['long', 'short', 'slender', color(seed)]
    bodypart = ['toed', 'legged', 'tailed']
    adject = ['western', 'southern', 'eastern', 'northern', 'spotted', 'lesser', 'greater', land(startseed, 'demonym')]
    denom = ['Tiger', 'cloud', 'aboreal', 'wandering', 'mountain', 'garden', 'alpine', 'desert', 'river', 'brook',
             'spring', 'dusky', 'pygmy', 'giant', 'slimy']
    return choose([choose(bodyadject) + '-' + choose(bodypart), choose(adject)]) + ' ' + boose(denom) + choose(
        ['salamander', 'newt', 'eft', 'olm'])


def amphibian(startseed):
    # makes amphibians
    # https://en.wikipedia.org/wiki/List_of_amphibians_of_Europe
    # http://www.californiaherps.com/allsalamanders.
    # http://www.californiaherps.com/allfrogs.html
    global seed
    seed = startseed
    bodymodifier = ['long', 'feather', 'star', 'greater', 'fire', 'straight', 'flame', 'stripe', 'curved', 'hammer',
                    'thick', 'thin', 'slender', 'round']
    bodypart = ['legged', 'headed', 'bellied', 'kneed', 'toed', 'footed', 'backed', 'mouth', 'shouldered']
    subvar = choose(
        ['cloud', 'common', 'water', 'creasted', 'painted', 'tree', 'widwife', 'brook', 'alpine', 'stream', 'agile',
         'fire', 'marbled', 'pool', 'hybrid', 'imperial', 'wood', 'smooth', 'ribbed', 'marsh', 'regal', 'royal',
         'tiger', 'cloud', 'aboreal', 'wandering', 'mountain', 'garden', 'alpine', 'desert', 'river', 'brook', 'spring',
         'dusky', 'pygmy', 'giant', 'slimy', 'boreal', 'spectal', 'king', 'queen', 'leopard', 'chorus', 'clawed'])
    genera = ['frog', 'salamander', 'toad', 'newt', 'spadefoot', 'bullfrog', 'eft', 'olm', 'axolotl', 'treefrog']
    subvar = choose([subvar, pattern(startseed)])
    tempor = choose(['$', '%', '&', '$ %', '$ &', '% &', '$ % &']) + ' ' + choose(genera)
    return tempor.replace('$', color(seed)).replace('%', land(seed, 'demonym')).replace('&', subvar)


def carving(startseed, epithets=True):
    global seed
    seed = startseed
    prey = choose(['fox', 'bear', 'moose', 'deer', 'stag', 'rabbit'])
    royal = royalty(startseed)
    if not epithets:
        royal = royal.split(',')[0]
    picture = choose([
        boose([hero(seed) + ' leading troops in ']) + battle(startseed),
        hero(seed) + ', ' + choose([
            'fighting',
            'slaying',
            'defeating'
            , 'vanquishing'
        ]) + ' ' + choose([
            beast(seed),
            horde(seed)
        ]),
        choose([
            'hunters',
            'huntsmen',
            'hounds',
            'dogs',
            plural(dog(startseed)),
            'a ' + dog(startseed),
            professional(startseed, 'hunter')
        ]) + ' ' + choose([
            'hunting',
            'chasing'
        ]) + ' ' + choose([
            'a ' + boose([
                'wild '
            ]) + prey,
            plural(prey),
            legendry_game(startseed)
        ]),
        'a scene from ' + book(startseed),
        royal + '\'s ' + dog(startseed) + ' ' + word('Dog', startseed)
    ])
    return 'a depiction of ' + picture


def stringthing(startseed):
    # makes literal strings.
    # like for bows and such.
    global seed
    seed = startseed
    mamsource = ['elk', 'deer', 'moose', 'pig', 'cow']
    return choose([choose(mamsource) + ' ' + choose(['sinew']), spider(startseed) + ' silk'])


def clothlore(startseed):
    # provides short lore for cloth
    global seed
    seed = startseed
    color_chart = {'purple': ['murex']}
    lore = ''
    lore += choose(['woven', 'spun']) + ' from ' + choose(
        [spider(startseed) + ' silk', 'hemp', 'straw', 'grass', 'sisal', 'cotton', 'wool', 'cashmere', 'qiviut', 'silk',
         choose([specificmetal(startseed), normalmetal(startseed)])]) + boose(
        [' by ' + professional(startseed, 'weaver')])
    return lore


def fabric(startseed):
    global seed
    seed = startseed
    return choose([choose(
        ['raw hide', choose(['cow', 'goat', 'deer', 'elk', 'caribou', 'reindeer', 'ox', 'bison', 'buffalo']) + ' hide',
         'cloth', color(startseed) + ' cloth', color(startseed) + ' wool', color(startseed) + ' silk', 'fabric',
         'velvet', 'silk', 'leather', 'black leather', 'brown leather', 'red leather', 'bat leather', 'fish leather',
         'deerskin', 'human skin', 'goblin skin', 'snakeskin', 'lizard skin', 'dragon skin']),
        boose([color(seed)]) + ' ' + choose(['cloth', 'fabric']) + ' ' + clothlore(startseed)])


def bird(startseed):
    # this makes bird names
    '''Makes Birds'''
    global seed
    seed = startseed
    genera_count = 0

    def bird_genera(startseed):
        # this makes forulaic bird genera names
        global seed
        seed = startseed
        global genera_count
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
        genera_count = len(prefixes) * len(suffixes)
        # print genera_count
        return choose(prefixes) + choose(suffixes)

    voriabel = bird_genera(seed)
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
    genera_count = 1144
    # print (len(common_genera)+len(uncommon_genera)+len(rare_genera)+genera_count+2)*(len(prefix)+(len(body_adjective)
    # +60)*len(body_part)+60)
    return choose([choose(prefix), choose([color(seed), choose(body_adjective)]) + choose(body_part), color(seed),
                   word('Bird', startseed) + '\'s', land(seed, 'demonym')]) + ' ' + choose(
        [choose(common_genera), choose(uncommon_genera), choose(rare_genera), bird_genera(startseed)])


def blood(startseed):
    # makes blood
    global seed
    seed = startseed
    reflist = {'': 15, 'coagulated ': 1}
    return woose(reflist) + boose(
        ['orc', 'woad', 'goblin', 'hobgoblin', 'kobold', 'gnome', 'troll', 'giant', 'cyclops', 'minotaur',
         cavespawn(startseed)]) + ' blood'


def ant(startseed):
    # makes the names of types of ants
    # http://www.antstuff.net/html/species_of_ants.html
    # http://www.myrmecos.net/north-american-ants/
    global seed
    seed = startseed
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
    return boose([land(seed, 'demonym') + ' ', color(seed) + ' ',
                  choose([choose(bodymodifier), color(seed)]) + ' ' + choose(bodypart) + ' ']) + choose(adject) + ' ant'


def antlore(startseed):
    # A generator for the descriptions of ant species
    # I have no plans of implementation I just noticed that the descriptions on this website
    # (http://www.antstuff.net/html/species_of_ants.html) looked very formulaic so I decided to emulate them
    global seed
    seed = startseed
    antname = ant(startseed)
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
        ['small', 'large']) + ', ' + color(seed) + ' ant closely related to the ' + ant(seed) + ' (' + precep(
        choose(antvar)) + '). It nests in ' + nestplaces[0] + ', ' + nestplaces[1] + ' or ' + nestplaces[
                    2] + '. It also builds nests in ' + nestplaces[3] + '. The nests in the ground are ' + choose(
        nesttype) + ' of very fine soil. '

    template2 = 'Belonging to the ' + choose(family) + ' family, ' + plural(antname) + ' are ' + plural(
        choose(antvar)) + ' of which there are over ' + str(
        randint(1, 40)) + '0 species worldwide. A typical ' + antname + ' colony produces ' + choose(
        nesttype) + ' in ' + nestplaces[0] + ', and feeds mostly on ' + foods[0] + ' and ' + foods[1] + '. ' + plural(
        antname.capitalize()) + ' often attack small animals and can kill them. '

    tempant = ant(seed)
    template3 = 'The ' + (antname) + ' is one of about a dozen species of ' + plural(
        tempant) + ' in the family ' + choose(family) + ', found from ' + land(seed) + ' to ' + land(
        seed) + '. This species is one of the ' + choose(['largest',
                                                          'smallest']) + ' ' + tempant + \
                ' species, and can be recognized by the smooth and shining ' + choose(
        bodypart) + ' of the ' + choose(['largest', 'smallest']) + ' ' + choose(
        [choose(antrole), plural(choose(antrole))]) + ' in a colony. '

    temprole = choose(antrole)
    extra1 = capitalize(plural(antname)) + ' have two sizes of ' + plural(temprole) + ' -- major ' + plural(
        temprole) + ' and minor ' + plural(temprole) + '. ' + choose(['Major', 'Minor']) + ' ' + plural(
        temprole) + ' have a ' + boose(['very ']) + 'large ' + choose(bodypart) + ' in proportion to their bodies.'

    extra2 = capitalize(plural(antname)) + ' are social insects found in warmer regions of ' + land(seed) + '. '

    extra3 = ' These ants are ' + relsize + ', ranging from ' + str(size) + ' mm to ' + str(
        size) + '.5 mm in length. The ' + plural(choose(antrole)) + ' are ' + color(seed) + ' to ' + color(
        seed) + ', while the winged reproductives are ' + color(seed) + '.'

    return choose([template1, template2, template3]) + boose([extra1, extra2, extra3])


def battle(startseed):
    # makes a battle or seige
    # room for improvement
    global seed
    seed = startseed
    return 'the ' + choose(['battle', 'seige']) + ' of ' + choose([word('Batel', startseed), location(seed, choose(
        ['valley', 'mountains', 'hills', 'caves', 'caverns', 'plains', 'plateu', 'island', 'desert', 'lake', 'swamp',
         'forest', 'canyon', 'ravine', 'chasm', 'hollow']))])


def seige(startseed):
    # this makes only seiges
    # in case you need a seige but no a battle
    global seed
    seed = startseed
    return 'the seige of ' + word('Seig', startseed)


def gramcheck(string):
    '''Checks for common errors/basic grammar'''
    local_string = string
    local_string = local_string.replace(' .', '.').replace('  ', ' ').replace(',.', '.').replace('..', '.').replace('the the', 'the')
    for letter in list('abcdefghijklmnopqrstuvwxyz'):
        local_string = local_string.replace('. ' + letter, '. ' + letter.upper())
    for letter in list('aeiou'):
        local_string = local_string.replace(' a ' + letter, ' an ' + letter)
        local_string = local_string.replace(' a ' + letter.upper(), ' an ' + letter.upper())
    return local_string


def ghost(startseed):
    # this makes the name of a ghost
    global seed
    seed = startseed
    return 'the ' + choose(['ghost', 'spirit']) + ' of ' + choose(
        [royalty(seed), hero(seed), professional(seed, 'singular', 'wizard')])


def paintinglore(startseed):
    # this makes the lore of a painting
    global seed
    seed = startseed

    def commission(startseed):
        # this makes the starting description for commisioned paintings
        # I stole and modified this code from swordlore
        # this should probably be made a separate function if I ever use it again
        global seed
        seed = startseed
        royal1, royal2 = royalty(seed), royalty(startseed)
        while royal1 == royal2:
            # In the unlikely event that the royals are the same 
            # (It has happened)
            # try again
            royal1 = royalty(seed)
            seed += 1
        tlore = choose([
            choose([
                'It was ',
                'It is one of ' + str(randint(2, 11)) + ' paintings '
            ]),
            choose([
                'Commissioned',
                'One of ' + str(randint(2, 11)) + ' paintings commissioned'
            ]) + ' by ' + choose([
                royalty(startseed),
                council(startseed)
            ]) + ', it was ',
            'A painting gifted from ' + royal1 + ' to ' + royal2 + boose([' as a peace offering']) + ', it was '
        ])
        return tlore

    year_of_creation = randint(1, 1500)

    return gramcheck(
        choose([
            'Painted by ' + professional(startseed, 'painter') + boose([
                ' for ' + royalty(startseed),
                ' during the ' + age(startseed)
            ]) + ', ',
            'One of ' + professional(startseed, 'painter') + '\'s lesser known works, ',
            commission(startseed) + 'painted by ' + professional(startseed, 'painter') + boose([
                choose([
                    ' during',
                    ' in'
                ]) + ' the ' + age(startseed),
                choose([
                    ' during',
                    ' in'
                ]) + ' the year ' + str(year_of_creation),
                ' under a ' + moonphase(startseed) + ' moon'
            ]) + '. '
        ]) + choose([
            'it is ' + carving(startseed, False),
            carving(startseed, False).replace('a depiction of', 'it depicts'),
            'it is a landscape painting' + boose(
                [' of ' + location(seed, choose(['valley', 'plain', 'forest', 'woods', 'mountain']))])
        ]) + '. ' + boose([
            'It was ' + choose([
                'lost',
                'stolen'
            ]) + choose([
                choose([
                    ' during',
                    ' in'
                ]) + ' the ' + age(seed),
                choose([
                    ' during',
                    ' in'
                ]) + ' the year ' + str(randint(year_of_creation, 1501)),
                ' during ' + seige(startseed),
                ' during ' + war(seed)
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
                ]) + ' the ' + age(seed),
                choose([
                    ' during',
                    ' in'
                ]) + ' the year ' + str(randint(year_of_creation, 1501)),
                ' during ' + seige(startseed),
                ' during ' + war(seed)
            ]) + '. '
        ])
    )


def potterylore(startseed):
    # This makes pottery lore
    global seed
    seed = startseed
    pass


def musiclore(startseed):
    # This makes the lore for a piece of music
    global seed
    seed = startseed
    pass


def music(startseed):
    # This makes the name of a piece of music
    global seed
    seed = startseed
    pass

def scuplpturelore(startseed):
    # This makes the lore for a sculpture
    global seeed
    seed = startseed
    pass


def strangelore(startseed):
    # This was originally contained within the swordlore generator
    # I also wanted to use it for the bowlore generator so I have moved it outside
    global seed
    seed = startseed
    lore = ''

    def smell(startseed):
        # describes the smell of the sword
        global seed
        seed = startseed
        smell = ['metal', blood(startseed), 'sulfur', 'brimstone', 'smoke', 'bile', 'sweat', 'the sea']
        smells = choose(smell, 2)
        return 'smells ' + boose(['strongly ', 'faintly ']) + 'of ' + smells[0] + boose([' and ' + smells[1]])

    def detection(startseed):
        # swords that react to a certain situation
        global seed
        seed = startseed
        signal = ['when ' + plural(
            choose(['orc', 'goblin', 'troll', 'giant', 'cyclops', cavespawn(startseed)])) + ' are ' + choose(
            ['near', 'nearby']), 'in the presence of ' + boose(['dark', 'black']) + ' magic',
                  'when emersed in ' + choose(['magma', 'lava', 'fire', 'water']),
                  'when it touches ' + blood(startseed), 'in ' + choose(['the dark', 'low light', 'bright light'])]
        response = ['glows', 'glows ' + color(seed), 'turns ' + color(startseed),
                    'becomes ' + choose(['cold', 'cool', 'warm', 'hot']), 'vibrates', 'pulses', 'shakes',
                    '>>> A hidden ' + script(startseed) + ' enscription becomes visible']
        return choose(response) + ' ' + choose(signal)

    def haunted(startseed):
        # swords that are haunted by ghosts
        global seed
        seed = startseed
        haunts = choose(['is haunted by the ' + ghost(seed),
                         '>>>' + professional(startseed, 'wizard') + ', bound the ' + ghost(
                             seed) + ', to this ' + choose(['sword', 'blade'])])
        return haunts

    def useless(startseed):
        # currently houses anything that I can't fit into any of the other generators above.
        # I don't think is large enough to warrant its own generator.
        # Generally this is minor stuff hence the term useless.
        # Some of this stuff will be moved out later as I flesh out parts of this function.
        global seed
        seed = startseed
        temp = 'is ' + boose(['strangely', 'suprisingly', 'oddly']) + ' ' + choose(
            ['cold', 'cool', 'warm', 'hot']) + ' to the touch'
        weight = 'is ' + choose(['strangely', 'suprisingly', 'oddly']) + ' ' + choose(['heavy', 'light'])
        creeps = 'feels as if ' + choose(
            ['it can read your thoughts', 'it has a mind of its own', 'it is watching you'])
        speaks = 'feels as if ' + choose(['speaks', 'whispers']) + ' to you' + boose(
            [' in a' + choose(['n ancient ', ' forgotten ', 'n archaic ']) + choose(['tongue', 'language'])])
        vibrates = choose(['vibrates', 'pulses', 'hums']) + choose(
            [' gently', ' with ' + choose(['mysterious', 'ancient']) + ' ' + choose(['energy', 'power'])])
        return choose([temp, weight, creeps, speaks, vibrates])

    lore += 'It ' + choose([smell(startseed), detection(startseed), haunted(startseed), useless(startseed)]) + '.'
    lore = lore.replace('It >>>', '')
    return lore


def bowlore(startseed):
    global seed
    seed = startseed
    lore = ''
    lore += 'It was ' + boose(['painstakingly ', 'skillfully ', 'artfully ']) + 'carved from ' + biomaterial(startseed,
                                                                                                             'large') \
            + boose([' by ' + professional(startseed, 'bowyer')])
    lore += '. '
    enscription = boose(['It is enscribed with ' + choose(['a' + choose(['n ancient', ' mysterious']) + ' script',
                                                           choose(['ancient', 'mysterious']) + ' ' + choose(
                                                               ['runes', 'glyphs', 'hieroglyphics']),
                                                           script(startseed)]),
                         'It is engraved with ' + carving(startseed),
                         'There is a crudely scratched ' + script(startseed) + ' enscription',
                         'It is engraved with a ' + choose(['geometric', 'floral']) + ' pattern',
                         'It is engraved with ' + choose(['an unknown', 'the ' + land(startseed, 'demonym'),
                                                          'the ' + word('Famil',
                                                                        startseed) + ' family']) + ' coat of arms'])
    lore += enscription
    lore += '. '
    lore += boose(['Its bowstring is made of ' + stringthing(startseed) + '. '])
    if randint(0, 1) == 0:
        lore += strangelore(seed)
    return gramcheck(lore)


def swordlore(startseed):
    # This is the heart and soul of this program
    # This makes the lore for a particular sword
    # I will comment this better in the future
    global seed
    seed = startseed
    known = True
    lore = ''
    gocation = choose(['the ' + choose(['depths', 'flames', 'hearth', 'fires']) + ' of Hell', 'fire', 'flame',
                       choose(['white', 'red']) + ' hot ' + choose(['flames', 'fire']), 'darkness',
                       'the ' + forge(startseed, choose(['sword', ])), 'beneath ' + mountain(startseed)])
    #                                       add material in here ^
    time = choose(['during the ' + age(startseed), 'during the year ' + str(randint(1, 1500)),
                   'under a ' + moonphase(startseed) + ' moon'])

    def commission(startseed):
        # this makes the starting description for a sword commissioned
        # currently in use in both the glass and metal swords
        global seed
        seed = startseed
        tlore = choose([
            choose([
                'It was ',
                'It is one of ' + str(randint(2, 11)) + ' swords '
            ]),
            choose([
                'Commissioned',
                'One of ' + str(randint(2, 11)) + ' swords commissioned'
            ]) + ' by ' + choose([
                royalty(startseed),
                council(startseed)
            ]) + ', it was ',
            'A decorative sword gifted from ' + royalty(seed) + ' to ' + royalty(seed+1) + boose(
                [' as a peace offering']) + ', it was '
        ])
        return tlore

    def wroughtsword(gocation, time):
        tlore = ''
        if gocation[:7] != 'beneath':
            gocation = 'in ' + gocation
        else:
            gocation = choose(['beneath', 'under', 'below']) + ' ' + gocation[7:]
        body_metal = choose([
                        specificmetal(startseed),
                        normalmetal(startseed),
                        element(startseed),
                        loredmetal(startseed)
                    ])
        gild_metal = choose([
            specificmetal(seed+1),
            normalmetal(seed+1),
            element(seed+1),
            loredmetal(seed+1)
        ])        
        tlore += commission(startseed)
        tlore += choose(['forged', 'wrought', 'cast', 'conceived'])
        if gocation in ['in fire', 'in flame', 'in darkness', 'in the shadows']:
            tlore += ' ' + gocation
        tlore += ' from ' + body_metal + boose([
            ' and gilded with ' + gild_metal
        ])
        tlore += ' by ' + choose([blacksmiths(startseed, 'sword'), blacksmith(startseed, 'sword')])
        if gocation not in ['in fire', 'in flame', 'in darkness']:
            tlore += ' ' + choose([gocation, time]) + '. '
        else:
            tlore += '. '
        return tlore

    def glasssword(gocation, time):
        tlore = ''
        if gocation[:7] != 'beneath':
            gocation = 'in ' + gocation
        else:
            gocation = choose(['beneath', 'under', 'below']) + ' ' + gocation[7:]
        tlore += commission(startseed)
        tlore += 'made from ' + choose([glass(startseed), specificglass(seed)])
        tlore += boose([' by ' + choose([glassmith(startseed), glassmiths(startseed)]) + ' ' + boose([gocation, time])])
        tlore += '. '
        tlore += boose([choose(['A single ' + color(startseed) + ' ' + choose(['rose', 'flower', 'feather']),
                                capitalize(precep(boose(['single ']) + bird(startseed) + ' feather')), capitalize(
                precep(choose(['salamander', 'frog', 'toad', 'newt', 'eft', 'olm', 'worm', amphibian(startseed),
                               spider(startseed), worm(startseed)])))]) + ' is ' + boose(['perfectly ']) + choose(
            ['encased', 'preserved']) + ' within the glass. '])
        return tlore

    def giftsword():
        tlore = ''
        tlore = 'It was '
        tlore += choose(['given to ', 'gifted to ', 'presented to '])
        tlore += hero(startseed)
        tlore += ', by ' + choose([spirit(startseed), royalty(startseed) + ','])
        if randint(0, 1) == 1:
            tlore += ' for his ' + choose(['victory at ' + battle(startseed),
                                           choose(['defeating', 'killing', 'slaying', 'vanquishing']) + ' ' + beast(
                                               seed), choose(
                    ['valor', 'honesty', 'bravery', 'kindness', 'skill', 'fairness', 'gentle spirit'])])
        tlore += '. '
        if lore[-3:] == ',. ':
            tlore = lore[:-3] + '. '
        return tlore

    def craftsword(time):
        tlore = ''
        tlore = 'It was '
        tlore += choose(['painstakingly ', 'meticulously ', ''])
        tlore += choose(['carved', 'crafted'])
        tlore += ' from one solid piece of '
        tlore += choose([biomaterial(startseed, 'large')])
        tlore += boose([' by ' + choose([craftsman(startseed), craftsmen(startseed)])])
        tlore += boose([' ' + time])
        tlore += '. '
        return tlore

    def unknownsword():
        tlore = 'The sword is '
        tlore += 'of '
        tlore += choose(
            [choose(['dwarven', 'elvish', 'goblin', cavespawn(startseed)]), 'unknown', land(startseed, 'demonym')])
        tlore += ' origin. '
        return choose(['The sword is ' + land(startseed, 'demonym') + '. ', tlore])

    def strangesword():
        tlore = ''
        tlore += 'The sword ' + choose(['seems like it is', 'seems to be', 'is']) + ' made of ' + material(startseed,
                                                                                                           'Large')
        tlore += '. '
        return tlore

    def warsword():
        pass

    lore += choose(
        [glasssword(gocation, time), wroughtsword(gocation, time), giftsword(), craftsword(time), unknownsword(),
         strangesword()])
    if lore[:3] == 'The':
        known = False
    enscription = ' ' + boose([
        'its blade is enscribed with ' + choose([
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
            script(startseed)
        ]),
        'its blade is engraved with ' + carving(startseed),
        'there is ' + precep(choose([
            'crudely',
            'unskillfully'
        ])) + ' scratched ' + script(startseed) + ' enscription on its blade',
        'its blade is engraved with a ' + choose([
            'geometric',
            'floral'
        ]) + ' pattern',
        'its blade is engraved with ' + choose([
            'an unknown',
            'the ' + land(startseed, 'demonym'),
            'the ' + word('Famil', startseed) + ' family'
        ]) + ' coat of arms'
    ]) + '. '
    if randint(0, 2) == 0:
        wrapping = fabric(startseed)
        encrusting = choose([normalgem(startseed), specificgem(startseed), element(startseed + 1)])
        if randint(0, 1) == 0:
            lore += choose([
                'Its hilt is ' + boose(['made of ' + material(startseed) + ' ']) + 'encrusted with ' + encrusting,
                'Its ' + encrusting + ' encrusted hilt is ' + choose(['worn', 'smooth']) + ' from ' + choose(
                    ['battle', 'use', 'combat'])
            ])
        else:
            addition = choose([
                'Its hilt is ' + boose(['made of ' + material(startseed) + ' ']) + boose([boose(['tightly ']) + choose(
                    ['wrapped in ', 'wound with ']) + boose(
                    ['worn', 'tattered', 'bloodstained', 'frayed']) + ' ' + wrapping]),
                'Its hilt is ' + choose(['worn', 'smooth']) + ' from ' + choose(['battle', 'use', 'combat'])
            ])
            if addition != 'Its hilt is ':
                lore += addition
        if enscription.strip(' ') != '.' and lore[-2:] != '. ':
            lore += ' and ' + enscription
        else:
            lore += enscription
    elif randint(0, 1) == 0:
        # The code below adds swords with repaired cracks
        if known:
            lore += choose([
                'A crack in the blade ' + choose(
                    ['has been filled with ' + choose([specificmetal(seed), normalmetal(seed), element(seed)]),
                     'was ' + choose(['filled', 'repaired']) + ' by ' + professional(seed, 'blacksmith', dobject = 'sword')]),
                'Originally destroyed ' + choose(['during', 'in']) + ' the ' + choose(
                    [age(seed), war(seed)]) + ', it was repaired by ' + professional(seed, 'blacksmith', dobject = 'sword') + boose(
                    [choose([' in' + ' during']) + ' the ' + age(seed)])
            ])
        else:
            lore += 'A crack in the blade has been filled with ' + choose(
                [specificmetal(seed), normalmetal(seed), element(seed)])
        lore += '. '
    else:
        lore += capitalize(enscription)
    lore = lore.replace('  ', ' ')
    lore = lore.replace('ts hilt is and i', '')
    if randint(0, 2) == 0 and known:
        lore += choose(['Wielded by ', 'In the hands of ', 'Held by ']) + choose(
            [hero(startseed).split(',')[0], hero(seed)]) + ', it ' + choose(['once ']) + choose(
            ['slew ', 'defeated ', 'killed ', 'vanquished ']) + choose([horde(startseed), beast(startseed)]) + '.'
    elif randint(0, 1) == 0 and known:
        lore += 'It was ' + choose(['wielded by ', 'held by ']) + choose(
            [hero(startseed).split(',')[0], hero(seed) + ',']) + choose([' in ', ' during ']) + battle(
            startseed) + ' ' + choose(
            ['', ' where it ' + choose(['slew', 'killed']) + ' ' + choose([hero(seed), royalty(seed)])]) + '.'
    else:
        lore += strangelore(seed)
    return gramcheck(lore)


'''
   ▄████████  ▄█     █▄   ▄██████▄     ▄████████ ████████▄        ▄█        ▄██████▄     ▄████████    ▄████████
  ███    ███ ███     ███ ███    ███   ███    ███ ███   ▀███      ███       ███    ███   ███    ███   ███    ███
  ███    █▀  ███     ███ ███    ███   ███    ███ ███    ███      ███       ███    ███   ███    ███   ███    █▀
  ███        ███     ███ ███    ███  ▄███▄▄▄▄██▀ ███    ███      ███       ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄
▀███████████ ███     ███ ███    ███ ▀▀███▀▀▀▀▀   ███    ███      ███       ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀
         ███ ███     ███ ███    ███ ▀███████████ ███    ███      ███       ███    ███ ▀███████████   ███    █▄
   ▄█    ███ ███ ▄█▄ ███ ███    ███   ███    ███ ███   ▄███      ███▌    ▄ ███    ███   ███    ███   ███    ███
 ▄████████▀   ▀███▀███▀   ▀██████▀    ███    ███ ████████▀       █████▄▄██  ▀██████▀    ███    ███   ██████████
                                      ███    ███                 ▀                      ███    ███
'''

if __name__ == '__main__':
    #print(swordlore(142637))
    #print
    #print(loredmetal(30))
    #print
    #print(paintinglore(352))
    #print
    for x in range(0, 90):
        print(professional(seed+x,'blacksmith','singular','sword'))
    print
    # for x in range(0,30):
    # print epithet(seed+x,'noble','male')
