"""General helper functions for accessing the Chamoru dictionary"""


def check_dict_for_word(chamoru_dict, word_to_search):
    """Checks the dictionary for the word being searched.

    1st it tries to get the word from the dict. If nothing is found, it will
    attempt to search for the word in lowercase. If nothing is found again,
    it will attempt to search for the word with the first letter capitalized.

    Args:
        chamoru_dict (dict): Chamoru dictionary.
        word_to_search (str): Word being searched.

    Returns:
        dict: Data associated with word_to_search, otherwise None.
    """

    word_data = chamoru_dict.get(word_to_search)
    if word_data is None:
        # Check as lowercase
        _lower = word_to_search.lower()
        word_data = chamoru_dict.get(_lower)

    if word_data is None:
        # Check with capitalized letter since some words are stored with a capitalized 1st letter
        _capital = word_to_search.title()
        word_data = chamoru_dict.get(_capital)

    # We won't check for uppercase as the dictionary should not contain uppercased words.
    if word_data is None:
        print(f'No definition found for "{word_to_search}"\n')
        return None

    return word_data


def handle_input():
    """Retrieves input from user.

    Returns:
        str: User input.
    """
    word_to_search = input("Enter word (leave blank to exit): ")
    return word_to_search


def print_numbered_list(data: list):
    """Enumerates through 'data' and prints it as a numbered list.

    Args:
        data (list): Data to display.
    """
    for index, value in enumerate(data):
        print(f" {index+1}: {value}")


def stylize_output(word_data):
    """Helper function to stylize the output.

    Args:
        word_data (dict): Chamoru word data.

    Returns:
        None: If no values are found, None is returned.
    """

    try:
        word_def = word_data["definitions"]
        word_types = word_data["types"]
        word_syn = word_data["see_also"]
        word_ch_ex = word_data["chamoru_examples"]
        word_en_ex = word_data["english_examples"]

        print("Definitions:")
        print_numbered_list(word_def)

        print("Types:")
        print_numbered_list(word_types)

        # Check if example sentences are stored
        if len(word_ch_ex) > 0:
            print("Chamoru Examples:")
            print_numbered_list(word_ch_ex)

            print("English Examples Translations:")
            print_numbered_list(word_en_ex)

        # Check if related-words are stored
        if len(word_syn) > 0:
            print("See also:")
            print_numbered_list(word_syn)

        print()

    except KeyError as key_error:
        print(f"{word_data} missing required key")
        raise key_error
