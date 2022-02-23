# cli-chamoru-dictionary

Chamoru dictionary accessed via the CLI

# Pre-requisites

## Software

- Python 3.X
- pytest
- pytest-cov

## Files

- Dictionary file stored as `.json`. **NOTE**: to get the necessary file, please see the [chamoru-site-scrapers](https://github.com/DJTai/chamoru-site-scrapers/tree/main/learning-chamoru) repo.

As of 2022 FEB 02, the application runs using the versions specified in `requirements.txt`.

## Usage

From the CLI, get into `cli_chamoru_dictionary` directory and run `python main.py (search|add)` to either search the dictionary or add a word to the dictionary.

## Running Tests

To run pytest, go to the root directory and run `python -m pytest -v --cov=cli_chamoru_dictionary tests/`. You can generate an HTML report by running `coverage html` after.
