"""For adding words to the Chamoru dictionary"""

import json
import logging

import dict_helper


def _handle_new_word_input(chamoru_dict, word_to_add, value):
    """Helper function to process user inputs during _add_word_to_dict.

    Args:
        chamoru_dict (dict): Chamoru dictionary.
        word_to_add (str): Word being added.
        value (str): Value being prompted for.

    Returns:
        str: Value response for the value prompt.
    """

    value_response = input(f"{value}: ")
    if value_response == "q":
        chamoru_dict.pop(word_to_add)
        return None

    return value_response


def _add_word_to_dict(chamoru_dict, word_to_add):
    """Helper function to process adding a word to the Chamoru dictionary.

    Args:
        chamoru_dict (dict): Chamoru dictionary being updated.
        word_to_add (str): Word being added to chamoru_dict.

    Returns:
        dict: Data for word just added.
    """

    # Init word to empty dict
    chamoru_dict[word_to_add] = {}

    print("...enter 'q' to quit during any prompt.\n")

    definition = _handle_new_word_input(chamoru_dict, word_to_add, "Definition")
    if definition is None:
        print(f'Abandoning adding "{word_to_add}".\n')
        return None

    word_type = _handle_new_word_input(chamoru_dict, word_to_add, "Type")
    if word_type is None:
        print(f'Abandoning adding "{word_to_add}".\n')
        return None

    ch_ex = _handle_new_word_input(chamoru_dict, word_to_add, "Chamoru example")
    if ch_ex is None:
        print(f'Abandoning adding "{word_to_add}".\n')
        return None

    if ch_ex != "":
        en_ex = _handle_new_word_input(chamoru_dict, word_to_add, "English translation")
        if en_ex is None:
            print(f'Abandoning adding "{word_to_add}".\n')
            return None

    otro = _handle_new_word_input(chamoru_dict, word_to_add, "Other spelling")
    if otro is None:
        print(f'Abandoning adding "{word_to_add}".\n')
        return None

    source = _handle_new_word_input(chamoru_dict, word_to_add, "Source")
    if source is None:
        print(f'Abandoning adding "{word_to_add}".\n')
        return None

    print()  # Add blank line before next prompt
    chamoru_dict[word_to_add]["definitions"] = [definition]
    chamoru_dict[word_to_add]["types"] = [word_type]
    chamoru_dict[word_to_add]["chamoru_examples"] = []
    chamoru_dict[word_to_add]["english_examples"] = []
    chamoru_dict[word_to_add]["see_also"] = []
    chamoru_dict[word_to_add]["other_spellings"] = []
    chamoru_dict[word_to_add]["sources"] = []
    chamoru_dict[word_to_add]["pronunciation"] = ""
    chamoru_dict[word_to_add]["origin"] = ""

    if ch_ex != "":
        chamoru_dict[word_to_add]["chamoru_examples"].append(ch_ex)
        chamoru_dict[word_to_add]["english_examples"].append(en_ex)
    if otro != "":
        chamoru_dict[word_to_add]["other_spellings"].append(otro)
    if source != "":
        chamoru_dict[word_to_add]["sources"].append(source)

    return chamoru_dict[word_to_add]


def add_to_dictionary(filename, chamoru_dict):
    """Adds to the Chamoru dictionary.

    Args:
        filename (str): Chamoru dictionary JSON file.
        chamoru_dict (dict): Chamoru dictionary object.
    """

    print(f"Adding to {filename}")

    # Run continuously until done
    while True:
        # Init empty dict
        word_data = None

        word_to_add = dict_helper.handle_input()
        if word_to_add == "":
            print("Exiting. Saina Ma'åsi'")
            break

        word_data = dict_helper.check_dict_for_word(chamoru_dict, word_to_add)

        # word_data will exist if the word is already defined
        if word_data is None:
            print(f'Adding the word, "{word_to_add}"')
            # assigned returned data to an unused variable
            logging.info(f"Trying to add {word_to_add}")
            _ = _add_word_to_dict(chamoru_dict, word_to_add)

            if _ is None:
                logging.warning(f"Abandoned adding {word_to_add}")
            else:
                logging.info(f"Successfully added {word_to_add}")
        else:
            print(f"{word_to_add} already exists.\n")

    # Add all new words to the file
    with open(filename, "w", encoding="utf-8") as merged_file:
        json.dump(chamoru_dict, merged_file, indent=4, ensure_ascii=False)
