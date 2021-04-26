import argparse


def define_args() -> argparse.ArgumentParser:

    description = "Visualize colors from arbitrary input"
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("-a", metavar="\"color\"",
                     help="Print a hex color to RGB format.")

    arg.add_argument("-e", metavar="\"input\"",
                     help="Extract Hex colors from input and print in RGB format.")

    arg.add_argument("-f", metavar="\"input\"",
                     help="Extract Hex colors from file input and print in RGB format.")

    arg.add_argument("-ng", help="No GUI.")
    return arg
