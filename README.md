# cli-chamoru-dictionary

> Chamoru dictionary accessed via the CLI

[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]

# Pre-requisites

## Software

- Python >= 3.X (currently using 3.10 but validating earlier versions)
- See **requirement.txt** file for modules

## Files

- Dictionary file stored as `.json`. **NOTE**: to get the necessary file, please see the [chamoru-site-scrapers](https://github.com/DJTai/chamoru-site-scrapers/tree/main/learning-chamoru) repo.

## Environment Setup

Run the following in a terminal:
```bash
# Get repo
git clone https://github.com/DJTai/cli-chamoru-dictionary.git
cd cli-chamoru-dictionary

# Setup virtual environment
python -m venv env
. env/bin/activate

# Install dependencies
make deps
#--OR----
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Usage

From the CLI, get into `cli_chamoru_dictionary` directory and run `python main.py (search|add)` to either search the dictionary or add a word to the dictionary.

## Getting Coverage and Tests

To get coverage & run tests, run the following:
```bash
make coverage
#--OR--------
python -m coverage erase
python -m coverage run --include=cli_chamoru_dict/* -m pytest -ra
python -m coverage report -m
```

For more info on pytest, visit [pytest docs](https://docs.pytest.org/en/6.2.x/usage.html#detailed-summary-report)

You can generate an HTML report by running `coverage html` after.