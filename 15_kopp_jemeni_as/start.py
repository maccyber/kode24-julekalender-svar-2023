#!/usr/bin/python3

import itertools

words = ["svelte", "angular", "jquery", "ember"]

# Ta tredje bokstav fra den søteste.
# Tredje bokstav fra den hippeste.
# Nest siste bokstav fra den kjipeste.
# Bokstaven i midten fra den asiatiske = Vue (U)
# Siste bokstav fra den vanligste = React (T)
# Siste bokstav fra den eldste.


def print_word(list_of_words):
    print(
        *list_of_words[0][2]
        + list_of_words[1][2]
        + list_of_words[2][-2]
        + "u"
        + "t"
        + list_of_words[3][-1],
        sep=""
    )


word_permutations = itertools.permutations(words)

for perm in word_permutations:
    print_word(list(perm))
