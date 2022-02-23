import pytest

import cli_chamoru_dictionary.orthography_helper as orthography_helper


@pytest.fixture
def example_word_list():
    return [
        "håfa",     # For å vs a
        "Mungnga",  # For Titlecase & ng-ng
        "månngi",   # For n-ng
        "LACHI",    # For uppercase
    ]

@pytest.fixture
def example_word_list_sorted():
    return [
        "håfa",
        "LACHI",
        "månngi",
        "Mungnga"
    ]

def test_chamoru_sort__word_values(example_word_list):
    """Tests the returned word values from chamoru_sort().
    """
    assert orthography_helper.chamoru_sort(example_word_list[0]) == [9, 2, 7, 1]
    assert orthography_helper.chamoru_sort(example_word_list[1]) == [13, 22, 16, 16, 1]
    assert orthography_helper.chamoru_sort(example_word_list[2]) == [13, 2, 14, 16, 10]
    assert orthography_helper.chamoru_sort(example_word_list[3]) == [12, 1, 4, 10]
    assert orthography_helper.chamoru_sort("water") is None

def test_chamoru_sort__sorted_list(example_word_list, example_word_list_sorted):
    """Tests the correctness of chamoru_sort().
    """
    assert sorted(example_word_list, key=lambda x: orthography_helper.chamoru_sort(x)) == example_word_list_sorted

def test_update_glota():
    """Tests if the incorrect glota's are replaced in the word.
    """
    assert orthography_helper.update_glota("fa‘cho‘chu") == "fa'cho'chu"
    assert orthography_helper.update_glota("fa\u2019cho\u2019chu") == "fa'cho'chu"
