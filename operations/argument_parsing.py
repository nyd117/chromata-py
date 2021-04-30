import argparse


def check_positive(value):
    try:
        value = int(value)
        if value <= 0:
            raise argparse.ArgumentTypeError("{} is not a positive integer".format(value))
    except ValueError:
        raise argparse.ArgumentTypeError("{} is not an integer".format(value))
    return value


def define_args() -> argparse.ArgumentParser:

    description = "Visualize colors from arbitrary input"
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("-a", metavar="\"color\"",
                     help="Print a hex color to RGB format.")

    arg.add_argument("-e", metavar="\"colors\"",
                     help="Extract Hex colors from input and print in RGB format.")

    arg.add_argument("-f", metavar="\"path\"",
                     help="Extract Hex colors from file input and print in RGB format.")

    arg.add_argument("-p", metavar="\"path\"",
                     help="Provide path for palette generation.")

    arg.add_argument("-b", choices=["colorThief", "colorz"],
                     help="Define backend.")

    arg.add_argument("-c", type=check_positive,
                     help="Number of colors to be extracted from backend.")

    arg.add_argument("-g", action='store_true',
                     help="Generate templates.")

    arg.add_argument("-t", metavar="\"template name\"",
                     help="Define which template.")

    arg.add_argument("-n", action='store_true'
                     , help="No GUI.")

    return arg
