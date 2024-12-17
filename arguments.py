# command line arguments

import argparse

parser = argparse.ArgumentParser(
    description = "Provides a personal greeting."

)

parser.add_argument(
    "-n","--name", metavar = "name",required = True,help ="The name of the person to greet."
)

parser.add_argument(
    "-l", "--lang",metavar = "language",
    required = True, choices=["English","Spanish","German"],
)


args = parser.parse_args()