"""Program main"""

import json
import logging
import sys

import add
import search


def _init_logger():
    """Initializes the application logger"""

    log_filename = "log__words_searched.log"
    logging.basicConfig(
        filename=log_filename,
        filemode="a",
        format="%(asctime)s %(name)s %(funcName)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
    )

    console = logging.StreamHandler()
    console.setLevel(logging.CRITICAL)
    formatter = logging.Formatter("%(funcName)-12s: %(levelname)-8s %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)


def main():
    """Main function"""

    _init_logger()
    chamoru_dict = None
    filename = "chamoru_dictionary.json"

    with open(filename, "r", encoding="utf-8") as json_file:
        chamoru_dict = json.load(json_file)

    if chamoru_dict is None:
        print("File can't be loaded. Exiting.")
        logging.critical(f"{filename} cannot be found.")
        return None

    # CLI argument
    prog = str(sys.argv[1]).lower()

    if prog == "search":
        search.start_search(chamoru_dict)
    elif prog == "add":
        add.add_to_dictionary(filename, chamoru_dict)
    else:
        print("Invalid option")

    return None


if __name__ == "__main__":
    main()
