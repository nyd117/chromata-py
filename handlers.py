import argparse
import extraction
from color_conversions import hex_to_rgb
from gui import gui
from system_utils import is_path_exists_or_creatable
from utils import trim


def handle_input(parser: argparse.ArgumentParser) -> None:
    args = parser.parse_args()
    gui_enabled: bool = args.ng is None
    execute_arg = (lambda arg, func: func(arg) if arg is not None else False)

    def extract_input(arg):
        colors = extraction.extract(arg)
        show(colors, "Colors from arguments")

    def extract_file(arg):
        path = arg
        if is_path_exists_or_creatable(path):
            with open(path, mode='r') as file:
                lines = file.read()
            colors = extraction.extract(lines)
            show(colors, "Colors from file")

    def show(colors, header):
        print(header)
        for element in colors:
            print(hex_to_rgb(element))
        assert_gui(trim(colors))

    def assert_gui(col):
        if gui_enabled:
            gui(col)

    execute_arg(args.a, lambda arg: print(hex_to_rgb(arg)))
    execute_arg(args.e, lambda arg: extract_input(arg))
    execute_arg(args.f, lambda arg: extract_file(arg))
