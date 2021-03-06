# -*- coding: utf-8 -*-
#
#    TypeAtlas Morse Code Data
#    Written in 2018-2021 by Milko Krachounov
#
#    This file is part of TypeAtlas.
#
#    To the extent possible under law, Milko Krachunov has waived all copyright
#    and related or neighboring rights to TypeAtlas Morse Code Data.
#    This software is distributed without any warranty.
#
#    You should have received a copy of the CC0 legalcode along with this
#    work.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
#

from collections import ChainMap
from typeatlas.charsets import add_morse_code, MULTICHAR_REMAP

N_ = lambda s: s


MORSE_INTER = {
    'A': ". -",
    'B': "- . . .",
    'C': "- . - .",
    'D': "- . .",
    'E': ".",
    'F': ". . - .",
    'G': "- - .",
    'H': ". . . .",
    'I': ". .",
    'J': ". - - -",
    'K': "- . -",
    'L': ". - . .",
    'M': "- -",
    'N': "- .",
    'O': "- - -",
    'P': ". - - .",
    'Q': "- - . -",
    'R': ". - .",
    'S': ". . .",
    'T': "-",
    'U': ". . -",
    'V': ". . . -",
    'W': ". - -",
    'X': "- . . -",
    'Y': "- . - -",
    'Z': "- - . .",
    '0': "- - - - -",
    '1': ". - - - -",
    '2': ". . - - -",
    '3': ". . . - -",
    '4': ". . . . -",
    '5': ". . . . .",
    '6': "- . . . .",
    '7': "- - . . .",
    '8': "- - - . .",
    '9': "- - - - .",
    '.': ". - . - . -",
    ',': "- - . . - -",
    '?': ". . - - . .",
    "'": ". - - - - .",
    '!': "- . - . - -",
    '/': "- . . - .",
    '(': "- . - - .",
    ')': "- . - - . -",
    '&': ". - . . .",
    ':': "- - - . . .",
    ';': "- . - . - .",
    '=': "- . . . -",
    '+': ". - . - .",
    '-': "- . . . . -",
    '_': ". . - - . -",
    '"': ". - . . - .",
    '$': ". . . - . . -",
    '@': ". - - . - .",
}



MORSE_AMERICAN = {
    'A': ". --",
    'B': "-- . . .",
    'C': ". .  .",
    'D': "-- . .",
    'E': ".",
    'F': ". -- .",
    'G': "-- -- .",
    'H': ". . . .",
    'I': ". .",
    'J': "-- . -- .",
    'K': "-- . --",
    'L': "---",
    'M': "-- --",
    'N': "-- .",
    'O': ".  .",
    'P': ". . . . .",
    'Q': ". . -- .",
    'R': ".  . .",
    'S': ". . .",
    'T': "--",
    'U': ". . --",
    'V': ". . . --",
    'W': ". -- --",
    'X': ". -- . .",
    'Y': ". .  . .",
    'Z': ". . .  .",
    '0': "-----",
    '1': ". -- -- .",
    '2': ". . -- . .",
    '3': ". . . -- .",
    '4': ". . . . --",
    '5': "-- -- --",
    '6': ". . . . . .",
    '7': "-- -- . .",
    '8': "-- . . . .",
    '9': "-- . . --",

    '.': ". . -- . .",
    ',': ". -- . --",
    '?': "-- . . -- .",
    "'": ". . -- .  . -- . .",
    '!': "-- -- -- .",
    '/': ". . --  --",
    '(': ". . . . .  -- .",
    ')': ". . . . .  . .  . .",
    '&': ".  . . .",
    ':': "-- . --  . .",
    ';': ". . .  . .",
    '???': ". . -- .  -- .",
    '???': ". . -- .  -- . -- .",
}


MORSE_INTER_PROSIGNS = {
    '????': ". . . - - - . . .", # SOS
    '\x04': ". . . - . -", # End of work
    '\x18': ". . . . . . . .", # Error
    '\x05': "- . -",  # Invitation to transmit
    '\x02': "- . - . - .", # Starting signal, also bell is appropriate
    '\f': ". - . - .", # New page
    '\x06': ". . . - .", # Understood
    #'': ". . . - .", # Wait
}

MORSE_INTER_NONENGLISH = {
    '??': ". - - . -",
    '??': ". - . -",
    '??': ". - - . -",
    '??': ". - . -",
    '??': ". - . -",
    '??': "- . - . .",
    '??': "- . - . .",
    '??': "- . - . .",
    'CH': "- - - -",
    '??': ". . - . .",
    '??': ". . - - .",
    '??': ". . - . .",
    '??': ". - . . -",
    '??': ". . - . .",
    '??': "- - . - .",
    '??': "- - - -",
    '??': ". - - - .",
    '??': ". - . . -",
    '??': "- - . - -",
    '??': "- - . - -",
    '??': "- - - .",
    '??': "- - - .",
    '??': "- - - .",
    '??': ". . . - . . .",
    '??': ". . . - .",
    '??': "- - - -",
    '??': ". - - . .",
    '??': ". . - -",
    '??': ". . - -",
    '??': "- - . . - .",
    '??': "- - . . -",
}


MORSE_INTER_COMPLETE = dict(ChainMap(MORSE_INTER_NONENGLISH, MORSE_INTER))
MORSE_PERSIAN_LATIN_BASE = dict(MORSE_INTER_COMPLETE, **{
    'CH': "- - - .",
    'KH': "- . . -",
    'SH': "- - - -",
    'AI': "- - -",
    'GH': ". . - -",
})



MAP_GREEK = {
    '??': 'A',
    '??': 'B',
    '??': 'G',
    '??': 'D',
    '??': 'E',
    '??': 'Z',
    '??': 'H',
    '??': 'C',
    '??': 'I',
    '??': 'K',
    '??': 'L',
    '??': 'M',
    '??': 'N',
    '??': 'X',
    '??': 'O',
    '??': 'P',
    '??': 'R',
    '??': 'S',
    '??': 'T',
    '??': 'Y',
    '??': 'F',
    '??': 'CH',
    '??': 'Q',
    '??': 'W',
}

MAP_RUSSIAN = {
    '??': 'A',
    '??': 'B',
    '??': 'W',
    '??': 'G',
    '??': 'D',
    '??': 'E',
    '??': 'V',
    '??': 'Z',
    '??': 'I',
    '??': 'J',
    '??': 'K',
    '??': 'L',
    '??': 'M',
    '??': 'N',
    '??': 'O',
    '??': 'P',
    '??': 'R',
    '??': 'S',
    '??': 'T',
    '??': 'U',
    '??': 'F',
    '??': 'H',
    '??': 'C',
    '??': '??',
    '??': 'CH',
    '??': 'Q',
    '??': 'X',
    '??': 'Y',
    '??': '??',
    '??': '??',
    '??': '??',
    '??': '??',
}

VARIANT_BULGARIAN = {
    '??': '??',
    '??': '??',
}

VARIANT_UKRAINIAN = {
    '??': '??',
    '??': '??',
}

MAP_BULGARIAN = {VARIANT_BULGARIAN.get(char, char): latin
                 for char, latin in MAP_RUSSIAN.items()}

MAP_UKRAINIAN = {VARIANT_UKRAINIAN.get(char, char): latin
                 for char, latin in MAP_RUSSIAN.items()}


MAP_HEBREW = {
    '??': 'A',
    '??': 'B',
    '??': 'G',
    '??': 'D',
    '??': 'O',
    '??': 'E',
    '??': 'Z',
    '??': 'H',
    '??': 'U',
    '??': 'I',
    '??': 'K',
    '??': 'L',
    '??': 'M',
    '??': 'N',
    '??': 'C',
    '??': 'J',
    '??': 'P',
    '??': 'W',
    '??': 'Q',
    '??': 'R',
    '??': 'S',

}

MAP_ARABIC = {
    '??': 'A',
    '??': 'B',
    '??': 'T',
    '??': 'C',
    '??': 'J',
    '??': 'H',
    '??': 'O',
    '??': 'D',
    '??': 'Z',
    '??': 'R',
    '??': '??',
    '??': 'S',
    '??': 'CH',
    '??': 'X',
    '??': 'V',
    '??': 'L',
    '??': 'M',
    '??': 'N',
    '??': '??',
    '??': 'W',
    '??': 'I',
    '???': 'E',
}

MAP_PERSIAN = {
    '??': 'A',
    '??': 'B',
    '??': 'P',
    '??': 'T',
    '??': 'C',
    '??': 'J',
    '??': 'CH',
    '??': 'H',
    '??': 'KH',
    '??': 'D',
    '??': 'Z',
    '??': 'R',
    '??': 'J',
    '??': 'G',
    '??': 'S',
    '??': 'SH',
    '??': 'S',
    '??': 'Z',
    '??': 'T',
    '??': 'Z',
    '??': 'AI',
    '??': 'GH',
    '??': 'F',
    '??': 'Q',
    '??': 'K',
    '??': 'G',
    '??': 'L',
    '??': 'M',
    '??': 'N',
    '??': 'W',
    '??': 'H',
    '??': 'I',
}

MAP_KOREAN = SKATS = {
     '???': 'L',
     '???': 'F',
     '???': 'B',
     '???': 'V',
     '???': 'M',
     '???': 'W',
     '???': 'G',
     '???': 'K',
     '???': 'P',
     '???': 'C',
     '???': 'X',
     '???': 'Z',
     '???': 'O',
     '???': 'J',
     '???': 'E',
     '???': 'I',
     '???': 'T',
     '???': 'S',
     '???': 'A',
     '???': 'N',
     '???': 'H',
     '???': 'R',
     '???': 'D',
     '???': 'U',
     '???': 'TU',
     '???': 'EU',
     '???': 'SU',
     '???': 'IU',
}


FIVE_NEEDLE = {
    'A': r" /|||\ ",
    'B': r" /||\| ",
    #'C': r"",
    'D': r" |/||\ ",
    'E': r" /|\|| ",
    'F': r" |/|\| ",
    'G': r" ||/|\ ",
    'H': r" /\||| ",
    'I': r" |/\|| ",
    #'J': r"",
    'K': r" ||/\| ",
    'L': r" |||/\ ",
    'M': r" \/||| ",
    'N': r" |\/|| ",
    'O': r" ||\/| ",
    'P': r" |||\/ ",
    #'Q': r"",
    'R': r" \|/|| ",
    'S': r" |\|/| ",
    'T': r" ||\|/ ",
    #'U': r"",
    'V': r" \||/| ",
    'W': r" |\||/ ",
    #'X': r"",
    'Y': r" \|||/ ",
    #'Z': r"",
}

FIVE_NEEDLE_SUBSTITUTIONS = {
    'J': 'G',
    'Q': 'K',
    'Z': 'S',
    'U': 'V',

    'C': 'K', # ?????
    'X': 'KS', # ?????
}

FIVE_NEEDLE_FULL_ALPHABET = dict(sorted(dict(
                                    [(k, k) for k in FIVE_NEEDLE],
                                    **FIVE_NEEDLE_SUBSTITUTIONS).items()))


MORSE_GREEK = {k: MORSE_INTER_COMPLETE[v] for k, v in MAP_GREEK.items()}
MORSE_RUSSIAN = {k: MORSE_INTER_COMPLETE[v] for k, v in MAP_RUSSIAN.items()}
MORSE_BULGARIAN = {k: MORSE_INTER_COMPLETE[v] for k, v in MAP_BULGARIAN.items()}
MORSE_UKRAINIAN = {k: MORSE_INTER_COMPLETE[v] for k, v in MAP_UKRAINIAN.items()}
MORSE_HEBREW = {k: MORSE_INTER_COMPLETE[v] for k, v in MAP_HEBREW.items()}
MORSE_ARABIC = {k: MORSE_INTER_COMPLETE[v] for k, v in MAP_ARABIC.items()}
MORSE_PERSIAN = {k: MORSE_PERSIAN_LATIN_BASE[v] for k, v in MAP_PERSIAN.items()}
MORSE_KOREAN = {k: ' '.join(MORSE_INTER_COMPLETE[v] for v in vs)
                for k, vs in MAP_KOREAN.items()}
add_morse_code(N_("International Morse code (1865-present)"), MORSE_INTER)
add_morse_code(N_("International Morse code with extensions"),
               dict(ChainMap(MORSE_INTER_PROSIGNS,
                             MORSE_INTER_NONENGLISH,
                             MORSE_INTER)))
add_morse_code(N_("Morse code for Greek"), MAP_GREEK, MORSE_INTER_COMPLETE)
add_morse_code(N_("Morse code for Russian"), MAP_RUSSIAN, MORSE_INTER_COMPLETE)
add_morse_code(N_("Morse code for Bulgarian"), MAP_BULGARIAN, MORSE_INTER_COMPLETE)
add_morse_code(N_("Morse code for Ukrainian"), MAP_UKRAINIAN, MORSE_INTER_COMPLETE)
add_morse_code(N_("Morse code for Hebrew"), MAP_HEBREW, MORSE_INTER_COMPLETE)
add_morse_code(N_("Morse code for Arabic"), MAP_ARABIC, MORSE_INTER_COMPLETE)
add_morse_code(N_("Morse code for Persian"), MAP_PERSIAN, MORSE_PERSIAN_LATIN_BASE)
add_morse_code(N_("Morse code for Korean"), MAP_KOREAN, MORSE_INTER_COMPLETE,
                                            remap_mode=MULTICHAR_REMAP)
add_morse_code(N_("American Morse code (1844-1970s)"), MORSE_AMERICAN,
                                                       length_coded=True)
add_morse_code(N_("Five-needle telegraph code"), FIVE_NEEDLE_FULL_ALPHABET,
                                                 FIVE_NEEDLE,
                                                 remap_mode=MULTICHAR_REMAP,
                                                 needle_coded=True)
