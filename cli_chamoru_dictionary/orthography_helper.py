"""Linguistic-related Chamoru information."""

import logging

CHAMORU_ALPHABET = {
    "'": 0, "a": 1, "å": 2, "b": 3, "ch": 4, "d": 5,
    "e": 6, "f": 7, "g": 8, "h": 9, "i": 10, "k": 11,
    "l": 12, "m": 13, "n": 14, "ñ": 15, "ng": 16, "o": 17,
    "p": 18, "r": 19, "s": 20, "t": 21, "u": 22, "y": 23,
    # Non-letters
    "-": 24, " ": 25,
    # Accented vowels
    "á": 1, "é": 6, "í": 10, "ó": 17, "ú": 22
    # Pronoun letters
    # TODO
}


def chamoru_sort(word: str):
    """
    Intended for use as function passed to `sorted()`. Sorts using the Chamoru alphabet.

    Example usage: Let `ch` be a list of Chamoru words. To sort the list you can do
        sorted(ch, key=lambda x: chamoru_sort(x))
    ...where x is the word.

    Args:
        word (str): Chamoru word as a str, not the Class.

    Returns:
        List[int]: List of CHAMORU_ALPHABET values.
    """

    wal = []
    lowercase_word = word.lower()
    done = False
    i = 0

    while not done:
        try:
            if i + 1 == len(lowercase_word):
                # last letter so don't check ahead
                wal.append(CHAMORU_ALPHABET[lowercase_word[i]])
                done = True
            else:
                # Check i & i+1
                # We increase i for ng and ch since they're technically 1 letter
                if lowercase_word[i] == 'n' and i != len(lowercase_word) - 1:
                    # We found n & it's not the last letter
                    if lowercase_word[i + 1] == 'g':
                        print("it is ng")
                        wal.append(CHAMORU_ALPHABET['ng'])
                        i = i+1
                    else:
                        wal.append(CHAMORU_ALPHABET[lowercase_word[i]])
                elif lowercase_word[i] == 'c':
                    # c only appears with h
                    wal.append(CHAMORU_ALPHABET['ch'])
                    i += 1
                else:
                    wal.append(CHAMORU_ALPHABET[lowercase_word[i]])
        except KeyError as ke:
            logging.warning(f"{ke} in {lowercase_word}")
            return None
        i += 1

    return wal


def update_glota(word: str) -> str:
    """
    Updates the Chamoru word to use the preferred  glota, '.

    Args:
        word (str): Chamoru word to update.

    Returns:
        str: Word with updated glota.
    """

    bad_glotas = ['\u0027', '\u2018', '\u2019']
    glota = "'"

    wal = list(word)  # word as a list
    for ltr in range(len(word)):
        if wal[ltr] in bad_glotas:
            wal[ltr] = glota

    return "".join(wal)
