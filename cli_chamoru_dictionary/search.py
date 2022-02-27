"""Functions for searching in the Chamoru dictionary"""

import logging

import dict_helper


def start_search(chamoru_dict):
    """Starts the search through the Chamoru dictionary.

    Args:
        chamoru_dict (dict): Chamoru dictionary.
    """

    done = False
    while not done:
        word_to_search = dict_helper.handle_input()
        if word_to_search == "":
            print("Exiting. Saina Ma'åsi'")
            done = True
        else:
            # Look for word in dictionary
            word_data = dict_helper.check_dict_for_word(chamoru_dict, word_to_search)
            if word_data:
                logging.info(word_to_search)
                dict_helper.stylize_output(word_data)
            else:
                logging.warning(f"{word_to_search} not found")
