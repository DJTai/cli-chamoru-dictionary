import pytest

import cli_chamoru_dictionary.dict_helper as dict_helper


@pytest.fixture
def example_dict_data():
    """Example Chamoru dictionary data.
    """
    return {
        "lowercase_word": {
            "definitions": ["def_00"],
            "types": ["type_00"],
            "chamoru_examples": ["chex_00"],
            "english_examples": ["enex_00"],
            "see_also": ["Title_Word"],
            "other_spellings": ["os_00"],
            "sources": ["src_00"],
            "pronunciation": "",
            "origin": ""
        },
        "Title_Word": {
            "definitions": ["def_01"],
            "types": ["type_01"],
            "chamoru_examples": ["chex_01"],
            "english_examples": ["enex_01"],
            "see_also": [],
            "other_spellings": ["os_01"],
            "sources": ["src_01"],
            "pronunciation": "",
            "origin": ""
        },
        "missing_keys": {}
    }


def test_check_dict_for_word__no_data(example_dict_data):
    """Tests check_dict_for_word by searching for a word that isn't defined.
    """
    assert dict_helper.check_dict_for_word(example_dict_data, 'not_in_dict') is None


def test_check_dict_for_word__lowercase(example_dict_data):
    """Tests 3 variations for a lowercase word that exists in the dict.

    Given the fact that a word exists in the dict, styled as lowercase, 
    ensures that we'll find the word whether it's passed as-is, as a Title 
    Word, or as UPPERCASE.
    """
    assert dict_helper.check_dict_for_word(example_dict_data, "lowercase_word") is not None
    assert dict_helper.check_dict_for_word(example_dict_data, "Lowercase_Word") is not None
    assert dict_helper.check_dict_for_word(example_dict_data, "LOWERCASE_WORD") is not None


def test_check_dict_word_word__title(example_dict_data):
    """Tests 3 variations for a Title Word that exists in the dict.

    Given the fact that a word exists in the dict, styled as a Title Word, 
    ensures that we'll find the word whether it's passed as-is, as lowercase, 
    or as UPPERCASE.
    """
    assert dict_helper.check_dict_for_word(example_dict_data, "Title_Word") is not None
    assert dict_helper.check_dict_for_word(example_dict_data, "title_word") is not None
    assert dict_helper.check_dict_for_word(example_dict_data, "TITLE_WORD") is not None


def test_stylize_output__data_exists(example_dict_data):
    """Tests the stylized output of a word, given that we know it is defined.
    """

    assert dict_helper.stylize_output(example_dict_data['lowercase_word']) is None
    assert dict_helper.stylize_output(example_dict_data['Title_Word']) is None


def test_stylize_output__key_error(example_dict_data):
    """Tests that a KeyError is raised for a word with missing keys.
    """

    with pytest.raises(KeyError):
        assert dict_helper.stylize_output(example_dict_data['missing_keys']) is None
