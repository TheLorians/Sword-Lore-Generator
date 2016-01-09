# Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from swordlore import *

# Classes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Weapon Classes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class WeaponHandle(object):
    def __init__(self, name):
        self.name = name
        self.wrappable = True
        self.material = 'standard'
    def lore(self):
        variation = self.name
        lore = ''
        wrapping = fabric()
        encrusting = gem()
        if boose([True]):
            lore += choose([
                'Its %s is ' %variation + boose([
                    'made of ' + material() + ' '
                ]) + 'encrusted with ' + encrusting,
                'Its ' + encrusting + ' encrusted %s is ' %variation + choose([
                    'worn',
                    'smooth'
                ]) + ' from ' + choose([
                    'battle',
                    'use',
                    'combat'
                ])
            ])
        else:
            addition = choose([
                'Its %s is ' %variation + boose([
                    'made of ' + material() + ' '
                ]) + boose([
                    boose([
                        'tightly '
                    ]) + choose([
                        'wrapped',
                        'wound'
                    ]) +' in ' + boose([
                        'worn',
                        'tattered',
                        'bloodstained',
                        'frayed'
                    ]) + ' ' + wrapping
                ]),
                'Its %s is ' %variation + choose([
                    'worn',
                    'smooth'
                ]) + ' from ' + choose([
                    'battle',
                    'use',
                    'combat'
                ])
            ])
            if addition != 'Its %s is ' %variation:
                lore += addition
        lore = lore.replace('ts %s is and i' %variation, '')
        return lore + '. '

class WeaponMain(object):
    def __init__(self, name):
        self.name = name
        self.wrappable = False
        self.material = 'standard'
    def lore(self):
        # Work in progress
        # Makes the description for the main part of the weapon e.g. blade
        variation = self.name
        gocation = choose([
            'the ' + choose([
                'depths',
                'flames',
                'hearth',
                'fires'
            ]) + ' of Hell', 'fire', 'flame',
            choose([
                'white',
                'red'
            ]) + ' hot ' + choose([
                'flames',
                'fire'
            ]),
            'darkness',
            'the ' + forge(choose(['sword', ])), 'beneath ' + mountain()
        ])
            #                   add material in here ^
        time = choose([
            'during the ' + age(),
            'during the year ' + str(randint(1, 1500)),
            'under ' + precep(moonphase()) + ' moon'
        ])
        
        def commission():
                # this makes the starting description for a sword commissioned
                # currently in use in both the glass and metal swords
                tlore = choose([
                    choose([
                        'The %s was ' %(variation),
                        'The %s one of %d %ss ' %(variation, randint(2, 11), variation)
                    ]),
                    choose([
                        'Commissioned',
                        'One of %d %ss commissioned' %(randint(2, 11), variation)
                    ]) + ' by ' + choose([
                        royalty(),
                        council()
                    ]) + ', it was ',
                    'The %s is a decorative %s gifted from %s to %s %s, it was' 
                    %(variation, variation, royalty(), royalty(), boose(['as apeace offering']))
                ])
                return tlore
        
        def wroughtmain(gocation, time):
            tlore = ''
            if gocation[:7] != 'beneath':
                gocation = 'in ' + gocation
            else:
                gocation = choose(['beneath', 'under', 'below']) + ' ' + gocation[7:]
            body_metal = metal()
            gild_metal = metal()
            tlore += commission()
            tlore += choose(['forged', 'wrought', 'cast', 'conceived'])
            if gocation in ['in fire', 'in flame', 'in darkness', 'in the shadows']:
                tlore += ' ' + gocation
            tlore += ' from ' + body_metal + boose([
                ' and gilded with ' + gild_metal
            ])
            tlore += ' by ' + professional('blacksmith', dobject='%s')
            if gocation not in ['in fire', 'in flame', 'in darkness']:
                tlore += ' ' + choose([gocation, time]) + '. '
            else:
                tlore += '. '
            return tlore
        
        def craftmain(time):
            tlore = 'The %s was '%variation
            tlore += choose(['painstakingly ', 'meticulously ', ''])
            tlore += choose(['carved', 'crafted'])
            tlore += ' from ' + boose(['one ' + boose(['solid']) + 'piece of '])
            tlore += choose([biomaterial('large')])
            tlore += boose([' by ' + professional('craftsman')])
            tlore += boose([' ' + time])
            tlore += '. '
            return tlore
        
        def glassmain(gocation, time):
            tlore = ''
            if gocation[:7] != 'beneath':
                gocation = 'in ' + gocation
            else:
                gocation = choose(['beneath', 'under', 'below']) + ' ' + gocation[7:]
            tlore += commission()
            tlore += 'made from ' + glass()
            tlore += boose([' by ' + professional('glassmith') + ' ' + boose([gocation, time])])
            tlore += '. '
            tlore += boose([
                choose([
                    'A single ' + color() + ' ' + choose([
                        'rose',
                        'flower',
                        'feather'
                    ]),
                    capitalize(precep(boose(['single ']) + bird() + ' feather')),
                    capitalize(precep(choose([
                        'salamander',
                        'frog',
                        'toad',
                        'newt',
                        'eft',
                        'olm',
                        'worm',
                        amphibian(),
                        spider(),
                        worm()
                        ])))
                    ]) + ' is ' + boose(['perfectly ']) + choose([
                        'encased',
                        'preserved'
                    ]) + ' within the glass. '
            ])
            return tlore
        #temporary line change implementation later
        known = True
        if boose([True]):
            # The code below adds swords with repaired cracks
            if known:
                lore = choose([
                    'A crack in the %s ' %variation + choose([
                        'has been filled with ' + metal(),
                        'was ' + choose(['filled', 'repaired']) + ' by ' + professional('blacksmith', dobject='sword')
                    ]),
                    'Originally destroyed ' + choose([
                        'during',
                        'in'
                    ]) + ' the ' + choose([
                        age(),
                        war()
                    ]) + ', the %s was repaired by %s' %(variation, professional('blacksmith', dobject='sword')) + boose([
                        choose([
                            ' in',
                            ' during'
                        ]) + ' the ' + choose([
                            age(),
                            war()
                        ])
                    ])
                ])
            else:
                lore = 'A crack in the %s has been filled with ' + metal()
            lore += '. '
        else:
            lore = capitalize(enscript(variation))
        lore = lore.replace('  ', ' ')
        return choose([wroughtmain(gocation, time), glassmain(gocation, time), craftmain(time), lore])


class Weapon(object):
    def __init__(self, archetype, parts):
        self.archetype = archetype
        self.parts = parts
    # These lore functions are not constant
    # They depend on the current state
    # (i.e. the result of these lore functions depends on the order in which they are called)
    def commission(self):
        # this makes the starting description for a weapon commissioned
        tlore = choose([
            'It is one of ' + str(randint(2, 11)) + ' %ss, ' %self.archetype,
            choose([
                'Commissioned',
                'One of ' + str(randint(2, 11)) + ' %ss commissioned' %self.archetype
            ]) + ' by ' + choose([
                royalty(),
                council()
            ]) + ', ',
            'A decorative %s gifted from ' %self.archetype + royalty() + ' to ' + royalty() + boose(
                [' as a peace offering']) + ', '
        ])
        return tlore
    def partlore(self):
        # Describes the lore of each individual part
        return ''.join(map(lambda x: choose([x.lore(),'']), self.parts))
    def historylore(self):
        if boose([True]):
            return choose([
                'Wielded by ',
                'In the hands of ',
                'Held by '
                ]) + hero() + ', it ' + choose(['once ']) + choose([
                    'slew',
                    'defeated',
                    'killed',
                    'vanquished',
                    'struck down'
                ]) + ' ' + choose([
                    horde(),
                    beast()
                ]) + '. '
        else:
            return 'It was ' + choose([
                'wielded by ',
                'held by '
            ]) + hero()+',' + choose([
                ' in ',
                ' during '
            ]) + battle() + ' ' + boose([
                ' where it ' + choose([
                    'slew',
                    'killed'
                ]) + ' ' + choose([
                    hero(),
                    royalty()
                ])
            ]) + '. '
    def strangelore(self):
        lore = ''
        def smell():
            # describes the smell of the sword
            # http://grammar.yourdictionary.com/style-and-usage/descriptive-words-for-scents.html#VrGLY7AqDbAPBGlv.99
            smell = ['metal', blood(), 'sulfur', 'brimstone', 'smoke', 'bile', 'sweat', 'the sea', 'loam', fruit()]
            smells = choose(smell, randint(1,2))
            smell_descriptor = ['acrid', 'airy', 'clean', 'crisp', 'dirty', 'earthy', 'faint', 'fetid', 'fishy', 'fresh','floral', 'flowery', 'light', 'loamy', 'musty', 'nauseating', 'perfumed', 'pungent', 'putrid', 'rancid', 'redolent', 'repulsive', 'rotten', 'sharp', 'sour', 'stale', 'stinking', 'sweet']
            return 'smells ' + boose([
                'strongly ',
                'faintly '
            ]) + choose([
                'of ' + read_list(smells),
                choose(smell_descriptor)
            ])
    
        def detection():
            # swords that react to a certain situation
            signal = ['when ' + plural(
                choose(['orc', 'goblin', 'troll', 'giant', 'cyclops', cavespawn()])) + ' are ' + choose(
                ['near', 'nearby']), 'in the presence of ' + boose(['dark', 'black']) + ' magic',
                      'when emersed in ' + choose(['magma', 'lava', 'fire', 'water']),
                      'when it touches ' + blood(), 'in ' + choose(['the dark', 'low light', 'bright light'])]
            response = ['glows', 'glows ' + color(), 'turns ' + color(),
                        'becomes ' + choose(['cold', 'cool', 'warm', 'hot']), 'vibrates', 'pulses', 'shakes',
                        '>>> A hidden ' + script() + ' enscription becomes visible']
            return choose(response) + ' ' + choose(signal)
    
        def haunted():
            # swords that are haunted by ghosts
            haunts = choose(['is haunted by the ' + ghost(),
                             '>>>' + professional('wizard') + ', bound the ' + ghost(
                                 ) + ', to this ' + self.archetype])
            return haunts
    
        def maddening():
            # swords that have lead their owners to ill fate
            madness = 'has driven ' + boose(['all of ']) + 'its owners to '+choose(['madness', 'insanity', 'suicide'])
        def useless():
            # currently houses anything that I can't fit into any of the other generators above.
            # I don't think is large enough to warrant its own generator.
            # Generally this is minor stuff hence the term useless.
            # Some of this stuff will be moved out later as I flesh out parts of this function.
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
    
        lore += 'It ' + choose([smell(), detection(), haunted(), useless()]) + '.'
        lore = lore.replace('It >>>', '')
        return lore
    def lore(self):
        tlore = gramcheck(boose([self.commission()]) + self.partlore() + self.historylore() + self.strangelore())
        if self.archetype == 'light saber':
            return tlore.replace('wizard','jedi').replace('magic','the force')
        return tlore
if __name__ == "__main__":
    seed(10)
    weap = Weapon('axe',[WeaponMain('head'),WeaponHandle('handle')])
    print weap.lore()